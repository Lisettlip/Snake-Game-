import pygame
import random
import sys

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (220, 0, 0)
YELLOW = (255, 255, 0)

WIDTH = 800
HEIGHT = 600
BLOCK = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

font = pygame.font.SysFont("bahnschrift", 30)
score_font = pygame.font.SysFont("comicsansms", 28)


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def draw_text(text, color, x, y, font_type=font):
    message = font_type.render(text, True, color)
    screen.blit(message, (x, y))


class Snake:
    def __init__(self):
        self.body = [
            Position(WIDTH // 2, HEIGHT // 2),
            Position(WIDTH // 2 - BLOCK, HEIGHT // 2),
            Position(WIDTH // 2 - BLOCK * 2, HEIGHT // 2)
        ]

        self.x_change = BLOCK
        self.y_change = 0

    def move(self):
        head = self.body[0]

        new_head = Position(
            head.x + self.x_change,
            head.y + self.y_change
        )

        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        head = self.body[0]

        new_head = Position(
            head.x + self.x_change,
            head.y + self.y_change
        )

        self.body.insert(0, new_head)

    def draw(self):
        for part in self.body:
            pygame.draw.rect(
                screen,
                GREEN,
                [part.x, part.y, BLOCK, BLOCK]
            )

    def score(self):
        return len(self.body) - 3

    def hit_wall(self):
        head = self.body[0]

        return (
            head.x < 0 or
            head.x >= WIDTH or
            head.y < 0 or
            head.y >= HEIGHT
        )

    def hit_self(self):
        head = self.body[0]

        for part in self.body[1:]:
            if head.x == part.x and head.y == part.y:
                return True

        return False


class Food:
    def __init__(self):
        self.position = Position(0, 0)
        self.randomize([])

    def randomize(self, snake_body):
        while True:
            self.position.x = random.randrange(0, WIDTH - BLOCK, BLOCK)
            self.position.y = random.randrange(0, HEIGHT - BLOCK, BLOCK)

            food_on_snake = False

            for part in snake_body:
                if self.position.x == part.x and self.position.y == part.y:
                    food_on_snake = True

            if not food_on_snake:
                break

    def draw(self):
        pygame.draw.rect(
            screen,
            RED,
            [self.position.x, self.position.y, BLOCK, BLOCK]
        )


class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.game_over = False
        self.speed = 10
        self.high_score = 0

    def reset(self):
        self.snake = Snake()
        self.food = Food()
        self.game_over = False
        self.speed = 10

    def draw_score(self):
        draw_text(
            "Score: " + str(self.snake.score()),
            WHITE,
            10,
            10,
            score_font
        )

        draw_text(
            "High Score: " + str(self.high_score),
            YELLOW,
            10,
            45,
            score_font
        )

    def check_food_collision(self):
        head = self.snake.body[0]

        if head.x == self.food.position.x and head.y == self.food.position.y:
            self.snake.grow()
            self.food.randomize(self.snake.body)

            if self.snake.score() > self.high_score:
                self.high_score = self.snake.score()

    def check_game_over(self):
        if self.snake.hit_wall() or self.snake.hit_self():
            self.game_over = True

    def game_over_screen(self):
        screen.fill(BLACK)

        draw_text("GAME OVER", RED, WIDTH // 2 - 110, HEIGHT // 2 - 100)
        draw_text("Score: " + str(self.snake.score()), WHITE, WIDTH // 2 - 70, HEIGHT // 2 - 50)
        draw_text("High Score: " + str(self.high_score), YELLOW, WIDTH // 2 - 100, HEIGHT // 2)

        draw_text("Press C to play again", WHITE, WIDTH // 2 - 140, HEIGHT // 2 + 60)
        draw_text("Press Q to quit", WHITE, WIDTH // 2 - 100, HEIGHT // 2 + 100)

        pygame.display.update()

        waiting = True

        while waiting:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        self.reset()
                        waiting = False

                    elif event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()

    def handle_keys(self, event):
        if event.key == pygame.K_LEFT:
            if self.snake.x_change != BLOCK:
                self.snake.x_change = -BLOCK
                self.snake.y_change = 0

        elif event.key == pygame.K_RIGHT:
            if self.snake.x_change != -BLOCK:
                self.snake.x_change = BLOCK
                self.snake.y_change = 0

        elif event.key == pygame.K_UP:
            if self.snake.y_change != BLOCK:
                self.snake.y_change = -BLOCK
                self.snake.x_change = 0

        elif event.key == pygame.K_DOWN:
            if self.snake.y_change != -BLOCK:
                self.snake.y_change = BLOCK
                self.snake.x_change = 0

    def run(self):
        while True:

            while self.game_over:
                self.game_over_screen()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    self.handle_keys(event)

            screen.fill(BLACK)

            self.food.draw()
            self.snake.move()
            self.snake.draw()
            self.draw_score()

            self.check_food_collision()
            self.check_game_over()

            pygame.display.update()
            clock.tick(self.speed)


game = Game()
game.run()
