export interface LLMResponse {
    content: string;
}

export interface LLMProvider {
    generate(prompt: string): Promise<LLMResponse>;
}
