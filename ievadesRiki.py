def pieprasit_un_apstradat_vertibu(teksts, funkcija):
    while True:
        ievade = input(teksts)
        ir_kluda, dati = funkcija(ievade)
        if ir_kluda: # Izvadīt kļūdas paziņojumu
            print(dati)
        else: # Nav kļūdas, vērtība tika veiksmīgi ievadīta
            return dati

def pieprasit_naturalu_robezas(teksts, min = 1, max_neieskaitot = float('inf')):
    def derigs_skaitlis(n):
        try:
            n = int(n)
        except ValueError:
            return True, "Nav ievadīts vesels skaitlis."
        if n < min:
            return True, "Skaitlis ir pārāk mazs."
        if n >= max_neieskaitot:
            return True, "Skaitlis ir pārāk liels."
        return False, n

    return pieprasit_un_apstradat_vertibu(teksts, derigs_skaitlis)