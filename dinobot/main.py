from PIL import Image, ImageGrab
import pyautogui
import time

cactus = 80
bird = 45

class Dino:

    def __init__(self):
        self.coords = (276, 390)
        self.speed = 0

    def obstacle(self):
        ''' Проверка препятствия на пути динозаврика '''
        area = (self.coords[0] + int(self.speed), self.coords[1],
                     self.coords[0] + 25 + int(self.speed), self.coords[1] + 131)

        screenshot = ImageGrab.grab(bbox = area)
        pixels = screenshot.load()

        background_color = pixels[0, 130]

        for i in reversed(range(0, 25)):
            if pixels[i, cactus] != background_color\
                or pixels[i, bird] != background_color:
                return True
        return False

    def jump(self):
        ''' Прыжок динозаврика '''
        self.increase_speed()
        pyautogui.keyDown('space')
        time.sleep(0.08)
        pyautogui.keyUp('space')

    def increase_speed(self):
        ''' Увеличение скорости динозаврика '''
        if self.speed < 14:
            self.speed += 0.4
        elif self.speed < 100:
            self.speed += 0.9

game = True
dino = Dino()

while game:
    try:
        if dino.obstacle():
            dino.jump()
    except Exception as e:
        game = False
        print(e)
