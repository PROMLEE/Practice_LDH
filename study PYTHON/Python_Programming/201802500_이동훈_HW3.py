from random import randint


class Player:
    def __init__(self, v):
        self.name = v
        self.balance = 5000
        self.place = 0
        self.Lose = False

    def move(self, n):
        self.place += n
        if self.place > 9:
            self.place -= 10

    def pay_balance(self, n):
        self.balance -= n

    def get_balance(self, n):
        self.balance += n


class City:
    def __init__(self, v):
        self.name = v
        self.owner = 'empty'
        self.purchase = 300
        self.toll = 600

    def arrival(self, player):
        if self.name == 'start':
            print(self.name)
            print('Nothing happens')
            return
        if self.owner == 'empty':
            print(self.name, '(%s)' % self.owner)
            if player.balance >= self.purchase:
                player.pay_balance(self.purchase)
                self.owner = player
                print(player.name, 'buys', self.name)
            else:
                print('can\'t buy', self.name)
        elif player != self.owner:
            print(self.name, '(%s)' % self.owner.name)
            if player.balance >= self.toll:
                print('pay toll')
                player.pay_balance(self.toll)
                self.owner.get_balance(self.toll)
            else:
                print('can\'t pay toll')
                player.Lose = True
        else:
            print(self.name, '(%s)' % self.owner.name)
            print('Nothing happens')


def print_board():
    print('='*75)
    for i in range(5, 10):
        t = board[i]
        if t.owner != 'empty':
            result = t.name + '(' + t.owner.name[-1] + ')'
        else: result = t.name
        if i != 9: result += ' →'
        else: result += '  '
        print('%15s' % result, end='')
    print('\n%6s' % '', end='')
    for i in range(5, 10):
        if Player1.place == i and Player2.place == i:
            print('%6s' % '(1)(2)', end='')
        elif Player1.place == i: print('%6s' % '(1)', end='')
        elif Player2.place == i: print('%6s' % '(2)', end='')
        else: print('%6s' % '', end='')
        print('%9s' % '', end='')
    print('\n%12s' % '↑', '%57s' % '↓')
    for i in range(4, -1, -1):
        t = board[i]
        if t.owner != 'empty':
            result = t.name + '(' + t.owner.name[-1] + ')'
        else: result = t.name
        if i != 0: result += ' ←'
        else: result += '  '
        print('%15s' % result, end='')
    print('\n%6s' % '', end='')
    for i in range(4, -1, -1):
        if Player1.place == i and Player2.place == i:
            print('%6s' % '(1)(2)', end='')
        elif Player1.place == i: print('%6s' % '(1)', end='')
        elif Player2.place == i: print('%6s' % '(2)', end='')
        else: print('%6s' % '', end='')
        print('%9s' % '', end='')
    print('\n','='*75, sep ='')


Player1 = Player('player 1')
Player2 = Player('player 2')
Start = City('start')
Seoul = City('Seoul')
Tokyo = City('Tokyo')
Sydney = City('Sydney')
La = City('LA')
Cairo = City('Cairo')
Phuke = City('Phuke')
New_delhi = City('New delhi')
Hanoi = City('Hanoi')
Paris = City('Paris')
board = [Start, Seoul, Tokyo, Sydney, La, Cairo, Phuke, New_delhi, Hanoi, Paris]
turn = Player1
for i in range(30):
    print('★  turn', i+1)
    dice = randint(1, 6)
    print(turn.name, ':', dice)
    turn.move(dice)
    print_board()
    board[turn.place].arrival(turn)
    print(Player1.name, '\'s balance is ', Player1.balance, sep='')
    print(Player2.name, '\'s balance is ', Player2.balance, sep='')
    if turn.Lose:
        break
    if turn == Player1:
        turn = Player2
    else:
        turn = Player1
    print('◈'*75)
if Player1.balance > Player2.balance:
    print('Winner is player 1')
elif Player1.balance < Player2.balance:
    print('Winner is player 2')
else:
    print('Draw!')