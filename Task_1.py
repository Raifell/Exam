class Main:
    def __init__(self):
        self.name = input('Select:\n1) - Peperoni\n2) - BBQ\n3) - Gift of Sea\nEnter: ')
        self.dopp = input('Select:\n1) - add cheese\n2) - add tomato\n3) - add mushrooms\n4) - none\nEnter: ') + 'add'
        self.price = self.sort(self.name) + self.sort(self.dopp)
        self.text = (self.text(self.name), self.text(self.dopp))
        self.vir = 'E'

    def __str__(self):
        if self.text[0]:
            self.vir = f'\nName: {self.text[0]}\nDopp: {self.text[1]}\nPrice: {self.price}$'
        return self.vir

    @staticmethod
    def sort(value):
        name = {'1': 20, '2': 30, '3': 40}
        dopp = {'1add': 10, '2add': 15, '3add': 20, '4add': 0}
        if value in name:
            return name[value]
        elif value in dopp:
            return dopp[value]
        else:
            return 0

    @staticmethod
    def text(value):
        name = {'1': 'Peperoni', '2': 'BBQ', '3': 'Gift of Sea'}
        dopp = {'1add': 'Cheese', '2add': 'Tomato', '3add': 'Mushrooms', '4add': 'None'}
        if value in name:
            return name[value]
        elif value in dopp:
            return dopp[value]


class Terminal:
    def __init__(self):
        self.count = self.combine()
        self.overprice = sum([x.price for x in self.count])

    def get_info(self):
        print('Order Details:')
        for x in [z for z in self.count if str(z) != 'E']:
            print(x)
        print(f'\nTotal price: {self.overprice}$')

    @staticmethod
    def combine():
        basket = []
        while True:
            a = Main()
            basket.append(a)
            print(f'Add:{a}') if str(a) != 'E' else print('\nWrong order!')
            cont = input('Another one? Y/N\n')
            if cont.lower().strip() == 'n':
                break
        return basket


a = Terminal()
a.get_info()
