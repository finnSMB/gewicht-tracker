# Gewicht-Tracker-App
The API runs with FastAPI, you can look at its swagger-ui under `{{ip adress shown in console after launching:port}}/docs`

You might be able to run and look at the UI without launching the API. Just go to "using/testing/running" -> "Vue3 Frontend with javascript"

## Foreword!
This does not feature high quality code :D the goal was to try to get it done as fast as possible
while mainting somewhat of a readable codebase.

(the git commits have the same problem)

## Installation
This probably only runs on MacOS or WSL (Windows Subsystem for Linux). But you can try running this anyway.

Required:
- Python 3.11
- - Poetry (a package manager)
- NPM / NodeJs (latest works)
- Docker

All the docker files to create a new container are in the `./docker` folder.

## using/testing/running

After launching all the parts of this application an IP address will be displayed in the console

### Python
Run `poetry install` in the projects root folder.

Wait until the packages are installed and then launch a poetry shell:
`poetry shell`

*new*
Run `poetry run start` to launch the FastAPI backend.

*old*
CD into the api folder: `cd api`
run: `uvicorn main:app --reload`

### Vue3 Frontend with javascript
CD into the frontend folder `cd frontend`

Run `npm install` to install all the packages and then launch it with `npm run dev`

###  Docker / Database
Check the docker folder!

Launch Dockerfile with Docker to create an Image of our Database. Name the image `gewichttracker` (it should be suggested) or change the name accordingly in the docker-compose.dev.yml

Run the docker-compose file to launch the database!

If you don't want to use docker, the `db_schema.sql` contains all the information you need.

