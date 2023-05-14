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