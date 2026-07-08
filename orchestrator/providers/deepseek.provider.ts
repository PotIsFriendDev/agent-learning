import OpenAI from 'openai';
import { type LLMProvider, type LLMResponse } from './llm.provider.js';

export class DeepSeekProvider implements LLMProvider {
    private client: OpenAI;
    private model: string;

    constructor(apiKey: string, model: string = 'deepseek-chat') {
        this.client = new OpenAI({
            apiKey,
            baseURL: 'https://api.deepseek.com'
        });
        this.model = model;
    }

    async generate(prompt: string): Promise<LLMResponse> {
        const response = await this.client.chat.completions.create({
            model: this.model,
            messages: [{ role: 'user', content: prompt }],
        });

        const content = response.choices[0]?.message?.content;
        if (!content) {
            throw new Error('Unexpected DeepSeek response content');
        }

        return { content };
    }
}
