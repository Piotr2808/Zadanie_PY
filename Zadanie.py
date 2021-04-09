#Stwórz program, który na podstawie tabeli inflacji wartości oprocentowania kredytu,
# kwoty początkowej kredytu i stałej wartości raty wyliczy wartość zadłużenia
# w każdym miesiącu przez 2 nadchodzące lata.
#
#Niech program wydrukuje dla każdego miesiąca następującą linię:
#Twoja pozostała kwota kredytu to X, to Y mniej niż w poprzednim miesiącu.
#
#Napisz program tak, by wysokość początkowego kredytu,
# oprocentowanie kredytu (ponad inflację), i kwota raty były pobierane
# ze standardowego wejścia (terminal).
#
#Przykładowe wartości kredytu i formułę do jego wyliczenia znajdziesz
# w załączniku powyżej. Skopiuj z niego wartości inflacji dla każdego miesiąca.
#
#Wyślij link do swojego repozytorium (nie spakowany kod).
# Repozytorium powinno zawierać więcej, niż jeden commit.

#Dodaje plik na repozytorium w GitHub, dodaje commit i zaczynam zadanie.

print("Witamy na stronie banku. Podaj imię: ")
user_name = input()
print(user_name)

#inflacja = x
x = (1.592824484)

#pozyczka = y
y = 12000

#pozostała kwota = z
z = (1+((x + 3)/1200))*y-200

#m = wysokość raty
m = y - z

print("\nTwoja pozostała kwota kredytu (Styczeń) to: " + str(z) + "\nTo: " + str(m) + " mniej niż w poprzednim miesiącu.")


# Lista inflacja zaczyna się od lutego, kwota od stycznia.

inflacja = [-0.453509101, 2.324671717, 1.261254407, 1.782526286, 2.329384541, 1.502229842, 1.782526286,
            2.328848994, 0.616921348, 2.352295886, 0.337779545, 1.577035247, -0.292781443, 2.48619659,
            0.267110318, 1.417952672, 1.054243267, 1.480520104, 1.577035247, -0.07742069, 1.165733399,
            -0.404186718, 1.499708521]

#kwota do spłaty = kwota

kwota = [11845.92824, 11671.0662, 11522.85337, 11363.77154, 11209.06115, 11058.84232, 10900.33353,
         10743.77614, 10591.4861, 10423.40991, 10269.90089, 10098.46645, 9936.983976, 9759.401966,
         9604.020297, 9430.168126, 9264.886489, 9096.188242, 8930.151288, 8764.212635, 8585.557724,
         8415.362011, 8233.565935, 8064.439807]

#print(inflacja[]) Do wywolania elementu listy

#pozostała kwota = z
#z = (1+((x + 3)/1200))*y-200

#pozostala kwota = pk
pk = (1 + ((inflacja[0] + 3)/1200)) * kwota[0] - 200
#wysokosc raty = wr
wr = kwota[0] - pk
print("\nTwoja pozostała kwota kredytu (Luty) to: " + str(pk) + "\nTo: " + str(wr) + " mniej niż w poprzednim miesiącu.")

pk = (1 + ((inflacja[1] + 3)/1200)) * kwota[1] - 200
wr = kwota[1] - pk
print("\nTwoja pozostała kwota kredytu (Marzec) to: " + str(pk) + "\nTo: " + str(wr) + " mniej niż w poprzednim miesiącu.")

pk = (1 + ((inflacja[2] + 3)/1200)) * kwota[2] - 200
wr = kwota[2] - pk
print("\nTwoja pozostała kwota kredytu (Kwiecień) to: " + str(pk) + "\nTo: " + str(wr) + " mniej niż w poprzednim miesiącu.")

pk = (1 + ((inflacja[3] + 3)/1200)) * kwota[3] - 200
wr = kwota[3] - pk
print("\nTwoja pozostała kwota kredytu (Maj) to: " + str(pk) + "\nTo: " + str(wr) + " mniej niż w poprzednim miesiącu.")

pk = (1 + ((inflacja[4] + 3)/1200)) * kwota[4] - 200
wr = kwota[4] - pk
print("\nTwoja pozostała kwota kredytu (Czerwiec) to: " + str(pk) + "\nTo: " + str(wr) + " mniej niż w poprzednim miesiącu.")

pk = (1 + ((inflacja[5] + 3)/1200)) * kwota[5] - 200
wr = kwota[5] - pk
print("\nTwoja pozostała kwota kredytu (Lipiec) to: " + str(pk) + "\nTo: " + str(wr) + " mniej niż w poprzednim miesiącu.")

pk = (1 + ((inflacja[6] + 3)/1200)) * kwota[6] - 200
wr = kwota[6] - pk
print("\nTwoja pozostała kwota kredytu (Sierpień) to: " + str(pk) + "\nTo: " + str(wr) + " mniej niż w poprzednim miesiącu.")

