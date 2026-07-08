import { type LLMProvider, type LLMResponse } from './llm.provider.js';
export declare class OpenAIProvider implements LLMProvider {
    private client;
    private model;
    constructor(apiKey: string, model?: string);
    generate(prompt: string): Promise<LLMResponse>;
}
//# sourceMappingURL=openai.provider.d.ts.map