#!/bin/env python3
# -*- coding: utf-8 -*-

""" Module de la class qui se charge de l'affichage pour l'utilisateur """


class DisplayGame:

    def __init__(self, scoreboard=None):

        self.__display_default_score = "*** Aucun score à affichés ***"
        self.scoreboard = scoreboard

    def home(self):
        """ Retourne un un acceuil avec les scores s'il y en a """

        if self.scoreboard is not None:
            file_score = list(sorted(self.scoreboard.items(), key=lambda t: t[1], reverse=True))
            print("""
                Bienvenue sur le jeu du pendu !!

                 ________ Meilleur score: _______
                """)

            for i in file_score:
                print("   --- Joueur:[ {} >> {} pts ] ---\n".format(i[0], i[1]))

            print("Commencer une nouvelle partie [Y/n] ?")
        else:
            print("""
            
                    Bienvenue sur le jeu du pendu !!
                
                    {}
                        
                Commencer une nouvelle partie [Y/n] ?
                """.format(self.__display_default_score))

    def display_hidden_word(self, secret_word, hid_word, character):
        """ Retourne la representation du mots masqué"""
        hid_wrd = [c for c in hid_word[0]]

        for i in range(len(secret_word)):

            if character == secret_word[i]:
                hid_wrd[i] = character

        return "".join(hid_wrd)

    def welcome_player(self, name_player, actual_score):
        """Souhaite la bienvenue au jouer et affiche sont score precedent"""

        try:

            print("\nContent de vous revoir {} vous avez un total de {} pts\n".format(name_player,
                                                                                      actual_score[name_player]))


        except KeyError:
            print("Bienvenue {} !!".format(name_player))
            return None


    def eng_game(self, secret_word, hidd_word):

        if secret_word == hidd_word:
            return """
            Victoire !!! 
            
            Vous remportez {} pts"""
        else:
            return """
            
            Dommage !!
            
            Nombre de point enlever a votre score: {} """
