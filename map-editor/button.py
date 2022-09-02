import math

import pygame


class Button():
	def __init__(self,pos, valeur):
		self.rect=pygame.Rect(pos[0], pos[1], 30,30)

		self.pressed=False
		self.valeur = valeur

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)


	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False
