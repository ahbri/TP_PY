class Rectangle:
    def __init__(self,largeur,longeur):
        self.largeur=largeur;
        self.longeur=longeur;
    
    def calculer_surface(self):
        return self.largeur*self.longeur
    def calculer_perimetre(self):
        return 2*(self.largeur+self.longeur)

rec=Rectangle(4,6)
print(rec.calculer_surface())
print(rec.calculer_perimetre())