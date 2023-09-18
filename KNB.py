import random


class Main:
    def __init__(self):
        self.text = 'Greatings, Player!\n1) - Paper\n2) - Rock\n3) - Scissors'
        self.li = ['Paper', 'Rock', 'Scissors']
        self.robot = random.choice(self.li)

    def __str__(self):
        return self.text


class Player(Main):
    def __init__(self):
        self.player = input('\nEnter your choice: ')
        super().__init__()
        self.player_choice = self.find(self.player, self.li)
        self.result = self.find_result(self.robot, self.player_choice)

    def __str__(self):
        return f'Your choice is - {self.player_choice}\nComputer choice is - {self.robot}\nResult: ' \
               f'{str(self.result).capitalize()}'

    @staticmethod
    def find(num, li):
        return li[int(num)-1] if 0 < int(num) < 4 else 'Error'

    @staticmethod
    def find_result(comp, play):
        if comp == 'Paper':
            res = 'lost' if play == 'Rock' else 'tie' if play == 'Paper' else 'win' if play == 'Scissors' else 'Wrong value!'
            return res
        elif comp == 'Scissors':
            res = 'lost' if play == 'Paper' else 'tie' if play == 'Scissors' else 'win' if play == 'Rock' else 'Wrong value!'
            return res
        elif comp == 'Rock':
            res = 'lost' if play == 'Scissors' else 'tie' if play == 'Rock' else 'win' if play == 'Paper' else 'Wrong value!'
            return res
        else:
            res = 'Error'
            return res


class Terminal:
    def __init__(self):
        self.win = 0
        self.lost = 0
        self.ind = None
        self.a = None
        self.b = None

    def get(self):
        while str(self.ind).lower() != 'n':
            self.a = Main()
            print(self.a)
            self.b = Player()
            print(self.b)
            self.win += 1 if self.b.result == 'win' else 0
            self.lost += 1 if self.b.result == 'lost' else 0
            self.ind = input('\nContinue? Y/N: ')

        print(f'\nWin: {self.win}, Lost: {self.lost}')


a = Terminal()
a.get()
