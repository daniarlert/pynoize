import os
import pygame
from perlin_noise import PerlinNoise

noise = PerlinNoise(octaves=10, seed=42)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

os.environ["SDL_VIDEO_CENTERED"] = "1"
RES = WIDTH, HEIGHT = 640, 1080
FPS = 24

chars = ".,-~:;=!*#$@"

pygame.init()

pygame.display.set_caption("Pynoize")

screen = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
font = pygame.font.SysFont("Fira Code", 20, bold=True)
char_width, char_height = font.size(" ")

scale = 0.1
# scale = 0.015  # Controls noise granularity
rows = int(HEIGHT / char_height)
cols = int(WIDTH / char_width)

start_time = pygame.time.get_ticks()

i = 0
record = True
while True:
    clock.tick(FPS)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                pygame.quit()
                exit()
            elif event.key == pygame.K_r:
                record = not record

    current_time = pygame.time.get_ticks()
    elapsed_time = current_time - start_time

    for row in range(rows):
        for col in range(cols):
            x = col * scale + elapsed_time / 1000
            y = row * scale  # * 0.4 + elapsed_time / 1000

            noise_value = noise([x, y])
            index = int((len(chars) - 1) * noise_value)
            char = chars[index]
            text_surface = font.render(char, True, WHITE)
            screen.blit(text_surface, (col * char_width, row * char_height))

    if record:
        pygame.image.save(screen, f"frames/frame_{i}.png")
        i += 1

    pygame.display.update()
