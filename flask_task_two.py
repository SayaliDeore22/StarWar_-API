from flask import Flask
from task_two import first_task, second_task, third_task, forth_task, fifth_task

app = Flask(__name__)


@app.route("/")
def welcome():
    return "hello"


@app.route("/tasktwo/<resource>")
def task_two(resource):
    first_result = first_task()

    if resource == "characters":
        character_data = second_task(first_result)
        return character_data

    if resource == "planets":
        planet_data = third_task(first_result)
        return planet_data

    if resource == "vehicles":
        vehicle_data = forth_task(first_result)
        return vehicle_data

    if resource == "starships":
        starship_data = fifth_task(first_result)
        return  starship_data

