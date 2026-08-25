import random
import characters
from datetime import date
from itertools import combinations
from time import time
import json
class group:
    def __init__(self, name: str) -> None:
        self.name = name
        self.characters = []
        self.character_names = []
    def add_character(self, character) -> None:
        self.characters.append(character)
        self.character_names.append(character.name)
class character:
    def __init__(self, dicty:dict) -> None:
        self.name = dicty["name"]
        self.groups = dicty["groups"]
        self.origin = dicty["origin"]
    def __str__(self) -> str:
        return self.name + " from " + self.origin
class world:
    def __init__(self) -> None:
        self.groups = []
        self.characters = []
        self.charactersMin = {}
    def sort_by_groups(self, x):
        string = ""
        for i in sorted(x.groups):
            string += i
        return string
    def sort_by_r1(self, x):
        n = []
        for j in [i.character_names for i in self.groups if i.name in x.groups]:
            n += [k for k in j if k in [l.name for l in self.charactersMin.keys()]]
        return len(set(n))
    
    def add_characters(self, characters: list) -> None:
        for i in characters:
            char = character(i)
            self.characters.append(char)
            for g in i["groups"]:
                if g not in [x.name for x in self.groups]:
                    self.groups.append(group(g))
                for group_obj in self.groups:
                    if group_obj.name == g:
                        group_obj.add_character(char)
        self.MinimizeCharacters()
    def MinimizeCharacters(self):
        self.characters.sort(key=self.sort_by_groups)
        chars = {}
        start = 0
        for i in range(len(self.characters)):
            if not set(self.characters[i].groups) == set(self.characters[start].groups):
                chars[self.characters[start]] = i-start
                start = i
        self.charactersMin = chars
    def print_characters(self) -> None:
        for i in self.characters:
            print(f"{i} is in {', '.join(i.groups)} ({len(i.groups)} groups)")
    def print_groups(self) -> None:
        for i in self.groups:
            print(f"{i.name} has {', '.join(i.character_names)} ({len(i.character_names)} characters)")
    def CreateRandomGame(self):
        start = random.choice(self.characters)
        end = random.choice(self.characters)
        while start == end:
            end = random.choice(self.characters)
        self.CreateCustomGame(start, end)
    def CreateCustomGame(self, start, end):
        round = 0
        cur = start
        print(f"Start: {start.name} from {start.origin}. End : {end.name} from {end.origin}")
        cur_group = group("")
        while cur != end:
            round += 1
            in_loop = True
            while in_loop:
                inp = input(f"Enter Next Group (Cur Character is {cur.name}): ").lower()
                if inp in [i.name.lower() for i in self.groups if cur in i.characters]:
                    in_loop = False
                    cur_group = [i for i in self.groups if i.name.lower() == inp][0]
                else:
                    print("Error: unknown group / character not in group")
            in_loop = True
            while in_loop:
                inp = input(f"Enter Next Character:").lower()
                if inp in [i.lower() for i in cur_group.character_names]:
                    in_loop = False
                    lst = [i for i in cur_group.characters if i.name.lower() == inp]
                    if len(lst) == 1:
                        cur = lst[0]
                    else:
                        iin = True
                        while iin:
                            inp = input(f"From? \n options: {[i.origin for i in lst]}").lower()
                            if inp in [i.origin.name.lower() for i in lst]:
                                cur = [i for i in lst if i.origin.lower() == inp]
                                iin = False
        print("Game Won in", round, "rounds")
    def needed_characters(self):
        dict = {}
        for i in self.characters:
            if i.origin in dict.keys():
                dict[i.origin]+=1
            else:
                dict[i.origin]= 1
        for i in dict.keys():
            if dict[i]< 10:
                input(f'{i} needs {10-dict[i]} more characters')
    def top_groups(self, n=None):
        if n == None:
            print([f"{i.name}, {len(i.characters)}" for i in sorted(self.groups, key=lambda x: len(x.characters))])
            return
        print([f"{i.name}, {len(i.characters)}" for i in sorted(self.groups, key=lambda x: len(x.characters), reverse=True)][:n-1])
        print("Game Won in", round, "rounds")
    def CreateDailyGame(self):
        d = date.today() - date(1970, 1 , 1)
        random.seed(d.days)
        start = random.choice(self.characters)
        end = random.choice(self.characters)
        while start == end or len([i for i in start.groups if i in end.groups])>0:
             end = random.choice(self.characters)
        self.CreateCustomGame(start, end)
    def CheckMinLen(self, start, end):
        round = 0
        all_characters = {start}
        while True:
            round += 1
            for i in all_characters:
                for j in [k for k in self.groups if k.name in i.groups]:
                    all_characters = all_characters.union(set(j.characters))
            if end in all_characters:
                return round
    def CheckAllLengths(self):
        start = 0
        for i in range(len(self.characters)):
            if not set(self.characters[i].groups) == set(self.characters[start].groups):
                self.charactersMin[self.characters[start]] = i-start
                start = i
        print(len(self.charactersMin.keys()))
        answer = {1:0,2:0,3:0,4:0,5:0,6:0}
        check = set()
        s = time()
        for i in combinations(sorted(self.charactersMin.keys(), key=self.sort_by_r1), 2):
            if i[0] not in check:
                print(len(check))
                print(time()-s)
                s=time()
                print(self.sort_by_r1(i[0]))
                print(i[0].__str__(), self.charactersMin[i[0]], i[0].groups , answer)
                answer[1] += (self.charactersMin[i[0]]-1)*self.charactersMin[i[0]]
                check.add(i[0])
            a = self.CheckMinLen(i[0], i[1])
            if a in answer.keys():
                answer[a] += self.charactersMin[i[0]] *self.charactersMin[i[1]]
            else:
                    answer[a] = self.charactersMin[i[0]] *self.charactersMin[i[1]]
        with open("answer.json", "w") as f:
            json.dump(answer, f, indent=4)
            



world_obj = world()
world_obj.add_characters(characters.characters())
# world_obj.print_groups()
# world_obj.top_groups()
# world_obj.CreateDailyGame()
# world_obj.CreateRandomGame()
# world_obj.needed_characters()
print(len(world_obj.groups))
world_obj.CheckAllLengths()