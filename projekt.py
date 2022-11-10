import requests
import bs4
def aita_koodi_tagastja(linn):
    try:
        lehe_nimi = "https://www.iata.org/en/publications/directories/code-search/?airport.search=" + linn
        res = requests.get(lehe_nimi)
        res.raise_for_status()
        iata_soup = bs4.BeautifulSoup(res.text, "html.parser")
        koodid = iata_soup.select(".datatable")
        scrape_list = str(koodid).split("\n")
        aita_kood = scrape_list[12].replace("<td>", "")
        aita_kood = aita_kood.replace("</td>", "")
        return aita_kood
    except:
        return False
    
def parim_pilet(sihtkoha_kood, algus_kuupäev, lõpp_kuupäev):
    lähtekoha_kood = "TLL"
    #kuupäeva sisendid on juba YYYY-MM-DD vormis
    aadress = "https://www.momondo.ee/flight-search/"+lähtekoha_kood+"-"+sihtkoha_kood+"/"+algus_kuupäev+"/"+lõpp_kuupäev+"?sort=bestflight_a"
    res = requests.get(aadress)
    res.raise_for_status()
    pilet_soup = bs4.BeautifulSoup(res.text, "html.parser")
    hinnad = pilet_soup.find_all("span", class_="price option-text")
    return str(hinnad)