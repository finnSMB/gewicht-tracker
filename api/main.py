from fastapi import FastAPI
import uvicorn

from api.projectTypes import Animal
from api.db import Connection

app = FastAPI()
con = Connection()

versions: list[str] = ["v1"]

resources_v1: list[str] = ["tracker"]
methods_v1: list[str] = ["amount", "animal"]


# User guidance stuff
@app.get("/api/")
def get_api_versions():
    return {"versions": versions}


@app.get("/api/v1/")
def get_api_resources():
    return {"resources": resources_v1}


# Resource functionality starts here
@app.get("/api/v1/tracker/")
def get_api_methods():
    return {"methods/subresources": methods_v1}


@app.get("/api/v1/tracker/amount")
def get_amount_of_tracked_units():
    return {"trackedAnimals": 42482}


@app.options("/api/v1/tracker/amount")
def options_amount_of_tracked_units():
    return {"options": "GET, OPTIONS"}


# Animals methods
@app.get("/api/v1/tracker/animals")
def get_animals() -> Animal:
    animals: Animal = con.get_animals()
    return { animals }


@app.options("/api/v1/tracker/animals")
def options_animals():
    return {"options": "GET, OPTIONS"}


# Animal methods
@app.get("/api/v1/tracker/animal")
def get_animal():
    return 1


@app.post("/api/v1/tracker/animal")
def post_animal():
    return 1


@app.put("/api/v1/tracker/animal")
def put_animal():
    return 1


@app.delete("/api/v1/tracker/animal")
def delete_animal():
    return 1


@app.options("/api/v1/tracker/animal")
def options_animal():
    return {"options": "GET, POST, PUT, DELETE, OPTIONS"}


# Make this runnable with poetry
def start():
    """Launched with `poetry run start` in poetry shell at root project level"""
    uvicorn.run("rtt.main:app", host="127.0.0.1", port=8000, reload=True)


if __name__ == "__main__":
    start()