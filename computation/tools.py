from typing import Any, Dict
import numpy as np
from sandbox import read_file, write_file, list_files, execute_script

class ToolRegistry:
    def __init__(self):
        self.tools = {}

    def register(self, name, func):
        self.tools[name] = func

    def execute(self, name, params: Dict[str, Any]):
        if name not in self.tools:
            raise ValueError(f"Tool {name} not found")
        return self.tools[name](**params)

# Define some computation tools
def calculate_sum(a: float, b: float) -> float:
    """Calculates the sum of two numbers."""
    return a + b

def analyze_text(text: str) -> Dict[str, Any]:
    """Performs basic text analysis."""
    return {
        "length": len(text),
        "word_count": len(text.split()),
        "uppercase_count": sum(1 for c in text if c.isupper())
    }

def get_system_stats() -> Dict[str, Any]:
    """Returns mock system stats."""
    return {"cpu_usage": "15%", "memory_usage": "2.4GB", "status": "healthy"}

# Initialize registry
registry = ToolRegistry()
registry.register("calculate_sum", calculate_sum)
registry.register("analyze_text", analyze_text)
registry.register("get_system_stats", get_system_stats)
registry.register("read_file", read_file)
registry.register("write_file", write_file)
registry.register("list_files", list_files)
registry.register("execute_script", execute_script)
