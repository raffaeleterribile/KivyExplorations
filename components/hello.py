""" Modulo per la classe Hello """
from kivy.properties import StringProperty
from kivy.uix.floatlayout import FloatLayout
from components.component import Component

class Hello(Component, FloatLayout):
	""" Classe Hello """
	text = StringProperty("Hello, World!")
