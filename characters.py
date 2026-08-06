
import json
new_characters = [ 
                  ]

def add_charcters():
    with open("character.json", "r") as f:
        char_json = json.load(f)
    for i in new_characters:
            new_dict = {"name": i[0], "origin": i[1], "groups": i[1:]}
            char_json.append(new_dict)
    with open("character.json", "w") as f:
        json.dump(char_json, f)
    print("charcters added")
def characters():
    with open("character.json", "r") as f:
        return json.load(f)

# add_charcters()