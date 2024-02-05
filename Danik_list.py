nimed = ["Mati", "Kati"]

while True:
    valik = input("Andmete lisamine-add\nAndmete näitamine-show\n Kustutamine-del\nJärjendi pööramine-rev\nAndmete kustutamine-clear\nAndemete sortimine-sort\n")
    
    try:
        if valik == "add":
            valik_täpsustus = input("Kas lisame mitu inimest (mitu) lisamine või positsioonile (pos)? ")
            if valik_täpsustus == "mitu":
                mitu = int(input("Mitu inimest lisame? "))
                for i in range(mitu):
                    nimi = input("Sisesta nimi: ")
                    nimed.append(nimi)
            else:
                indeks = int(input("Kuhu lisamine "))
                nimi = input("Mis nimi: ")
                nimed.insert(indeks - 1, nimi)
                
        elif valik == "del":
            valik_täpsustus = input("Kas kustutame nimi (nimi) või indeksi järgi (ind)? ")
            if valik_täpsustus == "nimi":
                nimi = input("Mis nimi in vaja kustutada? ")
                kogus = nimed.count(nimi)
                if kogus > 0:
                    for i in range(kogus):
                        nimed.remove(nimi)
                else:
                    print(f"Nimi {nimi} ei ole nimekirjas")
            else:
                indeks = int(input("Mis on järjekordne number? "))
                nimed.pop(indeks - 1)
                
        elif valik == "show":
            print(nimed)
            
        elif valik == "rev":
            nimed.reverse()
            print(nimed)
            
        elif valik == "sort":
            nimed.sort()
            print(nimed)
            
        elif valik == "clear":
            nimed.clear()
            print(nimed)
            
        elif valik == "ots":
            nimi = input("Mis nime otsime? ")
            if nimed.count(nimi) > 0:
                for i in range(len(nimed)):
                    ind = nimed.index(nimi, ind + 1)
                    print(f"{nimi} on indeksiga {ind}")
            else:
                print(f"{nimi} ei ole nimekirjas")
                
    except ValueError:
        print(f"Viga: Palun sisesta korrektne väärtus.")
   
    