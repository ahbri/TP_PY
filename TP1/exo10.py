#exo10
def fusionner_dicts(dict1, dict2):
    dict=dict1.copy()
    for cle, value in dict2.items():
        if cle in dict:
            dict[cle]+=value
        else:
            dict[cle]=value
    return dict
dict1={'banane': 1,'pomme' :3,'fraise': 2}
dict2={'banane': 1,'orange' :3,'poire': 2,'fraise':5,'abricot':4}
print(fusionner_dicts(dict1,dict2))