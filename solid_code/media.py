"""Module with mass-media classes."""


class NewsCompany:
    """Class of media company with newspaper and TV production."""
    def __init__(self, name):
        self.name = name
        self.types = {'newspaper': 'The Daily Bugle', 'tv': 'See It Now'}

    def create_news(self, media_type, hero, place):
        """Creating news of selected type based on hero and location."""
        hero_name = getattr(hero, 'name', 'Hero')
        place_name = getattr(place, 'name', getattr(place, 'coordinates', 'place'))
        print(f'{self.name} {self.types[media_type]}: {hero_name} saved the {place_name}!')
