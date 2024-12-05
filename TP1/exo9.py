#exo9
def analyse_text(text):
   M=text.split(" ")
   nbM=len(M)
   nbC=len(text)
   return{
      'nbr_mots' : nbM,
      'nbr_caractere' : nbC
   }
print(analyse_text("Bonjour tout le monde"))