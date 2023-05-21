#trojkat
def trojkat(bok_a, bok_b, bok_c, h_a):
    pole = bok_a * h_a / 2
    obwod = bok_a + bok_b + bok_c
    return pole, obwod

print(f'Pole i obwod wynosi: {trojkat(10, 15, 12, 8)}')


#trapez
def trapez(bok_a, bok_b, bok_c, h_a,bok_d):
    pole = (bok_a + bok_b) * h_a * 0.5
    obwod = bok_a + bok_b + bok_c +bok_d
    return pole, obwod

print(f'Pole i obwod wynosi: {trapez(10, 15, 12, 8, 12)}')


#romb
def romb(bok_a, h_a):
    pole = bok_a * h_a
    obwod = 4 * bok_a
    return pole, obwod

print(f'Pole i obwod wynosi: {romb(10, 8)}')