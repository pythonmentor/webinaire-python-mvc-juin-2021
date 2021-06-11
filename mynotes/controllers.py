from .views import home, note_creation, notebook_creation, end


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

    def run(self):

        home.render()
        next_action = home.get_user_choice()
        if next_action == "1":
            return NoteCreationController()
        elif next_action == "2":
            return NotebookCreationController()
        elif next_action == "3":
            return EndController()
        else:
            home.notify_invalid_choice()
            return HomeController()


class NoteCreationController:
    """Contrôleur responsable de gérer le menu de création d'une nouvelle
    note.
    """

    def run(self):
        note_creation.render()
        next_action = note_creation.get_user_choice()
        if next_action == "1":
            return HomeController()
        elif next_action == "2":
            return EndController()
        else:
            note_creation.notify_invalid_choice()
            return NoteCreationController()


class NotebookCreationController:
    """Contrôleur responsable de gérer le menu de création d'un nouveau
    notebook.
    """

    def run(self):
        notebook_creation.render()
        next_action = notebook_creation.get_user_choice()
        if next_action == "2":
            return HomeController()
        elif next_action == "1":
            return NoteCreationController()
        elif next_action == "3":
            return EndController()
        else:
            notebook_creation.notify_invalid_choice()
            return NotebookCreationController()


class EndController:
    """Contrôleur responsable de gérer la fin du programme."""

    def run(self):
        end.render()
        choice = end.get_user_choice()
        if choice == "oui":
            return
        elif choice == "non":
            return HomeController()
        else:
            end.notify_invalid_choice()
            return EndController()
