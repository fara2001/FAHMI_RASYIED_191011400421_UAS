# create fuzzy with 3 variables and 10 rules with following variables and rules:
from fuzzy_3 import (
    turun,
    Permintaan,
    Persediaan,
    Produksi,
    naik
)
Permintaan = Permintaan()
Persediaan = Persediaan()
Produksi = Produksi()

# define the rules
class Permintaan():
    minimum = 2100
    maximum = 3500

    def turun(self, x):
        if x >= self.maximum:
            return 0
        elif x<= self.minimum:
            return 1
        else:
            return down(x, self.minimum, self.maximum)

    def naik(self, x):
        if x >= self.maximum:
            return 1
        elif x<= self.minimum:
            return 0
        else:
            return up(x, self.minimum, self.maximum)

    def tetap(self, x):
        if x >= self.maximum or x<= self.minimum:
            return 0
        elif self.minimum < x < self.maximum:
            return 1
        else:
            return 0
    
# define the rules
class Persediaan():
    minimum = 100
    maximum = 250

    def sedikit(self, x):
        if x >= self.maximum:
            return 0
        elif x<= self.minimum:
            return 1
        else:
            return down(x, self.minimum, self.maximum)

    def banyak(self, x):
        if x >= self.maximum:
            return 1
        elif x<= self.minimum:
            return 0
        else:
            return up(x, self.minimum, self.maximum)
    
    def tetap(self, x):
        if x >= self.maximum or x<= self.minimum:
            return 0
        elif self.minimum < x < self.maximum:
            return 1
        else:
            return 0
    
# define the rules
class Produksi():
    minimum = 1000
    maximum = 5000
    permintaan = 0
    persediaan = 0

    def _berkurang(self, a):
        return self.maximum - a*(self.maximum - self.minimum)

    def _bertambah(self, a):
        return a*(self.maximum - self.minimum) + self.minimum
    
    def tetap(self, x):
        if x >= self.maximum or x<= self.minimum:
            return 0
        elif self.minimum < x < self.maximum:
            return 1
        else:
            return 0