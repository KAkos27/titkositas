def titkositas(lista):
    szoveg:str = str(input("Kérek egy szöveget!: "))
    szoveg=szoveg.upper()

    for i in range(0,len(szoveg),1):
        for a in range(0,len(lista),1):
            if szoveg[i] == lista[a].eredeti:
                print(lista[a].titkositott,end="")