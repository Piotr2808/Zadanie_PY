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

#print("Witamy na stronie banku. Podaj imię: ")
#user_name = input()
#print(user_name)

#inflacja = x
x = (1.592824484)

#pozyczka = y
y = 12000

#pozostała kwota = z
z = (1+((x + 3)/1200))*y-200

#m = wysokość raty
m = y - z

print("Twoja pozostała kwota kredytu to: " + str(z) + "\nTo: " + str(m) + " mniej niż w poprzednim miesiącu.")

inflacja = [-0.453509101, 2.324671717, 1.261254407, 1.782526286, 2.329384541, 1.502229842, 1.782526286,
            2.328848994, 0.616921348, 2.352295886, 0.337779545, 1.577035247, -0.292781443, 2.48619659,
            0.267110318, 1.417952672, 1.054243267, 1.480520104, 1.577035247, -0.07742069, 1.165733399,
            -0.404186718, 1.499708521]

#print(inflacja[]) Do wywolania elementu listy

#kwota do spłaty = kwota

kwota = [11845.92824, 11671.0662, 11522.85337, 11363.77154, 11209.06115, 11058.84232, 10900.33353,
         10743.77614, 10591.4861, 10423.40991, 10269.90089, 10098.46645, 9936.983976, 9759.401966,
         9604.020297, 9430.168126, 9264.886489, 9096.188242, 8930.151288, 8764.212635, 8585.557724,
         8415.362011, 8233.565935, 8064.439807]