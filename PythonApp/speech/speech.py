#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-30 07:39:40
# @Author  : King-Key
# @Email   : guo_wang_113@163.com
# @Link    : https://king-key.github.io


from aip import AipSpeech
import pygame
import time
 
""" 你的 APPID AK SK """
APP_ID = '17387925'
API_KEY = 'dkVIhFTLstUr9gVgjbtG6ypg'
SECRET_KEY = 'KA1NVpQ7MyQVLjsVuPyPuPXZcsM6DxXp'
 
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

path="auido.mp3"
text_path="text.txt"

with open(text_path) as txt:
	print(txt.readlines())

	result  = client.synthesis("你好", 'zh', 1, {
	    'vol': 5,'per':0
	})
	 
	 
	# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
	if not isinstance(result, dict):
	    with open(path, 'wb') as f:
	    	f.write(result)

	pygame.mixer.init()
	track = pygame.mixer.music.load(path)
	pygame.mixer.music.play()
	time.sleep(2)