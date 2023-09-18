# -*- coding: utf-8 -*-
import random


class Main:
    def __init__(self):
        self.questions = [
            ['Название великого дома внутренней сферы, символом которого является меч, на фоне солнца?',
             ['1) - Дом Штайнер', '2) - Дом Дайвион', '3) - Дом Ляо'], 2],
            ['К какому клану принадлежит Наташа Керенская?', ['1) - Клан Волка', '2) - Клан Нефритового Сокола',
                                                              '3) - Клан Призрачного Медведя'], 2],
            ["Паладином какого бога является Леди Арибет Де'тильморанд?", ['1) - Морн', '2) - Латандер', '3) - Тир'], 3]
        ]

    def user(self):
        win = 0
        while self.questions:
            self.count = random.choice(self.questions)
            self.questions.remove(self.count)
            print(self.count[0])
            print(*self.count[1], sep='\n')
            while True:
                self.us = input('Введите номер ответа: ')
                if int(self.us) == self.count[2]:
                    print('Правильный ответ!')
                    win += 1
                    break
                else:
                    print('Не правильный ответ!')
                    break
        print('\nКонец')
        print(f'Правильных ответов {win}')



a = Main()
a.user()
