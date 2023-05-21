class Student:
    def __init__(self, imie, nazwisko, numer_indeksu):
        self.imie_studenta = imie
        self.nazwisko = nazwisko
        self.numer_indeksu = numer_indeksu
        self.indeks = []

    def __str__(self):
        return self.imie_studenta + ' ' + self.nazwisko + ' ' + str(self.numer_indeksu)

    def dodaj_ocene(self, ocena):
        self.indeks.append(ocena)

    def srednia_ocen(self):
        if len(self.indeks) == 0:
            return 0
        else:
            return sum(self.indeks) / len(self.indeks)

srednia=Student.srednia_ocen      
student_ala = Student("Alicja", "Radke", 12345)
student_ala.dodaj_ocene(5.0)
student_ala.dodaj_ocene(4.0)
student_ala.dodaj_ocene(3.0)
print(student_ala.indeks)
print(student_ala.srednia_ocen())