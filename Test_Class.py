class Monster: # Class is blueprint for an object
    
    # Variable inside Class is called attributes
    health = 100
    magic = 100

    # Function inside Class is called methods
    # Calling method require a parameter at the beginning as a reference to the class. Else error occur.
    # In this case, the parameter is called self.
    # The first parameter used for passing the local variable inside the class into the method.
    # After the first parameter, multiple usefull parameter can be added inside the method.
    def attack(self,damage):
        print('The monster has attacked!')
        print('{} damage was dealt'.format(damage))
        print('Monster health:' + str(Monster.health))

    def move(self,atk_speed):
        print('Attack Speed: {}'.format(atk_speed))

shark = Monster() # Object

print(shark.health) # Calling method from the Class Monster

shark.attack(20) # The value passed into the damage parameter

shark.move(1)