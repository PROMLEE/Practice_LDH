from random import*
#일반유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed=speed
        print("{0} 유닛이 생성되었습니다.".format(name))

    def move(self,location):
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -=damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name,self.hp))
        if self.hp<=0:
            print("{0} : 파괴되었습니다.".format(self.name))

class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
    
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))
    
class  Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    def stimpack(self):
        if self.hp>10:
            self.hp-=10
            print("{0}: 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

class Tank(AttackUnit):
    #시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능, 이동불가.
    seize_developed=False #시즈모드 개발여부
    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode=False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return

        if  self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *=2
            self.seize_mode=True
        else:
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /=2
            self.seize_mode=False

#드랍쉽 : 공중 유닛, 수송기 마린/파이어뱃/탱크 등을 수송 공격불가
class flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))

#공중 공격 유닛 클래스
class flyableAttackUnit(AttackUnit, flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0,damage)#지상speed 0
        flyable.__init__(self, flying_speed)

    def move(self, location):
        self.fly(self.name, location)

# #발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사
# valkyrie=flyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")
#벌쳐 : 지상 유닛, 기동성이 좋음
# vulture= AttackUnit("벌쳐", 80, 10,20)
# #배틀크루저 : 공중 유닛 ,체력도 굉장히 좋음, 공격력도 좋음
# battlecruiser= flyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# battlecruiser.move("9시")

#건물
class Wraith(flyableAttackUnit):
    def __init__(self):
        flyableAttackUnit.__init__(self, "레이스", 80, 20 , 5)
        self.clocked=False
    
    def clocking(self):
        if self.clocked ==True:
            print("{0} : 클로킹 모드 해제합니다.".format(self.name))
            self.clocked=False
        else:
            print("{0} : 클로킹 모드 설정합니다.".format(self.name))
            self.clocked=True

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("Player : gg")
    print("[Player]님이 게임에서 퇴장하셨습니다.")

#실제 게임 진행
game_start()

m1= Marine()
m2=Marine()
m3=Marine()

t1=Tank()
t2=Tank()

w1=Wraith()

attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

#전군 이동
for unit in attack_units:
    unit.move("1시")

Tank.seize_developed = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

for unit in attack_units:
    unit.attack("1시")

for unit in attack_units:
    unit.damaged(randint(5,21))

game_over()

