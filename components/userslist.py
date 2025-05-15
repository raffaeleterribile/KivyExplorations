""" Classe per la lista degli utenti """
from components.component import Component
from kivy.uix.recycleview import RecycleView
from kivy.properties import ListProperty

class UsersList(Component, RecycleView):
	""" Classe per la lista degli utenti """
	users = ListProperty([])  # Lista di utenti

	def __init__(self, **kwargs):
		super(UsersList, self).__init__(**kwargs)
		self.data = []  # Inizializza la lista dei dati
		self.bind(users=self.update_data)  # Collega l'evento di aggiornamento dei dati

	def update_data(self, instance, value):
		"""Aggiorna i dati della lista."""
		self.data = [{'user_name': user['user_name'], 'email': user['email']} for user in value]