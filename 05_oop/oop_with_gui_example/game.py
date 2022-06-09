from characters import Swordsman, Rogue, Wizard, Monster

# Адаптер
class Game:
    def __init__(self):
        self.heroes = (Swordsman('Jack'), Rogue('Moxie'), Wizard('Arkalis'))
        self.selected_hero = self.heroes[0]
        self.create_monster()

    def get_hero_status(self):
        return self.selected_hero.health, str(self.selected_hero)

    def get_monster_status(self):
        return self.monster.health, str(self.monster)

    def create_monster(self):
        self.monster = Monster('Demon', 5)

    def get_heroes_list(self):
        return [h.__class__.__name__ for h in self.heroes]

    def select_hero_by_class_name(self, hero_class_name):
        for h in self.heroes:
            if hero_class_name == h.__class__.__name__:
                self.selected_hero = h

    def monster_move(self):
        monster_attack = self.monster.attack()
        result = f'{self.monster.name} attacks with {monster_attack.name}: {monster_attack.damage} {monster_attack.type.value}\n'
        self.selected_hero.health -= monster_attack.damage
        if self.selected_hero.health == 0:
            result += f'\n {self.monster.name} wins!\n'
        return result

    def hero_move(self):
        hero_attack = self.selected_hero.attack()
        result = f'{self.selected_hero.name} attacks with {hero_attack.name}: {hero_attack.damage} {hero_attack.type.value} '
        if hero_attack.type != self.monster.resist:
            self.monster.health -= hero_attack.damage
        else:
            result += 'No effect!'
        if self.monster.health == 0:
            result += f'\n {self.selected_hero.name} wins!'
        return result + '\n'

    def game_continues(self):
        return self.selected_hero.health and self.monster.health
