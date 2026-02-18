import os
import time

def clear_screen():
    """Efface l'écran de la console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title):
    """Affiche un en-tête stylisé."""
    clear_screen()
    print("=" * 50)
    print(f"{title.center(50)}")
    print("=" * 50)
    print()

def get_valid_input(prompt, type_func=str, condition=lambda x: True, error_msg="Entrée invalide."):
    """
    Demande une entrée utilisateur et la valide.

    Args:
        prompt (str): Le message à afficher à l'utilisateur.
        type_func (callable): La fonction pour convertir l'entrée (ex: int, str).
        condition (callable): Une fonction qui retourne True si l'entrée est valide.
        error_msg (str): Le message d'erreur à afficher.

    Returns:
        La valeur convertie et validée.
    """
    while True:
        try:
            user_input = input(prompt)
            value = type_func(user_input)
            if condition(value):
                return value
            else:
                print(f"❌ {error_msg}")
        except ValueError:
            print(f"❌ {error_msg}")
