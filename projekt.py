import requests
from bs4 import BeautifulSoup

#Beta versiooniks on plaanis luua programm, mis võtab kõik funktsioonid kasutusse ja luua sellele EasyGUI-ga graafiline liide.
#Samuti arendame me funktsioone, et nad tagastaksid täpsemat infot ja seda paremal kujul.

def aita_koodi_tagastja(linn):
    #Linna nime sisestades tagastab 3-tähelise AITA koodi, mida on vaja järgmise funkt. jaoks
    try:
        lehe_nimi = "https://www.iata.org/en/publications/directories/code-search/?airport.search=" + linn
        res = requests.get(lehe_nimi)
        res.raise_for_status()
        iata_soup = BeautifulSoup(res.text, "html.parser")
        koodid = iata_soup.select(".datatable")
        scrape_list = str(koodid).split("\n")
        aita_kood = scrape_list[12].replace("<td>", "")
        aita_kood = aita_kood.replace("</td>", "")
        return aita_kood
    except:
        return False
    
def parim_pilet(sihtkoha_kood, algus_kuupäev, lõpp_kuupäev):
    #Tagastab lennupiletite ostmise lingi
    try:
        lähtekoha_kood = "TLL"
        #kuupäeva sisendid on juba YYYY-MM-DD vormis
        aadress = "https://www.momondo.ee/flight-search/"+lähtekoha_kood+"-"+sihtkoha_kood+"/"+algus_kuupäev+"/"+lõpp_kuupäev
        res = requests.get(aadress)
        res.raise_for_status()
        pilet_soup = BeautifulSoup(res.text, "html.parser")
        hinnad = pilet_soup.find_all(href=compile("book"))
        return hinnad
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