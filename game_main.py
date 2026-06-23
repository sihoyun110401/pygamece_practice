import pygame # type: ignore

# reset
pygame.init()

# screen size
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))

# title
pygame.display.set_caption("test")

# FPS
clock = pygame.time.Clock()

# load background image
background = pygame.image.load("C:/Users/user/Desktop/pygame/assets/bg.png")

# load sprite(not drink)
character = pygame.image.load("C:/Users/user/Desktop/pygame/assets/cha.png")
character_size = character.get_rect().size # get image size 
character_width = character_size[0] # character width
character_height = character_size[1] # character height
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

# coord to move
to_x = 0
to_y = 0

# speed
character_speed = 0.5

# enemy
enemy = pygame.image.load("C:/Users/user/Desktop/pygame/assets/ene.png")
enemy_size = enemy.get_rect().size # get image size 
enemy_width = enemy_size[0] # enemy width
enemy_height = enemy_size[1] # enemy height
enemy_x_pos = (screen_width / 2) - (enemy_width / 2)
enemy_y_pos = (screen_height / 2) - (enemy_height / 2)

# define font
game_font = pygame.font.Font(None, 40) # summon font (font, size)

# total time
total_time = 10

# calculate time
start_ticks = pygame.time.get_ticks() # get tick

# event loop
running = True # is game running?
while running:
    dt = clock.tick(30) # set fps

    print("fps : " + str(clock.get_fps()))

    for event in pygame.event.get(): # which event did happen?
        if event.type == pygame.QUIT: # did the window closed?
            running = False
    
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_a: 
                to_x -= character_speed
            elif event.key == pygame.K_d: 
                to_x += character_speed
            elif event.key == pygame.K_w: 
                to_y -= character_speed
            elif event.key == pygame.K_s: 
                to_y += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                to_x = 0
            elif event.key == pygame.K_w or event.key == pygame.K_s:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # garo
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    
    # sero
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # rect update for collision
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # check collision
    if character_rect.colliderect(enemy_rect):
        print("=======================")
        print("")
        print("게임 종료 사유: 적과 충돌")
        print("")
        print("=======================")
        running = False

    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    # insert timer
    # calculate elapsed time
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # (ms) / 1000 = (s)

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255)) # texts to print, True, text color
    screen.blit(timer, (10, 10))

    # time 0 = exit
    if total_time - elapsed_time <= 0:
        print("=======================")
        print("")
        print("게임 종료 사유: 타임 아웃")
        print("")
        print("=======================")
        running = False

    pygame.display.update()

# wait two seconds
pygame.time.delay(2000)

pygame.quit()