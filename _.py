class HomeView:
    """Vue responsable d'afficher le menu d'accueil."""

    @staticmethod
    def render():
        print(
            "Menu d'accueil\n"
            "==============\n"
            "1. créer une nouvelle note\n"
            "2. créer un nouveau notebook\n"
            "3. quitter le programme\n"
        )

    def get_user_choice(self):
        return input("Que voulez-vous faire ? ").lower()

    def notify_invalid_choice(self):
        print("Choix non valable !\n\n")


class NoteCreationView:
    """Vue responsable de l'affichage du menu de création de note."""

    def render(self):
        print(
            "Menu de création d'un notebook\n"
            "==============================\n"
            "1. retour à l'accueil\n"
            "2. quitter le programme\n"
        )

    def get_user_choice(self):
        return input("Que voulez-vous faire ? ").lower()

    def notify_invalid_choice(self):
        print("Choix non valable !\n\n")


class NotebookCreationView:
    """Vue responsable de l'affichage du menu de creation de notebook."""

    def render(self):
        print(
            "Menu de création d'une note\n"
            "==============================\n"
            "1. créer une nouvelle note\n"
            "2. retour à l'accueil\n"
            "3. quitter le programme\n"
        )

    def get_user_choice(self):
        return input("Que voulez-vous faire ? ").lower()

    def notify_invalid_choice(self):
        print("Choix non valable !\n\n")


class EndView:
    """Vue responsable de l'affichage de menu de fin d'application."""

    def render(self):
        print("Voulez-vous vraiment quitter l'application ?")

    def get_user_choice(self):
        return input("oui ou non ? ")

    def notify_invalid_choice(self):
        print("Choix non valable !\n\n")
