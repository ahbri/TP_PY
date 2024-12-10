class Personne:
    def __init__(self,nom,prenom,age):
        self.nom=nom;
        self.prenom=prenom;
        self.age=age;
    
    def se_presenter(self):
        print(f"My name is {self.nom} {self.prenom} and I have {self.age} years old.");
# p=Personne("ahbri","jihad",24)
# p.se_presenter()        

class Etudiant(Personne):
    def __init__(self,nom,prenom,age,matricule):
        super().__init__(nom,prenom,age)
        self.matricule=matricule;
    def etudier(self):
        print("Studying")
e1=Etudiant("AHBRI","Jihad",24,12345)
e1.se_presenter()
e1.etudier()