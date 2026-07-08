#  Agent Learning Project (Refactored)

This project is a learning implementation of an AI Agent, split into an Orchestration layer and a Computation layer.

## Architecture

- **Orchestration Layer (TypeScript)**: Handles the core agent loop (Think $\rightarrow$ Act $\rightarrow$ Observe). It manages the state, communicates with the LLM (Claude), and decides which tools to call.
- **Computation Layer (Python)**: Provides the actual tool implementations and heavy-duty processing via a FastAPI server.

## Project Structure

```
.
├── orchestrator/      # TypeScript - The "Brain"
│   ├── index.ts       # Main agent loop
│   └── package.json
└── computation/       # Python - The "Muscles"
    ├── main.py        # FastAPI Server
    ├── tools.py       # Tool definitions
    ├── sandbox.py     # Secure filesystem sandbox logic
    └── requirements.txt
```

## How to Run

### 1. Start the Computation Layer
```bash
cd computation
pip install -r requirements.txt
python main.py
```
The server will start at `http://localhost:8000`.

### 2. Start the Orchestrator
1. Open `orchestrator/index.ts` and replace `'YOUR_ANTHROPIC_API_KEY'` with your actual API key.
2. Run the orchestrator:
```bash
cd orchestrator
npm install
npx ts-node index.ts
```

## Sandbox Capabilities
The agent is equipped with a secure sandbox in `D:\claude-agent-learning\sandbox\workspace` that allows it to:
- **Read/Write Files**: Securely interact with documents within the sandbox.
- **List Directories**: Explore the sandbox filesystem.
- **Execute Scripts**: Run Python scripts to perform complex calculations or data processing.

### Security Measures:
- **Path Confinement**: Prevents directory traversal attacks (e.g., `../`) using absolute path resolution and root validation.
- **No-Shell Execution**: Uses `subprocess.run` with `shell=False` to block command injection.
- **Resource Limits**: Implements a 30-second timeout on script execution to prevent DoS.

## Key Concepts Demonstrated
- **Decoupled Architecture**: Separating logic (TS) from execution (Py).
- **Think-Act-Observe Loop**: Autonomous goal pursuit.
- **Tool Use**: Dynamic interaction between different languages and runtimes.
- **Secure Sandboxing**: Implementing restricted filesystem access (rwx) with path confinement and execution timeouts.
