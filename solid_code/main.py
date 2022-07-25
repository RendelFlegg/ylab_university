import random

from heroes import BlackWidow, Shaun, Superman, SuperHero
from media import NewsCompany
from places import Hala, Kostroma, Tokyo, Place


def save_the_place(hero: SuperHero, news: NewsCompany, place: Place):
    """Function initiating all superheroic mess."""
    hero.find(place)
    hero.attack()
    if hero.can_use_ultimate_attack:
        hero.ultimate()
    news.create_news(random.choice(tuple(news.types.keys())), hero, place)


if __name__ == '__main__':
    save_the_place(Superman(), NewsCompany('CBS'), Kostroma())
    print('-' * 20)
    save_the_place(BlackWidow(), NewsCompany('CBS'), Hala())
    print('-' * 20)
    save_the_place(Shaun(), NewsCompany('CBS'), Kostroma())
    print('-' * 20)
    save_the_place(SuperHero('Chuck Norris', False), NewsCompany('CBS'), Tokyo())
