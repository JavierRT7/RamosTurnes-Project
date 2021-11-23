import pygame
import random
# -- Global Constants
# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
BROWN = (155,103,60)
GREY = (140, 143, 141)
# -- Initialise PyGame
pygame.init()
# -- Blank Screen
size = (1000,480)
screen = pygame.display.set_mode(size)
# -- Title of new window/screen
pygame.display.set_caption("My Project")
#Classes
class Player(pygame.sprite.Sprite):
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
        if demo_game == True:
            for foo in monster_player_hit_list:
                player.rect.x = player.old_x
                player.rect.y = player.old_y
                player.health = player.health - 1
                self.rect.x = self.old_x
                self.rect.y = self.old_y
                player.speed_x = random.randint(-2, 2)
                player.speed_y = random.randint(-2, 2)
                self.speed_x = random.randint(-2, 2)
                self.speed_y = random.randint(-2, 2)
        else:
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
        if self.rect.x - 150 > player.rect.x or self.rect.x + 150 < player.rect.x or self.rect.y - 150 > player.rect.y or self.rect.y + 150 < player.rect.y:
            drawing_group.remove(self)
        else:
            drawing_group.add(self)
        for sprite in brick_left_group:
            if self.rect.x < sprite.rect.x:
                drawing_group.remove(self)
        for sprite in brick_right_group:
            if self.rect.x > sprite.rect.x:
                drawing_group.remove(self)
        for sprite in brick_up_group:
            if self.rect.y > sprite.rect.y:
                drawing_group.remove(self)
        for sprite in brick_down_group:
            if self.rect.y < sprite.rect.y:
                drawing_group.remove(self)
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
    def update(self):
        self.image.fill(WHITE)
        if self.rect.x - 150 > player.rect.x or self.rect.x + 150 < player.rect.x or self.rect.y - 150 > player.rect.y or self.rect.y + 150 < player.rect.y:
            self.image.fill(GREY)
        else:
            self.image.fill(WHITE)  
        for sprite in brick_left_group:
            if self.rect.x < sprite.rect.x:
                self.image.fill(GREY)
        for sprite in brick_right_group:
            if self.rect.x > sprite.rect.x:
                self.image.fill(GREY)
        for sprite in brick_up_group:
            if self.rect.y > sprite.rect.y:
                self.image.fill(GREY)
        for sprite in brick_down_group:
            if self.rect.y < sprite.rect.y:
                self.image.fill(GREY)
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
    def update(self):
        brick_left_group.remove(self)
        brick_right_group.remove(self)
        brick_up_group.remove(self)
        brick_down_group.remove(self)
        if self.rect.x > player.rect.x and self.rect.x - 150 < player.rect.x and (self.rect.y > player.rect.y - 40 and self.rect.y < player.rect.y + 40):
            brick_right_group.add(self)
        elif self.rect.x < player.rect.x and self.rect.x + 150 > player.rect.x and (self.rect.y > player.rect.y - 40 and self.rect.y < player.rect.y + 40):
            brick_left_group.add(self)
        elif self.rect.y > player.rect.y and self.rect.y - 150 < player.rect.y and (self.rect.x > player.rect.x - 40 and self.rect.x < player.rect.x + 40):
            brick_up_group.add(self)
        elif self.rect.y < player.rect.y and self.rect.y + 150 > player.rect.y and (self.rect.x > player.rect.x - 40 and self.rect.x < player.rect.x + 40):
            brick_down_group.add(self)
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
        if demo_game == True:
            for foo in player_door_hit_list:
                if self.state == True:
                    self.state = False
                    self.image = pygame.image.load('opendoor2.png')
        else:
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
        if self.state == False:
            brick_left_group.remove(self)
            brick_right_group.remove(self)
            brick_up_group.remove(self)
            brick_down_group.remove(self)
            if self.rect.x > player.rect.x and self.rect.x - 150 < player.rect.x and (self.rect.y > player.rect.y - 40 and self.rect.y < player.rect.y + 40):
                brick_right_group.add(self)
            elif self.rect.x < player.rect.x and self.rect.x + 150 > player.rect.x and (self.rect.y > player.rect.y - 40 and self.rect.y < player.rect.y + 40):
                brick_left_group.add(self)
            elif self.rect.y > player.rect.y and self.rect.y - 150 < player.rect.y and (self.rect.x > player.rect.x - 40 and self.rect.x < player.rect.x + 40):
                brick_up_group.add(self)
            elif self.rect.y < player.rect.y and self.rect.y + 150 > player.rect.y and (self.rect.x > player.rect.x - 40 and self.rect.x < player.rect.x + 40):
                brick_down_group.add(self)
