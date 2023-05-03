import globalVars
import ProduktuTipi
import Grozs
import valutuRiki
import ievadesRiki

def __main__():
    produkti = []
    produkti.append(ProduktuTipi.Elektronika("Dators", 200.45, "Labs dators™", "ElectoInc"))
    produkti.append(ProduktuTipi.Apgerbs("Krekls", 12.00, "Šis ir krekls", "8 Grapefruit"))
    produkti.append(ProduktuTipi.Gramata("Svešinieks", 1.23, "OK grāmata", ["A. Kamī"], "Zvaigzne ABC"))
    
    mans_grozs = Grozs.Grozs()
    print("# Groza lietošanas piemērs:")
    print("1.", mans_grozs.pievienot_produktu(produkti[0], 1))
    print("2.", mans_grozs.pievienot_produktu(produkti[1], 1))
    print("3.", mans_grozs.pievienot_produktu(produkti[1], 1)) # Nestrādās, jo produkts jau ir pievienots
    print("4.", mans_grozs.mainit_produkta_skaitu(produkti[1], 2))
    print("5.", mans_grozs.nonemt_produktu(produkti[2])) # Nestrādās, jo produkts nav pievienots
    print("6.", mans_grozs.pievienot_produktu(produkti[2], 1))
    print("7.", mans_grozs.nonemt_produktu(produkti[2]))
    print()
    
    print(mans_grozs)
    print()
    
    print("## Visi produkti:")
    for p in produkti:
        print(p)
    
    while True:
        ievade_darbiba = input("# Darbības:\nsp - parādīt visus produktus,\nap - izveidot jaunu produktu,\ndp - dzēst produktu,\nsg - parādīt visus produktus grozā,\nag - pievienot produktu grozam,\ndg - dzēst no groza,\nv - mainīt valūtu,\nx - iziet.\n")
        if ievade_darbiba == "sp":
            print("## Visi produkti:")
            for p in produkti:
                print(p)
        elif ievade_darbiba == "ap":
            ievade_tips = ievadesRiki.pieprasit_un_apstradat_vertibu("Produktu tipi: el - elektronika, ap - apģērbs, gr - grāmata. ", lambda x: (False, x) if x in ["el", "ap", "gr"] else (True, "Ievadiet kādu no norādītajiem produktu tipiem."))
            if ievade_tips == "el":
                jaunais_objekts = ProduktuTipi.Elektronika()
                jaunais_objekts.pieprasit_un_mainit_nosaukums()
                jaunais_objekts.pieprasit_un_mainit_cena()
                jaunais_objekts.pieprasit_un_mainit_apraksts()
                jaunais_objekts.pieprasit_un_mainit_razotajs()
                produkti.append(jaunais_objekts)
            if ievade_tips == "ap":
                jaunais_objekts = ProduktuTipi.Apgerbs()
                jaunais_objekts.pieprasit_un_mainit_nosaukums()
                jaunais_objekts.pieprasit_un_mainit_cena()
                jaunais_objekts.pieprasit_un_mainit_apraksts()
                jaunais_objekts.pieprasit_un_mainit_brends()
                produkti.append(jaunais_objekts)
            if ievade_tips == "gr":
                jaunais_objekts = ProduktuTipi.Gramata()
                jaunais_objekts.pieprasit_un_mainit_nosaukums()
                jaunais_objekts.pieprasit_un_mainit_cena()
                jaunais_objekts.pieprasit_un_mainit_apraksts()
                jaunais_objekts.pieprasit_un_mainit_autori()
                jaunais_objekts.pieprasit_un_mainit_izdevejs()
                produkti.append(jaunais_objekts)
        elif ievade_darbiba == "dp":
            print("# Visi produkti:")
            for i in range(len(produkti)):
                print(i, produkti[i].get_nosaukums())
            i = ievadesRiki.pieprasit_naturalu_robezas("Ievadiet dzēšamā produkta indeksu: ", 0, len(produkti))
            produkti.pop(i)
        elif ievade_darbiba == "sg":
            print(mans_grozs)
        elif ievade_darbiba == "ag":
            print("# Visi produkti:")
            for i in range(len(produkti)):
                print(i, produkti[i].get_nosaukums())
            while True:
                i = ievadesRiki.pieprasit_naturalu_robezas("Ievadiet pievienojamā produkta indeksu: ", 0, len(produkti))
                prod = produkti[i]
                if mans_grozs.atrast_produktu(prod)[0]: # Jau pastāv
                    print("Ievadītais produkts jau ir grozā.")
                else:
                    break
            skaits = ievadesRiki.pieprasit_naturalu_robezas("Ievadiet skaitu: ")
            mans_grozs.pievienot_produktu(prod, skaits)
        elif ievade_darbiba == "dg":
            print("# Grozs:")
            for i in range(len(mans_grozs.saraksts)):
                print(i, mans_grozs.saraksts[i].get_nosaukums())
            i = ievadesRiki.pieprasit_naturalu_robezas("Ievadiet dzēšamā produkta indeksu: ", 0, len(produkti))
            mans_grozs.nonemt_indeksu(i)
        elif ievade_darbiba == "v":
            print("Pieejamās valūtas:")
            print(valutuRiki.printejami_visu_valutu_nosaukumi())
            ievade_val = ievadesRiki.pieprasit_un_apstradat_vertibu("Ievadīt jauno valūtu: ", lambda x: (False, x) if x in valutuRiki.valutu_kursi_no_EUR else (True, "Valūta nav pieejama."))
            valutuRiki.set_izvades_valuta(ievade_val)
        elif ievade_darbiba == "x":
            break

__main__()