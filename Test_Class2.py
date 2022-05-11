# Multiple Class interaction
class Monster:
    def __init__(self,func):
        self.func = func

class Attack:

    def bite(self):
        print('Bite')

    def slash(self):
        print('Slash')

    def kick(self):
        print('Kick')


Shark = Monster(func = Attack().bite)

Shark.func()