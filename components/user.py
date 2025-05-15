""" Classe per gli utenti """
from components.component import Component
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty

class User(Component, GridLayout):
    user_name = StringProperty()
    first_name = StringProperty()
    last_name = StringProperty()
    email = StringProperty()

