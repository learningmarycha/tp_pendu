#!/bin/env python3
# -*- coding: utf-8 -*-

import file_management
import display
import recovery_user_input


def launch_game():
    """Lancement du jeu """

    game_data = file_management.ManagementData()
    player_input = recovery_user_input.RequestToThePlayer()
    game_display = display.DisplayGame(scoreboard=game_data.recovery())

    game_display.home()
    
    answer = None
    while answer is None:
        answer = player_input.stop_or_again()
    if answer:

        players_scores = game_data.recovery()
        player_name = None
        while player_name is None:
            player_name = player_input.get_name()

        if game_display.welcome_player(name_player=player_name, actual_score=players_scores) is None:
            players_scores[player_name] = 0

        secret_word = game_data.get_secret_word()
        hidden_word = '*' * len(secret_word)
        game_score = int(len(secret_word))

        print(" Voici le mots mytere: {} vous avez {} chances pour le trouvé. Facile ! "
              .format(hidden_word, len(secret_word)))

        while secret_word != hidden_word and game_score > 0:

            answer = None
            while answer is None:
                answer = player_input.get_character()

            if answer in secret_word and answer not in hidden_word:

                print("\nBravo !\n")
                hidden_word = game_display.display_hidden_word(secret_word=secret_word, hid_word=hidden_word.split(),
                                                               character=answer)
            elif answer in hidden_word:

                print("\nVous aves deja tapez {} vous perdez 1 pts\n".format(answer))
                game_score -= 1

            else:

                print("\n{} n'est pas dans le mots vous perdez 1 pts\n".format(answer))
                game_score -= 1

            print("Mot mystère: {} \n Chance restantes: {}".format(hidden_word, str(game_score)))

        for c in hidden_word:
            if c == "*":
                game_score -= 1

        print(game_display.eng_game(secret_word=secret_word, hidd_word=hidden_word).format(game_score))

        players_scores[player_name] += game_score

        game_data.saving(players_scores)

        return None

    else:

        print("A bientot")
        return False


while launch_game() is None: pass
