"""HomeWork Classes"""
import random


class Warrior:
    """
    Parent class for Hero and Soldier
    """
    def __init__(self, idx, color):
        self.idx = idx
        self.color = color

    def __repr__(self):
        fields = [str(f"{k}={v}") for k, v in self.__dict__.items()]
        fileds_str = ",".join(fields)
        return f"{type(self).__name__}({fileds_str})"


class Hero(Warrior):
    """ Hero  has id, color and level"""
    def __init__(self, idx, color):
        self.level = random.choice([0, 1])
        super().__init__(idx, color)

    def level_increase(self):
        """increase the level"""
        self.level += 1


class Soldier(Warrior):
    """Soldier has id, color and hero"""
    def __init__(self, idx, color):
        super().__init__(idx, color)
        self.hero = None

    def set_follow_hero(self, hero: Hero):
        """set the hero of the team"""
        self.hero = hero


class Team:
    """
    Creat team with specific color and hero
    """
    def __init__(self, hero: Hero):
        self.color = hero.color
        self.hero = hero
        self.soldiers = []

    def apply(self, soldier):
        """Apply the soldier to the team"""
        self.soldiers.append(soldier)

    @property
    def count(self):
        """Counts the soldiers"""
        return len(self.soldiers)

    @property
    def scouts(self):
        """"Create a scouts included hero and 3 random soldier"""
        scouts = []
        if len(scouts) == 0:
            scouts.append(self.hero)
            scouts.extend(random.choices(self.soldiers, k=3))
        return scouts


def main():
    """main logic"""
    teams = {"red": None, "yellow": None, "green": None}
    i = 0

    for color in teams:
        hero = Hero(i, color)
        team = Team(hero)
        teams[color] = team
        i += 1

    for idx in range(i, 1000 + i):
        color = random.choice(list(teams))
        team = teams[color]
        soldier = Soldier(idx, color)
        soldier.set_follow_hero(team.hero)
        team.apply(soldier)

    for team in teams.values():
        print(f"Team {team.color} has {team.count} soldiers.")

    biggest_team = sorted(teams.values(), key=lambda x: x.count)[-1]
    print(f"Team {biggest_team.color} has more soldiers than others.")
    biggest_team.hero.level_increase()

    for scout in biggest_team.scouts:
        print(f"Scout: {scout}")


# run
main()
