def render():
    print(
        "Menu d'accueil\n"
        "==============\n"
        "1. créer une nouvelle note\n"
        "2. créer un nouveau notebook\n"
        "3. quitter le programme\n"
    )


def get_user_choice():
    return input("Que voulez-vous faire ? ").lower()


def notify_invalid_choice():
    print("Choix non valable !\n\n")
