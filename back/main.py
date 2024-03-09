from fastapi import FastAPI, HTTPException
from models.execution_models import CodeSnippet
import subprocess
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World!"}

@app.post("/execute_r")
async def execute_r(request: CodeSnippet):
    code_to_execute = request.code
    try:
        result = subprocess.run(["Rscript", "-e" , code_to_execute],
                                capture_output=True, text=True, check=True)        
        return {"stdout":result.stdout, "stderr":result.stderr}
    except subprocess.CalledProcessError as e:
        return {"error": "코드 실행중 에러발생", "details":str(e)}