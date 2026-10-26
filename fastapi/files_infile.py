import json
from fastapi import FastAPI
import os
app = FastAPI()

@app.post("/")
def load_file():
    with open("FASTAPI" , "r") as f:
        data = os.listdir()
    data()