import pygame
import random
import sys

# 初始化Pygame
pygame.init()

# 游戏常量
WIDTH = 800
HEIGHT = 400
FPS = 60
GRAVITY = 0.8
JUMP_FORCE = -16
OBSTACLE_SPEED = 8

# 颜色定义
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 初始化游戏窗口
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

        # 地面碰撞检测
        if self.y >= HEIGHT - 100 - self.height:
            self.y = HEIGHT - 100 - self.height
            self.is_jumping = False
            self.vel_y = 0

    def draw(self):
        pygame.draw.rect(screen, BLACK, (self.x, self.y, self.width, self.height))

class Obstacle:
    def __init__(self):
        self.width = 30
        self.height = 50
        self.x = WIDTH
        self.y = HEIGHT - 100 - self.height
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
    score = 0

    running = True
    game_active = True

    while running:
        screen.fill(WHITE)

        # 绘制地面
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
                    main()  # 重新开始游戏

        if game_active:
            # 生成障碍物
            spawn_timer += 1
            if spawn_timer > random.randint(40, 80):
                obstacles.append(Obstacle())
                spawn_timer = 0

            # 更新游戏元素
            dino.update()
            for obstacle in obstacles:
                obstacle.update()
                # 碰撞检测
                if (dino.x < obstacle.x + obstacle.width and
                    dino.x + dino.width > obstacle.x and
                    dino.y < obstacle.y + obstacle.height and
                    dino.y + dino.height > obstacle.y):
                    game_active = False

            # 移除屏幕外的障碍物
            obstacles = [obstacle for obstacle in obstacles if not obstacle.off_screen()]

            # 更新分数
            score += 1

        # 绘制元素
        dino.draw()
        for obstacle in obstacles:
            obstacle.draw()

        # 显示分数
        font = pygame.font.Font(None, 36)
        text = font.render(f'Score: {score//10}', True, BLACK)
        screen.blit(text, (10, 10))

        if not game_active:
            game_over()

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()