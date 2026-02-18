# 🎮 Jeux Console en Python — Plus ou Moins & Pendu

Deux jeux classiques de console implémentés en **Python**, avec une architecture modulaire et professionnelle.

## 📁 Structure du Projet

```
.
├── main.py                 # Point d'entrée de l'application
├── games/
│   ├── __init__.py
│   ├── utils.py            # Fonctions utilitaires partagées
│   ├── plus_ou_moins.py    # Logique du jeu "Plus ou Moins"
│   └── pendu.py            # Logique du jeu "Le Pendu"
└── data/
    └── mots_pendu.txt      # Liste de mots pour le Pendu
```

## ⚙️ Prérequis

- **Python 3.x** installé sur votre machine.
- Aucune dépendance externe requise (bibliothèque standard uniquement).

## 🚀 Lancement

```bash
python3 main.py
```

Un menu interactif s'affiche pour choisir le jeu.

## 🎲 Jeux Disponibles

### 1. Plus ou Moins

Devinez un nombre mystère généré aléatoirement.

| Difficulté | Plage    | Essais |
|------------|----------|--------|
| Facile     | 1 – 50   | 4      |
| Normal     | 1 – 100  | 6      |
| Difficile  | 1 – 500  | 8      |
| Expert     | 1 – 1000 | 10     |

- Feedback à chaque essai : **Plus (+)** ou **Moins (-)**.
- Option de rejouer après chaque partie.

### 2. Le Pendu

Devinez un mot caché lettre par lettre avant d'être "pendu".

- 📄 Mots chargés depuis `data/mots_pendu.txt`.
- 🎨 Dessin ASCII progressif à chaque erreur (6 erreurs max).
- ⚠️ Détection des lettres déjà proposées.
- Option de rejouer après chaque partie.

## 🏗️ Architecture

Le projet suit une **architecture modulaire** :

- **`utils.py`** : fonctions partagées (`clear_screen`, `print_header`, `get_valid_input`) pour éviter la duplication de code.
- **Chaque jeu** est encapsulé dans sa propre classe (`PlusOuMoinsGame`, `PenduGame`), ce qui facilite l'ajout de nouveaux jeux.
- **Séparation données / logique** : la liste de mots est externalisée dans un fichier texte.

## 🔄 Version R

Une version équivalente de ce projet existe en R : [jeux-console-r](https://github.com/VicoKev/jeux-console-r)
