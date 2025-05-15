""" Classe per la lista degli utenti"""
from components.component import Component
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, ListProperty
from components.user import User  # pylint: disable=unused-import (W0611)
from components.user import User  # Importa il componente User

class Users(Component, BoxLayout):
	""" Classe per la lista degli utenti """
	new_user = ObjectProperty(User())
	users = ListProperty([])
	users_list = ListProperty([])  # Lista di utenti

	def __init__(self, **kwargs):
		super(Users, self).__init__(**kwargs)
		self.orientation = "vertical"

	def add_user(self, user):
		"""Aggiunge un nuovo utente alla lista."""
		if user.user_name and user.email:  # Controlla che i campi siano popolati
			user_data = {
				'user_name': user.user_name,
				'first_name': user.first_name,
				'last_name': user.last_name,
				'email': user.email
			}
			self.users.append(user_data)  # Aggiungi il dizionario alla lista
			print(f"Utente aggiunto: {user_data}")
			self.refresh_users()  # Aggiorna la visualizzazione degli utenti
		else:
			print("Errore: i campi utente non sono completi.")

	def remove_user(self, user):
		"""Rimuove un utente dalla lista e aggiorna l'interfaccia."""
		if user in self.users:
			self.users.remove(user)
			# self.refresh_users()

	def refresh_users(self):
		"""Aggiorna la visualizzazione degli utenti."""
		pass
		# self.ids.users.refresh_from_data()  # Aggiorna la visualizzazione
