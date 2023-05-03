import valutuRiki

class GrozaSaturs():
    """docstring for GrozaSaturs."""
    def __init__(self, produkts, skaits):
        self.produkts = produkts
        self.skaits = skaits
    
    def get_nosaukums(self):
        return self.produkts.get_nosaukums()
    
    def get_produkts(self):
        return self.produkts
    def set_produkts(self, produkts):
        self.produkts = produkts
    
    def get_skaits(self):
        return self.skaits
    def set_skaits(self, skaits):
        self.skaits = skaits
    
    def get_vienibas_cena(self):
        return self.produkts.get_cena()
    def get_kopeja_cena(self):
        return self.produkts.get_cena() * self.skaits
    def printejama_kopeja_cena(self):
        return valutuRiki.printejama_vertiba_no_EUR(self.get_kopeja_cena())
    
    def __str__(self):
        return f"{self.get_nosaukums()} ({self.get_skaits()} x {self.get_vienibas_cena()})"

class Grozs():
    """docstring for Grozs."""
    def __init__(self):
        self.saraksts = []
    
    def get_kopeja_cena(self):
        summa = 0.
        for item in self.saraksts:
            summa += item.get_kopeja_cena()
        return summa
    def printejama_kopeja_cena(self):
        return valutuRiki.printejama_vertiba_no_EUR(self.get_kopeja_cena())
    
    def atrast_produktu(self, produkts): # Atgriež GrozaSaturs objektu un attiecīgo saraksta id, kurā ir tāds objekts, kāds tika ievadīts
        for id in range(len(self.saraksts)):
            item = self.saraksts[id]
            if item.get_produkts() == produkts:
                return item, id
        return None, None
    def parbaudit_izdzestus_produktus(self):
        index = 0
        while index < len(self.saraksts):
            item = self.saraksts[index]
            if item.get_produkts() == None or item.get_produkts().get_izdzests() == True:
                self.nonemt_indeksu(index)
            else:
                index += 1

    
    def pievienot_produktu(self, produkts, skaits):
        kluda = ""
        produkts_groza_satura, id = self.atrast_produktu(produkts)
        if produkts_groza_satura: # Ja pievienojamais produkts jau ir šajā grozā, radīt kļūdu
            kluda += f"Kļūda: Produkts '{produkts_groza_satura.get_nosaukums()}' jau ir grozā ar skaitu {produkts_groza_satura.get_skaits()}.\n"
            
        if kluda == "": # Nevienas kļūdas nav
            self.saraksts.append(GrozaSaturs(produkts, skaits))
        else:
            return kluda[:-1]
        
    def mainit_produkta_skaitu(self, produkts, skaits):
        kluda = ""
        produkts_groza_satura, id = self.atrast_produktu(produkts)
        if not produkts_groza_satura: # Ja maināmais produkts nav šajā grozā, radīt kļūdu
            kluda += f"Kļūda: Produkts '{produkts.get_nosaukums()}' nav grozā.\n"
            
        if kluda == "": # Nevienas kļūdas nav
            produkts_groza_satura.set_skaits(skaits)
        else:
            return kluda[:-1]
    
    def nonemt_produktu(self, produkts):
        kluda = ""
        produkts_groza_satura, id = self.atrast_produktu(produkts)
        if not id: # Ja pievienojamais produkts nav šajā grozā, radīt kļūdu
            kluda += f"Kļūda: Produkts '{produkts.get_nosaukums()}' nav grozā.\n"
            
        if kluda == "": # Nevienas kļūdas nav
            self.saraksts.pop(id)
        else:
            return kluda[:-1]
    
    def nonemt_indeksu(self, indekss):
        self.saraksts.pop(indekss)
    
    def __str__(self):
        self.parbaudit_izdzestus_produktus()
        res = "# Iepirkumu grozs:\n"
        for item in self.saraksts:
            res += str(item) + ",\n"
        res += f"Kopējā cena: {self.printejama_kopeja_cena()}"
        return res