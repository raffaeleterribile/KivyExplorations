""" Modulo per la classe InputComponent """
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from components.component import Component

class Input(Component, BoxLayout):
	""" Classe Input """
	input_text = StringProperty("")
	output_text = StringProperty("")

	def on_button_press(self):
		"""Gestisce l'evento di pressione del bottone."""
		print(f"Testo inserito: {self.input_text}")
		self.output_text = f"Output: {self.input_text}"
