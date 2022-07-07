def turun(x, xmin, xmax):
    return (xmax - x) / (xmax - xmin)

def naik(x, xmin, xmax):
    return (x - xmin) / (xmax - xmin)


class PermintaanBaru():
    def _berkurang(self, a):
        return self.maximum - a*(self.maximum - self.minimum)
    
    def _bertambah(self, a):
        return a*(self.maximum - self.minimum) + self.minimum

    def turun(self, x):
        if x >= self.median:
            return 0
        elif x<= self.minimum:
            return 1
        else:
            return turun(x, self.minimum, self.median)
    
    def naik(self, x):
        if x >= self.maximum:
            return 1
        elif x<= self.median:
            return 0
        else:
            return naik(x, self.median, self.maximum)
    
    def tetap(self, x):
        if x >= self.maximum or x<= self.minimum:
            return 0
        elif self.minimum < x < self.median:
            return naik(x, self.minimum, self.median)
        elif self.median < x < self.maximum:
            return turun(x, self.median, self.maximum)
        else:
            return 1

# class permintaan lama
class PermintaanLama():
    def _berkurang(self, a):
        return self.maximum - a*(self.maximum - self.minimum)
    
    def _bertambah(self, a):
        return a*(self.maximum - self.minimum) + self.minimum

    def turun(self, x):
        if x >= self.maximum:
            return 0
        elif x<= self.minimum:
            return 1
        else:
            return turun(x, self.minimum, self.maximum)
    
    def naik(self, x):
        if x >= self.maximum:
            return 1
        elif x<= self.minimum:
            return 0
        else:
            return naik(x, self.minimum, self.maximum)
    
    def tetap(self, x):
        if x >= self.maximum or x<= self.minimum:
            return 0
        elif self.minimum < x < self.maximum:
            return 1
        else:
            return 0

# create fuzzy with 3 variables and 10 rules in class Persediaan() and define the rules
class PersediaanBaru():
    def _berkurang(self, a):
        return self.maximum - a*(self.maximum - self.minimum)
    
    def _bertambah(self, a):
        return a*(self.maximum - self.minimum) + self.minimum

    def sedikit(self, x):
        if x >= self.median:
            return 0
        elif x<= self.minimum:
            return 1
        else:
            return turun(x, self.minimum, self.median)
    
    def banyak(self, x):
        if x >= self.maximum:
            return 1
        elif x<= self.median:
            return 0
        else:
            return naik(x, self.median, self.maximum)
    
    def tetap(self, x):
        if x >= self.maximum or x<= self.minimum:
            return 0
        elif self.minimum < x < self.median:
            return naik(x, self.minimum, self.median)
        elif self.median < x < self.maximum:
            return turun(x, self.median, self.maximum)
        else:
            return 1

# class persediaan lama
class PersediaanLama():
    def _berkurang(self, a):
        return self.maximum - a*(self.maximum - self.minimum)
    
    def _bertambah(self, a):
        return a*(self.maximum - self.minimum) + self.minimum

    def sedikit(self, x):
        if x >= self.maximum:
            return 0
        elif x<= self.minimum:
            return 1
        else:
            return turun(x, self.minimum, self.maximum)
    
    def banyak(self, x):
        if x >= self.maximum:
            return 1
        elif x<= self.minimum:
            return 0
        else:
            return naik(x, self.minimum, self.maximum)
    
    def tetap(self, x):
        if x >= self.maximum or x<= self.minimum:
            return 0
        elif self.minimum < x < self.maximum:
            return naik(x, self.minimum, self.maximum)
        else:
            return 1


class ProduksiBaru():
    def _berkurang(self, a):
        return self.maximum - a*(self.maximum - self.minimum)
    
    def _bertambah(self, a):
        return a*(self.maximum - self.minimum) + self.minimum

    def interensi(self, x):
        return self.tetap(x) * self.turun(x) * self.naik(x)

    def turun(self, x):
        if x >= self.median:
            return 0
        elif x<= self.minimum:
            return 1
        else:
            return turun(x, self.minimum, self.median)
    
    def naik(self, x):
        if x >= self.maximum:
            return 1
        elif x<= self.median:
            return 0
        else:
            return naik(x, self.median, self.maximum)
    
    def tetap(self, x):
        if x >= self.maximum or x<= self.minimum:
            return 0
        elif self.minimum < x < self.median:
            return naik(x, self.minimum, self.median)
        elif self.median < x < self.maximum:
            return turun(x, self.median, self.maximum)
        else:
            return 1

# new class produk lama
class ProduksiLama():
    def _berkurang(self, a):
        return self.maximum - a*(self.maximum - self.minimum)
    
    def _bertambah(self, a):
        return a*(self.maximum - self.minimum) + self.minimum

    def interensi(self, x):
        return self.tetap(x) * self.turun(x) * self.naik(x)

    def turun(self, x):
        if x >= self.median:
            return 0
        elif x<= self.minimum:
            return 1
        else:
            return turun(x, self.minimum, self.median)
    
    def naik(self, x):
        if x >= self.maximum:
            return 1
        elif x<= self.median:
            return 0
        else:
            return naik(x, self.median, self.maximum)
    
    def tetap(self, x):
        if x >= self.maximum or x<= self.minimum:
            return 0
        elif self.minimum < x < self.median:
            return naik(x, self.minimum, self.median)
        elif self.median < x < self.maximum:
            return turun(x, self.median, self.maximum)
        else:
            return 1
    # def interferensi self pmt psd pdt

def interferensi(self, pmt, psd, pdt):
    return self.tetap(pmt) * self.turun(pmt) * self.naik(pmt) * self.tetap(psd) * self.turun(psd) * self.naik(psd) * self.tetap(pdt) * self.turun(pdt) * self.naik(pdt)