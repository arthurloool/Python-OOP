# Simple Class inheritance
# Parent Class
class Monster:
    def __init__(self,health,power):
        self.health = health
        self.power = power

    def damage(self):
        self.damage = 10
        print('Damaged : {}'.format(self.damage))

# Child Class: Shark
class Shark(Monster):
    def __init__(self,speed,health,power):
        super().__init__(health,power)
        self.speed = speed
    
    def damage(self):
        self.damage = 15
        print('Bitten: {}'.format(self.damage))

shark = Shark(speed = 120, health = 100, power = 100)

print(shark.speed)
print(shark.health)
shark.damage()