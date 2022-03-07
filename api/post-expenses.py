from fastapi import FastAPI

app = FastAPI()


@app.post('/expenses')
def post(date=None):
    return {"expenses": None}
