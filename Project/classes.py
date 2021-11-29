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