import json
from pathlib import Path

def get_path():
    cwd = str(Path(__file__).parents[1])
    return cwd

def read_json(filename):
    cwd = get_path()
    with open(f"{cwd}/{filename}.json", "r") as file:
        data = json.load(file)
    return data

def write_json(data, filename):
    cwd = get_path()
    with open(f"{cwd}/{filename}.json", "w") as file:
        json.dump(data, file, indent=4)