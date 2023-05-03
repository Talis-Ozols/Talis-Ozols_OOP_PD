import globalVars
import valutuRiki
import ievadesRiki

class Produkts():
    """Produkts ir abstrakta klase, no kuras tiek atvasināti visi produktu veidi, kas veikalā tiek piedāvāti.
    cena - dotā produkta cena EUR. Izvadot tiek apaļota līdz diviem cipariem aiz komata."""
    def __init__(self, nosaukums, cena, apraksts):
        self.nosaukums = nosaukums
        self.cena = cena
        self.apraksts = apraksts
    
    def get_nosaukums(self):
        return self.nosaukums
    def set_nosaukums(self, nosaukums):
        self.nosaukums = nosaukums
    def parse_nosaukums(self, nosaukums):
        nosaukums = nosaukums.strip()
        if nosaukums == "":
            return True, "Nosaukums nedrīkst būt tukšs."
        return False, nosaukums
    def pieprasit_nosaukums(self):
        return ievadesRiki.pieprasit_un_apstradat_vertibu("Nosaukums: ", self.parse_nosaukums)
    def pieprasit_un_mainit_nosaukums(self):
        self.set_nosaukums(self.pieprasit_nosaukums())

    def get_cena(self):
        return self.cena
    def set_cena(self, cena):
        self.cena = cena
    def printejama_cena(self):
        return valutuRiki.printejama_vertiba_no_EUR(self.cena)
    def parse_cena(self, cena):
        cena = cena.strip().replace(",", ".")
        try:
            cena = float(cena)
        except ValueError:
            return True, "Cenu ir jāievada kā decimāldaļu."
        if cena <= 0:
            return True, "Cenai ir jābūt pozitīvai."
        return False, cena
    def pieprasit_cena(self):
        return ievadesRiki.pieprasit_un_apstradat_vertibu("Cena (EUR, decimāldaļa): ", self.parse_cena)
    def pieprasit_un_mainit_cena(self):
        self.set_cena(self.pieprasit_cena())

    def get_apraksts(self):
        return self.apraksts
    def set_apraksts(self, apraksts):
        self.apraksts = apraksts
    def parse_apraksts(self, apraksts):
        apraksts = apraksts.strip()
        if apraksts == "":
            return True, "Apraksts nedrīkst būt tukšs."
        return False, apraksts
    def pieprasit_apraksts(self):
        return ievadesRiki.pieprasit_un_apstradat_vertibu("Apraksts: ", self.parse_apraksts)
    def pieprasit_un_mainit_apraksts(self):
        self.set_apraksts(self.pieprasit_apraksts())

    def __str__(self):
        return f"# Produkts:\nnosaukums: {self.get_nosaukums()},\ncena: {self.printejama_cena()},\napraksts: {self.get_apraksts()}"
    
    

    