""" Modulo per la classe base per i componenti """
import os
from kivy.uix.widget import Widget
from kivy.lang import Builder
from threading import Lock

class Component(Widget):
    """ Classe base per i componenti """
    # Variabile di classe per tracciare i file .kv caricati
    _loaded_kv_files = set()
    _lock = Lock()

    def __init__(self, **kwargs):
        # Disabilita il caricamento automatico di Kivy
        kwargs['__no_builder'] = True
        super(Component, self).__init__(**kwargs)
        
        # Determina il percorso relativo del file .kv basato sul nome del modulo e della classe
        class_name = self.__class__.__name__.lower()
        module_path = os.path.dirname(__file__)
        kv_file = os.path.join(module_path, f"{class_name}.kv")
        
        # Controllo preliminare fuori dal lock
        if kv_file in Component._loaded_kv_files:
            return
        
        # Caricamento thread-safe
        with Component._lock:
            if kv_file not in Component._loaded_kv_files:
                if os.path.exists(kv_file):
                    Builder.load_file(kv_file)
                    # Aggiunge il file al set
                    Component._loaded_kv_files.add(kv_file)
                    print(f"File .kv caricato: {kv_file}")
                else:
                    raise FileNotFoundError(f"File .kv non trovato: {kv_file}")