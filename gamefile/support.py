from csv import reader
from os import walk
from settings import *
import math
import pygame

def import_csv_layout(path):
	terrain_map = []
	with open(path) as level_map:
		layout = reader(level_map,delimiter = ',')
		for row in layout:
			terrain_map.append(list(row))
		return terrain_map

def import_folder(path):
	surface_list = []

	for _,__,img_files in walk(path):
		for image in img_files:
			full_path = path + '/' + image
			image_surf = pygame.image.load(full_path).convert_alpha()
			surface_list.append(image_surf)
	return surface_list

def display_message(message,background):
	screen = pygame.display.set_mode((WIDTH, HEIGTH))
	main_background = pygame.image.load(background)
	screen.blit(main_background,(0,0))
	font = pygame.font.Font("C:/Users/kgdjd/PycharmProjects/pythongame2/graphics/font/joystix.ttf")
	timer = pygame.time.Clock()
	snip = font.render("",True,"white")
	counter = 0
	speed = 3
	done = False
	run = True
	while run:
		timer.tick(60)
		pygame.draw.rect(screen,"black",[0,630,1280,100])
		if counter<speed*len(message):
			counter+=1
		else:
			done=True

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				run = False
			elif event.type == pygame.QUIT:
				run = False
				pygame.quit()
				return 1
		snip = font.render(message[0:counter//speed],True,"white")
		screen.blit(snip,(330 - len(message) * math.log10(len(message)),650))
		pygame.display.flip()
	return -1

def cutscene1():
	display_message("Божество: «Мой старый друг, я так долго ждал нашей встречи».","background2.png")
	display_message("Аксолотль: «Давно не виделись Иса, я ушел в отставку не для того, чтобы тебя снова увидеть».","1 сцена для игры (1).png")
	display_message("Божество: «Я с радостью бы выпил с тобой в трактире, но мне нужна твоя помощь».","background2.png")
	display_message("Божество: «Твой брат уничтожает все что видит, нужно как можно скорее его остановить».","background2.png")
	display_message("Аксолотль: «Я так понимаю, он стал свирепее чем раньше... он всё-таки мой брат». ","1 сцена для игры (1).png")
	display_message("Божество: «Это твой долг хранителя».","background2.png")
	display_message("Божество: «Я тебе уже давно нашел учителя, он тебя ждет».","background2.png")
	display_message("Аксолотль: «Я ... еще не готов...».","black.bmp")
def cutscene2():
	display_message("Учитель: «О, привет, я твой наставник, меня зовут Модест».","teache_dialoge.png")
	display_message("Аксолотль: «Ты точно не ошибся?».", "teache_dialoge.png")
	display_message("Учитель: «Фи, не смей мне дерзить, у меня есть плащ и посох, значит я мудрее».", "teache_dialoge.png")
	display_message("Учитель: «Этот плащ передавался из поколения в поколение, я столько отважных подвигов совершил».", "teache_dialoge.png")
	display_message("Аксолотль: «Я промолчу тогда»..", "teache_dialoge.png")
	display_message("Учитель: «Пока я буду тут стоять фотогенично, тебе нужно будет бить противников, меня лично все устраивает».", "teache_dialoge.png")