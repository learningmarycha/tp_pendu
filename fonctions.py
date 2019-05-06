#!/bin/env python3
# -*- coding: utf-8 -*-


import pickle
import donnee
from random import randrange


def initialization_game():
    """ Verifie que le fichier existe"""

    try:
        with open("score", "rb") as file:
            score = pickle.load(file)

        return score

    except IOError:
        return None
        pass


def home(array):
    """Home affiche l'ecran d'acceuil """

    score = sorted(array.items(), key=lambda t: t[1], reverse=True)

    print("""
    Bienvenue sur le jeu du pendu !!
    
     ________ Meilleur score: _______
    """)

    for i in score:
        print("   --- Joueur:[ {} >> {} pts ] ---\n".format(i[0], i[1]))

    print("Commencer une nouvelle partie [Y/n] ?")


def user_name():
    """ Recupere le nom de l'utilisateur avec nos criteres"""

    name = str(input("Quel est votre nom/pseudo ? "))

    if len(name) > 8 or len(name) < 1:
        print(" Entrez un pseudo ou un nom entre 1 et 8 caractere")

    elif not name.isalnum():
        print("Merci de mettre aucun espace dans le pseudo")

    else:
        return name


def collect_name(scoreboard):
    """ Regarde si le nom est deja inscris dans le tableaux des scores"""
    user = None
    while user is None:
        user = user_name()
    try:
        scoreboard[user]
        print("""Content de vous revoir {}! 
        
        Voici votre score actuel: {} pts\n""".format(user, scoreboard[user]))
        return user

    except KeyError:
        print("\nBienvenue {} !\n".format(user))
        scoreboard[user] = 0
        return user
        pass


def yes_or_not_answer():
    """ Recupere seulement oui ou non quand la question est poser"""

    user = str(input("[ Y / n ]: ")).lower()

    if user != 'y' and user != 'n':
        print(" Tapez seulement [ y ] pour oui [ n ] pour non ")

        return None
    else:
        return user


def choice_word(number):
    """ Se charge de chercher un mots parmis le fichier"""

    with open("dico.txt", "r") as file:
        for i in range(number):
            word = file.readlines(1)

        return word


def capture_character():
    """ Capture un seul caractere """

    user = str(input("Tapez un caractere: ")).upper()

    if user.isdigit() and len(user) > 1:
        print("Merci de tapez une lettre")

        return None
    else:
        return user


def change_character(c, word, star_word):
    """Cherche le cararctere et le remplace s'il trouve"""

    word = [i for i in word[0]]
    star_word = [i for i in star_word[0]]

    for i in range(len(word)):
        if c == word[i]:
            star_word[i] = c

    return "".join(star_word)


def end_game(scrt_wrd, hid_wrd, scr_ply):
    """ renvois le score du joueur """

    count = 0
    if scrt_wrd == hid_wrd:
        print(""" ****  Victoire !! **** 
        
        Le mots mystère etait: {}
        
        Vous remporter {} pts 
        
        """.format(scrt_wrd, scr_ply))
    else:
        for i in hid_wrd:
            if i == '*':
                count += 1
        print("""
        Désoler vous n'avez pas trouver cette fois si !!
        
        Le mots mystere etait : {}
        
        Vous perdez {} pts
        """.format(scrt_wrd, count))

    return scr_ply - count


def score_save(score):
    """ Fait une sauvegarde des scores """

    with open("score", "wb") as file:
        pickle.dump(score, file)


def begin_game(name_ply):
    """ commencement du jeu """
    secret_word = choice_word(randrange(1, donnee.number_word_in_file))
    secret_word = "".join(secret_word).strip('\n')

    hidden_word = str()
    for i in range(len(secret_word)):
        hidden_word += '*'

    score_player = {name_ply: len(secret_word)}

    first_pass = True
    while hidden_word != secret_word and score_player[name_ply] > 0:

        if first_pass:
            print("""Voici le mots mystère {} 
                Pour ce mots vous avez {} chances""".format(hidden_word, score_player[name_ply]))

            first_pass = False

        else:
            print("\nMots mystère : {}  nombre coups restant {}\n".format(hidden_word, score_player[name_ply]))

        character = None
        while character is None:
            character = capture_character()

        if character in secret_word and character not in hidden_word:
            hidden_word = change_character(character, secret_word.split(), hidden_word.split())

        elif character in hidden_word:
            print("Vous avez déja tapé le cararactere {} vous perdez 1 pts".format(character))
            score_player[name_ply] -= 1

        else:
            print("Il n'y a pas le caractere {} dans le mot vous perdez 1 pts".format(character))
            score_player[name_ply] -= 1

    return int(end_game(scrt_wrd=secret_word, hid_wrd=hidden_word, scr_ply=score_player[name_ply]))


def course_of_the_game():
    """Recupere les scores et le nom du joueur """

    donnee.scoreboard = initialization_game()
    if donnee.scoreboard is not None:
        home(array=donnee.scoreboard)
    else:
        donnee.scoreboard = dict()

        print("""
        Bienvenue sur le jeu du pendu !!
        
            ** Aucun score a affiché **
            
        Commencer la partie ?""")

    user = None
    while user is None:
        user = yes_or_not_answer()

    if user == 'y':

        player_name = collect_name(scoreboard=donnee.scoreboard)

        score = begin_game(name_ply=player_name)
        donnee.scoreboard[player_name] += score
        score_save(score=donnee.scoreboard)

    else:
        print("A bientot! ")
        return None

    return True
