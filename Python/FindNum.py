import random


class Main:
    def __init__(self):
        self.num = random.randint(1, 20)

    def operation(self):
        while True:
            self.inp = input('Enter numder: ')
            if float(self.inp) == self.num:
                print(f'You win, the nubber is {self.inp}')
                break
            elif float(self.inp) > self.num:
                print(f'The number is low than {self.inp}')
            elif float(self.inp) < self.num:
                print(f'The number is high than {self.inp}')


a = Main()
a.operation()
