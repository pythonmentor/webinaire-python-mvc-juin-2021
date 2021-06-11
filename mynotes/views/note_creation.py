def render():
    print(
        "Menu de création d'un notebook\n"
        "==============================\n"
        "1. retour à l'accueil\n"
        "2. quitter le programme\n"
    )


def get_user_choice():
    return input("Que voulez-vous faire ? ").lower()


def notify_invalid_choice():
    print("Choix non valable !\n\n")
