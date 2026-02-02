from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="Minha API Simples-")

class EchoIn(BaseModel):
    text: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/hello")
def hello(name: str = "world"):
    return {"message": f"hello, {name}"}

@app.post("/echo")
def echo(payload: EchoIn):
    return {"text": payload.text, "length": len(payload.text)}

@app.get("/sum")
def sum(a,b):
    valor =  int(a) + int(b)
    return{"Result": valor}


if __name__ == "__main__":
    uvicorn.run(app, port=8000)