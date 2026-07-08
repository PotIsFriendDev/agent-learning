import { type LLMProvider, type LLMResponse } from './llm.provider.js';
export declare class AnthropicProvider implements LLMProvider {
    private client;
    private model;
    constructor(apiKey: string, model?: string);
    generate(prompt: string): Promise<LLMResponse>;
}
//# sourceMappingURL=anthropic.provider.d.ts.map