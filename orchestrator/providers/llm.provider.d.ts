export interface LLMResponse {
    content: string;
}
export interface LLMProvider {
    generate(prompt: string): Promise<LLMResponse>;
}
//# sourceMappingURL=llm.provider.d.ts.map