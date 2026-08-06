import random
import characters
class group:
    def __init__(self, name: str) -> None:
        self.name = name
        self.characters = []
        self.character_names = []
    def add_character(self, character: character) -> None:
        self.characters.append(character)
        self.character_names.append(character.name)
class character:
    def __init__(self, lst:list) -> None:
        self.name = lst[0]
        self.groups = lst[1:]
        self.main_group = self.groups[0]
class world:
    def __init__(self) -> None:
        self.groups = []
        self.characters = []
    def add_characters(self, characters: list) -> None:
        for i in characters:
            char = character(i)
            self.characters.append(char)
            for g in i[1:]:
                if g not in [x.name for x in self.groups]:
                    self.groups.append(group(g))
                for group_obj in self.groups:
                    if group_obj.name == g:
                        group_obj.add_character(char)
    def print_characters(self) -> None:
        for i in self.characters:
            print(f"{i.name} is in {', '.join(i.groups)} ({len(i.groups)} groups)")
    def print_groups(self) -> None:
        for i in self.groups:
            print(f"{i.name} has {', '.join(i.character_names)} ({len(i.character_names)} characters)")
    def CreateRandomGame(self):
        round = 0
        start = random.choice(self.characters)
        end = random.choice(self.characters)
        while start == end:
            end = random.choice(self.characters)
        cur = start
        print(f"Start: {start.name} from {start.main_group}. End : {end.name} from {end.main_group}")
        while cur != end:
            round += 1
            in_loop = True
            while in_loop:
                inp = input(f"Enter Next Group (Cur Character is {cur.name}): ")
                if inp in [i.name for i in self.groups if cur in i.characters]:
                    in_loop = False
                    cur_group = [i for i in self.groups if i.name == inp][0]
                else:
                    print("Error: unknown group / character not in group")
            in_loop = True
            while in_loop:
                inp = input(f"Enter Next Character:")
                if inp in cur_group.character_names:
                    in_loop = False
                    lst = [i for i in cur_group.characters if i.name == inp]
                    if len(lst) == 1:
                        cur = lst[0]
                    else:
                        iin = True
                        while iin:
                            inp = input(f"From? \n options: {[i.main_group for i in lst]}")
                            if inp in [i.main_group.name for i in lst]:
                                cur = [i for i in lst if i.main_group == inp]
                                iin = False
        print("Game Won in", round, "rounds")
    def needed_characters(self):
        dict = {}
        for i in self.characters:
            if i.main_group in dict.keys():
                dict[i.main_group]+=1
            else:
                dict[i.main_group]= 1
        for i in dict.keys():
            if dict[i]< 10:
                input(f'{i} needs {10-dict[i]} more characters')
    def top_groups(self, n=None):
        if n == None:
            print([f"{i.name}, {len(i.characters)}" for i in sorted(self.groups, key=lambda x: len(x.characters))])
            return
        print([f"{i.name}, {len(i.characters)}" for i in sorted(self.groups, key=lambda x: len(x.characters), reverse=True)][:n-1])
    def CreateCustomGame(self, start, end):
        round = 0
        cur = start
        print(f"Start: {start.name} from {start.main_group}. End : {end.name} from {end.main_group}")
        while cur != end:
            round += 1
            in_loop = True
            while in_loop:
                inp = input(f"Enter Next Group (Cur Character is {cur.name}): ")
                if inp in [i.name for i in self.groups if cur in i.characters]:
                    in_loop = False
                    cur_group = [i for i in self.groups if i.name == inp][0]
                else:
                    print("Error: unknown group / character not in group")
            in_loop = True
            while in_loop:
                inp = input(f"Enter Next Character:")
                if inp in cur_group.character_names:
                    in_loop = False
                    lst = [i for i in cur_group.characters if i.name == inp]
                    if len(lst) == 1:
                        cur = lst[0]
                    else:
                        iin = True
                        while iin:
                            inp = input(f"From? \n options: {[i.main_group for i in lst]}")
                            if inp in [i.main_group.name for i in lst]:
                                cur = [i for i in lst if i.main_group == inp]
                                iin = False
        print("Game Won in", round, "rounds")
        



world_obj = world()
world_obj.add_characters(characters.characters)
# world_obj.print_groups()
world_obj.top_groups()
world_obj.CreateRandomGame()
# world_obj.needed_characters()
# world_obj.CreateCustomGame([i for i in world_obj.characters if i.name == "Fluttershy"][0], [i for i in world_obj.characters if i.name == "Funshine Bear"][0])