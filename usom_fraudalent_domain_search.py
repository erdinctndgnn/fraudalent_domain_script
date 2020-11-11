import requests
from bs4 import BeautifulSoup
import re 
list=[]
taranacak_sayfa=int(input("Taranacak Sayfa Sayısını Giriniz:"))
for i in range(1,taranacak_sayfa+1) : #1'den istenen sayfaya kadar olan sayfaları tarar
    url="https://www.usom.gov.tr/zararli-baglantilar/"+str(i)+".html"
    html=requests.get(url).content
    soup=BeautifulSoup(html,"html.parser")
    liste=soup.find("div",{"class":"article"}).find_all("tr")
    eleman_sayisi=len(liste)
    
    for i in range (100) :
        sorgu=liste[i].text.splitlines()
        list.append(sorgu[2])

aranacak_deger=input("Aramak İstediğiniz Veriyi Giriniz:")
print(f"Taranan Sayfa Sayısı:{taranacak_sayfa}".format(taranacak_sayfa)) #kaç tane sayfa tarandığını yazdırır
print(f"Taranan URL Sayısı:{len(list)}".format(len(list))) #kaç tane url tarandığını yazdırır
sorgu_liste=[]
def main() :
    for item in list :
        if re.search(aranacak_deger,item) : 
            sorgu_liste.append(item) #bulunan sonuçlar liste içerisine eklenir
        

if __name__ == "__main__":
    main()

if len(sorgu_liste) == 0 :
    print("Sorgulanan Değer Bulunamadı...")
else :
    print(f"Bulunan Sonuç Sayısı:{len(sorgu_liste)}".format(len(sorgu_liste))) #bulunan sonuç sayısını yazdırır
    print("Sonuçlar".center(50,"-"))
    for sonuc in sorgu_liste :
        print(sonuc) #bulunan sonuçları yazdırır

