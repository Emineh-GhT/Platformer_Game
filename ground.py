import arcade

class Ground(arcade.Sprite):
    def __init__(self , x , y):
        super().__init__()
        self.texture = arcade.load_texture(':resources:images/tiles/grass.png')

        self.w = 80
        self.h = 80
        
        self.center_x = x
        self.center_y = y

class Box(arcade.Sprite):
    def __init__(self , x , y):
        super().__init__()
        self.texture = arcade.load_texture(':resources:images/tiles/grassHalf_mid.png')

        self.w = 80
        self.h = 80
        
        self.center_x = x
        self.center_y = y
