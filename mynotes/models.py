from datetime import datetime


class Note:
    """Représente une note prise par l'utilisateur."""

    def __init__(self, title, content=None, notebook=None, tags=[]):
        self.updated_datetime = None
        self.title = title
        self.content = content
        self.created_datetime = datetime.now()
        self.notebook = notebook
        self.tags = []
        self.add_tags(*tags)

    @property
    def title(self):
        """Titre de la note."""
        return self._title

    @title.setter
    def title(self, new_title):
        self._title = new_title
        self.updated_datetime = datetime.now()

    def add_tags(self, *tags):
        """Ajouter un ou plusieurs tags à la note."""
        for tag in tags:
            tag = Tag(tag)
            tag.add_note(self)
            self.tags.append(tag)

    def move(self, new_notebook):
        """Déplacer la note dans un autre notebook."""
        self.notebook = new_notebook

    def __repr__(self):
        return f"Note(title={self.title})"


class Notebook:
    def __init__(self):
        self.title = None
        self.notes = []
        self.created_datetime = None
        self.updated_datetime = None

    def create_note(self):
        pass

    def search(self, text):
        pass

    def search_content(self, text):
        pass

    def __repr__(self):
        return f"Notebook(title={self.title})"


class Tag:
    def __init__(self, name):
        self.name = name
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)

    def __repr__(self):
        return f"Tag(name={self.name})"
