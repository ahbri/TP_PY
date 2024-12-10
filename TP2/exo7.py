class Livre:
    def __init__(self,titre,auteur,anne_pub):
        self.titre=titre;
        self.auteur=auteur;
        self.anne_pub=anne_pub;


class Biblio:
    def __init__(self):
        self.livres =[]
    def ajouter_livre(self,titre,auteur,anne_pub):
        nouveau_livre = Livre(titre, auteur, anne_pub)
        self.livres.append(nouveau_livre)
        print(f"Le livre '{titre}' a été ajouté à la bibliothèque.")
    def afficher_livres(self):
         if not self.livres:
            print("La bibliothèque ne contient aucun livre.")
         else:
            print("Livres disponibles dans la bibliothèque :")
            for livre in self.livres:
                print(f"- {livre.titre} ({livre.anne_pub}), écrit par {livre.auteur}")
    
bib=Biblio()
bib.ajouter_livre("Le Meilleur des mondes" ,"Aldous Huxley",1932)
bib.ajouter_livre("Neuromancien","William Gibson",19484)
bib.afficher_livres()

