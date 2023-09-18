import random


class Main:
    def __init__(self):
        self.words = ['Program', 'Container', 'Computer', 'Planet']
        self.choice = random.choice(self.words)
        self.count_word = len(self.choice)
        self.result = ['_' for _ in range(self.count_word)]
        self.res = ''

    def get(self):
        self.ind = 0
        while True:
            self.curd = input('Enter: ')
            if self.curd in self.choice.lower():
                self.i = self.choice.find(self.curd)
                self.result[self.i] = self.curd


a = Main()
print(a.choice)
print(a.result)
a.get()

