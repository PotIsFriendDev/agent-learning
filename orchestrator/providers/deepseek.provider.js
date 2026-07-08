import OpenAI from 'openai';
import {} from './llm.provider.js';
export class DeepSeekProvider {
    client;
    model;
    constructor(apiKey, model = 'deepseek-chat') {
        this.client = new OpenAI({
            apiKey,
            baseURL: 'https://api.deepseek.com'
        });
        this.model = model;
    }
    async generate(prompt) {
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
//# sourceMappingURL=deepseek.provider.js.map