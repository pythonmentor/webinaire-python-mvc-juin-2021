from . import views


class ApplicationController:
    """Représente l'application elle-même et permet de la démarrer."""

    def __init__(self):
        """Initialise la classe principale de l'application."""
        self.current_controller = HomeController()

    def start(self):
        """Démarre l'application."""
        while self.current_controller is not None:
            next_controller = self.current_controller.run()
            self.current_controller = next_controller


class HomeController:
    """Contrôleur responsable de gérer le menu d'accueil."""

    def __init__(self):
        self.view = views.HomeView()

    def run(self):
        self.view.render()
        next_action = self.view.get_user_choice()
        if next_action == "1":
            return NoteCreationController()
        elif next_action == "2":
            return NotebookCreationController()
        elif next_action == "3":
            return EndController()
        else:
            self.view.notify_invalid_choice()
            return HomeController()


class NoteCreationController:
    """Contrôleur responsable de gérer le menu de création d'une nouvelle
    note.
    """

    def __init__(self):
        self.view = views.NoteCreationView()

    def run(self):
        self.view.render()
        next_action = self.view.get_user_choice()
        if next_action == "1":
            return HomeController()
        elif next_action == "2":
            return EndController()
        else:
            self.view.notify_invalid_choice()
            return NoteCreationController()


class NotebookCreationController:
    """Contrôleur responsable de gérer le menu de création d'un nouveau
    notebook.
    """

    def __init__(self):
        self.view = views.NotebookCreationView()

    def run(self):
        self.view.render()
        next_action = self.view.get_user_choice()
        if next_action == "2":
            return HomeController()
        elif next_action == "1":
            return NoteCreationController()
        elif next_action == "3":
            return EndController()
        else:
            self.view.notify_invalid_choice()
            return NotebookCreationController()


class EndController:
    """Contrôleur responsable de gérer la fin du programme."""

    def __init__(self):
        self.view = views.EndView()

    def run(self):
        self.view.render()
        choice = self.view.get_user_choice()
        if choice == "oui":
            return
        elif choice == "non":
            return HomeController()
        else:
            self.view.notify_invalid_choice()
            return EndController()
