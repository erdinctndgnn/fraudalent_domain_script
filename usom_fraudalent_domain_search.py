import requests
from bs4 import BeautifulSoup
import re 
list=[]
for i in range(1,801) : #1'den 800'e kadar olan sayfaları tarar
    url="https://www.usom.gov.tr/zararli-baglantilar/"+str(i)+".html"
    html=requests.get(url).content
    soup=BeautifulSoup(html,"html.parser")
    liste=soup.find("div",{"class":"article"}).find_all("tr")
    eleman_sayisi=len(liste)
    
    for i in range (100) :
        sorgu=liste[i].text.splitlines()
        list.append(sorgu[2])

aranacak_deger=input("Aramak İstediğiniz Veriyi Giriniz:")
print(len(list)) #kaç tane url tarandığını yazdırır

def main() :
    for item in list :
        if re.search(aranacak_deger,item) : #aranmak istenen değişken 'para' kısmına yazılmalıdır
            print(item,end="\t")

if __name__ == "__main__":
    main()
