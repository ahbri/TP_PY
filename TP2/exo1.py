class Chien :
    def __init__(self,nom,race,age):
        self.nom=nom;
        self.race=race;
        self.age=age;
    def aboyer(self):
        print("Woof")

ch1=Chien("abc","chienpolice",4)
ch1.aboyer()