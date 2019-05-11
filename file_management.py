#!/bin/env python3faire de a sau
# -*- coding: utf-8 -*-

""" Module de la classe qui se charge de faire la sauvergarde """

import pickle
import os
from random import randrange

class ManagementData:

    """
     Classe qui se charge du fichier des scores.

    - get_save_file:  cherche le dossier s'il exite
    - saving:  serialise le tableau de score
    - recovery: deserialise le donner du fichier

    """

    def __init__(self):
        """ Initialisaton de la classe avec un attribut privé : le chemin du fichier des scores """

        self.__save_path = "score"
        self.__file_french_word = "dico.txt"
        self.number_word_in_file = 323577


    def saving(self, players_score):
        """ Effectue la sauvegarde """

        with open(self.__save_path, "wb") as file:
            pickle.dump(players_score, file)

    def recovery(self):
        """ Renvoie le tableau des scores """
        try :

            if os.path.getsize(self.__save_path) > 0:
                with open(self.__save_path, "rb") as file:
                    score = pickle.load(file)
                return score
            else:
                return None
        except FileNotFoundError:
            return None

    def get_secret_word(self):

        number_line = randrange(1, self.number_word_in_file)

        with open(self.__file_french_word, "r")as file:
            for i in range(number_line):
                secret_word = file.readlines(1)[0].strip("\n")

        return secret_word



