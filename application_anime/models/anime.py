import os

class Episode:

    def __init__(self, title, filepath):
        self.title = title
        self.filepath = filepath


class Anime:

    def __init__(self, name, author, genre, episodes):
        self.name = name

        self.author = author
        self.genre = genre
        self.episodes = episodes
        self.episodes_count = len(episodes)

    def __repr__(self):
        return f"{self.name} by {self.author}"

    def play_pilot(self):
        os.system(f"totem {self.episodes[0].filepath}")