#question 1

class Student:
    def __init__(self,_name,_major):
        self.name = _name
        self.major = _major
        
    def get_name(self):
        return self.name
    def get_major(self):
        return self.major
    def set_major(self,new_major):
        self.major = new_major
    def __str__(self):
        return f"I'm {self.get_name()}, I'm a {self.get_major()} major."
    

#question 12

class TVShow:
    def __init__(self,_title = 'Unknown',_genre = 'Unknown'):
        self.title = _title
        self.genre = _genre

    def get_genre(self):
        return self.genre
    def set_genre(self,new_genre):
        self.genre = new_genre
    def get_title(self):
        return self.title
    def set_title(self,new_title):
        self.title = new_title
    
    def __str__(self):
        return f'Title: {self.get_title()} Genre: {self.get_genre()}'
    
class NetflixDashboard:
    def __init__(self,_profile_name = "Unknown"):
        self.profile_name = _profile_name
        self.shows : TVShow = []

    def get_name(self):
        return self.profile_name
    
    def add_show(self,show : TVShow):
        self.shows.append(show)
    
    def display_recommendations(self):
        for show in self.shows:
            print(show)

    def __str__(self):
        return f"Profile Name: {self.get_name()}"
    

account1 = NetflixDashboard("Nils")
account1.add_show(TVShow('Maters Tall Tales','adventure'))
account1.add_show(TVShow('Stranger Things','idk'))
account1.display_recommendations()