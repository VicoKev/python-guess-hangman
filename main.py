from games.plus_ou_moins import PlusOuMoinsGame
from games.pendu import PenduGame
from games.utils import print_header, get_valid_input, clear_screen
import sys

def main_menu():
    """Affiche le menu principal et gère la navigation."""
    while True:
        print_header("MENU PRINCIPAL - JEUX PYTHON")
        print("1. Jouer au Plus ou Moins")
        print("2. Jouer au Pendu")
        print("3. Quitter")
        
        choice = get_valid_input(
            "\nVotre choix (1-3): ",
            int,
            lambda x: 1 <= x <= 3,
            "Veuillez choisir une option valide (1, 2 ou 3)."
        )

        if choice == 1:
            clear_screen()
            game = PlusOuMoinsGame()
            game.play()
        elif choice == 2:
            clear_screen()
            game = PenduGame()
            game.play()
        elif choice == 3:
            print("\nMerci d'avoir joué ! À bientôt.")
            sys.exit()
        
        input("\nAppuyez sur Entrée pour revenir au menu principal...")

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n\nArrêt du programme. Au revoir !")
        sys.exit()