pk = (1 + ((inflacja[7] + 3)/1200)) * kwota[7] - 200
wr = kwota[7] - pk
print("\nTwoja pozostała kwota kredytu (Wrzesień) to: " + str(pk) + "\nTo: " + str(wr) + " mniej niż w poprzednim miesiącu.")

pk = (1 + ((inflacja[8] + 3)/1200)) * kwota[8] - 200
wr = kwota[8] - pk
print("\nTwoja pozostała kwota kredytu (Październik) to: " + str(pk) + "\nTo: " + str(wr) + " mniej niż w poprzednim miesiącu.")

pk = (1 + ((inflacja[9] + 3)/1200)) * kwota[9] - 200
wr = kwota[9] - pk
print("\nTwoja pozostała kwota kredytu (Listopad) to: " + str(pk) + "\nTo: " + str(wr) + " mniej niż w poprzednim miesiącu.")

pk = (1 + ((inflacja[10] + 3)/1200)) * kwota[10] - 200
wr = kwota[10] - pk
print("\nTwoja pozostała kwota kredytu (Grudzień) to: " + str(pk) + "\nTo: " + str(wr) + " mniej niż w poprzednim miesiącu.")

pk = (1 + ((inflacja[11] + 3)/1200)) * kwota[11] - 200
wr = kwota[11] - pk
print("\nTwoja pozostała kwota kredytu (Styczeń) to: " + str(pk) + "\nTo: " + str(wr) + " mniej niż w poprzednim miesiącu.")

pk = (1 + ((inflacja[12] + 3)/1200)) * kwota[12] - 200
wr = kwota[12] - pk
print("\nTwoja pozostała kwota kredytu (Luty) to: " + str(pk) + "\nTo: " + str(wr) + " mniej niż w poprzednim miesiącu.")

pk = (1 + ((inflacja[13] + 3)/1200)) * kwota[13] - 200
wr = kwota[13] - pk
print("\nTwoja pozostała kwota kredytu (Marzec) to: " + str(pk) + "\nTo: " + str(wr) + " mniej niż w poprzednim miesiącu.")

pk = (1 + ((inflacja[14] + 3)/1200)) * kwota[14] - 200
wr = kwota[14] - pk
print("\nTwoja pozostała kwota kredytu (Kwiecień) to: " + str(pk) + "\nTo: " + str(wr) + " mniej niż w poprzednim miesiącu.")

pk = (1 + ((inflacja[15] + 3)/1200)) * kwota[15] - 200
wr = kwota[15] - pk
print("\nTwoja pozostała kwota kredytu (Maj) to: " + str(pk) + "\nTo: " + str(wr) + " mniej niż w poprzednim miesiącu.")

pk = (1 + ((inflacja[16] + 3)/1200)) * kwota[16] - 200
wr = kwota[16] - pk
print("\nTwoja pozostała kwota kredytu (Czerwiec) to: " + str(pk) + "\nTo: " + str(wr) + " mniej niż w poprzednim miesiącu.")

pk = (1 + ((inflacja[17] + 3)/1200)) * kwota[17] - 200
wr = kwota[17] - pk
print("\nTwoja pozostała kwota kredytu (Lipiec) to: " + str(pk) + "\nTo: " + str(wr) + " mniej niż w poprzednim miesiącu.")

pk = (1 + ((inflacja[18] + 3)/1200)) * kwota[18] - 200
wr = kwota[18] - pk
print("\nTwoja pozostała kwota kredytu (Sierpień) to: " + str(pk) + "\nTo: " + str(wr) + " mniej niż w poprzednim miesiącu.")

pk = (1 + ((inflacja[19] + 3)/1200)) * kwota[19] - 200
wr = kwota[19] - pk
print("\nTwoja pozostała kwota kredytu (Wrzesień) to: " + str(pk) + "\nTo: " + str(wr) + " mniej niż w poprzednim miesiącu.")

pk = (1 + ((inflacja[20] + 3)/1200)) * kwota[20] - 200
wr = kwota[20] - pk
print("\nTwoja pozostała kwota kredytu (Październik) to: " + str(pk) + "\nTo: " + str(wr) + " mniej niż w poprzednim miesiącu.")

pk = (1 + ((inflacja[21] + 3)/1200)) * kwota[21] - 200
wr = kwota[21] - pk
print("\nTwoja pozostała kwota kredytu (Listopad) to: " + str(pk) + "\nTo: " + str(wr) + " mniej niż w poprzednim miesiącu.")

pk = (1 + ((inflacja[22] + 3)/1200)) * kwota[22] - 200
wr = kwota[22] - pk
print("\nTwoja pozostała kwota kredytu (Grudzień) to: " + str(pk) + "\nTo: " + str(wr) + " mniej niż w poprzednim miesiącu.")