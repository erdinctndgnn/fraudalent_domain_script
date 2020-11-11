import requests
from bs4 import BeautifulSoup
import re 
list=[]
for i in range(1,801) : #1 den 800 e kadar olan sayfalari tarar
    url="https://www.usom.gov.tr/zararli-baglantilar/"+str(i)+".html"
    html=requests.get(url).content
    soup=BeautifulSoup(html,"html.parser")
    liste=soup.find("div",{"class":"article"}).find_all("tr")
    eleman_sayisi=len(liste)
    
    for i in range (100) :
        sorgu=liste[i].text.splitlines()
        list.append(sorgu[2])

aranacak_deger=input("Aramak istediginiz Veriyi Giriniz:")
print(len(list)) #kac tane url tarandigini yazdirir

def main() :
    for item in list :
        if re.search(aranacak_deger,item) :
            print(item,end="\t")

if __name__ == "__main__":
    main()
