# 5

# make easy class
from dataclasses import dataclass


# var1 without imports
class Clan:
    def __init__(self, clan, palms):
        self.clan = clan
        self.palms = palms


Hinata1 = Clan("Hyuga", 64)


# var2 with import dataclasses
@dataclass()
class Rank:
    chuunin_exams: str
    class_B_missions: int


Hinata2 = Rank("passed on second try", 2)


# var3 crafted dataclass
def data_class_master(c_class):
    def inner_master(*args, **kwar):
        c_class.__annotations__
        return

    return inner_master


@data_class_master
class Battles:
    third_shinoby_war: str
    fourth_shinoby_war: str
    total_battles: int


Hinata3 = Battles("Not attended", "Attended", 3)

if __name__ == "__main__":
    print("\nvar1 - classic")
    print(Hinata1)
    print(Hinata1.clan)
    print("\nvar2 - built in")
    print(Hinata2)
    print(Hinata2.class_B_missions)
    print("\nvar3 - crafted")
    print(Hinata3)
    print(Hinata3.fourth_shinoby_war)