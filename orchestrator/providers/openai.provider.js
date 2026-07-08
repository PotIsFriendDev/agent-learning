import OpenAI from 'openai';
import {} from './llm.provider.js';
export class OpenAIProvider {
    client;
    model;
    constructor(apiKey, model = 'gpt-4o') {
        this.client = new OpenAI({ apiKey });
        this.model = model;
    }
    async generate(prompt) {
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
//# sourceMappingURL=openai.provider.js.map