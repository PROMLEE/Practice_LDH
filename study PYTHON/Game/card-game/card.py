import pgzrun
import math
import random 

WIDTH = 963 
HEIGHT = 464

CARD_WIDTH = 71
CARD_HEIGHT = 96
GAP = 20
	
ROWMAX = 4
COLMAX = 13
	
class CardTile:
  def __init__(self, x, y, w, h):
    self.x = x
    self.y = y
    self.width = w
    self.height = h

  def contains(self, px, py):
    return self.x < px and px < self.x+self.width and self.y < py and py < self.y+self.height

cardNames = [
  "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "cj", "cq", "ck",
  "d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10", "dj", "dq", "dk",
  "s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "sj", "sq", "sk",
  "h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9", "h10", "hj", "hq", "hk"
  ]

cardSprites = [Actor(card) for card in cardNames]
cardSpritesDic = {}
for card in cardNames:
  cardSpritesDic[card] = Actor(card)
cardSpritesDic["back"] = Actor("b1fv")

WHITE = (255,255,255)
BACK_GROUND = (0x00, 0x66, 0x33)


TOP_LEFT = 0
CW2 = CARD_WIDTH / 2
CH2 = CARD_HEIGHT / 2

tile2d = [None]*COLMAX*ROWMAX
for i in range(ROWMAX):
  for j in range(COLMAX):
    tile2d[i*COLMAX+j] = CardTile(j*CARD_WIDTH+GAP, i*CARD_HEIGHT+GAP, CARD_WIDTH, CARD_HEIGHT)

cardStatus = cardNames[:]
cardStatusOpen = [False]*COLMAX*ROWMAX

def suffle(count):
  for _ in range(count):
    r1 = math.floor(random.random() * ROWMAX)
    r2 = math.floor(random.random() * ROWMAX)
    c1 = math.floor(random.random() * COLMAX)
    c2 = math.floor(random.random() * COLMAX)
    card1 = cardStatus[r1*COLMAX + c1]
    cardStatus[r1*COLMAX + c1] = cardStatus[r2*COLMAX + c2]
    cardStatus[r2*COLMAX + c2] = card1

turn = True
white = (255,255,255)
first_pick = (255,165,0)
second_pick = (255,0,0)
A_score = 0
B_score = 0
playerA = "Player A: "
A_color = first_pick
playerB = "Player B: "
B_color = white

# 두 플레이어의 차례를 정한다.
def turn_change():
  global turn
  global A_color, B_color
  global first_pick, second_pick, white
  if turn:
    if A_color == first_pick:
      A_color = second_pick
    elif A_color == second_pick:
      A_color = white
      B_color = first_pick
      turn = not turn
  else:
    if B_color == first_pick:
      B_color = second_pick
    elif B_color == second_pick:
      B_color = white
      A_color = first_pick
      turn = not turn

# 두 플레이어의 점수를 업데이트한다.
def score_update(a):
  global A_score, B_score, turn
  if cardStatus[a[0]][1] == cardStatus[a[1]][1]:
    if turn == False:
      A_score += 1
    elif turn == True:
      B_score += 1


def draw():
  screen.fill(WHITE)
  screen.draw.filled_rect(Rect(TOP_LEFT,TOP_LEFT,TOP_LEFT+WIDTH,TOP_LEFT+HEIGHT),BACK_GROUND)
  screen.draw.text(playerA+str(A_score),(91,420),color = A_color)
  screen.draw.text(playerB+str(B_score),(517,420), color = B_color)
  for loc, tile in enumerate(tile2d):
    card = cardStatus[loc]
    isopen = cardStatusOpen[loc]
    if tile2d[loc]!=None:
      sprite = cardSpritesDic[card] if isopen else cardSpritesDic["back"]
      sprite.pos = tile.x+CW2, tile.y+CH2
      sprite.draw()

# 현재 뒤집혀 있는 카드의 위치를 리턴.
def find_true():
  a = []
  for i in range(len(cardNames)):
    if cardStatusOpen[i] == True:
      a.append(i)
  return a

# 뒤집혀있는 두 카드가 같으면 없앤다.
def update():
  a = find_true()
  if len(a) == 2:
    clock.schedule(roll_back, 1)
    if cardStatus[a[0]][1] == cardStatus[a[1]][1]:
      tile2d[a[0]] = None
      tile2d[a[1]] = None

# 뒤집혀있는 두 카드를 다시 뒤집는다.
def roll_back():
  a = find_true()
  if len(a) == 2:
    for i in a:
      cardStatusOpen[i] = not cardStatusOpen[i]
  clock.unschedule(roll_back)

def find_mouse_point_tile(px, py):
  for i, ti in enumerate(tile2d):
    try:
      if ti.contains(px, py):
        return i
    except AttributeError:
      continue
  return -1

def on_mouse_down(pos):
  a = find_true()
  if len(a)<=1:
    px, py = pos
    pos = find_mouse_point_tile(px, py)
    if pos == -1:
      pass
    elif pos not in a:
      cardStatusOpen[pos] = not cardStatusOpen[pos]
      turn_change()
    a = find_true()
    if len(a)==2:
      score_update(a)
  return pos

suffle(1000)
pgzrun.go()