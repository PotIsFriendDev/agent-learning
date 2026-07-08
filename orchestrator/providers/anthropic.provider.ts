import Anthropic from '@anthropic-ai/sdk';
import { type LLMProvider, type LLMResponse } from './llm.provider.js';

export class AnthropicProvider implements LLMProvider {
    private client: Anthropic;
    private model: string;

    constructor(apiKey: string, model: string = 'claude-3-5-sonnet-20240620') {
        this.client = new Anthropic({ apiKey });
        this.model = model;
    }

    async generate(prompt: string): Promise<LLMResponse> {
        const response = await this.client.messages.create({
            model: this.model,
            max_tokens: 1024,
            messages: [{ role: 'user', content: prompt }],
        });

        const contentBlock = response.content[0];
        if (!contentBlock || !('text' in contentBlock)) {
            throw new Error('Unexpected Anthropic content block');
        }

        return { content: contentBlock.text };
    }
}
