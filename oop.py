import random

class Person:

    def __init__(self, name, age=10000, health=100):
        self.name = name
        self.age = age
        self.health = health
        self.crit_chance = random.randint(0,5)/100
    
    def get_info(self):
        return f'My name is {self.name}, and I\'m {self.age} years old.'

    def hit(self, other):
        damage = random.randint(5, 20)
        other.health -= damage

    def is_dead(self):
        return self.health <= 0

class Player(Person):

    def __init__(self, name, age):
        super().__init__(name, age)

    def hit(self, other):
        damage = random.randint(15,20)
        if self.crit_chance > 0.03:
            damage *= 2 
            print(f'Critical! Damage:{damage}')
        other.health -= damage

class Enemy(Person):

    def __init__(self, name=''):
        random_name = random.choice(['Joker', 'Two-face', 'Penguin'])
        super().__init__(random_name)

class Game:

    def __init__(self):
        player_name = input("Player give me your name: ")
        player_age = input(f"{player_name} give me your age: ")

        self.player = Player(player_name, player_age)
        self.enemy = Enemy()

    def start_game(self):
        while not self.player.is_dead() and not self.enemy.is_dead():
            answer = input(f'{self.player.name} hit or quit? (h/q)')

            if answer == 'Q' or answer == "q":
                print(f'You lost by quitting!')
                exit()
            elif answer == 'H' or answer == 'h':
                self.player.hit(self.enemy)
            else:
                continue

            self.enemy.hit(self.player)

            print(f'Your health: {self.player.health} \nEnemy health: {self.enemy.health}')
        
        if self.player.is_dead():
            print("You lost!")
        else:
            print("YOU WON")

game = Game()
game.start_game()