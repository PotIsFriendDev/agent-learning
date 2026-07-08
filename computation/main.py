from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Any, Dict
from tools import registry

app = FastAPI(title="Agent Computation Layer")

class ToolRequest(BaseModel):
    tool_name: str
    params: Dict[str, Any]

@app.post("/execute")
async def execute_tool(request: ToolRequest):
    try:
        result = registry.execute(request.tool_name, request.params)
        return {"status": "success", "result": result}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
