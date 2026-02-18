import random
import os
from .utils import print_header, get_valid_input, clear_screen

class PenduGame:
    HANGMAN_PICS = [
        r"""
          +---+
          |   |
              |
              |
              |
              |
        =========
        """,
        r"""
          +---+
          |   |
          O   |
              |
              |
              |
        =========
        """,
        r"""
          +---+
          |   |
          O   |
          |   |
              |
              |
        =========
        """,
        r"""
          +---+
          |   |
          O   |
         /|   |
              |
              |
        =========
        """,
        r"""
          +---+
          |   |
          O   |
         /|\  |
              |
              |
        =========
        """,
        r"""
          +---+
          |   |
          O   |
         /|\  |
         /    |
              |
        =========
        """,
        r"""
          +---+
          |   |
          O   |
         /|\  |
         / \  |
              |
        =========
        """
    ]

    def __init__(self):
        self.word_list = self.load_words()
        self.secret_word = ""
        self.guesses = set()
        self.attempts = 0
        self.max_attempts = len(self.HANGMAN_PICS) - 1

    def load_words(self):
        try:
            file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'mots_pendu.txt')
            with open(file_path, 'r', encoding='utf-8') as f:
                return [word.strip().upper() for word in f.readlines() if len(word.strip()) > 0]
        except FileNotFoundError:
            print("Erreur: Le fichier de mots est introuvable.")
            return ["PYTHON", "PROGRAMMATION", "ORDINATEUR"]

    def display_game_state(self):
        print_header("JEU DU PENDU")
        print(self.HANGMAN_PICS[self.attempts])
        print("\nMot à deviner : ", end=" ")
        
        display_word = ""
        for letter in self.secret_word:
            if letter in self.guesses:
                display_word += letter + " "
            else:
                display_word += "_ "
        print(display_word)
        print("\nLettres essayées : " + ", ".join(sorted(list(self.guesses))))
        print(f"Essais restants : {self.max_attempts - self.attempts}")

    def play(self):
        if not self.word_list:
            print("Aucun mot chargé. Impossible de jouer.")
            return

        self.secret_word = random.choice(self.word_list)
        self.guesses = set()
        self.attempts = 0
        
        while self.attempts < self.max_attempts:
            self.display_game_state()
            
            guess = get_valid_input(
                "\nDevinez une lettre : ",
                lambda x: x.upper(),
                lambda x: len(x) == 1 and x.isalpha(),
                "Veuillez entrer une SEULE lettre."
            )

            if guess in self.guesses:
                print(f"⚠️ Vous avez déjà essayé la lettre '{guess}'.")
                input("Appuyez sur Entrée pour continuer...")
                continue
            
            self.guesses.add(guess)

            if guess in self.secret_word:
                if all(letter in self.guesses for letter in self.secret_word):
                    self.display_game_state()
                    print(f"\n🎉 FELICITATIONS ! Vous avez trouvé le mot : {self.secret_word}")
                    self._ask_replay()
                    return
            else:
                self.attempts += 1
                if self.attempts == self.max_attempts:
                    self.display_game_state()
                    print(f"\n💀 PERDU ! Le mot était : {self.secret_word}")
                    self._ask_replay()
                    return

    def _ask_replay(self):
        replay = get_valid_input(
            "\nVoulez-vous rejouer ? (o/n): ",
            str,
            lambda x: x.lower() in ['o', 'n'],
            "Répondez par 'o' ou 'n'."
        )
        if replay.lower() == 'o':
            self.play()
