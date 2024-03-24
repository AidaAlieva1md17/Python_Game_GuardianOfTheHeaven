from csv import reader
from os import walk
from settings import *
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

def display_message(message):
	screen = pygame.display.set_mode((WIDTH, HEIGTH))
	font = pygame.font.Font("C:/Users/kgdjd/PycharmProjects/pythongame2/graphics/font/joystix.ttf")
	timer = pygame.time.Clock()
	snip = font.render("",True,"white")
	counter = 0
	speed = 3
	done = False
	run = True
	while run:
		timer.tick(60)
		pygame.draw.rect(screen,"black",[0,520,1280,200])
		if counter<speed*len(message):
			counter+=1
		else:
			done=True

		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				run = False
			elif event.type == pygame.QUIT:
				run = False
				pygame.quit()
				return 1
		snip = font.render(message[0:counter//speed],True,"white")
		screen.blit(snip,(550,550))
		pygame.display.flip()
	return -1
