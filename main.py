from Abc import Abc
import feladatok

betuk=[]
fajl=open("szovegek.txt","r",encoding="utf-8")
string_lista=fajl.readlines()
fajl.close()

for i in range(0,len(string_lista),1):
    aktsor=string_lista[i].strip()
    sor_lista=aktsor.split("@")
    betu = Abc(sor_lista[0],sor_lista[1])
    betuk.append(betu)

feladatok.titkositas(betuk)