from datetime import datetime
class Game:
    def __init__(self,name,plateform,genre,status="In progress",rating=None,comment=None,played_time=0,image_path=None):
        self.name=name
        self.platform=plateform
        self.genre=genre
        self.status = status
        self.rating = rating
        self.comment=comment
        self.played_time=played_time
        self.added_date = datetime.now().strftime("%Y-%m-%d")
        self.image_path=image_path
        
        def to_dict(self):
            return self.__dict__