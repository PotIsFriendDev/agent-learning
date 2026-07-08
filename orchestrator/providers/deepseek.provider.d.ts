import { type LLMProvider, type LLMResponse } from './llm.provider.js';
export declare class DeepSeekProvider implements LLMProvider {
    private client;
    private model;
    constructor(apiKey: string, model?: string);
    generate(prompt: string): Promise<LLMResponse>;
}
//# sourceMappingURL=deepseek.provider.d.ts.map