from abc import ABC, abstractmethod # Abstract Base Class
from enum import Enum, unique
from dataclasses import dataclass
from random import choice, randint

# перечисления - набор констант
@unique
class DamageType(Enum):
    PHYSICAL = '🗡️'
    FIRE = '🔥'
    ICE = '🧊'
    LIGHTNING = '⚡'
    POISON = '💀'

@unique
class DamageRange(Enum):
    MELEE = 0
    RANGE = 1
    AREA = 2


@dataclass
class Attack:
    name: str
    type: DamageType
    range: DamageRange
    damage: int = 0


class Character(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name
        self._health = 100
        self._mana = 100
        self._resist = ()
        self._attacks = ()

    @property
    def resist(self):
        return self._resist

    @property   # property - managed attribute
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health = value if value >= 0 else 0

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, value):
        self._mana = value if value >= 0 else 0

    @abstractmethod
    def attack(self):
        pass

    def __str__(self):
        return f'{self.__class__.__name__} {self.name} 🔴{self.health} 🔵{self.mana}'

    def __repr__(self):
        return str(self)


class Swordsman(Character):
    def __init__(self, name):
        super().__init__(name)
        self._attacks = (
            Attack('Sword slash', DamageType.PHYSICAL, DamageRange.MELEE, 15),
            Attack('Shield bash', DamageType.PHYSICAL, DamageRange.MELEE, 3),
        )

    def attack(self):
        picked_attack = Attack(**choice(self._attacks).__dict__)
        picked_attack.damage += int((randint(-20, 20) / 100) * picked_attack.damage)
        return picked_attack

class Rogue(Character):
    def __init__(self, name):
        super().__init__(name)
        self._attacks = (
            Attack('Bow shot', DamageType.PHYSICAL, DamageRange.RANGE, 5),
            Attack('Poisoned arrow', DamageType.PHYSICAL, DamageRange.RANGE, 10),
            Attack('Dagger stab', DamageType.PHYSICAL, DamageRange.MELEE, 5),
        )

    def attack(self):
        picked_attack = Attack(**choice(self._attacks).__dict__)
        picked_attack.damage += int((randint(-20, 20) / 100) * picked_attack.damage)
        return picked_attack


class Wizard(Character):
        def __init__(self, name):
            super().__init__(name)
            self._attacks = (
                Attack('Fireball', DamageType.FIRE, DamageRange.RANGE, 10),
                Attack('Blizzard', DamageType.ICE, DamageRange.AREA, 7),
                Attack('Charged bolt', DamageType.LIGHTNING, DamageRange.RANGE, 10),
                Attack('Staff bonk', DamageType.PHYSICAL, DamageRange.MELEE, 2),
            )

        def attack(self):
            picked_attack = Attack(**choice(self._attacks).__dict__)
            picked_attack.damage += int((randint(-20, 20) / 100) * picked_attack.damage)
            if picked_attack.type != DamageType.PHYSICAL:
                if self.mana >= picked_attack.damage:
                    self.mana -= picked_attack.damage
                else:
                    return self._attacks[-1]
            return picked_attack


class Monster(Character):
    def __init__(self, name, damage):
        super().__init__(name)
        self._attacks = (
            Attack('Slap', DamageType.PHYSICAL, DamageRange.MELEE, damage),
        )
        self._resist = choice(list(DamageType))

    def attack(self):
        return self._attacks[0]

    def __str__(self):
        return f'{self.__class__.__name__} {self.name} 🔴{self.health} {self.resist.value} resist'
