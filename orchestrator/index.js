import axios from 'axios';
import readline from 'node:readline/promises';
import { stdin as input, stdout as output } from 'node:process';
import {} from './providers/llm.provider.js';
import { AnthropicProvider } from './providers/anthropic.provider.js';
import { OpenAIProvider } from './providers/openai.provider.js';
import { DeepSeekProvider } from './providers/deepseek.provider.js';
const COMPUTE_URL = 'http://localhost:8000';
class Orchestrator {
    provider;
    state;
    constructor(provider, goal) {
        this.provider = provider;
        this.state = {
            goal,
            history: [],
            status: 'thinking'
        };
    }
    async run() {
        console.log(`🎯 Goal: ${this.state.goal}`);
        while (this.state.status !== 'completed') {
            await this.step();
        }
        console.log('✅ Goal achieved!');
    }
    async step() {
        this.state.status = 'thinking';
        console.log('\n🤔 Thinking...');
        const prompt = `You are an AI Agent. Your current goal is: ${this.state.goal}\n\n` +
            `Current History: ${JSON.stringify(this.state.history)}\n\n` +
            `Please respond in the following JSON format:\n` +
            `{\n  "thought": "your reasoning",\n  "action": "tool_name" or "final_answer",\n  "params": { "param1": "value1" }\n}`;
        try {
            const response = await this.provider.generate(prompt);
            const content = response.content;
            let decision;
            try {
                decision = JSON.parse(content);
            }
            catch (e) {
                console.error('Failed to parse LLM response as JSON:', content);
                return;
            }
            console.log(`💭 Thought: ${decision.thought}`);
            if (decision.action === 'final_answer') {
                console.log(`🏁 Final Answer: ${decision.params.answer}`);
                this.state.status = 'completed';
            }
            else {
                this.state.status = 'acting';
                console.log(`⚡ Action: Calling tool ${decision.action}...`);
                try {
                    const res = await axios.post(`${COMPUTE_URL}/execute`, {
                        tool_name: decision.action,
                        params: decision.params
                    });
                    console.log(`👀 Observation: ${JSON.stringify(res.data.result)}`);
                    this.state.history.push({
                        action: decision.action,
                        params: decision.params,
                        observation: res.data.result
                    });
                }
                catch (e) {
                    console.error(`❌ Tool error: ${e.message}`);
                    this.state.history.push({
                        action: decision.action,
                        error: e.message
                    });
                }
            }
        }
        catch (e) {
            console.error(`❌ LLM Provider Error: ${e.message}`);
            return;
        }
    }
}
// Usage examples
async function main() {
    // Use DeepSeek
    const provider = new DeepSeekProvider(process.env.DEEPSEEK_API_KEY || '');
    const rl = readline.createInterface({
        input: input,
        output: output
    });
    console.log('\n🤖 Agent Interactive Mode Started!');
    console.log('Type your goal and press Enter. Type "exit" or "quit" to stop.\n');
    while (true) {
        const goal = await rl.question('🎯 Enter your goal: ');
        if (goal.toLowerCase() === 'exit' || goal.toLowerCase() === 'quit') {
            console.log('👋 Exiting... Goodbye!');
            break;
        }
        if (!goal.trim())
            continue;
        console.log(`\n🚀 Initializing Agent with Goal: ${goal}`);
        const agent = new Orchestrator(provider, goal);
        await agent.run();
        console.log('\n--- Goal Completed ---\n');
    }
    rl.close();
}
main();
//# sourceMappingURL=index.js.map