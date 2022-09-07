import math

import pygame


class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color, listeType=[]):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
		self.deg = 0
		self.sonBouton = pygame.mixer.Sound("data/son/effets/boutonMenu.mp3")
		self.sonBouton.set_volume(0.1)
		self.sonBoutonPress = pygame.mixer.Sound("data/son/effets/boutonPress.mp3")
		self.sonBoutonPress.set_volume(0.1)
		self.pressed2 = False
		self.pressed=False
		self.imageSelect = pygame.transform.scale(pygame.image.load("data/menu/backButtonMapS.png").convert_alpha(), (self.image.get_width(), self.image.get_height()))
		self.listeType = listeType #une map
	def getColor(self, i):
		if i == 1:
			color= (149, 199, 95)
		if i == 2:
			color = (114, 114, 114)
		if i == 3:
			color = (38,1,112)
		if i == 4:
			color = (63, 111, 65)
		if i==5:
			color = (194,218,225)
		if i == 6:
			color = (255,235, 230)
		if i == 7:
			color = (147, 34, 2)
		return color


	def update(self, screen):
		
		if self.image is not None:
			screen.blit(self.image, self.rect)
			if self.pressed2:

				screen.blit(self.imageSelect, self.rect)
		elif self.listeType:
			infoObject = pygame.display.Info()
			scale =infoObject.current_w//90
			posX = infoObject.current_w//1.7
			posY = infoObject.current_h//5
			for y in range(len(self.listeType)):
				for x in range(len(self.listeType[y])):  
					pygame.draw.rect(screen, self.getColor(self.listeType[y][x]), pygame.Rect(scale*x+scale+posX, scale*y+scale+posY, scale, scale))

		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
      
			self.text = self.font.render(self.text_input, True, self.hovering_color)
			if not self.pressed :
				pygame.mixer.Sound.play(self.sonBouton)
			self.pressed=True
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)
			self.pressed=False
