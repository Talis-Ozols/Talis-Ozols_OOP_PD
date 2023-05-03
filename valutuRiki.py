import globalVars
import requests

valutu_json = {}
valutu_kursi_no_EUR = {}

# valutas_kurss_no_EUR = 10

def atjaunot_valutu_kursus():
    global valutu_json
    global valutu_kursi_no_EUR
    valutu_json = requests.get('http://open.er-api.com/v6/latest/EUR').json()
    # valutu_kursi_no_EUR = json.loads(valutu_json)["rates"]
    valutu_kursi_no_EUR = valutu_json["rates"]

atjaunot_valutu_kursus()


def printejami_visu_valutu_nosaukumi():
    res = ""
    for valuta in valutu_kursi_no_EUR:
        res += valuta + " "
    return res[:-1]
def ir_deriga_valuta(val):
    return val in valutu_kursi_no_EUR

def EUR_uz_citu_valutu(skaitlis):
    return skaitlis * valutu_kursi_no_EUR[globalVars.izvades_valuta['valuta']]
def printejama_vertiba_no_EUR(skaitlis):
    return "{:.2f}".format(EUR_uz_citu_valutu(skaitlis)).replace(".", ",") + " " + globalVars.izvades_valuta['valuta']

def set_izvades_valuta(jauna_valuta):
    global izvades_valuta
    globalVars.izvades_valuta['valuta'] = jauna_valuta
