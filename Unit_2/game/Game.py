# Необходимо разработать моделирование игры в виде консольного приложения. Участниками являются Компьютер и Игрок.
# Последовательность ходов определяется случайным образом. У каждого из игроков должно быть одинаковое количество
# здоровья (например 100) и выбор (тоже случайным образом) следующего из шагов:
# 1. должен нанести умеренный урон и имеет небольшой диапазон (например, 18-25)
# 2. должен иметь большой диапазон урона (например 10-35)
# 3. должен исцелить в небольшом диапазоне (в таком же как и в пункте 1)
#
# После каждого действия должно быть напечатано сообщение, которое сообщает что происходило и сколько здоровья
# у Игрока и Компьютера. Когда здоровье Компьютера достигает, например 35 % увеличьте его шанс на излечение.
#
# Игра завершается, если у одного из участников здоровье достигло 0.
import random


class Game:
    def __init__(self, player, AI):
        self.player = player
        self.AI = AI

    def game(self):
        while self.player.health > 0 and self.AI > 0:
            r_move = random.shuffle([self.AI, self.player])
            attacker = r_move[0]
            passive_life = r_move[1]
            r_choice = random.choice(attacker.moves.keys())
            r_choice(passive_life)


      def show_stats(self):
          pass

class Player:

    def __init__(self, name):
        self.is_comp = True
        self.name = name
        self.health = 100
        self.moves = {
            's_hit': self.small_hit,
            'b_hit': self.big_hit,
            'heal': self.heal,
        }

    def small_hit(self):
        low_dmg = random.sample(range(17, 25), 1)
        self.health = self.health - low_dmg

    def big_hit(self):
        high_dmg = random.sample(range(19, 35), 1)
        self.health = self.health - high_dmg

    def heal(self):
        healing = random.sample(range(17, 25), 1)
        self.health = self.health + healing

    def player_health(self):
        if self.health <= 35:
            self.moves['heal1'] = self.heal

        elif self.health >= 60:
            del self.moves[4]

        elif self.health >= 50:
            random.choice(self.small_hit, self.big_hit)

        elif self.health >= 50:
            random.choice(self.small_hit,self.big_hit)
