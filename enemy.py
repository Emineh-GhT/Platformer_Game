import random
import arcade

class Enemy(arcade.Sprite):

    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture(':resources:images/animated_characters/zombie/zombie_idle.png')
        
        self.center_x = random.randint(0 , 1000)
        self.center_y = 165
        self.speed = 2
        self.change_x = random.choice([-1 , 1])  #harekat ya be rast ya be chap

