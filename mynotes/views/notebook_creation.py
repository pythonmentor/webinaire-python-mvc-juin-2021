def render():
    print(
        "Menu de création d'une note\n"
        "==============================\n"
        "1. créer une nouvelle note\n"
        "2. retour à l'accueil\n"
        "3. quitter le programme\n"
    )


def get_user_choice():
    return input("Que voulez-vous faire ? ").lower()


def notify_invalid_choice():
    print("Choix non valable !\n\n")
