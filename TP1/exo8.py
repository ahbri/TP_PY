#exo8
def somme_varargs(*args):
    return(sum(args))
print(somme_varargs(3,5,1,3))
print(somme_varargs(1,3))
print(somme_varargs(14,5,0,1,3,3))