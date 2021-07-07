import pygame
import random
# -- Global Constants
# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
BROWN = (155,103,60)
# -- Initialise PyGame
pygame.init()
# -- Blank Screen
size = (1000,480)
screen = pygame.display.set_mode(size)
# -- Title of new window/screen
pygame.display.set_caption("My Project")
#Classes
class Player(pygame.sprite.Sprite):
    # Define the constructor for invader
    def __init__(self, x_ref, y_ref, speed_x, speed_y, health, apples):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.image.load('player4.png')
        self.rect = self.image.get_rect()
        # Set the position of the player attributes
        self.rect.x = x_ref
        self.rect.y = y_ref
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.old_x = self.rect.x
        self.old_y = self.rect.y
        self.health = health
        self.apples = apples
    #End Procedure
    def update(self):
        self.old_x = self.rect.x
        self.old_y = self.rect.y
#End Class
class Monster_Draw(pygame.sprite.Sprite):
    def __init__(self, x_ref, y_ref):
        super().__init__()
        self.image = pygame.image.load('monster.png')
        self.rect = self.image.get_rect()
        self.rect.x = x_ref
        self.rect.y = y_ref
class Monster(pygame.sprite.Sprite):
    # Define the constructor for invader
    def __init__(self, x_ref, y_ref, old_x, old_y):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.image.load('monster.png')
        self.rect = self.image.get_rect()
        # Set the position of the player attributes
        self.rect.x = x_ref
        self.rect.y = y_ref
        self.speed_x = random.randint(-2, 2)
        self.speed_y = random.randint(-2, 2)
        self.old_x = self.rect.x
        self.old_y = self.rect.y
    #End Procedure
    def update(self):
        self.rect.x = self.rect.x + self.speed_x
        self.rect.y = self.rect.y + self.speed_y
        monster_brick_hit_list = pygame.sprite.spritecollide(self, brick_group, False)
        monster_window_hit_list = pygame.sprite.spritecollide(self, window_group, False)
        monster_door_hit_list = pygame.sprite.spritecollide(self, closed_door_group, False)
        monster_player_hit_list = pygame.sprite.spritecollide(self, player_sprites_group, False)
        monster_group.remove(self)
        monster_monster_hit_list = pygame.sprite.spritecollide(self, monster_group, False)
        for foo in monster_monster_hit_list:
            self.speed_x = random.randint(-3, 3)
            self.speed_y = random.randint(-3, 3)
            self.rect.x = self.old_x
            self.rect.y = self.old_y
        #Next
        monster_group.add(self)
        for foo in monster_brick_hit_list:
            self.speed_x = 0
            self.speed_y = 0
            self.rect.x = self.old_x
            self.rect.y = self.old_y
            self.speed_x = random.randint(-2, 2)
            self.speed_y = random.randint(-2, 2)
        for foo in monster_window_hit_list:
            self.speed_x = 0
            self.speed_y = 0
            self.rect.x = self.old_x
            self.rect.y = self.old_y
            self.speed_x = random.randint(-2, 2)
            self.speed_y = random.randint(-2, 2)
        for foo in monster_door_hit_list:
            self.speed_x = 0
            self.speed_y = 0
            self.rect.x = self.old_x
            self.rect.y = self.old_y
            self.speed_x = random.randint(-2, 2)
            self.speed_y = random.randint(-2, 2)
        for foo in monster_player_hit_list:
            player.health = player.health - 1
            self.rect.x = self.old_x
            self.rect.y = self.old_y
            self.speed_x = random.randint(-2, 2)
            self.speed_y = random.randint(-2, 2)
            player.speed_x = 0
            player.speed_y = 0
            player.rect.x = player.old_x
            player.rect.y = player.old_y
        if self.rect.x > 610:
            self.speed_x = 0
            self.speed_y = 0
            self.rect.x = self.old_x
            self.rect.y = self.old_y
            self.speed_x = random.randint(-3, 3)
            self.speed_y = random.randint(-3, 3)
        if self.rect.x < 0:
            self.speed_x = 0
            self.speed_y = 0
            self.rect.x = self.old_x
            self.rect.y = self.old_y
            self.speed_x = random.randint(-2, 2)
            self.speed_y = random.randint(-2, 2)
        if self.rect.y > 450:
            self.speed_x = 0
            self.speed_y = 0
            self.rect.x = self.old_x
            self.rect.y = self.old_y
            self.speed_x = random.randint(-2, 2)
            self.speed_y = random.randint(-2, 2)
        if self.rect.y < 0:
            self.speed_x = 0
            self.speed_y = 0
            self.rect.x = self.old_x
            self.rect.y = self.old_y
            self.speed_x = random.randint(-2, 2)
            self.speed_y = random.randint(-2, 2)
        if self.speed_x == 0 and self.speed_y == 0:
            self.speed_x = random.randint(-2, 2)
            self.speed_y = random.randint(-2, 2)
        self.old_x = self.rect.x
        self.old_y = self.rect.y
