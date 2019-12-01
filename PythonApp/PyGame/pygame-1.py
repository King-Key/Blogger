#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-11-20 18:14:41
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import pygame
import sys
from pygame.locals import *
pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')
while True:  # main game loop
	for event in pygame.event.get():
		print(pygame.event.get())
		if event.type == QUIT:
			print(event.type)
			pygame.quit()
			sys.exit()
	pygame.display.update()
