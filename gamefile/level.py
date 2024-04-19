import pygame 
from settings import *
from tile import Tile
from player import Player
from debug import debug
from support import *
from random import choice
from weapon import Weapon
from HealthBar import healthbar
from enemy import Enemy


class Level:
	def __init__(self):

		# задача поверхности дисплея
		self.display_surface = pygame.display.get_surface()

		# установка групп спрайтов
		self.visible_sprites = YSortCameraGroup()
		self.obstacle_sprites = pygame.sprite.Group()

		self.current_attack = None
		self.attack_sprites = pygame.sprite.Group()
		self.attackable_sprites = pygame.sprite.Group()
		self.health = 5
		cutscene1()
		cutscene2()

		self.createhealth = healthbar()
		# установка спрайтов
		self.create_map()



	def create_map(self):
		layouts = {
			'boundary':import_csv_layout("C:/Users/kgdjd/PycharmProjects/pythongame2/map/Tutorial._Unvision.csv"),
			"trees": import_csv_layout("C:/Users/kgdjd/PycharmProjects/pythongame2/map/Tutorial._Деревья.csv"),
			'object': import_csv_layout('C:/Users/kgdjd/PycharmProjects/pythongame2/map/Tutorial._Объекты.csv'),
			"entities": import_csv_layout("C:/Users/kgdjd/PycharmProjects/pythongame2/map/Tutorial._Сущности.csv")
		}
		graphics = {
			'trees': import_folder('C:/Users/kgdjd/PycharmProjects/pythongame2/graphics/trees'),
			'objects': import_folder('C:/Users/kgdjd/PycharmProjects/pythongame2/graphics/objects')
		}
		for style,layout in layouts.items():
			for row_index,row in enumerate(layout):
				for col_index, col in enumerate(row):
					if col != '-1':
						x = col_index * TILESIZE
						y = row_index * TILESIZE
						if style == 'boundary':
							Tile((x,y),[self.obstacle_sprites],'invisible')
						if style == 'trees':
							random_trees_image = choice(graphics['trees'])
							Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'trees', random_trees_image)

						if style == 'object':
							surf = graphics['objects'][int(col)]
							Tile((x,y+128),[self.visible_sprites,self.obstacle_sprites],'object',surf)
						if style == "entities":
							if col == "2":
								self.player = Player((x,y+64),[self.visible_sprites],self.obstacle_sprites,self.create_attack,self.destroy_attack)
							if col == "0":
								Enemy("demon",(x,y+64),[self.visible_sprites,self.attackable_sprites],self.obstacle_sprites,self.damage_player)
							if col == "1":
								Enemy("big_demon", (x, y+64), [self.visible_sprites,self.attackable_sprites], self.obstacle_sprites, self.damage_player)
	def create_attack(self):
		self.current_attack = Weapon(self.player,[self.visible_sprites,self.attack_sprites])

	def destroy_attack(self):
		if self.current_attack:
			self.current_attack.kill()
		self.current_attack = None
	def player_attack_logic(self):
		if self.attack_sprites:
			for attack_sprite in self.attack_sprites:
				collision_sprites = pygame.sprite.spritecollide(attack_sprite,self.attackable_sprites,False)
				if collision_sprites:
					for target_sprite in collision_sprites:
						if target_sprite.sprite_type == 'grass':
							target_sprite.kill()
						else:
							target_sprite.get_damage(self.player,attack_sprite.sprite_type)
	def damage_player(self,amount,attack_type):
		if self.player.vulnerable:
			self.health -= 1
			self.createhealth.image = health_ani[self.health]
			self.createhealth.render(self.display_surface)
			self.player.vulnerable = False
			self.player.hurt_time = pygame.time.get_ticks()
	def run(self):
		# обновление и отрисовка игры
		self.visible_sprites.custom_draw(self.player)
		self.visible_sprites.update()
		self.visible_sprites.enemy_update(self.player)
		self.createhealth.render(self.display_surface)


class YSortCameraGroup(pygame.sprite.Group):
	def __init__(self):

		# главная установка
		super().__init__()
		self.display_surface = pygame.display.get_surface()
		self.half_width = self.display_surface.get_size()[0] // 2
		self.half_height = self.display_surface.get_size()[1] // 2
		self.offset = pygame.math.Vector2()

		# создание пола
		self.floor_surf = pygame.image.load('C:/Users/kgdjd/PycharmProjects/pythongame2/graphics/tilemap/ground.png').convert()
		self.floor_rect = self.floor_surf.get_rect(topleft = (0,75))

	def custom_draw(self, player):

		# getting the offset
		self.offset.x = player.rect.centerx - self.half_width
		self.offset.y = player.rect.centery - self.half_height

		# drawing the floor
		floor_offset_pos = self.floor_rect.topleft - self.offset
		self.display_surface.blit(self.floor_surf, floor_offset_pos)

		# for sprite in self.sprites():
		for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
			offset_pos = sprite.rect.topleft - self.offset
			self.display_surface.blit(sprite.image, offset_pos)

	def enemy_update(self, player):
		enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite, 'sprite_type') and sprite.sprite_type == 'enemy']
		for enemy in enemy_sprites:
			enemy.enemy_update(player)
