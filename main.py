from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from src.retrival_genaration import generation
from src.ingest import ingestdata
import uvicorn

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.on_event("startup")
def load_chain():
    global chain
    vstore = ingestdata()
    chain = generation(vstore)

@app.get("/", response_class=HTMLResponse)
async def get_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "response": None})

@app.post("/", response_class=HTMLResponse)
async def ask_bot(request: Request, question: str = Form(...)):
    response = chain.invoke(question)
    return templates.TemplateResponse("index.html", {"request": request, "response": response, "question": question})

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
