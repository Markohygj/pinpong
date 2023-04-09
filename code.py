from pygame import *
from random import randint

missEnemy = 0
def game():
    def showEndWindow(window, message):
        clock = time.Clock()
        run = True
        font.init()
        text = font.Font(None, 70).render(message, True, (255, 255, 255))
        while run:
            # обробка подій
            for e in event.get():
                if e.type == QUIT:
                    quit()

            #рендер
            window.blit(text, (250, 250))
            display.update()
            clock.tick(60)


    class GameSprite(sprite.Sprite):
        def __init__(self, player_image, x, y, speed, size_w, size_h):
            super().__init__()
            self.speed = speed
            self.player_image = transform.scale(image.load(player_image), (size_w, size_h))
            self.rect = self.player_image.get_rect()
            self.rect.x = x
            self.rect.y = y

        def draw(self, screen):
            screen.blit(self.player_image, (self.rect.x, self.rect.y))

    class Hero(GameSprite):
        def __init__(self, player_image, x, y, speed, size_w, size_h):
            super().__init__(player_image, x, y, speed, size_w, size_h)
            self.bullets = []

        def update(self):
            keys = key.get_pressed()
            if keys[K_a]:
                self.rect.x -= self.speed
            if keys[K_d]:
                self.rect.x += self.speed
            for bullet in self.bullets:
                bullet.update()

        def draw(self, screen):
            screen.blit(self.player_image, (self.rect.x, self.rect.y))
            for bullet in self.bullets:
                bullet.draw(screen)

    class Bullet(GameSprite):
        def update(self):
            self.rect.y -= self.speed

    class Enemy(GameSprite):
        def update(self):
            global missEnemy
            self.rect.y += self.speed
            if self.rect.y > 550:
                self.rect.y = -100
                self.rect.x = randint(0, 500)
                missEnemy += 1


    killEnemy = 0
    mixer.init()
    mixer.music.load('audio1.ogg')
    mixer.music.play(-1)
    mixer.music.set_volume(0.1)

    shootSound = mixer.Sound('audio2.ogg')
    shootSound.play()

    monsters = []
    y = 0
    for i in range(5):
        monsters.append(Enemy("asteroid.png", randint(0, 700), y, 2, 50, 50), )
        y -= 50
    rocket = Hero("rocket.png", 250, 400, 4, 81, 120)
    window = display.set_mode((700, 500))
    clock = time.Clock()
    background = transform.scale(image.load("galaxy.jpg"), (700, 500))


    font.init()
    font1 = font.Font(None, 20)

    while True:
        #обробка подій
        for e in event.get():
            if e.type == QUIT:
                quit()
            if e.type == KEYDOWN:
                if e.key == K_SPACE:
                    rocket.bullets.append(Bullet("pula.jpg", rocket.rect.centerx, rocket.rect.y, 10, 5, 10))
                    shootSound.play()

        # оновлення обєктів

        for mon in monsters:
            mon.update()
        rocket.update()

        text2 = font1.render("Кількість пропущених: " + str(missEnemy), False, (255, 255, 255))
        text = font1.render("Кількість знищенних: " + str(killEnemy), False, (255, 255, 255))

        for mon in monsters:
            if rocket.rect.colliderect(mon.rect):
                showEndWindow(window, "Ти програв!")
        if missEnemy >= 3:
            showEndWindow(window, "Ти програв!")

        window.blit(background, (0, 0))
        for mon in monsters:
            mon.draw(window)

        for mon in monsters:
            for bullet in rocket.bullets:
                if bullet.rect.colliderect(mon.rect):
                    mon.rect.x = randint(0, 500)
                    mon.rect.y = -100
                    rocket.bullets.remove(bullet)
                    killEnemy += 1
                    break
        rocket.draw(window)
        window.blit(text, [0, 0])
        window.blit(text2, [0, 50])
        display.update()
        clock.tick(60)