import Anthropic from '@anthropic-ai/sdk';
import {} from './llm.provider.js';
export class AnthropicProvider {
    client;
    model;
    constructor(apiKey, model = 'claude-3-5-sonnet-20240620') {
        this.client = new Anthropic({ apiKey });
        this.model = model;
    }
    async generate(prompt) {
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
//# sourceMappingURL=anthropic.provider.js.map