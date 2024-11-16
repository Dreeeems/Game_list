class Game:
    def __init__(self, name, platform, genre, status, rating, comments, time_played, image_path=None):
        self.name = name
        self.platform = platform
        self.genre = genre
        self.status = status
        self.rating = rating
        self.comments = comments
        self.time_played = time_played
        self.image_path = image_path

    def to_dict(self):
        return {
            "name": self.name,
            "platform": self.platform,
            "genre": self.genre,
            "status": self.status,
            "rating": self.rating,
            "comments": self.comments,
            "time_played": self.time_played,
            "image_path": self.image_path
        }
