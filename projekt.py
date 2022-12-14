import requests
from bs4 import BeautifulSoup
from easygui import *
#Beta versiooniks on plaanis luua programm, mis võtab kõik funktsioonid kasutusse ja luua sellele EasyGUI-ga graafiline liide.
#Samuti arendame me funktsioone, et nad tagastaksid täpsemat infot ja seda paremal kujul.
tiitel = "REISI ÄPP"
def main():
    while True:
        riik = enterbox("Sisestage riik kuhu soovite reisida:", tiitel)
        linn = enterbox("Sisestage linn kuhu soovite reisida:", tiitel)
        lahkumine = enterbox("Sisestage reisi alguskuupäev (YYYY-MM-DD)", tiitel)
        saabumine = enterbox("Sisestage reisi lõppkuupäev (YYYY-MM-DD)", tiitel)
        hind = parim_pilet(lahkumine.lower(), saabumine.lower(), riik, linn)
        if not hind:
            msgbox("Paistab, et olete sisendväljad valesti täitnud!", tiitel)
            continue
        else:
            msg = "Parim edasi-tagasi lennupilet sisestatud kuupäeval sihtkohta "+ riik + ", "+ linn + " maksab "+ hind
            valikud = ["Ööbimine", "Proovi uuesti"]
            vastus = buttonbox(msg, choices=valikud)

        if vastus == "Proovi uuesti":
            continue
        
        #Merlini osa

def parim_pilet(lahkumis_kuupäev, saabumis_kuupäev, sihtkoha_riik, sihtkoha_linn):
    #Tagastab lennupiletite ostmise lingi
    #Kuupäeva vorm: YYYY-MM-DD
    try:
        url = "https://www.kiwi.com/ee/search/results/tallinn-estonia/"+sihtkoha_riik+"-"+sihtkoha_linn+"/"+lahkumis_kuupäev+"/"+saabumis_kuupäev
        res = requests.get(url)
        res.raise_for_status()
        pilet_soup = BeautifulSoup(res.text, "html.parser")
        hinnad = pilet_soup.find_all("span", "length-5")
        parim_hind = str(hinnad[0]).replace('<span class="length-5">', "")
        parim_hind = parim_hind.replace("</span>", "")
        return parim_hind
    except:
        return False

def parim_ööbimiskoht(riigi_kood_2tahte_väikesed, linna_nimi):
#nt https://www.booking.com/city/us/new-york.et.html?label=gen173nr-1FCAEoggI46AdIM1gEaEKIAQGYAQu4ARfIAQzYAQHoAQH4AQuIAgGoAgO4AuzGtZsGwAIB0gIkODliOGQ5MjctZjNiMy00MTFiLTk1ODMtMzY5ZDU1MDcxNTgz2AIG4AIB&sid=2f31cf00ead6c4efcc67629c216d950a&aid=304142
    url="https://www.booking.com/city/"+riigi_kood_2tahte_väikesed+"/"+linna_nimi
    response=requests.get(url)
    soup=BeautifulSoup(response.text, "html.parser")
#soup.select() sees on bloki class kus kõik hotelli informatsioon kirjas on
    for element in soup.select(".sr_card.js-sr-card"):
        try:
        #hotelli nime "class"
            print(element.select(".bui-card_title")[0].get_text().strip())
        #hotelli hinna "class"
            print(element.select(".bui-price-display_value.bui-f-color_constructive")[0].get_text().strip())
        #eraldab hotellide nimed
            print("<----->")
        except:
            return False

main()