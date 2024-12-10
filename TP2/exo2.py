class Voiture:
 
    def __init__(self,marque,model,anne):
        self.marque=marque;
        self.model=model;
        self.anne=anne;
    def affiche_info(self):
        return '{} {} {}'.format(self.marque,self.model,self.anne)

v1=Voiture("Toyota","Verso",2016)
v2=Voiture("Jeep","Avenger",2019)
v3=Voiture("Volswagen","ID.3",2020)

print(v1.affiche_info())
print(v2.affiche_info())
print(v2.affiche_info())