#End Class
class Selector_Left(pygame.sprite.Sprite):
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
    def update(self):
        death = False
        player_apple_hit_list = pygame.sprite.spritecollide(self, player_sprites_group, False)
        for foo in player_apple_hit_list:
            drawing_group.remove(self)
            self.kill()
            player.apples = player.apples + 1
            death = True
        if death == False:
            if self.rect.x - 150 > player.rect.x or self.rect.x + 150 < player.rect.x or self.rect.y - 150 > player.rect.y or self.rect.y + 150 < player.rect.y:
                drawing_group.remove(self)
            else:
                drawing_group.add(self)
            for sprite in brick_left_group:
                if self.rect.x < sprite.rect.x:
                    drawing_group.remove(self)
            for sprite in brick_right_group:
                if self.rect.x > sprite.rect.x:
                    drawing_group.remove(self)
            for sprite in brick_up_group:
                if self.rect.y > sprite.rect.y:
                    drawing_group.remove(self)
            for sprite in brick_down_group:
                if self.rect.y < sprite.rect.y:
                    drawing_group.remove(self)
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
levels_menu = False
mapping = False
winner_of_level = False
loser_of_level = False
winner_of_all_levels = False
demo_mapping = False
demo_game = False
demo_end = False
no_player = False
no_apples = False
pause = False
invalid_map = False
level1 = [[5, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 6], 
[0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
[0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
[4, 0, 2, 4, 0, 1, 0, 0, 0, 0, 0, 0], 
[0, 0, 1, 6, 0, 1, 4, 0, 0, 0, 0, 0], 
[0, 4, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 1, 2, 1, 1, 3, 1, 1, 1], 
[0, 0, 0, 0, 2, 4, 0, 0, 0, 0, 0, 4], 
[6, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 4, 4, 1, 0, 0, 0, 4, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6]]
level2 = [[6, 1, 1, 1, 1, 1, 1, 1, 1, 4, 0, 6], 
[1, 0, 0, 0, 0, 0, 0, 4, 1, 1, 0, 0], 
[1, 0, 1, 0, 0, 0, 0, 1, 6, 2, 0, 0], 
[1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0], 
[1, 0, 3, 0, 0, 0, 0, 3, 0, 3, 0, 0], 
[1, 0, 1, 4, 0, 0, 4, 1, 0, 1, 1, 1], 
[1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 4, 1], 
[1, 0, 0, 0, 0, 5, 0, 0, 0, 0, 4, 1], 
[1, 6, 1, 1, 1, 1, 1, 1, 0, 0, 4, 1], 
[1, 0, 1, 4, 0, 0, 4, 1, 0, 6, 1, 1], 
[1, 0, 3, 0, 0, 0, 0, 1, 0, 1, 4, 6], 
[4, 0, 1, 0, 1, 0, 0, 2, 0, 1, 0, 0], 
[0, 0, 1, 0, 2, 0, 0, 1, 0, 3, 0, 0], 
[0, 0, 0, 0, 1, 4, 0, 0, 0, 1, 0, 0], 
[0, 1, 1, 0, 4, 1, 3, 1, 2, 1, 0, 0], 
[0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
level3 = [[6, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0], 
[0, 0, 0, 4, 2, 0, 0, 0, 0, 2, 4, 0], 
[0, 0, 6, 0, 1, 0, 0, 1, 1, 1, 0, 0], 
[0, 0, 1, 1, 1, 0, 6, 0, 4, 1, 0, 6], 
[0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 4, 0], 
[0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0], 
[6, 0, 1, 0, 6, 1, 0, 0, 1, 4, 1, 0], 
[0, 0, 3, 0, 0, 1, 0, 0, 1, 0, 1, 0], 
[0, 0, 1, 4, 4, 1, 0, 0, 1, 0, 1, 0], 
[0, 0, 1, 1, 1, 1, 3, 1, 1, 6, 2, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3], 
[2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], 
[4, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0]]
level4 = [[4, 0, 0, 6, 0, 0, 3, 0, 0, 0, 0, 0], 
[1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0], 
[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], 
[0, 0, 0, 5, 0, 0, 1, 0, 0, 1, 0, 0], 
[0, 0, 0, 0, 0, 0, 1, 4, 6, 1, 0, 0], 
[0, 0, 0, 0, 0, 1, 1, 2, 1, 1, 1, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], 
[0, 1, 2, 1, 1, 1, 1, 3, 1, 1, 1, 0], 
[0, 1, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 1, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 1, 2, 1, 1, 3, 1, 1, 1, 1, 6, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0], 
[0, 1, 4, 0, 0, 6, 0, 0, 0, 0, 0, 0], 
[0, 1, 2, 1, 1, 1, 1, 1, 3, 1, 0, 0], 
[0, 4, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0]]
level5 = [[4, 0, 0, 0, 1, 1, 4, 0, 0, 0, 6, 0], 
[0, 0, 0, 0, 6, 0, 1, 1, 0, 1, 1, 0], 
[1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0], 
[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0], 
[0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0], 
[0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 6, 0], 
[0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0], 
[0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0], 
[0, 1, 6, 0, 0, 0, 0, 0, 0, 0, 6, 1], 
[0, 1, 0, 0, 0, 0, 0, 0, 5, 0, 0, 1], 
[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[0, 3, 6, 0, 0, 0, 0, 0, 0, 0, 6, 1], 
[0, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1], 
[0, 3, 6, 0, 0, 0, 0, 0, 0, 0, 0, 4]]
level6 = [[0, 0, 0, 4, 4, 6, 0, 0, 0, 0, 6, 6], 
[0, 0, 0, 0, 4, 4, 0, 0, 0, 0, 6, 6], 
[0, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 0], 
[0, 1, 5, 0, 0, 0, 0, 0, 0, 6, 1, 0], 
[0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0], 
[0, 1, 0, 1, 4, 0, 0, 4, 1, 0, 1, 0], 
[0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0], 
[0, 3, 0, 0, 6, 0, 0, 0, 1, 4, 1, 0], 
[0, 3, 0, 0, 0, 6, 0, 0, 1, 4, 1, 0], 
[0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0], 
[0, 1, 0, 1, 1, 0, 0, 4, 1, 0, 1, 0], 
[0, 1, 0, 1, 4, 0, 1, 1, 1, 0, 1, 0], 
[0, 1, 6, 0, 0, 0, 0, 0, 0, 6, 1, 0], 
[0, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 0], 
[0, 0, 0, 0, 4, 4, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 4, 4, 6, 0, 0, 0, 0, 0, 6]]
level7 = [[5, 0, 0, 1, 1, 1, 1, 1, 1, 4, 0, 0], 
[0, 0, 0, 2, 4, 0, 0, 4, 2, 0, 0, 0], 
[1, 1, 0, 1, 0, 6, 0, 0, 1, 0, 1, 0], 
[4, 1, 0, 1, 1, 3, 3, 1, 1, 0, 0, 0], 
[0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0], 
[0, 1, 0, 0, 1, 6, 0, 1, 0, 0, 1, 0], 
[0, 0, 0, 0, 1, 3, 3, 1, 0, 0, 6, 0], 
[0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0], 
[0, 0, 1, 0, 1, 3, 3, 1, 0, 0, 0, 0], 
[1, 1, 1, 0, 1, 6, 0, 1, 0, 0, 1, 0], 
[1, 4, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0], 
[1, 0, 0, 1, 1, 3, 3, 1, 1, 0, 1, 0], 
[1, 0, 0, 1, 0, 6, 0, 0, 1, 0, 1, 6], 
[6, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1], 
[0, 0, 0, 2, 4, 0, 0, 4, 2, 0, 0, 0]]
level8 = [[5, 3, 4, 0, 0, 1, 0, 0, 6, 0, 1, 6], 
[1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 3, 4], 
[4, 0, 6, 1, 0, 1, 0, 1, 1, 3, 1, 1], 
[0, 0, 0, 1, 0, 2, 0, 2, 0, 0, 0, 6], 
[0, 0, 0, 1, 0, 1, 0, 2, 0, 0, 0, 0], 
[1, 3, 1, 1, 0, 1, 0, 2, 0, 0, 0, 0], 
[6, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0], 
[0, 0, 1, 1, 1, 1, 0, 2, 0, 0, 0, 0], 
[0, 0, 1, 6, 0, 3, 0, 2, 0, 0, 0, 0], 
[0, 0, 1, 1, 1, 1, 0, 2, 6, 4, 4, 6], 
[0, 0, 3, 0, 4, 1, 0, 1, 1, 1, 1, 1], 
[0, 4, 1, 0, 6, 1, 0, 0, 0, 0, 0, 0], 
[0, 6, 1, 1, 1, 1, 3, 1, 1, 1, 1, 0], 
[0, 1, 1, 4, 0, 0, 0, 0, 0, 6, 1, 0], 
[0, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
level9 = [[5, 0, 0, 1, 0, 0, 0, 6, 0, 0, 0, 4], 
[0, 0, 0, 1, 0, 0, 0, 6, 0, 0, 0, 0], 
[0, 0, 0, 1, 0, 1, 1, 2, 1, 1, 1, 1], 
[0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0], 
[0, 1, 0, 1, 0, 0, 1, 4, 0, 1, 0, 0], 
[0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 6, 0], 
[0, 1, 6, 1, 0, 0, 1, 6, 0, 1, 0, 0], 
[6, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0], 
[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 
[0, 1, 3, 1, 0, 1, 1, 1, 1, 1, 0, 0], 
[0, 1, 4, 1, 0, 0, 0, 0, 0, 0, 0, 4], 
[0, 1, 1, 1, 0, 1, 1, 2, 1, 1, 1, 1], 
[0, 0, 6, 0, 0, 3, 6, 0, 0, 0, 0, 4]]
level10 = [[5, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 4], 
[4, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0], 
[2, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 3], 
[4, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0], 
[0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 4], 
[3, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 2], 
[0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 4], 
[4, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0], 
[2, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 3], 
[4, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0], 
[0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 4], 
[3, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 2], 
[0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 4], 
[4, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0], 
[2, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 3], 
[4, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0]]
def Check(map):
    apples_x = []
    apples_y = []
    for y in range(12):
        for x in range(16):
            if map[x][y] == 5:
                player_x = x
                player_y = y
            #End If
        #Next
    #Next
    for y in range(12):
        for x in range(16):
            if map[x][y] == 4:
                apples_x.append(x)
                apples_y.append(y)
            #End If
        #Next
    #Next  
    for count in range(len(apples_x)):
        for y in range(12):
            for x in range(16):
                if map[x][y] == 7:
                    map[x][y] = 0
                #End If
            #Next
        #Next  
        found = False
        fail = False
        counter = 0
        current_x = player_x
        current_y = player_y
        last_x = player_x
        last_y = player_y
        map[current_x][current_y] = 7
        while found == False and fail == False:
            if apples_x[count] >= current_x and apples_y[count] >= current_y:
                if current_x == apples_x[count] and current_y + 1 == apples_y[count]:
                    apples_x[count] = 400
                    apples_y[count] = 400
                    found = True
                elif current_x + 1 == apples_x[count] and current_y == apples_y[count]:
                    apples_x[count] = 400
                    apples_y[count] = 400
                    found = True
                elif current_x == apples_x[count] and current_y - 1 == apples_y[count]:
                    apples_x[count] = 400
                    apples_y[count] = 400
                    found = True
                elif current_x - 1 == apples_x[count] and current_y == apples_y[count]:
                    apples_x[count] = 400
                    apples_y[count] = 400
                    found = True
                elif map[current_x][current_y + 1] == 0 or map[current_x][current_y + 1] == 3 or map[current_x][current_y + 1] == 6:
                    current_y = current_y + 1
                    map[current_x][current_y] = 7
                    last_x = current_x
                    last_y = current_y - 1
                elif map[current_x + 1][current_y] == 0 or map[current_x + 1][current_y] == 3 or map[current_x + 1][current_y] == 6:
                    current_x = current_x + 1
                    map[current_x][current_y] = 7
                    last_x = current_x - 1
                    last_y = current_y
                elif map[current_x][current_y - 1] == 0 or map[current_x][current_y - 1] == 3 or map[current_x][current_y - 1] == 6:
                    current_y = current_y - 1
                    map[current_x][current_y] = 7
                    last_x = current_x
                    last_y = current_y + 1
                elif map[current_x - 1][current_y] == 0 or map[current_x - 1][current_y] == 3 or map[current_x - 1][current_y] == 6:
                    current_x = current_x - 1
                    map[current_x][current_y] = 7
                    last_x = current_x + 1
                    last_y = current_y
                elif map[current_x][current_y + 1] == 7 and not (current_x == last_x and current_y + 1 == last_y):
                    current_y = current_y + 1
                    map[current_x][current_y] = 7
                    last_x = current_x
                    last_y = current_y - 1
                elif map[current_x + 1][current_y] == 7 and not (current_x + 1 == last_x and current_y == last_y):
                    current_x = current_x + 1
                    map[current_x][current_y] = 7
                    last_x = current_x - 1
                    last_y = current_y
                elif map[current_x][current_y - 1] == 7 and not (current_x == last_x and current_y - 1 == last_y):
                    current_y = current_y - 1
                    map[current_x][current_y] = 7
                    last_x = current_x
                    last_y = current_y + 1
                elif map[current_x - 1][current_y] == 7 and not (current_x - 1 == last_x and current_y == last_y):
                    current_x = current_x - 1
                    map[current_x][current_y] = 7
                    last_x = current_x + 1
                    last_y = current_y
                elif map[current_x][current_y + 1] == 7:
                    current_y = current_y + 1
                    map[current_x][current_y] = 7
                    last_x = current_x
                    last_y = current_y - 1
                elif map[current_x + 1][current_y] == 7:
                    current_x = current_x + 1
                    map[current_x][current_y] = 7
                    last_x = current_x - 1
                    last_y = current_y
                elif map[current_x][current_y - 1] == 7:
                    current_y = current_y - 1
                    map[current_x][current_y] = 7
                    last_x = current_x
                    last_y = current_y + 1
                elif map[current_x - 1][current_y] == 7:
                    current_x = current_x - 1
                    map[current_x][current_y] = 7
                    last_x = current_x + 1
                    last_y = current_y
                else:
                    fail = True
                #End If
            elif apples_x[count] >= current_x and apples_y[count] < current_y:
                if current_x == apples_x[count] and current_y - 1 == apples_y[count]:
                    apples_x[count] = 400
                    apples_y[count] = 400
                    found = True
                elif current_x + 1 == apples_x[count] and current_y == apples_y[count]:
                    apples_x[count] = 400
                    apples_y[count] = 400
                    found = True
                elif current_x == apples_x[count] and current_y + 1 == apples_y[count]:
                    apples_x[count] = 400
                    apples_y[count] = 400
                    found = True
                elif current_x - 1 == apples_x[count] and current_y == apples_y[count]:
                    apples_x[count] = 400
                    apples_y[count] = 400
                    found = True
                elif map[current_x][current_y - 1] == 0 or map[current_x][current_y - 1] == 3 or map[current_x][current_y - 1] == 6:
                    current_y = current_y - 1
                    map[current_x][current_y] = 7
                    last_x = current_x
                    last_y = current_y + 1
                elif map[current_x + 1][current_y] == 0 or map[current_x + 1][current_y] == 3 or map[current_x + 1][current_y] == 6:
                    current_x = current_x + 1
                    map[current_x][current_y] = 7
                    last_x = current_x - 1
                    last_y = current_y
                elif map[current_x][current_y + 1] == 0 or map[current_x][current_y + 1] == 3 or map[current_x][current_y + 1] == 6:
                    current_y = current_y + 1
                    map[current_x][current_y] = 7
                    last_x = current_x
                    last_y = current_y - 1
                elif map[current_x - 1][current_y] == 0 or map[current_x - 1][current_y] == 3 or map[current_x - 1][current_y] == 6:
                    current_x = current_x - 1
                    map[current_x][current_y] = 7
                    last_x = current_x + 1
                    last_y = current_y
                elif map[current_x][current_y - 1] == 7 and not (current_x == last_x and current_y - 1 == last_y):
                    current_y = current_y - 1
                    map[current_x][current_y] = 7
                    last_x = current_x
                    last_y = current_y + 1
                elif map[current_x + 1][current_y] == 7 and not (current_x + 1 == last_x and current_y == last_y):
                    current_x = current_x + 1
                    map[current_x][current_y] = 7
                    last_x = current_x - 1
                    last_y = current_y
                elif map[current_x][current_y + 1] == 7 and not (current_x == last_x and current_y + 1 == last_y):
                    current_y = current_y + 1
                    map[current_x][current_y] = 7
                    last_x = current_x
                    last_y = current_y - 1
                elif map[current_x - 1][current_y] == 7 and not (current_x - 1 == last_x and current_y == last_y):
                    current_x = current_x - 1
                    map[current_x][current_y] = 7
                    last_x = current_x + 1
                    last_y = current_y
                elif map[current_x][current_y - 1] == 7:
                    current_y = current_y - 1
                    map[current_x][current_y] = 7
                    last_x = current_x
                    last_y = current_y + 1
                elif map[current_x + 1][current_y] == 7:
                    current_x = current_x + 1
                    map[current_x][current_y] = 7
                    last_x = current_x - 1
                    last_y = current_y
                elif map[current_x][current_y + 1] == 7:
                    current_y = current_y + 1
                    map[current_x][current_y] = 7
                    last_x = current_x
                    last_y = current_y - 1
                elif map[current_x - 1][current_y] == 7:
                    current_x = current_x - 1
                    map[current_x][current_y] = 7
                    last_x = current_x + 1
                    last_y = current_y
                else:
                    fail = True
                #End If
            elif apples_x[count] < current_x and apples_y[count] >= current_y:
                if current_x == apples_x[count] and current_y + 1 == apples_y[count]:
                    apples_x[count] = 400
                    apples_y[count] = 400
                    found = True
                elif current_x - 1 == apples_x[count] and current_y == apples_y[count]:
                    apples_x[count] = 400
                    apples_y[count] = 400
                    found = True
                elif current_x == apples_x[count] and current_y - 1 == apples_y[count]:
                    apples_x[count] = 400
                    apples_y[count] = 400
                    found = True
                elif current_x + 1 == apples_x[count] and current_y == apples_y[count]:
                    apples_x[count] = 400
                    apples_y[count] = 400
                    found = True
                elif map[current_x][current_y + 1] == 0 or map[current_x][current_y + 1] == 3 or map[current_x][current_y + 1] == 6:
                    current_y = current_y + 1
                    map[current_x][current_y] = 7
                    last_x = current_x
                    last_y = current_y - 1
                elif map[current_x - 1][current_y] == 0 or map[current_x - 1][current_y] == 3 or map[current_x - 1][current_y] == 6:
                    current_x = current_x - 1
                    map[current_x][current_y] = 7
                    last_x = current_x + 1
                    last_y = current_y
                elif map[current_x][current_y - 1] == 0 or map[current_x][current_y - 1] == 3 or map[current_x][current_y - 1] == 6:
                    current_y = current_y - 1
                    map[current_x][current_y] = 7
                    last_x = current_x
                    last_y = current_y + 1
                elif map[current_x + 1][current_y] == 0 or map[current_x + 1][current_y] == 3 or map[current_x + 1][current_y] == 6:
                    current_x = current_x + 1
                    map[current_x][current_y] = 7
                    last_x = current_x - 1
                    last_y = current_y
                elif map[current_x][current_y + 1] == 7 and not (current_x == last_x and current_y + 1 == last_y):
                    current_y = current_y + 1
                    map[current_x][current_y] = 7
                    last_x = current_x
                    last_y = current_y - 1
                elif map[current_x - 1][current_y] == 7 and not (current_x - 1 == last_x and current_y == last_y):
                    current_x = current_x - 1
                    map[current_x][current_y] = 7
                    last_x = current_x + 1
                    last_y = current_y
                elif map[current_x][current_y - 1] == 7 and not (current_x == last_x and current_y - 1 == last_y):
                    current_y = current_y - 1
                    map[current_x][current_y] = 7
                    last_x = current_x
                    last_y = current_y + 1
                elif map[current_x + 1][current_y] == 7 and not (current_x + 1 == last_x and current_y == last_y):
                    current_x = current_x + 1
                    map[current_x][current_y] = 7
                    last_x = current_x - 1
                    last_y = current_y
                elif map[current_x][current_y + 1] == 7:
                    current_y = current_y + 1
                    map[current_x][current_y] = 7
                    last_x = current_x
                    last_y = current_y - 1
                elif map[current_x - 1][current_y] == 7:
                    current_x = current_x - 1
                    map[current_x][current_y] = 7
                    last_x = current_x + 1
                    last_y = current_y
                elif map[current_x][current_y - 1] == 7:
                    current_y = current_y - 1
                    map[current_x][current_y] = 7
                    last_x = current_x
                    last_y = current_y + 1
                elif map[current_x + 1][current_y] == 7:
                    current_x = current_x + 1
                    map[current_x][current_y] = 7
                    last_x = current_x - 1
                    last_y = current_y
                else:
                    fail = True
                #End If
            elif apples_x[count] < current_x and apples_y[count] < current_y:
                if current_x == apples_x[count] and current_y - 1 == apples_y[count]:
                    apples_x[count] = 400
                    apples_y[count] = 400
                    found = True
                elif current_x - 1 == apples_x[count] and current_y == apples_y[count]:
                    apples_x[count] = 400
                    apples_y[count] = 400
                    found = True
                elif current_x == apples_x[count] and current_y + 1 == apples_y[count]:
                    apples_x[count] = 400
                    apples_y[count] = 400
                    found = True
                elif current_x + 1 == apples_x[count] and current_y == apples_y[count]:
                    apples_x[count] = 400
                    apples_y[count] = 400
                    found = True
                elif map[current_x][current_y - 1] == 0 or map[current_x][current_y - 1] == 3 or map[current_x][current_y - 1] == 6:
                    current_y = current_y - 1
                    map[current_x][current_y] = 7
                    last_x = current_x
                    last_y = current_y + 1
                elif map[current_x - 1][current_y] == 0 or map[current_x - 1][current_y] == 3 or map[current_x - 1][current_y] == 6:
                    current_x = current_x - 1
                    map[current_x][current_y] = 7
                    last_x = current_x + 1
                    last_y = current_y
                elif map[current_x][current_y + 1] == 0 or map[current_x][current_y + 1] == 3 or map[current_x][current_y + 1] == 6:
                    current_y = current_y + 1
                    map[current_x][current_y] = 7
                    last_x = current_x
                    last_y = current_y - 1
                elif map[current_x + 1][current_y] == 0 or map[current_x + 1][current_y] == 3 or map[current_x + 1][current_y] == 6:
                    current_x = current_x + 1
                    map[current_x][current_y] = 7
                    last_x = current_x - 1
                    last_y = current_y
                elif map[current_x][current_y - 1] == 7 and not (current_x == last_x and current_y - 1 == last_y):
                    current_y = current_y - 1
                    map[current_x][current_y] = 7
                    last_x = current_x
                    last_y = current_y + 1
                elif map[current_x - 1][current_y] == 7 and not (current_x - 1 == last_x and current_y == last_y):
                    current_x = current_x - 1
                    map[current_x][current_y] = 7
                    last_x = current_x + 1
                    last_y = current_y
                elif map[current_x][current_y + 1] == 7 and not (current_x == last_x and current_y + 1 == last_y):
                    current_y = current_y + 1
                    map[current_x][current_y] = 7
                    last_x = current_x
                    last_y = current_y - 1
                elif map[current_x + 1][current_y] == 7 and not (current_x + 1 == last_x and current_y == last_y):
                    current_x = current_x + 1
                    map[current_x][current_y] = 7
                    last_x = current_x - 1
                    last_y = current_y
                elif map[current_x][current_y - 1] == 7:
                    current_y = current_y - 1
                    map[current_x][current_y] = 7
                    last_x = current_x
                    last_y = current_y + 1
                elif map[current_x - 1][current_y] == 7:
                    current_x = current_x - 1
                    map[current_x][current_y] = 7
                    last_x = current_x + 1
                    last_y = current_y
                elif map[current_x][current_y + 1] == 7:
                    current_y = current_y + 1
                    map[current_x][current_y] = 7
                    last_x = current_x
                    last_y = current_y - 1
                elif map[current_x + 1][current_y] == 7:
                    current_x = current_x + 1
                    map[current_x][current_y] = 7
                    last_x = current_x - 1
                    last_y = current_y
                else:
                    fail = True
                #End If
            #End If
            counter = counter + 1
            print(current_x)
            print(current_y)
            if counter == 1000 and found == False:
                fail = True
            #End If
        #End While
        print("next")
    #Next
    valid = True
    for i in range(len(apples_x)):
        if apples_x[i] != 400:
            valid = False
        #End If
    #Next
    return valid
#End Function
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
    drawing_group = pygame.sprite.Group()
    map_block_group = pygame.sprite.Group()
    brick_left_group = pygame.sprite.Group()
    brick_right_group = pygame.sprite.Group()
    brick_up_group = pygame.sprite.Group()
    brick_down_group = pygame.sprite.Group()
    apple_number = 0
    own_level = False
    all_levels = False
    all_level_mapping = False
    all_level_game = False
    apple_there = False
    is_player_there = False
    total_score = 0
    score = 0
    level_demo = random.randint(1, 10)
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
            own_level = False
        #End If
        if keys[pygame.K_2]:
            intro = False
            levels_menu = True
            own_level = True
        #End If
        if keys[pygame.K_3]:
            intro = False
            demo_mapping = True
            own_level = True
        #End If
        if  keys[pygame.K_4]:
            map = level1
            intro = False
            mapping = True
        # -- Game logic goes after this comment
        # -- Screen background is BLACK
        screen.fill(BLACK)
        # -- Draw here
        intro_screen = pygame.image.load('Template.png').convert_alpha()
        intro_screen = pygame.transform.smoothscale(intro_screen, (1000, 480)) 
        screen.blit(intro_screen, (0, 0))
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
    while levels_menu == True:
        # -- User input and controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                levels_menu = False
                my_game = False
                endgame = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    map = level1
                    levels_menu = False
                    mapping = True
                elif event.key == pygame.K_2:
                    map = level2
                    levels_menu = False
                    mapping = True
                elif event.key == pygame.K_3:
                    map = level3
                    levels_menu = False
                    mapping = True
                elif event.key == pygame.K_4:
                    map = level4
                    levels_menu = False
                    mapping = True
                elif event.key == pygame.K_5:
                    map = level5
                    levels_menu = False
                    mapping = True
                elif event.key == pygame.K_6:
                    map = level6
                    levels_menu = False
                    mapping = True
                elif event.key == pygame.K_7:
                    map = level7
                    levels_menu = False
                    mapping = True
                elif event.key == pygame.K_8:
                    map = level8
                    levels_menu = False
                    mapping = True
                elif event.key == pygame.K_9:
                    map = level9
                    levels_menu = False
                    mapping = True
                elif event.key == pygame.K_x:
                    map = level10
                    levels_menu = False
                    mapping = True
                elif event.key == pygame.K_a:
                    levels_menu = False
                    all_level_mapping = True
                    all_levels = True
                    total_score = 0
        #Next event
        screen.fill(BLACK)
        pygame.draw.rect(screen, BLACK, (640, 0, 360, 480))
        font = pygame.font.SysFont('ComicSans', 50, True, False)
        text = font.render('Which level do you want to do?', True, WHITE)
        screen.blit(text, [200, 30])
        font = pygame.font.SysFont('ComicSans', 45, True, False)
        text = font.render('Press 1 to play level 1', True, WHITE)
        screen.blit(text, [300, 70])
        text = font.render('Press 2 to play level 2', True, WHITE)
        screen.blit(text, [300, 100])
        text = font.render('Press 3 to play level 3', True, WHITE)
        screen.blit(text, [300, 130])
        text = font.render('Press 4 to play level 4', True, WHITE)
        screen.blit(text, [300, 160])
        text = font.render('Press 5 to play level 5', True, WHITE)
        screen.blit(text, [300, 190])
        text = font.render('Press 6 to play level 6', True, WHITE)
        screen.blit(text, [300, 220])
        text = font.render('Press 7 to play level 7', True, WHITE)
        screen.blit(text, [300, 250])
        text = font.render('Press 8 to play level 8', True, WHITE)
        screen.blit(text, [300, 280])
        text = font.render('Press 9 to play level 9', True, WHITE)
        screen.blit(text, [300, 310])
        text = font.render('Press x to play level 10', True, WHITE)
        screen.blit(text, [291, 340])
        text = font.render('Press a to play all levels', True, WHITE)
        screen.blit(text, [280, 370])
        # -- flip display to reveal new position of objects
        pygame.display.flip()
        # - The clock ticks over
        clock.tick(60)
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
                    apple_there = True
                if event.key == pygame.K_5:
                    if is_player_there == False:
                        player = Player(selector_left.rect.x + 5, selector_top.rect.y + 5, 0, 0, 0, 0)
                        draw_sprites_group.add(player)
                        all_sprites_group.add(player)
                        map[selector_top.pos_x][selector_top.pos_y] = 5
                        is_player_there = True
                if event.key == pygame.K_6:
                    monster = Monster_Draw(selector_left.rect.x + 5, selector_top.rect.y + 5)
                    draw_sprites_group.add(monster)
                    all_sprites_group.add(monster)
                    map[selector_top.pos_x][selector_top.pos_y] = 6
                if event.key == pygame.K_RETURN:
                    if is_player_there == False:
                        no_player = True
                    elif apple_there == False:
                        no_apples = True
                    elif Check(map) == False:
                        invalid_map = True
                    else:
                        map_draw = False
                        mapping = True
                #End If
        #Next event
        while invalid_map == True:
            # -- User input and controls
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    invalid_map = False
                    my_game = False
                    endgame = True
                elif event.type == pygame.KEYDOWN: # - a key is down
                    if event.key == pygame.K_RETURN:
                        invalid_map = False
                    if event.key == pygame.K_ESCAPE:
                        invalid_map = False
                        map_draw = False
                        my_game = False
                        endgame = True
                #End If
            #Next event
            screen.fill(BLACK)
            pygame.draw.rect(screen, BLACK, (640, 0, 360, 480))
            font = pygame.font.SysFont('ComicSans', 100, True, False)
            text = font.render('Invalid Map!', True, WHITE)
            screen.blit(text, [205, 70])
            font = pygame.font.SysFont('ComicSans', 30, True, False)
            text = font.render('Press enter to map drawing', True, WHITE)
            screen.blit(text, [310, 330])
            text = font.render('Press escape to quit', True, WHITE)
            screen.blit(text, [360, 360])
            # -- flip display to reveal new position of objects
            pygame.display.flip()
        while no_player == True:
            # -- User input and controls
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    no_player = False
                    my_game = False
                    endgame = True
                elif event.type == pygame.KEYDOWN: # - a key is down
                    if event.key == pygame.K_RETURN:
                        is_player_there = False
                        no_player = False
                    if event.key == pygame.K_ESCAPE:
                        no_player = False
                        map_draw = False
                        my_game = False
                        endgame = True
                #End If
            #Next event
            screen.fill(BLACK)
            pygame.draw.rect(screen, BLACK, (640, 0, 360, 480))
            font = pygame.font.SysFont('ComicSans', 100, True, False)
            text = font.render('Place a Player!', True, WHITE)
            screen.blit(text, [205, 70])
            font = pygame.font.SysFont('ComicSans', 30, True, False)
            text = font.render('Press enter to map drawing', True, WHITE)
            screen.blit(text, [310, 330])
            text = font.render('Press escape to quit', True, WHITE)
            screen.blit(text, [360, 360])
            # -- flip display to reveal new position of objects
            pygame.display.flip()
        while no_apples == True:
            # -- User input and controls
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    no_apples = False
                    my_game = False
                    endgame = True
                elif event.type == pygame.KEYDOWN: # - a key is down
                    if event.key == pygame.K_RETURN:
                        apple_there = False
                        no_apples = False
                    if event.key == pygame.K_ESCAPE:
                        no_apples = False
                        map_draw = False
                        my_game = False
                        endgame = True
                #End If
            #Next event
            screen.fill(BLACK)
            pygame.draw.rect(screen, BLACK, (640, 0, 360, 480))
            font = pygame.font.SysFont('ComicSans', 100, True, False)
            text = font.render('Place an Apple!', True, WHITE)
            screen.blit(text, [205, 70])
            font = pygame.font.SysFont('ComicSans', 30, True, False)
            text = font.render('Press enter to map drawing', True, WHITE)
            screen.blit(text, [310, 330])
            text = font.render('Press escape to quit', True, WHITE)
            screen.blit(text, [360, 360])
            # -- flip display to reveal new position of objects
            pygame.display.flip()
            # - The clock ticks over
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
    if all_levels == True:
        for counter in range(1, 10):
            if counter == 1:
                map = level1
            elif counter == 2:
                map = level2
            elif counter == 3:
                map = level3
            elif counter == 4:
                map = level4
            elif counter == 5:
                map = level5
            elif counter == 6:
                map = level6
            elif counter == 7:
                map = level7
            elif counter == 8:
                map = level8
            elif counter == 9:
                map = level9
            elif counter == 10:
                map = level10
            while all_level_mapping == True:
                for y in range(12):
                    for x in range(16):
                        map_block = Map_Block(WHITE, 40, 40, x*40, y *40)
                        map_sprites_group.add(map_block)
                        map_block_group.add(map_block)
                        all_sprites_group.add(map_block)
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
                score = 30000
                all_level_mapping = False
                all_level_game = True
            while all_level_game == True:
                # -- User input and controls
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        all_level_game = False
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
                if keys[pygame.K_p]:
                    pause = True
                while pause == True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pause = False
                            all_level_game = False
                            my_game = False
                            endgame = True
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:
                                pause = False
                            if event.key == pygame.K_ESCAPE:
                                pause = False
                                all_level_game = False
                                intro = True
                    screen.fill(BLACK)
                    pygame.draw.rect(screen, BLACK, (640, 0, 360, 480))
                    font = pygame.font.SysFont('ComicSans', 100, True, False)
                    text = font.render('Game Paused', True, WHITE)
                    screen.blit(text, [220, 70])
                    font = pygame.font.SysFont('ComicSans', 30, True, False)
                    text = font.render('Press enter to return to the game', True, WHITE)
                    screen.blit(text, [285, 330])
                    text = font.render('Press escape to return to the home page', True, WHITE)
                    screen.blit(text, [245, 360])
                    pygame.display.flip()
                    clock.tick(60)
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
                all_sprites_group.update()
                if player.apples == apple_number and counter == 10:
                    all_level_game = False
                    winner_of_all_levels = True
                elif player.apples == apple_number:
                    all_level_game = False
                    all_level_mapping = True
                if player.health < 1 and own_level == False:
                    all_level_game = False
                    loser_of_own_map = True
                if player.health < 1 and own_level == True:
                    all_level_game = False
                    loser_of_level = True
                # -- Screen background is BLACK
                screen.fill(WHITE)
                pygame.draw.rect(screen, BLACK, (640, 0, 360, 480))
                map_block_group.draw(screen)
                brick_group.draw(screen)
                window_group.draw(screen)
                door_group.draw(screen)
                player_sprites_group.draw(screen)
                drawing_group.draw(screen)
                font = pygame.font.SysFont('ComicSans', 30, True, False)
                text = font.render('Press 1 to open a door', True, WHITE)
                screen.blit(text, [650, 10])
                text = font.render('Health: ' + str(player.health), True, WHITE)
                screen.blit(text, [650, 40])
                text = font.render('Apples: ' + str(player.apples) + ' / ' + str(apple_number), True, WHITE)
                screen.blit(text, [650, 70])
                text = font.render('Press p to pause', True, WHITE)
                screen.blit(text, [650, 100])
                # -- Draw here
                # -- flip display to reveal new position of objects
                pygame.display.flip()
                # - The clock ticks over
                clock.tick(60)
                score = score - 1
            #End While - End of game loop
            for sprite in map_sprites_group:
                sprite.kill()
            for sprite in player_sprites_group:
                sprite.kill()
            total_score = total_score + score
            apple_number = 0
    while mapping == True:
        for y in range(12):
            for x in range(16):
                map_block = Map_Block(WHITE, 40, 40, x*40, y *40)
                map_sprites_group.add(map_block)
                map_block_group.add(map_block)
                all_sprites_group.add(map_block)
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
        score = 30000
        for sprite in draw_sprites_group:
            sprite.kill()
        mapping = False
        in_game = True
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
        if keys[pygame.K_p]:
            pause = True
        while pause == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pause = False
                    in_game = False
                    my_game = False
                    endgame = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pause = False
                    if event.key == pygame.K_ESCAPE:
                        pause = False
                        in_game = False
                        intro = True
            screen.fill(BLACK)
            pygame.draw.rect(screen, BLACK, (640, 0, 360, 480))
            font = pygame.font.SysFont('ComicSans', 100, True, False)
            text = font.render('Game Paused', True, WHITE)
            screen.blit(text, [220, 70])
            font = pygame.font.SysFont('ComicSans', 30, True, False)
            text = font.render('Press enter to return to the game', True, WHITE)
            screen.blit(text, [285, 330])
            text = font.render('Press escape to return to the home page', True, WHITE)
            screen.blit(text, [245, 360])
            pygame.display.flip()
            clock.tick(60)
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
        all_sprites_group.update()
        if player.apples == apple_number and own_level == False:
            score = score + player.health * 60
            in_game = False
            winner_of_own_map = True
        if player.health < 1 and own_level == False:
            in_game = False
            loser_of_own_map = True
        if player.apples == apple_number and own_level == True:
            score = score + player.health * 60
            in_game = False
            winner_of_level = True
        if player.health < 1 and own_level == True:
            in_game = False
            loser_of_level = True
        # -- Screen background is BLACK
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLACK, (640, 0, 360, 480))
        map_block_group.draw(screen)
        brick_group.draw(screen)
        window_group.draw(screen)
        door_group.draw(screen)
        drawing_group.draw(screen)
        player_sprites_group.draw(screen)
        font = pygame.font.SysFont('ComicSans', 30, True, False)
        text = font.render('Press 1 to open a door', True, WHITE)
        screen.blit(text, [650, 10])
        text = font.render('Health: ' + str(player.health), True, WHITE)
        screen.blit(text, [650, 40])
        text = font.render('Apples: ' + str(player.apples) + ' / ' + str(apple_number), True, WHITE)
        screen.blit(text, [650, 70])
        text = font.render('Press p to pause', True, WHITE)
        screen.blit(text, [650, 100])
        # -- Draw here
        # -- flip display to reveal new position of objects
        pygame.display.flip()
        # - The clock ticks over
        clock.tick(60)
        score = score - 1
    #End While - End of game loop
    while demo_mapping == True:
        if level_demo == 1:
            map = level1
        elif level_demo == 2:
            map = level2
        elif level_demo == 3:
            map = level3
        elif level_demo == 4:
            map = level4
        elif level_demo == 5:
            map = level5
        elif level_demo == 6:
            map = level6
        elif level_demo == 7:
            map = level7
        elif level_demo == 8:
            map = level8
        elif level_demo == 9:
            map = level9
        elif level_demo == 10:
            map = level10
        for y in range(12):
            for x in range(16):
                map_block = Map_Block(WHITE, 40, 40, x*40, y *40)
                map_sprites_group.add(map_block)
                map_block_group.add(map_block)
                all_sprites_group.add(map_block)
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
        score = 30000
        for sprite in draw_sprites_group:
            sprite.kill()
        player.speed_x = random.randint(-2, 2)
        player.speed_y = random.randint(-2, 2)
        demo_mapping = False
        demo_game = True
    while demo_game == True:
        # -- User input and controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                demo_game = False
                my_game = False
                endgame = True
            #End If
        #Next event
        keys = pygame.key.get_pressed()
        if keys[pygame.K_p]:
            pause = True
        while pause == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pause = False
                    demo_game = False
                    my_game = False
                    endgame = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pause = False
                    if event.key == pygame.K_ESCAPE:
                        pause = False
                        demo_game = False
                        intro = True
            screen.fill(BLACK)
            pygame.draw.rect(screen, BLACK, (640, 0, 360, 480))
            font = pygame.font.SysFont('ComicSans', 100, True, False)
            text = font.render('Game Paused', True, WHITE)
            screen.blit(text, [220, 70])
            font = pygame.font.SysFont('ComicSans', 30, True, False)
            text = font.render('Press enter to return to the game', True, WHITE)
            screen.blit(text, [285, 330])
            text = font.render('Press escape to return to the home page', True, WHITE)
            screen.blit(text, [245, 360])
            pygame.display.flip()
            clock.tick(60)
        # -- Game logic goes after this comment
        player.rect.x = player.rect.x + player.speed_x
        player.rect.y = player.rect.y + player.speed_y
        if player.speed_x == 0 and player.speed_y == 0:
            player.speed_x = random.randint(-2, 2)
            player.speed_y = random.randint(-2, 2)
        if player.rect.y < 0:
            player.rect.x = player.old_x
            player.rect.y = player.old_y
            player.speed_x = random.randint(-2, 2)
            player.speed_y = random.randint(-2, 2)
        if player.rect.y > 450:
            player.rect.x = player.old_x
            player.rect.y = player.old_y
            player.speed_x = random.randint(-2, 2)
            player.speed_y = random.randint(-2, 2)
        if player.rect.x > 610:
            player.rect.x = player.old_x
            player.rect.y = player.old_y
            player.speed_x = random.randint(-2, 2)
            player.speed_y = random.randint(-2, 2)
        if player.rect.x < 0:
            player.rect.x = player.old_x
            player.rect.y = player.old_y
            player.speed_x = random.randint(-2, 2)
            player.speed_y = random.randint(-2, 2)
        player_brick_hit_list = pygame.sprite.spritecollide(player, brick_group, False)
        for foo in player_brick_hit_list:
            player.rect.x = player.old_x
            player.rect.y = player.old_y
            player.speed_x = random.randint(-2, 2)
            player.speed_y = random.randint(-2, 2)
        player_window_hit_list = pygame.sprite.spritecollide(player, window_group, False)
        for foo in player_window_hit_list:
            player.rect.x = player.old_x
            player.rect.y = player.old_y
            player.speed_x = random.randint(-2, 2)
            player.speed_y = random.randint(-2, 2)
        if player.speed_x == 0 and player.speed_y == 0:
            player.speed_x = random.randint(-2, 2)
            player.speed_y = random.randint(-2, 2)
        all_sprites_group.update()
        if player.apples == apple_number:
            score = score + player.health * 60
            demo_game = False
            demo_end = True
        if player.health < 1:
            demo_game = False
            demo_end = True
        # -- Screen background is BLACK
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLACK, (640, 0, 360, 480))
        map_block_group.draw(screen)
        brick_group.draw(screen)
        window_group.draw(screen)
        door_group.draw(screen)
        drawing_group.draw(screen)
        player_sprites_group.draw(screen)
        font = pygame.font.SysFont('ComicSans', 30, True, False)
        text = font.render('Press 1 to open a door', True, WHITE)
        screen.blit(text, [650, 10])
        text = font.render('Health: ' + str(player.health), True, WHITE)
        screen.blit(text, [650, 40])
        text = font.render('Apples: ' + str(player.apples) + ' / ' + str(apple_number), True, WHITE)
        screen.blit(text, [650, 70])
        text = font.render('Press p to pause', True, WHITE)
        screen.blit(text, [650, 100])
        # -- Draw here
        # -- flip display to reveal new position of objects
        pygame.display.flip()
        # - The clock ticks over
        clock.tick(60)
        score = score - 1
    #End While - End of game loop
    while demo_end == True:
        # -- User input and controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                demo_end = False
                my_game = False
                endgame = True
            elif event.type == pygame.KEYDOWN: # - a key is down
                if event.key == pygame.K_RETURN:
                    demo_end = False
                    intro = True
                if event.key == pygame.K_ESCAPE:
                    demo_end = False
                    my_game = False
                    endgame = True
            #End If
        #Next event
        screen.fill(BLACK)
        pygame.draw.rect(screen, BLACK, (640, 0, 360, 480))
        font = pygame.font.SysFont('ComicSans', 100, True, False)
        text = font.render('Demo Ended', True, WHITE)
        screen.blit(text, [240, 70])
        font = pygame.font.SysFont('ComicSans', 30, True, False)
        text = font.render('Press enter to return to the home page', True, WHITE)
        screen.blit(text, [250, 330])
        text = font.render('Press escape to quit', True, WHITE)
        screen.blit(text, [360, 360])
        # -- flip display to reveal new position of objects
        pygame.display.flip()
        # - The clock ticks over
        clock.tick(60)
    while winner_of_own_map == True:
        # -- User input and controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                winner_of_own_map = False
                my_game = False
                endgame = True
            elif event.type == pygame.KEYDOWN: # - a key is down
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
        screen.blit(text, [315, 142])
        text = font.render('Your Score Was: ' + str(score), True, WHITE)
        screen.blit(text, [60, 214])
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
    while winner_of_level == True:
        # -- User input and controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                winner_of_level = False
                my_game = False
                endgame = True
            elif event.type == pygame.KEYDOWN: # - a key is down
                if event.key == pygame.K_RETURN:
                    winner_of_level = False
                    intro = True
                if event.key == pygame.K_ESCAPE:
                    winner_of_level = False
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
        screen.blit(text, [315, 142])
        text = font.render('Your Score Was: ' + str(score), True, WHITE)
        screen.blit(text, [60, 214])
        font = pygame.font.SysFont('ComicSans', 30, True, False)
        text = font.render('Press enter to return to the home page', True, WHITE)
        screen.blit(text, [250, 330])
        text = font.render('Press escape to quit', True, WHITE)
        screen.blit(text, [360, 360])
        # -- flip display to reveal new position of objects
        pygame.display.flip()
        # - The clock ticks over
        clock.tick(60)
    while loser_of_level == True:
        # -- User input and controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loser_of_level = False
                my_game = False
                endgame = True
            elif event.type == pygame.KEYDOWN: # - a key is down
                if event.key == pygame.K_RETURN:
                    loser_of_level = False
                    intro = True
                if event.key == pygame.K_ESCAPE:
                    loser_of_level = False
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
    while winner_of_all_levels == True:
        # -- User input and controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                winner_of_all_levels = False
                my_game = False
                endgame = True
            elif event.type == pygame.KEYDOWN: # - a key is down
                if event.key == pygame.K_RETURN:
                    winner_of_all_levels = False
                    intro = True
                if event.key == pygame.K_ESCAPE:
                    winner_of_all_levels = False
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
        screen.blit(text, [315, 142])
        text = font.render('Your Score Was: ' + str(total_score), True, WHITE)
        screen.blit(text, [60, 214])
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