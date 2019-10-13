#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-10-05 08:44:05
# @Author  : King-Key
# @Email   : guo_wang_113@163.com
# @Link    : https://king-key.github.io


from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color,Ellipse,Line



#画板
class MyPaintWidget(Widget):

	def on_touch_down(self,touch):
		print(touch)
		with self.canvas:
			#画笔颜色
			Color(1,1,0)
			#画笔大小
			d=5.
			Ellipse(pos=(touch.x-d/2,touch.y-d/2),size=(d,d))
			touch.ud['line']=Line(points=(touch.x,touch.y))


	def on_touch_move(self,touch):
		touch.ud['line'].points+=[touch.x,touch.y]
	


class MyPaintApp(App):
	"""docstring for Pain"""
	#初始化
	def build(self):
		parent=Widget()
		self.painter=MyPaintWidget()
		clean_button=Button(text="clean")
		clean_button.bind(on_release=self.clean_canvas)

		parent.add_widget(self.painter)
		parent.add_widget(clean_button)

		return parent

	#清除操作函数
	def clean_canvas(self,object):
		self.painter.canvas.clear()


if __name__ == '__main__':
	MyPaintApp().run()
		


 