#End Class
class Map_Block(pygame.sprite.Sprite):
    # Define the constructor for invader
    def __init__(self, color, width, height, x_ref, y_ref):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        # Set the position of the player attributes
        self.rect.x = x_ref
        self.rect.y = y_ref
    #End Procedure
#End Class
class Brick(pygame.sprite.Sprite):
    # Define the constructor for invader
    def __init__(self, x_ref, y_ref):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.image.load('Brick.jpg')
        self.rect = self.image.get_rect()
        # Set the position of the player attributes
        self.rect.x = x_ref
        self.rect.y = y_ref
    #End Procedure
#End Class
class Door(pygame.sprite.Sprite):
    # Define the constructor for invader
    def __init__(self, x_ref, y_ref, state):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.image.load('door.png')
        self.rect = self.image.get_rect()
        # Set the position of the player attributes
        self.rect.x = x_ref
        self.rect.y = y_ref
        self.state = state
    #End Procedure
    def update(self):
        player_door_hit_list = pygame.sprite.spritecollide(self, player_sprites_group, False)
        for foo in player_door_hit_list:
            if self.state == True:
                player.rect.x = player.old_x
                player.rect.y = player.old_y
                player.speed_x = 0
                player.speed_y = 0
                keys = pygame.key.get_pressed()
                if keys[pygame.K_1]:
                    self.state = False
                    self.image = pygame.image.load('opendoor2.png')
                    closed_door_group.remove(self)
                    open_door_group.add(self)
                #End If
            #End If
        #Next
#End Class
class Selector_Left(pygame.sprite.Sprite):
    # Define the constructor for invader
    def __init__(self, x_ref, y_ref):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([5,40])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        # Set the position of the player attributes
        self.rect.x = x_ref
        self.rect.y = y_ref
    #End Procedure
#End Class
class Selector_Right(pygame.sprite.Sprite):
    # Define the constructor for invader
    def __init__(self, x_ref, y_ref):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([5,40])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        # Set the position of the player attributes
        self.rect.x = x_ref
        self.rect.y = y_ref
    #End Procedure
#End Class
class Selector_Top(pygame.sprite.Sprite):
    # Define the constructor for invader
    def __init__(self, x_ref, y_ref, pos_x, pos_y):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([40,5])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        # Set the position of the player attributes
        self.rect.x = x_ref
        self.rect.y = y_ref
        self.pos_x = pos_x
        self.pos_y = pos_y
    #End Procedure
#End Class
class Selector_Bottom(pygame.sprite.Sprite):
    # Define the constructor for invader
    def __init__(self, x_ref, y_ref):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([40,5])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        # Set the position of the player attributes
        self.rect.x = x_ref
        self.rect.y = y_ref
    #End Procedure
#End Class
class Window(pygame.sprite.Sprite):
    # Define the constructor for invader
    def __init__(self, x_ref, y_ref):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.image.load('window.png')
        self.rect = self.image.get_rect()
        # Set the position of the player attributes
        self.rect.x = x_ref
        self.rect.y = y_ref
    #End Procedure
#End Class
class Apple(pygame.sprite.Sprite):
    # Define the constructor for invader
    def __init__(self, x_ref, y_ref):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.image.load('apple.png')
        self.rect = self.image.get_rect()
        # Set the position of the player attributes
        self.rect.x = x_ref
        self.rect.y = y_ref
    #End Procedure
