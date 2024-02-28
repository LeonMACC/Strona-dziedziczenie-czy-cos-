class Produkt:
    def __init__(self, nazwa, cena, opis, rodzaj):
        self.nazwa = nazwa
        self.cena = cena
        self.opis = opis
        self.rodzaj = rodzaj


class Merchandising(Produkt):
    def __init__(self, nazwa, cena, opis, tytul_anime):
        Produkt.__init__(self, nazwa, cena, opis, "Merchandising")
        self.tytul_anime = tytul_anime


class Manga(Produkt):
    def __init__(self, nazwa, cena, opis, autor):
        Produkt.__init__(self, nazwa, cena, opis, "Manga")
        self.autor = autor

   

class FigurkaAnime(Produkt):
    def __init__(self, nazwa, cena, opis, postac):
        Produkt.__init__(self, nazwa, cena, opis, "Figurka Anime")
        self.postac = postac


class GraAnime(Produkt):
    def __init__(self, nazwa, cena, opis, platforma):
        Produkt.__init__(self, nazwa, cena, opis, "Gra Anime")
        self.platforma = platforma


class BluRay(Produkt):
    def __init__(self, nazwa, cena, opis, wydawca):
        Produkt.__init__(self, nazwa, cena, opis, "Blu-ray")
        self.wydawca = wydawca

class Soundtrack(Produkt):
    def __init__(self, nazwa, cena, opis, artysta):
        Produkt.__init__(self, nazwa, cena, opis, "Soundtrack")
        self.artysta = artysta


class Koszulka(Produkt):
    def __init__(self, nazwa, cena, opis, rozmiar):
        Produkt.__init__(self, nazwa, cena, opis, "Koszulka")
        self.rozmiar = rozmiar     
