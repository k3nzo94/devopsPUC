from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

#/teste1
@app.get('/teste1')
async def funcaoteste():
    return {'teste': 'deu certo'}