from pydantic import BaseModel

class CodeSnippet(BaseModel):
    code:str
    ## {"code": "print('Hello world!')""}