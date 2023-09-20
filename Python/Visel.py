# -*- coding: utf-8 -*-
import random


class Main:
    def __init__(self):
        self.count_word = ['программа', 'компьютер', 'монитор']
        self.word = random.choice(self.count_word)
        self.choice = []
        self.worder = []
        self.var = 5
        self.user = None

    def get(self):
        print('Отгадай слово!')
        while self.var != 0:
            print('Осталось попыток: ', self.var)
            for x in self.word:
                if x in self.choice:
                    self.worder.append(x)
                else:
                    self.worder.append('_')
            print(''.join(self.worder).capitalize())
            self.worder = []
            self.user = input('\nВедите букву: ')
            if self.user in self.word:
                self.choice.append(self.user)
            else:
                self.var -= 1

            if len(self.word) == len(self.choice):
                print('Вы выиграли!')
                break
        if self.var == 0:
            print('Вы проиграли!')


a = Main()
print(a.word.lower())
a.get()
