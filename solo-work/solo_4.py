class Dzialka:
    def __init__(self, cena, powierzchnia, typ_dzialki, odleglosc_od_Poznan, media, procent_wklad_wlasny, budzet_klienta):
        self.cena = cena
        self.powierzchnia = powierzchnia
        self.typ_dzialki = typ_dzialki
        self.odleglosc_od_Poznan = odleglosc_od_Poznan
        self.media = media
        self.wklad_wlasny = procent_wklad_wlasny
        self.budzet_klienta = budzet_klienta

    def __str__(self):
        return 'Cena (zł): '+ str(self.cena) + ', powierzcnia (mkw): ' + str(self.powierzchnia) + ', typ działki: ' + str(self.typ_dzialki) + ', odległość od Poznania (km): ' + str(self.odleglosc_od_Poznan) + ', media: ' + self.media + ', Procent wkładu własnego deklarowany przez Klietna (%): ' + str(self.wklad_wlasny) + ', budżet Klienta wynosi (zł): ' + str(self.budzet_klienta)

    def cena_dostepnosc(self):
        dostepnosc = " "
        if self.cena >= self.budzet_klienta:
            dostepnosc = "nie dostepna"
        else:
            dostepnosc = "dostepna"
        return dostepnosc

    def cena_metr(self):
        cena_metr_kw = self.cena / self.powierzchnia
        zaokr_cena_metr_kw = round(cena_metr_kw, 2)
        return zaokr_cena_metr_kw

    def odl_Poznan(self):
        odl_od_Poznan = ' '
        if self.odleglosc_od_Poznan == 0:
            odl_od_Poznan = 'Działka znajduje się na terenie Poznania.'
        elif self.odleglosc_od_Poznan <= 15:
            odl_od_Poznan = 'Działka znajduje się blisko Poznania.'
        else:
            odl_od_Poznan = 'Działka znajduje się daleko od Poznania.'
        return odl_od_Poznan

    def wymagany_wklad_wlasny(self):
        wklad_wlasny = self.wklad_wlasny / 100 * self.cena
        return wklad_wlasny

    def status(self):
        status_dzialki =' '
        if self.typ_dzialki == 'budowlana' and self.media == 'tak':
            status_dzialki = 'gotowa do zabudowy.'
        else:
            status_dzialki = 'nie gotowa do zabudowy.'
        return status_dzialki


dzialka_1 = Dzialka(212000, 1610, "budowlana", 30, "tak", 20, 200000)
dzialka_2 = Dzialka(555000, 1010, "budowlana", 10, "nie", 25, 500000)

print(f'Podstawowe informacje {dzialka_1}')
print(f'Czy działka dostępna według budżetu Klienta? {dzialka_1.cena_dostepnosc()}')
print(f'Cena za metr kwadratowy wynosi {dzialka_1.cena_metr()}')
print(dzialka_1.odl_Poznan())
print(f'Wymagalny wklad wlasny: {dzialka_1.wymagany_wklad_wlasny()}')
print(f'Działka {dzialka_1.status()}')

print('')

print(f'Podstawowe informacje {dzialka_2}')
print(f'Czy działka dostępna według budżetu Klienta? {dzialka_2.cena_dostepnosc()}')
print(f'Cena za metr kwadratowy wynosi {dzialka_2.cena_metr()}')
print(dzialka_2.odl_Poznan())
print(f'Wymagalny wklad wlasny: {dzialka_2.wymagany_wklad_wlasny()}')
print(f'Działka {dzialka_2.status()}')