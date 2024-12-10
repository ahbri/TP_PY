class Personne:
    def __init__(self,nom,prenom,age):
        self.nom=nom;
        self.prenom=prenom;
        self.age=age;
        self.amis = [] 

    def ajouter_ami(self, ami):
         if ami not in self.amis and ami != self:
            self.amis.append(ami)
            print(f"{ami.prenom} {ami.nom} a été ajouté à la liste des amis de {self.prenom} {self.nom}.")
         elif ami == self:
            print("Une personne ne peut pas être amie avec elle-même.")
         else:
            print(f"{ami.prenom} {ami.nom} est déjà un ami de {self.prenom} {self.nom}.")
    
    def afficher_amis(self):
        
         if not self.amis:
            print(f"{self.prenom} {self.nom} n'a pas encore d'amis.")
         else:
            print(f"Les amis de {self.prenom} {self.nom} :")
            for ami in self.amis:
                print(f"- {ami.prenom} {ami.nom}, {ami.age} ans")

personne1 = Personne("AHBRI", "JIHAD", 30)
personne2 = Personne("ALLAMI", "MOHAMED", 25)
personne3 = Personne("CHARKI", "SALMA", 28)


personne1.ajouter_ami(personne2)
personne1.ajouter_ami(personne3)
personne1.ajouter_ami(personne2)  
personne1.ajouter_ami(personne1)  


personne1.afficher_amis()