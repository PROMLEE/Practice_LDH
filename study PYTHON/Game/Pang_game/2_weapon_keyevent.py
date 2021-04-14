# project) 오락실 pang 게임 만들기
# [게임조건]
# 캐릭터는 화면 아래에 위치, 좌우로만 이동 가능
# 스페이스를 누르면 무기를 쏘아 올림
# 큰 공 1개가 나타나서 바운스
# 무기에 닿으면 공은 작은 크기 2개로 분할, 가장 작은 크기의 공은 사라짐
# 모든 공을 없애면 게임 종료(성공)
# 캐릭터는 공에 닿으면 게임 종료(실패)
# 시간 제한 99초 초과 시 게임 종료(실패)
# FPS는 30으로 고정(필요시 speed값을 조정)

# [게임 이미지]
# 배경 : 640 * 480(가로, 세로) - background.png
# 무대 : 640 * 50 - stage.png
# 캐릭터 : 60 * 33 - character.png
# 무기 : 20 * 430 - weapon.png
# 공 : 160 * 160, 80 * 80, 40 * 40, 20 * 20 - balloon1.png ~ balloon4.png
import pygame
import os
pygame.init()

screen_width = 640  # 배경화면 가로
screen_height = 480  # 배경화면 세로
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("pang 게임")

clock = pygame.time.Clock()  # fps

# 1. 사용자 게임 초기화(배경화면, 게임 이미지, 좌표, 속도, 폰트 등)

# 배경이미지 불러오기
current_path = os.path.dirname(__file__)  # 현재 파일의 위치 반환
image_path = os.path.join(current_path, "images")
# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))
# 스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]
# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width/2-character_width/2
character_y_pos = screen_height-stage_height-character_height

# 무기 만들기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]
weapon_height = weapon_size[1]
# 무기는 한 번에 여러 발 발사 가능
weapons = []
# 무기 이동 속도
weapon_speed = 10

balloon1 = pygame.image.load(os.path.join(image_path, "balloon1.png"))
balloon2 = pygame.image.load(os.path.join(image_path, "balloon2.png"))
balloon3 = pygame.image.load(os.path.join(image_path, "balloon3.png"))
balloon4 = pygame.image.load(os.path.join(image_path, "balloon4.png"))

# 이동할 거리
character_to_x = 0
# 이동 속도
character_speed = 5
# 폰트 정의

# 총 시간

# 시작 시간 정보

# 이벤트 루프
running = True
while running:
    dt = clock.tick(60)
# ---------------------------------------------------------------------------------------
# 2. 이벤트 처리 (키보드 , 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:  # 무기발사
                weapon_x_pos = character_x_pos + character_width/2 - weapon_width/2
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0
# -------------------------------------------------------------------------------------
# 3. 게임 캐릭터 위치 정의
    character_x_pos += character_to_x
    #  경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 무기 위치 조정
    # 100, 200 -> 180, 160, 140 ...
    # 500, 200 -> 180, 160, 140 ...
    weapons = [[w[0], w[1] - weapon_speed] for w in weapons]
    # 천장에 닿은 무기 없애기
    weapons = [[w[0], w[1]] for w in weapons if w[1] > 0] 
    # weapon_heigt 가 0보다 큰 항목만 생존
# ----------------------------------------------------------------------------------
# 4. 충돌 처리
    # 충돌 처리

    # 충돌 체크

# -----------------------------------------------------------------------------------
# 5. 화면에 그리기
    screen.blit(background, (0, 0))
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()  # 게임화면 다시 그리기 !!!
# pygame 대기
# pygame.time.delay(2000)  # 2초 정도 대기 (ms)
# pygame종료
pygame.quit()
