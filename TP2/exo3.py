class CompteBancaire:
   def __init__(self,titulaire,solde):
      self.titulaire=titulaire;
      self.solde=solde;
    
   def deposer(self,montant):
        self.solde=self.solde+montant;
        print("Votre solde après la disposition ")

   def retirez(self,montant):
      if self.solde<montant :
        return "votre solde est insuffisant"
      else:
         self.solde=self.solde-montant;
         print("Votre solde après que vous avez retirer ")

   def afficher_solde(self):
      print(f"votre solde est : {self.solde}");


c1 =CompteBancaire("jihad",10000);
c1.afficher_solde();
c1.deposer(1000);
c1.afficher_solde();
c1.retirez(2500);
c1.afficher_solde();

