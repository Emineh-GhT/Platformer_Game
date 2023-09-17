import time
import arcade


from player import Player
from ground import Ground , Box
from enemy import Enemy


class Game(arcade.Window):
    def __init__(self):
        self.w = 1000
        self.h = 700
        self.gravity = 0.3
        self.game_over_flag = False
        self.win_flag = False
        self.background_image = arcade.load_texture('pic/background.png')
        super().__init__(self.w , self.h , 'Platformer Game')

        self.t1 = time.time()

        self.me = Player()
        self.ground_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()

        self.key = arcade.Sprite(':resources:images/items/keyYellow.png')
        self.key.center_x = 200
        self.key.center_y = 450
        self.key.width = 50
        self.key.height = 50

        self.lock = arcade.Sprite(':resources:images/tiles/lockYellow.png')
        self.lock.center_x = 950
        self.lock.center_y = 130
        self.lock.width = 50
        self.lock.height = 50


        for i in range(0 , 1000, 80): # (start , stop , step)
            ground = Ground(i , 40)
            self.ground_list.append(ground)

        for i in range(600 , 800 , 120):
            box = Box(i , 250)
            self.ground_list.append(box)

        for i in range(200 , 400 , 120):
            box = Box(i , 350)
            self.ground_list.append(box)



        self.my_physics_engine= arcade.PhysicsEnginePlatformer(self.me , self.ground_list, gravity_constant=self.gravity) #jazebe
        self.enemy_physics_engine_list = []
    
        self.heart_image = arcade.load_texture(':resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png')
        self.heart_w = 80
        self.heart_h = 80
        self.heart_padding = 10
        self.hearts_start_x = self.w - 240
        self.hearts_start_y = self.h - 80
        self.remaining_hearts = 3

    def on_draw(self):
        arcade.start_render() # frame qabli ra pak va frame jadidra rasm mikond
        arcade.draw_lrwh_rectangle_textured(0 , 0 , self.w , self.h , self.background_image)

        if self.me.health <= 0:
                arcade.draw_text("Game Over !!! ", self.w//2-200, self.h//2, arcade.color.RED_VIOLET, 20, width=400, align="center")
        else:
            self.me.draw()

            self.enemy_list.draw()

            try:
                self.key.draw()
            except:
                pass

            self.lock.draw()

            for ground in self.ground_list:
                ground.draw()
            
            for i in range(self.remaining_hearts):
                x = self.hearts_start_x + (self.heart_w + self.heart_padding) * i
                y = self.hearts_start_y
                arcade.draw_texture_rectangle(x, y, self.heart_w, self.heart_h, self.heart_image)

    
    def on_key_press(self , key , modifiers):
        if key == arcade.key.LEFT:
            self.me.change_x = -1 * self.me.speed
        elif key == arcade.key.RIGHT:
            self.me.change_x = 1 * self.me.speed

        elif key == arcade.key.UP:
            if self.my_physics_engine.can_jump():
                self.me.change_y = 12


    def on_key_release(self , key , modifiers):
        self.me.change_x = 0

    
    def on_update(self , delta_time:float):
        if not self.game_over_flag :
            self.t2 = time.time()

            self.me.update_animation()

            self.my_physics_engine.update() #update kardan mojodiat ha
            for item in self.enemy_physics_engine_list:
                item.update()

            try:
                if arcade.check_for_collision(self.me , self.key):
                    self.me.pocket.append(self.key)
                    del self.key
            except:
                pass

            if arcade.check_for_collision(self.me , self.lock) and len(self.me.pocket)==1 :
                self.lock.texture = arcade.load_texture(':resources:images/items/gemBlue.png')
                self.win()
            
            if self.t2 - self.t1 > 5 :
                new_enemy = Enemy()
                self.enemy_list.append(new_enemy)
                self.enemy_physics_engine_list.append(arcade.PhysicsEnginePlatformer(new_enemy , self.ground_list , gravity_constant=self.gravity))
                self.t1 = time.time()

            for enemy in self.enemy_list:
                if arcade.check_for_collision(self.me , enemy):
                    self.me.health -= 1
                    self.remaining_hearts -= 1
                    self.enemy_list.remove(enemy)
                if self.me.health <= 0:
                    self.remaining_hearts = 0
            
            if self.me.health == 0:
                self.game_over()

    def game_over(self):
        self.game_over_flag = True
        arcade.draw_text("Game Over!", 50, 250, arcade.color.RED, 70)
        arcade.finish_render()
        arcade.pause(5)  # توقف بازی به مدت 5 ثانیه
        arcade.close_window()  # بستن پنجره بازی

    def win(self):
        self.win_flag = True
        arcade.draw_text("you win :)", 50, 250, arcade.color.RED, 70)
        arcade.finish_render()
        arcade.pause(5)  # توقف بازی به مدت 5 ثانیه
        arcade.close_window()  # بستن پنجره بازی



game = Game()
arcade.run()