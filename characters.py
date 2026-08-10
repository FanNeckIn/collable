
import json
new_characters = [ 
     ["Ribbon Girl", "ARMS", "Super Smash Bros Ultimate"],
     ["Martial Artist Gi", "Dragon Quest", "Super Smash Bros Ultimate"],
     ["Flying Man", "EarthBound", "Super Smash Bros Ultimate"],
     ["Pig", "Minecraft", "Super Smash Bros Ultimate"],
     ["Ryo Sakazaki", "Art of Fighting", "Super Smash Bros Ultimate"],
     ["Shantae", "Shantae", "Super Smash Bros Ultimate"],
     ["Iori Yagami", "The King of Fighters", "Super Smash Bros Ultimate"],
     ["Jacky", "Virtua Fighter", "Super Smash Bros Ultimate"],
     ["Nia", "Xenoblade Chronicles", "Super Smash Bros Ultimate"],
     ["Erdrick", "Dragon Quest", "Super Smash Bros Ultimate"],
     ["Veronica", "Dragon Quest", "Super Smash Bros Ultimate"],
     ["Aerith", "Final Fantasy", "Super Smash Bros Ultimate"],
     ["Arthur", "Ghosts 'n Goblins", "Super Smash Bros Ultimate"],
     ["Viridi", "Kid Icarus", "Super Smash Bros Ultimate"],
     ["Altair", "Assassin's Creed", "Super Smash Bros Ultimate"],
     ["Gil", "Babylonian Castle Saga", "Super Smash Bros Ultimate"],
     ["Dante", "Devil May Cry", "Super Smash Bros Ultimate"],
     ["Goemon", "Goemon", "Super Smash Bros Ultimate"],
     ["Lloyd", "Tales", "Super Smash Bros Ultimate"],
     ["Geno", "Mario Bros", "Super Smash Bros Ultimate"],
     ["Doom Slayer", "DOOM", "Super Smash Bros Ultimate"],
     ["Sans", "Undertale", "Super Smash Bros Ultimate"],
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

# add_characters()
