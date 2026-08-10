
import json
new_characters = [ 
     ["The Punisher", "Marvel Comics", "Fortnite"],
     ["The Punisher", "Bleach", "Fortnite"],
     ["Yoruichi Shihoin", "Bleach", "Fortnite"],
     ["Kisuke Urahara", "Bleach", "Fortnite"],
]

def add_characters():
    with open("character.json", "r") as f:
        char_json = json.load(f) #type: list[dict]
    for i in new_characters:
            if i[0] in [j["name"] for j in char_json if j["name"]==i[0] and j["origin"] == i[1]]:
                 print(i[0], "from", i[1], "is already in, adding new groups")
                 new_dict = char_json.pop(char_json.index([j for j in char_json if j["name"]==i[0] and j["origin"] == i[1]][0]))
                 new_groups = new_dict["groups"] + i[1:]
                 new_groups = list(set(new_groups))
                 new_dict["groups"] = new_groups
                 char_json.append(new_dict)
            else:
                new_dict = {"name": i[0], "origin": i[1], "groups": i[1:]}
                char_json.append(new_dict)
    with open("character.json", "w") as f:
        char_json.sort(key = lambda x: x["origin"]+x["name"])
        json.dump(char_json, f)
    print("charcters added")
def characters():
    with open("character.json", "r") as f:
        return json.load(f)

add_characters()
