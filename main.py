from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/get/{id}")
async def read_item(id):
    return {"item_id": id}
