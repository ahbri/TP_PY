
 #exo4
def compte_occurrences(list):
    dict={}
    for m in list:
         if m in dict:
             dict[m]+=1
         else:
             dict[m]=1
    return dict
print(compte_occurrences(["banane","pomme","orange","banane"]))