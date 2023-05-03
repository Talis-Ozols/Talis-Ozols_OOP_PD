from Produkts import Produkts
import ievadesRiki

class Elektronika(Produkts):
    """docstring for Elektronika."""
    def __init__(self, nosaukums="", cena=0., apraksts="", razotajs=""):
        super(Elektronika, self).__init__(nosaukums, cena, apraksts)
        self.razotajs = razotajs
    
    def get_razotajs(self):
        return self.razotajs
    def set_razotajs(self, razotajs):
        self.razotajs = razotajs
    def parse_razotajs(self, razotajs):
        razotajs = razotajs.strip()
        if razotajs == "":
            return True, "Ražotājs nedrīkst būt tukšs."
        return False, razotajs
    def pieprasit_razotajs(self):
        return ievadesRiki.pieprasit_un_apstradat_vertibu("Ražotājs: ", self.parse_razotajs)
    def pieprasit_un_mainit_razotajs(self):
        self.set_razotajs(self.pieprasit_razotajs())

    def __str__(self):
        return f"# Elektronikas produkts:\nnosaukums: {self.get_nosaukums()},\ncena: {self.printejama_cena()},\napraksts: {self.get_apraksts()},\nražotājs: {self.get_razotajs()}"

class Apgerbs(Produkts):
    """docstring for Apgerbs."""
    def __init__(self, nosaukums="", cena=0., apraksts="", brends=""):
        super(Apgerbs, self).__init__(nosaukums, cena, apraksts)
        self.brends = brends
    
    def get_brends(self):
        return self.brends
    def set_brends(self, brends):
        self.brends = brends
    def parse_brends(self, brends):
        brends = brends.strip()
        if brends == "":
            return True, "Brends nedrīkst būt tukšs."
        return False, brends
    def pieprasit_brends(self):
        return ievadesRiki.pieprasit_un_apstradat_vertibu("Brends: ", self.parse_brends)
    def pieprasit_un_mainit_brends(self):
        self.set_brends(self.pieprasit_brends())

    def __str__(self):
        return f"# Apģērbs:\nnosaukums: {self.get_nosaukums()},\ncena: {self.printejama_cena()},\napraksts: {self.get_apraksts()},\nbrends: {self.get_brends()}"

class Gramata(Produkts):
    """docstring for Gramata."""
    def __init__(self, nosaukums="", cena=0., apraksts="", autori=[], izdevejs=""):
        super(Gramata, self).__init__(nosaukums, cena, apraksts)
        self.autori = autori
        self.izdevejs = izdevejs
    
    def get_autori(self):
        return self.autori
    def set_autori(self, autori):
        self.autori = autori
    def parse_autori(self, autori):
        autori = autori.split(',')
        autori = [autors.strip() for autors in autori]
        if autori[-1] == "":
            autori = autori[:-1]
        for autors in autori:
            if autors == "":
                return True, "Neviens autors nedrīkst būt tukšs."
        return False, autori
    def pieprasit_autori(self):
        return ievadesRiki.pieprasit_un_apstradat_vertibu("Autori (atdalīti ar komatiem): ", self.parse_autori)
    def pieprasit_un_mainit_autori(self):
        self.set_autori(self.pieprasit_autori())

    def get_izdevejs(self):
        return self.izdevejs
    def set_izdevejs(self, izdevejs):
        self.izdevejs = izdevejs
    def parse_izdevejs(self, izdevejs):
        izdevejs = izdevejs.strip()
        if izdevejs == "":
            return True, "Izdevējs nedrīkst būt tukšs."
        return False, izdevejs
    def pieprasit_izdevejs(self):
        return ievadesRiki.pieprasit_un_apstradat_vertibu("Izdevējs: ", self.parse_izdevejs)
    def pieprasit_un_mainit_izdevejs(self):
        self.set_izdevejs(self.pieprasit_izdevejs())

    def __str__(self):
        return f"# Gramāta:\nnosaukums: {self.get_nosaukums()},\ncena: {self.printejama_cena()},\napraksts: {self.get_apraksts()},\nautori: {self.get_autori()},\nizdevējs: {self.get_izdevejs()}"