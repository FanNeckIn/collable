
import json
new_characters = []

def add_charcters():
    with open("character.json", "rw") as f:
        char_json = json.load(f)
        for i in characters:
            new_dict = {"name": i[0], "origin": i[1], "groups": i[1:]}
            char_json.append(new_dict)
        json.dump(char_json, f)
with open("character.json", "r") as f:
    characters = json.load(f)