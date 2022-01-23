class Monster:
    def __init__(self, color, heads):
        self.color = color
        self.heads = heads


# Create some real monster
fogthing = Monster("Black", 5)
mournsnake = Monster("Yellow", 10)
tangleface = Monster("white", 15)

# Check whether those monsters got different existence in memory or not
print('I have ' + str(fogthing.heads) + ' heads and I\'m ' + fogthing.color)
print('I also have ' + str(mournsnake.heads) + ' heads and I\'m ' + mournsnake.color)
print('I got ' + str(tangleface.heads) + ' heads and I\'m ' + tangleface.color)


# init method
class Monster:
    def __init__(self, color, heads):
        self.color = color
        self.heads = heads

    @staticmethod
    def attack():
        print("just attacked a hero , Boyyyyyyyyyyyyahhhhhhhh!!!")


mournsnake = Monster("Yellow", 4)
print('i am a ' + str(mournsnake.heads) + ' ' 'headed monsters')
mournsnake.attack()


# inheritance


class Monster:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def attack(self):
        print('I am attacking...')
        print('hey my name is' + str(self.name) + 'and my color is ' + str(self.color))


class Fogthing(Monster):

    @staticmethod
    def make_sound():
        print('Grrrrrrr\n')


class Mournsnake(Monster):

    @staticmethod
    def make_sound():
        print('Hiiiissssshhhhh\n')


fogthing = Fogthing("Fogthing", "Yellow")
fogthing.attack()
fogthing.make_sound()

mournsnake = Mournsnake("Mournsnake", "Red")
mournsnake.attack()
mournsnake.make_sound()
