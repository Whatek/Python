import random
class Liczby():
    @classmethod
    def gener(self):
        x = random.sample(range(1,50,1),6)
        print(x)

Liczby().gener()



