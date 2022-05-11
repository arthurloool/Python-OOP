# __Dunder__ methods
# Dunder stands for double underscore methods

class Monster: 

    def __init__(self,health,mana,physical_attack,magic_attack):
        self.health = health
        self.mana = mana
        self.physical_attack = physical_attack
        self.magic_attack = magic_attack

    def __str__(self):
        return 'health: ' + str(self.health) + ' mana: ' + str(self.mana) + ' physical_attack: ' + str(self.physical_attack) + ' magic_attack: ' + str(self.magic_attack)

    def attack(self,damage):
        print('The monster has attacked!')
        print('{} damage was dealt'.format(damage))
        print('Monster health:' + str(Monster.health))

    def move(self,atk_speed):
        print('Attack Speed: {}'.format(atk_speed))


Witch = Monster(5,10,1,10)
Shark = Monster(10,0,8,0)

print(str(Witch))