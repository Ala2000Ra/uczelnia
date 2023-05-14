#zad 1.1
hello = "Hello"
student = "Ola"

print(hello + " " + student)

#zad 1.2
student = input("Wpisz swoje imie ")
print("Hello "+ student)

#zad 1.3
studenci = ["Ania", "Kuba", "Piotr", "Jan"]
liczba_studentow = len(studenci)
print("Liczba studentów wynosi: " + str(liczba_studentow))

#zad 1.4
studenci = ["Ania", "Kasia", "Piotr", "Tomek"]
for x in studenci:
    print("Hello " + x)

#zad 1.5
liczba = 3
potega = 4
wynik = liczba**potega
print("Wynik wynosi: " +str(wynik))

#zad 1.6
ciag_znakow = "edbw(hdakqas(skqskahb))adwndwb(wgwidn()dsqwhjdw)"
liczba_nawiasow_otwierajacych = 0
for nawias in ciag_znakow:
    if nawias == "(":
        liczba_nawiasow_otwierajacych = liczba_nawiasow_otwierajacych + 1
        
print("Liczba nawiasow otwierajacych wynosi: " + str(liczba_nawiasow_otwierajacych))

#zad 1.7
studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
studenci.sort()
print("Alfabetyczna lista studentow wynosi: ")
for student in studenci:
    print(student)

# zad 1.8
studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
sort = sorted(studenci, key = lambda x : x.split()[-1])
print("Alfabetyczna lista studentow wynosi: ")
for student in sort:
    print(student)

# zad 1.9
studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
liczba_n = 0
for student in studenci:
    if student.split()[1][0] == "N":
        liczba_n +=1
print("Liczba studentow na N wynosi: " + str(liczba_n))


#zad 1.10
wykres_1 = [[2, 4], [4, 4], [6, 4]]
wykres_2 = [[2, 3], [4, 4], [6, 5]]
wykres_3 = [[2, 3], [4, 3], [5, 4]]

def czy_liniowa(wykres):
    a = None
    for i in range(len(wykres) - 1):
        x1, y1 = wykres[i]
        x2, y2 = wykres[i+1]
        spra = (y2 - y1)/(x2-x1)
        if a is None:
            a = spra
        elif spra != a:
            return False        
    return True
    
wykres_1_funkcja_liniowa = czy_liniowa(wykres_1)
wykres_2_funkcja_liniowa = czy_liniowa(wykres_2)
wykres_3_funkcja_liniowa = czy_liniowa(wykres_3)

if wykres_1_funkcja_liniowa:
    print("Dla punktow w wykres_1 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_1 nie mozna wyznaczyc funkcji liniowej.")

if wykres_2_funkcja_liniowa:
    print("Dla punktow w wykres_2 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_2 nie mozna wyznaczyc funkcji liniowej.")

if wykres_3_funkcja_liniowa:
    print("Dla punktow w wykres_3 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_3 nie mozna wyznaczyc funkcji liniowej.")
