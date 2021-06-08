class Application:
    """Représente l'application elle-même et permet de la démarrer."""

    def start(self):
        print("Hello, nous somme là")


def main():
    """Point d'entrée principal de l'application."""
    app = Application()
    app.start()


if __name__ == "__main__":
    main()
