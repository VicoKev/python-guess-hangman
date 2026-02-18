import random
from .utils import print_header, get_valid_input

class PlusOuMoinsGame:
    def __init__(self):
        self.min_val = 1
        self.max_val = 100
        self.max_attempts = 10
        self.target_number = 0

    def select_difficulty(self):
        print_header("PLUS OU MOINS - Difficulté")
        print("1. Facile (1-50, 4 essais)")
        print("2. Normal (1-100, 6 essais)")
        print("3. Difficile (1-500, 8 essais)")
        print("4. Expert (1-1000, 10 essais)")
        
        choice = get_valid_input(
            "\nChoisissez une difficulté (1-4): ",
            int,
            lambda x: 1 <= x <= 4,
            "Veuillez entrer un nombre entre 1 et 4."
        )

        if choice == 1:
            self.max_val = 50
            self.max_attempts = 4
        elif choice == 2:
            self.max_val = 100
            self.max_attempts = 6
        elif choice == 3:
            self.max_val = 500
            self.max_attempts = 8
        elif choice == 4:
            self.max_val = 1000
            self.max_attempts = 10

        self.target_number = random.randint(self.min_val, self.max_val)

    def play(self):
        self.select_difficulty()
        print_header(f"PLUS OU MOINS (1-{self.max_val})")
        print(f"Devinez le nombre mystère entre {self.min_val} et {self.max_val}.")
        print(f"Vous avez {self.max_attempts} essais.\n")

        attempts = 0
        while attempts < self.max_attempts:
            guess = get_valid_input(
                f"Essai {attempts + 1}/{self.max_attempts} - Votre proposition: ",
                int,
                lambda x: True, 
                "Veuillez entrer un nombre entier."
            )
            
            attempts += 1

            if guess < self.target_number:
                print(">>> C'est PLUS (+) !\n")
            elif guess > self.target_number:
                print(">>> C'est MOINS (-) !\n")
            else:
                print(f"\n🎉 BRAVO ! Vous avez trouvé le nombre {self.target_number} en {attempts} essais !")
                self._ask_replay()
                return

        print(f"\n💀 PERDU ! Le nombre mystère était {self.target_number}.")
        self._ask_replay()

    def _ask_replay(self):
        replay = get_valid_input(
            "\nVoulez-vous rejouer ? (o/n): ",
            str,
            lambda x: x.lower() in ['o', 'n'],
            "Répondez par 'o' ou 'n'."
        )
        if replay.lower() == 'o':
            self.target_number = 0
            self.play()
