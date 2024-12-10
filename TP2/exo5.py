class Animal:
    def __init__(self):
        pass
    def faire_du_bruit(self):
        pass

class Chat(Animal):
    def __init__(self):
        pass
    def faire_du_bruit(self):
        return "Meow"
    
class Chien(Animal):    
      def __init__(self):
        pass
      def faire_du_bruit(self):
        return "Woof"
      
cat=Chat()
print(cat.faire_du_bruit())
dog=Chien()
print(dog.faire_du_bruit())