""" Applicazione principale """
import kivy
from kivy.app import App
from kivy.lang import Builder  # Importa Builder per caricare manualmente i file .kv
from components.component import Component  # pylint: disable=unused-import (W0611)
from components.hello import Hello  # pylint: disable=unused-import (W0611)
from components.input import Input  # pylint: disable=unused-import (W0611)
from components.users import Users  # pylint: disable=unused-import (W0611)
from components.userslist import UsersList  # pylint: disable=unused-import (W0611)

kivy.require("2.3.1")  # Versione minima di Kivy richiesta


class Main(App):
	""" Classe principale dell'applicazione """
	def __init__(self, **kwargs):
		super(Main, self).__init__(**kwargs)
		self.title = "My Kivy App"
	
if __name__ == "__main__":
	app = Main()
	app.run()
