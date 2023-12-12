from fastapi import FastAPI, Request, logger
from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn
import json

from api.projectTypes import Animal, WeightSubmit
from api.db import Connection

app = FastAPI()
con = Connection()

origins = [
    "http://localhost:8000",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/v1/tracker/amount", tags=["Number of Animals"])
def get_amount_of_tracked_units():
    return to_valid_json(con.get_amount_tracked_animals())


# Animals methods
@app.get("/api/v1/tracker/animals", tags=["Animals"])
def get_animals():
    return to_valid_json(con.get_animals())


# Animal methods
@app.get("/api/v1/tracker/animal", tags=["Animal"])
def get_animal(id: int):
    return to_valid_json(con.get_animal(id))


@app.post("/api/v1/tracker/animal", tags=["Animal"])
def post_animal(payload: Animal):
    return {"response": con.add_animal(payload)}


@app.delete("/api/v1/tracker/animal", tags=["Animal"])
def delete_animal(id: int):
    con.delete_animal(id)


@app.get("/api/v1/tracker/animalweight", tags=["Animal Weight"])
def get_recored_animal_weights(id: int):
    return to_valid_json(con.get_animal_weight(id))


@app.post("/api/v1/tracker/animalweight", tags=["Animal Weight"])
def post_animal_weight_data(weight: WeightSubmit):
    con.post_animal_weight(weight)


"""
Helper function to create a valid json list.

:param data: list, containing all the database entries.
:return: list, in a valid json format.
"""


def to_valid_json(data: list) -> list:
    parsed_data: list = [json.loads(row[0]) for row in data]

    return parsed_data


# Make this runnable with poetry
def start():
    """Launched with `poetry run start` in poetry shell at root project level"""
    uvicorn.run("api.main:app", host="127.0.0.1", port=8000, reload=True)


if __name__ == "__main__":
    start()
