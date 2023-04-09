import random

from pygame import *


class Sprite:
    def __init__(self, x, y, filename, speed, w, h):
        self.image = transform.scale(image.load(filename), (w, h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(Sprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a]:
            self.rect.x -= self.speed
        if keys[K_d]:
            self.rect.x += self.speed


class Bot(Sprite):
    def update(self):
        self.rect.y += self.speed


init()

window = display.set_mode((700, 500))
fps = time.Clock()

run = True
background = transform.scale(image.load("galaxy.jpg"), (700, 500))
racketa = Player(400, 400, "rocket.png", 5, 100, 100)

bots = []
y = -500
for i in range(10):
    enemy = Bot(random.randint(0, 500), y, "asteroid.png", 10, 50, 50)
    bots.append(enemy)
    y -= 100
while run:
    # події
    for e in event.get():
        if e.type == QUIT:
            run = False
    # оновлення
    racketa.update()
    for bot in bots:
        bot.update()
        # якщо бот вийшов за нижню межу
        if bot.rect.y > 500:
            bot.rect.y -= 500

        # віднімаємо по y значення 500

    # рендер

    window.blit(background, [0, 0])
    for bot in bots:
        bot.draw(window)
    racketa.draw(window)
    display.flip()
    fps.tick(60)
