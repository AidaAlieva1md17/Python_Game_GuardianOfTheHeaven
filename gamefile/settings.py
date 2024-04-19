import pygame
# game setup
WIDTH    = 1280
HEIGTH   = 720
FPS      = 60
TILESIZE = 64

health_ani = [pygame.image.load("health1.png"),
              pygame.image.load("health2.png"), pygame.image.load("health3.png"),
              pygame.image.load("health4.png"), pygame.image.load("health5.png")]

weapon_data = {
	'sword': {'cooldown': 100, 'damage': 15,'graphic':'../graphics/weapons/sword/full.png'},
	}

monster_data = {
	'demon': {'health': 100,'damage':1,'attack_type': 'slash', 'speed': 1, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
	'big_demon': {'health': 300,'damage':1,'attack_type': 'claw','speed': 1, 'resistance': 3, 'attack_radius': 120, 'notice_radius': 400},
	}