#End Class
# -- Exit game flag set to false
my_game = True
intro = True
map_draw = False
in_game = False
endgame = False
winner_of_own_map = False
loser_of_own_map = False
is_player_there = False
while my_game == True:
    map = [[0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],]
    all_sprites_group = pygame.sprite.Group()
    selector_sprites_group = pygame.sprite.Group()
    map_sprites_group = pygame.sprite.Group()
    draw_sprites_group = pygame.sprite.Group()
    player_sprites_group = pygame.sprite.Group()
    brick_group = pygame.sprite.Group()
    window_group = pygame.sprite.Group()
    door_group = pygame.sprite.Group()
    open_door_group = pygame.sprite.Group()
    closed_door_group = pygame.sprite.Group()
    monster_group = pygame.sprite.Group()
    apple_group = pygame.sprite.Group()
    apple_number = 0
    # -- Manages how fast screen refreshes
    clock = pygame.time.Clock()
    ### -- Game Loop
    while intro == True:
        for item in all_sprites_group:
            item.kill()
        # -- User input and controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
                my_game = False
                endgame = True
            #End If
        #Next event
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            intro = False
            map_draw = True
        #End If
        # -- Game logic goes after this comment
        # -- Screen background is BLACK
        screen.fill(BLACK)
        font = pygame.font.SysFont('ComicSans', 50, True, False)
        text = font.render('Welcome to my Game!', True, WHITE)
        screen.blit(text, [285, 50])
        text = font.render('Press 1 to Draw your Map', True, WHITE)
        screen.blit(text, [250, 100])
        # -- Draw here
        # -- flip display to reveal new position of objects
        pygame.display.flip()
        # - The clock ticks over
        clock.tick(60)
    #End While - End of game loop
    #top selector
    selector_top = Selector_Top(0, 0, 0, 0)
    all_sprites_group.add(selector_top)
    selector_sprites_group.add(selector_top)
    #left selector
    selector_left = Selector_Left(0, 0)
    all_sprites_group.add(selector_left)
    selector_sprites_group.add(selector_left)
    #right selector
    selector_right = Selector_Right(35, 0)
    all_sprites_group.add(selector_right)
    selector_sprites_group.add(selector_right)
    #bottom selector
    selector_bottom = Selector_Bottom(0, 35)
    all_sprites_group.add(selector_bottom)
    selector_sprites_group.add(selector_bottom)
    while map_draw == True:
    # -- User input and controls
        size = (1000, 480)
        screen = pygame.display.set_mode(size)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                map_draw = False
                my_game = False
                endgame = True
            elif event.type == pygame.KEYDOWN: # - a key is down
                if event.key == pygame.K_RIGHT: # - if the left key pressed
                    selector_left.rect.x = selector_left.rect.x + 40
                    selector_right.rect.x = selector_right.rect.x + 40
                    selector_top.rect.x = selector_top.rect.x + 40
                    selector_bottom.rect.x = selector_bottom.rect.x + 40
                    selector_top.pos_x = selector_top.pos_x + 1
                    if selector_left.rect.x > 600:
                        selector_left.rect.x = selector_left.rect.x - 40
                        selector_right.rect.x = selector_right.rect.x - 40
                        selector_top.rect.x = selector_top.rect.x - 40
                        selector_bottom.rect.x = selector_bottom.rect.x - 40
                        selector_top.pos_x = selector_top.pos_x - 1
                if event.key == pygame.K_LEFT: # - if the left key pressed
                    selector_left.rect.x = selector_left.rect.x - 40
                    selector_right.rect.x = selector_right.rect.x - 40
                    selector_top.rect.x = selector_top.rect.x - 40
                    selector_bottom.rect.x = selector_bottom.rect.x - 40
                    selector_top.pos_x = selector_top.pos_x - 1
                    if selector_left.rect.x < 0:
                        selector_left.rect.x = selector_left.rect.x + 40
                        selector_right.rect.x = selector_right.rect.x + 40
                        selector_top.rect.x = selector_top.rect.x + 40
                        selector_bottom.rect.x = selector_bottom.rect.x + 40
                        selector_top.pos_x = selector_top.pos_x + 1
                if event.key == pygame.K_DOWN: # - if the left key pressed
                    selector_left.rect.y = selector_left.rect.y + 40
                    selector_right.rect.y = selector_right.rect.y + 40
                    selector_top.rect.y = selector_top.rect.y + 40
                    selector_bottom.rect.y = selector_bottom.rect.y + 40
                    selector_top.pos_y = selector_top.pos_y + 1
                    if selector_left.rect.y > 440:
                        selector_left.rect.y = selector_left.rect.y - 40
                        selector_right.rect.y = selector_right.rect.y - 40
                        selector_top.rect.y = selector_top.rect.y - 40
                        selector_bottom.rect.y = selector_bottom.rect.y - 40
                        selector_top.pos_y = selector_top.pos_y - 1
                if event.key == pygame.K_UP: # - if the left key pressed
                    selector_left.rect.y = selector_left.rect.y - 40
                    selector_right.rect.y = selector_right.rect.y - 40
                    selector_top.rect.y = selector_top.rect.y - 40
                    selector_bottom.rect.y = selector_bottom.rect.y - 40
                    selector_top.pos_y = selector_top.pos_y - 1
                    if selector_left.rect.y < 0:
                        selector_left.rect.y = selector_left.rect.y + 40
                        selector_right.rect.y = selector_right.rect.y + 40
                        selector_top.rect.y = selector_top.rect.y + 40
                        selector_bottom.rect.y = selector_bottom.rect.y + 40
                        selector_top.pos_y = selector_top.pos_y + 1
                if event.key == pygame.K_1:
                    brick = Brick(selector_left.rect.x, selector_top.rect.y)
                    draw_sprites_group.add(brick)
                    all_sprites_group.add(brick)
                    map[selector_top.pos_x][selector_top.pos_y] = 1
                if event.key == pygame.K_2:
                    window = Window(selector_left.rect.x, selector_top.rect.y)
                    draw_sprites_group.add(window)
                    all_sprites_group.add(window)
                    map[selector_top.pos_x][selector_top.pos_y] = 2
                if event.key == pygame.K_3:
                    door = Door(selector_left.rect.x, selector_top.rect.y, True)
                    draw_sprites_group.add(door)
                    all_sprites_group.add(door)
                    map[selector_top.pos_x][selector_top.pos_y] = 3
                if event.key == pygame.K_4:
                    apple = Apple(selector_left.rect.x, selector_top.rect.y)
                    draw_sprites_group.add(apple)
                    all_sprites_group.add(apple)
                    map[selector_top.pos_x][selector_top.pos_y] = 4
                if event.key == pygame.K_5:
                    for y in range(12):
                        for x in range(16):
                            if map[x][y] == 5:
                                is_player_there = True
                            #End If
                        #Next
                    #Next
                    if is_player_there == False:
                        player = Player(selector_left.rect.x + 5, selector_top.rect.y + 5, 0, 0, 0, 0)
                        draw_sprites_group.add(player)
                        all_sprites_group.add(player)
                        map[selector_top.pos_x][selector_top.pos_y] = 5
                if event.key == pygame.K_6:
                    monster = Monster_Draw(selector_left.rect.x + 5, selector_top.rect.y + 5)
                    draw_sprites_group.add(monster)
                    all_sprites_group.add(monster)
                    map[selector_top.pos_x][selector_top.pos_y] = 6
                if event.key == pygame.K_RETURN:
                    map_draw = False
                    in_game = True
                #End If
        #Next event
        # -- Game logic goes after this comment
        # -- Screen background is BLACK
        screen.fill (WHITE)
        pygame.draw.rect(screen, BLACK, (40, 0, 1, 480))
        pygame.draw.rect(screen, BLACK, (80, 0, 1, 480))
        pygame.draw.rect(screen, BLACK, (120, 0, 1, 480))
        pygame.draw.rect(screen, BLACK, (160, 0, 1, 480))
        pygame.draw.rect(screen, BLACK, (200, 0, 1, 480))
        pygame.draw.rect(screen, BLACK, (240, 0, 1, 480))
        pygame.draw.rect(screen, BLACK, (280, 0, 1, 480))
        pygame.draw.rect(screen, BLACK, (320, 0, 1, 480))
        pygame.draw.rect(screen, BLACK, (360, 0, 1, 480))
        pygame.draw.rect(screen, BLACK, (400, 0, 1, 480))
        pygame.draw.rect(screen, BLACK, (440, 0, 1, 480))
        pygame.draw.rect(screen, BLACK, (480, 0, 1, 480))
        pygame.draw.rect(screen, BLACK, (520, 0, 1, 480))
        pygame.draw.rect(screen, BLACK, (560, 0, 1, 480))
        pygame.draw.rect(screen, BLACK, (600, 0, 1, 480))
        pygame.draw.rect(screen, BLACK, (640, 0, 1, 480))
        pygame.draw.rect(screen, BLACK, (0, 40, 640, 1))
        pygame.draw.rect(screen, BLACK, (0, 80, 640, 1))
        pygame.draw.rect(screen, BLACK, (0, 120, 640, 1))
        pygame.draw.rect(screen, BLACK, (0, 160, 640, 1))
        pygame.draw.rect(screen, BLACK, (0, 200, 640, 1))
        pygame.draw.rect(screen, BLACK, (0, 240, 640, 1))
        pygame.draw.rect(screen, BLACK, (0, 280, 640, 1))
        pygame.draw.rect(screen, BLACK, (0, 320, 640, 1))
        pygame.draw.rect(screen, BLACK, (0, 360, 640, 1))
        pygame.draw.rect(screen, BLACK, (0, 400, 640, 1))
        pygame.draw.rect(screen, BLACK, (0, 440, 640, 1))
        pygame.draw.rect(screen, BLACK, (0, 480, 640, 1))
        pygame.draw.rect(screen, BLACK, (640, 0, 360, 480))
        font = pygame.font.SysFont('ComicSans', 30, True, False)
        text = font.render('Press 1 to place a wall', True, WHITE)
        screen.blit(text, [650, 10])
        text = font.render('Press 2 to place a window', True, WHITE)
        screen.blit(text, [650, 40])
        text = font.render('Press 3 to place a door', True, WHITE)
        screen.blit(text, [650, 70])
        text = font.render('Press 4 to place an apple', True, WHITE)
        screen.blit(text, [650, 100])
        text = font.render('Press 5 to place your player', True, WHITE)
        screen.blit(text, [650, 130])
        text = font.render('Press 6 to place a monster', True, WHITE)
        screen.blit(text, [650, 160])
        text = font.render('Press enter to start the game', True, WHITE)
        screen.blit(text, [650, 190])
        draw_sprites_group.draw(screen)
        selector_sprites_group.draw(screen)
        # -- Draw here
        # -- flip display to reveal new position of objects
        pygame.display.flip()
        # - The clock ticks over
        clock.tick(60)
    #End While - End of game loop
    for y in range(12):
        for x in range(16):
            if map[x][y] == 0:
                map_block = Map_Block(WHITE, 40, 40, x*40, y *40)
                map_sprites_group.add(map_block)
                all_sprites_group.add(map_block)
            #End If
        #Next
    #Next
    for y in range(12):
        for x in range(16):
            if map[x][y] == 1:
                brick = Brick(x*40, y*40)
                map_sprites_group.add(brick)
                all_sprites_group.add(brick)
                brick_group.add(brick)
            #End If
        #Next
    #Next
    for y in range(12):
        for x in range(16):
            if map[x][y] == 2:
                window = Window(x*40, y *40)
                map_sprites_group.add(window)
                all_sprites_group.add(window)
                window_group.add(window)
            #End If
        #Next
    #Next
    for y in range(12):
        for x in range(16):
            if map[x][y] == 3:
                door = Door(x*40, y *40, True)
                map_sprites_group.add(door)
                all_sprites_group.add(door)
                door_group.add(door)
                closed_door_group.add(door)
            #End If
        #Next
    #Next
    for y in range(12):
        for x in range(16):
            if map[x][y] == 4:
                apple = Apple(x*40, y *40)
                map_sprites_group.add(apple)
                apple_group.add(apple)
                all_sprites_group.add(apple)
                apple_number = apple_number + 1
            #End If
        #Next
    #Next
    for y in range(12):
        for x in range(16):
            if map[x][y] == 5:
                player = Player(x*40 + 5, y *40 + 5, 0, 0, 100, 0)
                player_sprites_group.add(player)
                all_sprites_group.add(player)
            #End If
        #Next
    #Next
    for y in range(12):
        for x in range(16):
            if map[x][y] == 6:
                monster = Monster(x*40 + 5, y *40 + 5, x*40 + 5, y*40 + 5)
                map_sprites_group.add(monster)
                all_sprites_group.add(monster)
                monster_group.add(monster)
            #End If
        #Next
    #Next
    while in_game == True:
        # -- User input and controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                in_game = False
                my_game = False
                endgame = True
            #End If
        #Next event
        # -- Game logic goes after this comment
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player.speed_y = -2
            player.rect.y = player.rect.y + player.speed_y
            if player.rect.y < 0:
                player.rect.y = player.rect.y - player.speed_y
        #End If
        if keys[pygame.K_DOWN]:
            player.speed_y = 2
            player.rect.y = player.rect.y + player.speed_y
            if player.rect.y > 450:
                player.rect.y = player.rect.y - player.speed_y
        #End If
        if keys[pygame.K_RIGHT]:
            player.speed_x = 2
            player.rect.x = player.rect.x + player.speed_x
            if player.rect.x > 610:
                player.rect.x = player.rect.x - player.speed_x
        #End If
        if keys[pygame.K_LEFT]:
            player.speed_x = -2
            player.rect.x = player.rect.x + player.speed_x
            if player.rect.x < 0:
                player.rect.x = player.rect.x - player.speed_x
        #End If
        player_brick_hit_list = pygame.sprite.spritecollide(player, brick_group, False)
        for foo in player_brick_hit_list:
            player.rect.x = player.old_x
            player.rect.y = player.old_y
            player.speed_x = 0
            player.speed_y = 0
        player_window_hit_list = pygame.sprite.spritecollide(player, window_group, False)
        for foo in player_window_hit_list:
            player.rect.x = player.old_x
            player.rect.y = player.old_y
            player.speed_x = 0
            player.speed_y = 0
        player_apple_hit_list = pygame.sprite.groupcollide(player_sprites_group, apple_group, dokilla=False, dokillb=True, collided=None)
        for foo in player_apple_hit_list:
            player.apples = player.apples + 1
        all_sprites_group.update()
        if player.apples == apple_number:
            in_game = False
            winner_of_own_map = True
        if player.health < 1:
            in_game = False
            loser_of_own_map = True
        # -- Screen background is BLACK
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLACK, (640, 0, 360, 480))
        map_sprites_group.draw(screen)
        player_sprites_group.draw(screen)
        font = pygame.font.SysFont('ComicSans', 30, True, False)
        text = font.render('Press 1 to open a door', True, WHITE)
        screen.blit(text, [650, 10])
        text = font.render('Health: ' + str(player.health), True, WHITE)
        screen.blit(text, [650, 40])
        text = font.render('Apples: ' + str(player.apples), True, WHITE)
        screen.blit(text, [650, 70])
        # -- Draw here
        # -- flip display to reveal new position of objects
        pygame.display.flip()
        # - The clock ticks over
        clock.tick(60)
    #End While - End of game loop
    while winner_of_own_map == True:
        # -- User input and controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                winner_of_own_map = False
                my_game = False
                endgame = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    winner_of_own_map = False
                    intro = True
                if event.key == pygame.K_ESCAPE:
                    winner_of_own_map = False
                    my_game = False
                    endgame = True
            #End If
        #Next event
        screen.fill(BLACK)
        pygame.draw.rect(screen, BLACK, (640, 0, 360, 480))
        font = pygame.font.SysFont('ComicSans', 100, True, False)
        text = font.render('All Apples Collected!', True, WHITE)
        screen.blit(text, [85, 70])
        text = font.render('You Win!', True, WHITE)
        screen.blit(text, [315, 200])
        font = pygame.font.SysFont('ComicSans', 30, True, False)
        text = font.render('Press enter to return to the home page', True, WHITE)
        screen.blit(text, [250, 330])
        text = font.render('Press escape to quit', True, WHITE)
        screen.blit(text, [360, 360])
        # -- flip display to reveal new position of objects
        pygame.display.flip()
        # - The clock ticks over
        clock.tick(60)
    while loser_of_own_map == True:
        # -- User input and controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loser_of_own_map = False
                my_game = False
                endgame = True
            elif event.type == pygame.KEYDOWN: # - a key is down
                if event.key == pygame.K_RETURN:
                    loser_of_own_map = False
                    intro = True
                if event.key == pygame.K_ESCAPE:
                    loser_of_own_map = False
                    my_game = False
                    endgame = True
            #End If
        #Next event
        screen.fill(BLACK)
        pygame.draw.rect(screen, BLACK, (640, 0, 360, 480))
        font = pygame.font.SysFont('ComicSans', 100, True, False)
        text = font.render('You Are Dead!', True, WHITE)
        screen.blit(text, [200, 70])
        text = font.render('You Lose!', True, WHITE)
        screen.blit(text, [285, 200])
        font = pygame.font.SysFont('ComicSans', 30, True, False)
        text = font.render('Press enter to return to the home page', True, WHITE)
        screen.blit(text, [250, 330])
        text = font.render('Press escape to quit', True, WHITE)
        screen.blit(text, [360, 360])
        # -- flip display to reveal new position of objects
        pygame.display.flip()
        # - The clock ticks over
        clock.tick(60)
if endgame == True:
    pygame.quit()