import pygame, sys
from pyvidplayer import Video
from settings import *
from level import Level
from button import ImageButton

vid = Video("background1.mp4")
vid.set_size((1280,720))
def intro():
    while True:
        vid.draw(screen,(0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                vid.close()
                main_menu()
                return -1

class Game:
	def __init__(self):

		# general setup
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
		pygame.display.set_caption('Game by Snya')
		self.clock = pygame.time.Clock()

		self.level = Level()

	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			self.screen.fill('black')
			self.level.run()
			pygame.display.update()
			self.clock.tick(FPS)

WIDTH, HEIGHT = 1280, 720
MAX_FPS = 60;

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu test")
main_background = pygame.image.load("background1.gif")
main_background  = pygame.transform.scale(main_background,(1280,720))

clock = pygame.time.Clock()

# Загрузка и установка курсора
cursor = pygame.image.load("cursor.png")
pygame.mouse.set_visible(False)  # Скрываем стандартный курсор

def main_menu():
    # Создание кнопок
    start_button = ImageButton(WIDTH/2-3*(252/2), 200, 252, 74, "", "button2_hover.png", "button2.png", "click.mp3")
    exit_button = ImageButton(WIDTH/2-3*(252/2), 300, 252, 74, "", "button1_on.png", "button1_off.png", "click.mp3")

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(main_background, (0, 0))
        font = pygame.font.Font(None, 72)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT and event.button == start_button:
                fade()
                return -1

            if event.type == pygame.USEREVENT and event.button == exit_button:
                running = False
                pygame.quit()
                sys.exit()

            for btn in [start_button, exit_button]:
                btn.handle_event(event)

        for btn in [start_button, exit_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        # Отображение курсора в текущей позиции мыши
        x, y = pygame.mouse.get_pos()
        screen.blit(cursor, (x-2, y-2))

        pygame.display.flip()

def fade():
    running = True
    fade_alpha = 0  # Уровень прозрачности для анимации

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Анимация затухания текущего экрана
        fade_surface = pygame.Surface((WIDTH, HEIGHT))
        fade_surface.fill((0, 0, 0))
        fade_surface.set_alpha(fade_alpha)
        screen.blit(fade_surface, (0, 0))

        # Увеличение уровня прозрачности
        fade_alpha += 5
        if fade_alpha >= 105:
            fade_alpha = 255
            running = False

        pygame.display.flip()
        clock.tick(MAX_FPS)  # Ограничение FPS


if __name__ == "__main__":
	intro()
	game = Game()
	game.run()