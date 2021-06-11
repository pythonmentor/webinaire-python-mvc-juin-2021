from .controllers import ApplicationController


def main():
    """Point d'entrée principal de l'application."""
    app = ApplicationController()
    app.start()


if __name__ == "__main__":
    main()
