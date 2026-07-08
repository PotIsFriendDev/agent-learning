import OpenAI from 'openai';
import { type LLMProvider, type LLMResponse } from './llm.provider.js';

export class OpenAIProvider implements LLMProvider {
    private client: OpenAI;
    private model: string;

    constructor(apiKey: string, model: string = 'gpt-4o') {
        this.client = new OpenAI({ apiKey });
        this.model = model;
    }

    async generate(prompt: string): Promise<LLMResponse> {
        const response = await this.client.chat.completions.create({
            model: this.model,
            messages: [{ role: 'user', content: prompt }],
        });

        const content = response.choices[0]?.message?.content;
        if (!content) {
            throw new Error('Unexpected OpenAI response content');
        }

        return { content };
    }
}
