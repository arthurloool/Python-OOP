# Complex Class inheritance
# Parent Class 1
class Monster:
    def __init__(self,hp,mp,**kwargs): # Any extra keyword arguments will be stored as dictionary type data
        self.hp = hp
        self.mp = mp
        super().__init__(**kwargs)
    
    def move(self):
        print('Move')


# Parent Class 2
class Fish:
    def __init__(self,speed,**kwargs):
        self.speed = speed
        super().__init__(**kwargs)

    def move(self):
        print('Swim')

# Child Class
class Shark(Monster,Fish):
    def __init__(self,hp,mp,speed):
        super().__init__(hp = hp,mp = mp,speed = speed) # In order to user super().__init__(**kwargs), keywords required

big_white = Shark(1,2,3)

print(big_white.hp)
print(big_white.mp)
print(big_white.speed)