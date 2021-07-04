import random


class LotoCard:
    def __init__(self, player_type):
        self.player_type = player_type
        self._card = [
            [],
            [],
            []
        ]
        self._MAX_NUMBER = 90
        self._MAX_NUMBER_IN_CARD = 15
        self._numbers_stroked = 0
        NEED_SPACES = 4
        NEED_NUMBERS = 5
        self._numbers = random.sample(range(1, self._MAX_NUMBER), self._MAX_NUMBER_IN_CARD)

        for line in self._card:
            for _ in range(NEED_SPACES):
                line.append(' ')
            for _ in range(NEED_NUMBERS):
                line.append(self._numbers.pop())


        def check_sort_item(item):
            if isinstance(item, int):
                return item
            else:
                return random.randint(1, self._MAX_NUMBER)

        for index, line in enumerate(self._card):
            self._card[index] = sorted(line, key=check_sort_item)

    class LotoGame:
        def start_game(self, player, computer):
            i = 0
            while i == 0:
                p_card_str = ' \n '.join([' '.join(map(str, line)) for line in player._card])
                c_card_str = ' \n '.join([' '.join(map(str, line)) for line in computer._card])
                p_card_str = ' ' + p_card_str + ' '
                c_card_str = ' ' + c_card_str + ' '
                num = random.sample(range(1, player._MAX_NUMBER), player._MAX_NUMBER_IN_CARD)
                player_point = 0
                computer_point = 0
                for step in enumerate(num):
                    print('__________________________')
                    print(p_card_str)
                    print('__________________________')
                    print(c_card_str)
                    print('__________________________')
                    round = input(f'Хотите зачеркнуть число {step[1]} ? y/n: ')
                    if round == 'y':
                        if f' {step[1]} ' not in p_card_str:
                            print('Вы проиграли, данного числа нет в вашем билете')
                            break
                        else:
                            p_card_str = p_card_str.replace(f' {step[1]} ', ' - ')
                            player_point += 1
                    elif round == 'n':
                        if f' {step[1]} ' in p_card_str:
                            print('Вы не зачеркнули число и проиграли')
                            break
                    if f' {step[1]} ' in c_card_str:
                        c_card_str = c_card_str.replace(f' {step[1]} ', ' - ')
                        computer_point += 1
                i += 1
                print(f'Игрок {human.player_type} набрал {player_point} очков')
                print(f'Компьютер {computer.player_type} набрал {computer_point} очков')


human = LotoCard('Илья')
computer = LotoCard('R2D2')
game = LotoCard.LotoGame()
game.start_game(human, computer)
