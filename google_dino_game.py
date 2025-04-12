import pygame
import random
import sys

pygame.init()

WIDTH = 800
HEIGHT = 400
FPS = 120
GRAVITY = 0.8
JUMP_FORCE = -16
OBSTACLE_SPEED = 8

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chrome Dino Game")

clock = pygame.time.Clock()

class Dino:
    def __init__(self):
        self.width = 40
        self.height = 50
        self.x = 100
        self.y = HEIGHT - 100 - self.height
        self.vel_y = 0
        self.is_jumping = False

    def jump(self):
        if not self.is_jumping:
            self.vel_y = JUMP_FORCE
            self.is_jumping = True

    def update(self):
        self.vel_y += GRAVITY
        self.y += self.vel_y

        if self.y >= HEIGHT - 100 - self.height:
            self.y = HEIGHT - 100 - self.height
            self.is_jumping = False
            self.vel_y = 0

    def draw(self):
        pygame.draw.rect(screen, BLACK, (self.x, self.y, self.width, self.height))

class Obstacle:
    def __init__(self):
        self.width = 30
        self.height = random.randint(20, 60)  # 随机高度
        self.x = WIDTH
        self.y = HEIGHT - 100 - self.height  # 贴地生成
        self.speed = OBSTACLE_SPEED

    def update(self):
        self.x -= self.speed

    def draw(self):
        pygame.draw.rect(screen, BLACK, (self.x, self.y, self.width, self.height))

    def off_screen(self):
        return self.x < -self.width

def game_over():
    font = pygame.font.Font(None, 74)
    text = font.render('GAME OVER', True, BLACK)
    screen.blit(text, (WIDTH//2-140, HEIGHT//2-50))
    pygame.display.flip()
    pygame.time.wait(2000)

def main():
    dino = Dino()
    obstacles = []
    spawn_timer = 0
    next_spawn_interval = random.randint(40, 100)  # 初始随机间隔
    score = 0
    if score >= 2:
        FPS + 10

    running = True
    game_active = True

    while running:
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLACK, (0, HEIGHT-100, WIDTH, 100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game_active:
                    dino.jump()
                if event.key == pygame.K_r and not game_active:
                    main()

        if game_active:
            # 动态障碍物生成逻辑
            spawn_timer += 1
            if spawn_timer >= next_spawn_interval:
                obstacles.append(Obstacle())
                spawn_timer = 0
                next_spawn_interval = random.randint(40, 100)  # 生成新的随机间隔

            dino.update()
            for obstacle in obstacles:
                obstacle.update()
                # 精确碰撞检测
                if (dino.x < obstacle.x + obstacle.width and
                    dino.x + dino.width > obstacle.x and
                    dino.y < obstacle.y + obstacle.height and
                    dino.y + dino.height > obstacle.y):
                    game_active = False

            obstacles = [obstacle for obstacle in obstacles if not obstacle.off_screen()]
            score += 1

        dino.draw()
        for obstacle in obstacles:
            obstacle.draw()

        # 显示分数和间隔提示
        font = pygame.font.Font(None, 36)
        text = font.render(f'Score: {score//10}  Next: {next_spawn_interval} frames', True, BLACK)
        screen.blit(text, (10, 10))

        if not game_active:
            game_over()

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()