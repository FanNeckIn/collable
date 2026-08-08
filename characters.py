
import json
new_characters = [ 
     ["Caeda", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Jagen", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Draug", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Wrys", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Bord", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Cord", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Barst", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Navarre", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Merric", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Minerva", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Linde", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Tiki", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Nyna", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Camus", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Sirius", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Medeus", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Gharnef", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Alm", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Celica", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Sigurd", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Deirdre", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Seliph", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Leif", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Julius", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Lilina", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Lyn", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Eliwood", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Hector", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Raven", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Ninian", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Karel", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Nino", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Eirika", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Ephraim", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["L'Arachel", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Lyon", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Titania", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Soren", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Mist", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Sothe", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Elincia", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Ashnard", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Zelgius", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Black Knight", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Micaiah", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Lissa", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Lon'qu", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Cordelia", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Tharja", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Anna", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Gangrel", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Walhart", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Owain", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Severa", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Azura", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Jakob", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Ryoma", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Hinoka", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Takumi", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Sakura", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Xander", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Camilla", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Leo", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Elise", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Garon", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Edelgard", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Dimitri", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Claude", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Sothis", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Rhea", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Seteth", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Dorothea", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Ingrid", "Fire Emblem", "Super Smash Bros Ultimate"],
     ["Hilda", "Fire Emblem", "Super Smash Bros Ultimate"],
                  ]

def add_charcters():
    with open("character.json", "r") as f:
        char_json = json.load(f)
    for i in new_characters:
            if i[0] in [j["name"] for j in char_json if j["name"]==i[0] and j["origin"] == i[1]]:
                 print(i[0], "from", i[1], "is already in, did you mean to add a new group?")
            else:
                new_dict = {"name": i[0], "origin": i[1], "groups": i[1:]}
                char_json.append(new_dict)
    with open("character.json", "w") as f:
        json.dump(char_json, f)
    print("charcters added")
def characters():
    with open("character.json", "r") as f:
        return json.load(f)

# add_charcters()