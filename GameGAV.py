import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Константы для экрана
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Survival Game")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Скорость игрока и врага
PLAYER_SPEED = 5
ENEMY_SPEED = 3

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

        # Ограничиваем движение в пределах экрана
        self.rect.x = max(0, min(WIDTH - self.rect.width, self.rect.x))
        self.rect.y = max(0, min(HEIGHT - self.rect.height, self.rect.y))

    def draw(self):
        pygame.draw.rect(SCREEN, WHITE, self.rect)

class Enemy:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(0, WIDTH - 50), random.randint(0, HEIGHT - 50), 50, 50)
        self.direction = random.choice([-1, 1]), random.choice([-1, 1])

    def move(self):
        self.rect.x += self.direction[0] * ENEMY_SPEED
        self.rect.y += self.direction[1] * ENEMY_SPEED

        # Меняем направление при столкновении с краем экрана
        if self.rect.x <= 0 or self.rect.x >= WIDTH - self.rect.width:
            self.direction = (-self.direction[0], self.direction[1])
        if self.rect.y <= 0 or self.rect.y >= HEIGHT - self.rect.height:
            self.direction = (self.direction[0], -self.direction[1])

    def draw(self):
        pygame.draw.rect(SCREEN, RED, self.rect)

class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.player = Player(WIDTH // 2, HEIGHT // 2)
        self.enemies = [Enemy() for _ in range(5)]
        self.running = True

    def run(self):
        while self.running:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(60)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        keys = pygame.key.get_pressed()
        dx = dy = 0
        if keys[pygame.K_LEFT]:
            dx = -PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            dx = PLAYER_SPEED
        if keys[pygame.K_UP]:
            dy = -PLAYER_SPEED
        if keys[pygame.K_DOWN]:
            dy = PLAYER_SPEED

        self.player.move(dx, dy)

        for enemy in self.enemies:
            enemy.move()
            if self.player.rect.colliderect(enemy.rect):
                print("Game Over!")
                self.running = False

    def draw(self):
        SCREEN.fill(BLACK)
        self.player.draw()
        for enemy in self.enemies:
            enemy.draw()
        pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()
    sys.exit()