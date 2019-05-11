#!/bin/env python3
# -*- coding: utf-8 -*-


class RequestToThePlayer:
    """ Class qui s'ocupper de regouper les methodes afin de recupere les elements pour le jeu venant du joueur"""


    def get_name(self):
        """ demande le nom """

        name = str(input("Quels est votre nom/pseudo ?")).capitalize()

        if 1 > len(name) or len(name) > 8:

            print("Merci de saisir un nom/pseudo entre 1 et 8 caracteres")
            return None
        elif not name.isalnum():

            print("Merci de ne pas mettre d'espace dans le nom/pseudo ")
            return None
        else:

            return name

    def get_character(self):
        """ Module demande le character au joureur"""

        char = str(input("Entrez un caractere: ")).upper()

        if char.isdigit():
            print("Merci de d'incrire un caracterer")
            return None

        elif len(char) > 1:
            print("merci de ne rentrer qu'un seul caratere")
            return None

        return char

    def stop_or_again(self):
        """Module demande oui ou non au joureur """

        response = str(input("[Y/n]: ")).lower()

        if response == "y":
            return True
        elif response == "n":
            return False
        else:
            return None
