# 게임 조건
# 캐릭터는 화면 가장 아래에 위치, 좌우로만 이동 가능
# 캐릭터가 똥을 피하면 다음 똥이 다시 떨어짐
# 캐릭터가 똥과 충돌하면 게임 종료
# FPS는 30으로 고정

# 게임 이미지
# 캐릭터 : 640 * 480(세로*가로) - background.png
# 캐릭터 : 70 * 70 - character.png
# 똥 : 70 * 70 - enemy.png
import pygame
import random
pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("똥 피하기")

clock = pygame.time.Clock()

background = pygame.image.load(
    "D:/LDH/visual studio LDH/study PYTHON/Game/dong_rain/background.png")

character = pygame.image.load(
    "D:/LDH/visual studio LDH/study PYTHON/Game/dong_rain/character.png")

character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]

character_x_pos = screen_width/2 - character_width/2
character_y_pos = screen_height - character_height

to_x = 0

character_speed = 0.6

dong = pygame.image.load("D:/LDH/visual studio LDH/study PYTHON/Game/dong_rain/dong.png")
dong_size = dong.get_rect().size
dong_width = dong_size[0]
dong_height = dong_size[1]
dong_x_pos = random.randint(0, screen_width-dong_width)
dong_y_pos = -character_height

game_font = pygame.font.Font(None, 40)
end_font = pygame.font.Font(None, 70)
start_ticks = pygame.time.get_ticks()


running = True

# ==========================================================
while running:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_LEFT:
                to_x -= character_speed

        if event.type ==pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key ==pygame.K_RIGHT:
                to_x = 0

    dong_y_pos += character_speed*40

    character_x_pos += to_x * dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if dong_y_pos >= screen_height:
        dong_y_pos = -dong_height
        dong_x_pos = random.randint(0,screen_width-dong_width)

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    dong_rect = dong.get_rect()
    dong_rect.left = dong_x_pos
    dong_rect.top = dong_y_pos

    if character_rect.colliderect(dong_rect):
        end_game_time = (pygame.time.get_ticks()-start_ticks)/1000
        end_game = game_font.render(str(int(end_game_time)),True, (255,255,255))
        screen.blit(end_game, (20,20))
        print("충돌했어요")
        running = False

    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(dong, (dong_x_pos, dong_y_pos))


    elapsed_time = (pygame.time.get_ticks()-start_ticks)/1000
    timer = game_font.render(str(int(elapsed_time)), True, (255,255,255))
    screen.blit(timer, (10, 10))

    pygame.display.update()


end_game_time = (pygame.time.get_ticks()-start_ticks)/1000
end_game = end_font.render(str(end_game_time)+"sec",True, (255,0,0))
game_over = end_font.render("Game Over", True, (255,0,0))
screen.blit(end_game, (screen_width/2-100 , screen_height/2-50))
screen.blit(game_over, (screen_width/2-130 , screen_height/2))

pygame.display.update()

pygame.time.delay(2000)
pygame.quit()