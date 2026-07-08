# Claude AI Agent 学习项目 (重构版)

这是一个关于 AI Agent (人工智能体) 的学习实现项目，采用了**编排层 (Orchestration Layer)** 与 **计算层 (Computation Layer)** 分离的解耦架构。

## 🏗️ 项目架构

本项目将 Agent 的“大脑”与“肌肉”分开，分别使用不同的语言实现以发挥各自优势：

- **编排层 (TypeScript)**：负责 Agent 的核心循环（思考 $\rightarrow$ 行动 $\rightarrow$ 观察）。它管理状态机，与大语言模型 (LLM) 通信，并决定调用哪个工具。**本项目采用了现代 Node.js 环境，全面支持原生 ESM (ECMAScript Modules) 和 `NodeNext` 模块解析，确保在最新版本的 Node.js 中拥有最佳性能和类型兼容性。**
- **计算层 (Python)**：通过 FastAPI 服务器提供实际的工具实现和高性能处理能力。

## 📁 项目结构

```
.
├── orchestrator/      # TypeScript - 编排层（大脑）
│   ├── index.ts       # Agent 主循环逻辑
│   └── package.json
└── computation/       # Python - 计算层（肌肉）
    ├── main.py        # FastAPI 服务端
    ├── tools.py       # 工具定义与实现
    ├── sandbox.py     # 安全文件系统沙箱逻辑
    └── requirements.txt
```

## 🚀 如何运行

### 1. 启动计算层 (Computation Layer)
```bash
cd computation
pip install -r requirements.txt
python main.py
```
服务将启动在 `http://localhost:8000`。

### 2. 启动编排层 (Orchestrator)
1. 在根目录下创建 `.env` 文件并配置 API 密钥：
   ```env
   DEEPSEEK_API_KEY=your_api_key_here
   ```
2. 运行编排层：
   ```bash
   cd orchestrator
   npm install
   npx ts-node index.ts
   ```

## 🛡️ 沙箱能力 (Sandbox Capabilities)
Agent 配备了一个安全沙箱，允许其在受限环境下执行以下操作：
- **读写文件**：安全地与沙箱内的文档进行交互。
- **列出目录**：探索沙箱文件系统。
- **执行脚本**：运行 Python 脚本进行复杂计算或数据处理。

### 安全措施：
- **路径隔离 (Path Confinement)**：通过绝对路径解析和根路径校验，防止目录遍历攻击（如 `../`）。
- **禁止 Shell 执行**：使用 `subprocess.run` 且设置 `shell=False`，有效拦截命令注入。
- **资源限制**：对脚本执行设置 30 秒超时，防止拒绝服务 (DoS) 攻击。

## 💡 核心技术要点
- **解耦架构**：将逻辑控制 (TS) 与执行环境 (Py) 分离。
- **Think-Act-Observe 循环**：实现自主的目标追求能力。
- **跨语言工具调用**：演示了不同语言和运行时的动态交互。
- **安全沙箱实现**：实现了具有路径隔离和执行超时的受限文件系统访问 (rwx)。
