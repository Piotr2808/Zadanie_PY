# Stwórz program, który na podstawie tabeli inflacji wartości oprocentowania kredytu,
# kwoty początkowej kredytu i stałej wartości raty wyliczy wartość zadłużenia
# w każdym miesiącu przez 2 nadchodzące lata.
#
# Niech program wydrukuje dla każdego miesiąca następującą linię:
# Twoja pozostała kwota kredytu to X, to Y mniej niż w poprzednim miesiącu.
#
# oprocentowanie kredytu (ponad inflację), i kwota raty były pobierane
# ze standardowego wejścia (terminal).
#
# Przykładowe wartości kredytu i formułę do jego wyliczenia znajdziesz
# w załączniku powyżej. Skopiuj z niego wartości inflacji dla każdego miesiąca.
#
# Wyślij link do swojego repozytorium (nie spakowany kod).
# Repozytorium powinno zawierać więcej, niż jeden commit.

# inflacja = inflation = inf(inf1 - inf24)

tra = 12000.00000
inf1 = 1.592824484
inf2 = -0.453509101
inf3 = 2.324671717
inf4 = 1.261254407
inf5 = 1.782526286
inf6 = 2.329384541
inf7 = 1.502229842
inf8 = 1.782526286
inf9 = 2.328848994
inf10 = 0.616921348
inf11 = 2.352295886
inf12 = 0.337779545
inf13 = 1.577035247
inf14 = -0.292781443
inf15 = 2.48619659
inf16 = 0.267110318
inf17 = 1.417952672
inf18 = 1.054243267
inf19 = 1.480520104
inf20 = 1.577035247
inf21 = -0.07742069
inf22 = 1.165733399
inf23 = -0.404186718
inf24 = 1.499708521

# pozyczka = pozostała kwota = the renaining amount = tra(tra - tra24)
# tra = (1 + ((inf + 3) / 1200)) * tra - 200

tra1  = (1 + ((inf1 + 3) / 1200)) * tra - 200
tra2 = (1 + ((inf2 + 3) / 1200)) * tra1 - 200
tra3 = (1 + ((inf3 + 3) / 1200)) * tra2 - 200
tra4 = (1 + ((inf4 + 3) / 1200)) * tra3 - 200
tra5 = (1 + ((inf5 + 3) / 1200)) * tra4 - 200
tra6 = (1 + ((inf6 + 3) / 1200)) * tra5 - 200
tra7 = (1 + ((inf7 + 3) / 1200)) * tra6 - 200
tra8 = (1 + ((inf8 + 3) / 1200)) * tra7 - 200
tra9 = (1 + ((inf9 + 3) / 1200)) * tra8 - 200
tra10 = (1 + ((inf10 + 3) / 1200)) * tra9 - 200
tra11 = (1 + ((inf11 + 3) / 1200)) * tra10 - 200
tra12 = (1 + ((inf12 + 3) / 1200)) * tra11 - 200
tra13 = (1 + ((inf13 + 3) / 1200)) * tra12 - 200
tra14 = (1 + ((inf14 + 3) / 1200)) * tra13 - 200
tra15 = (1 + ((inf15 + 3) / 1200)) * tra14 - 200
tra16 = (1 + ((inf16 + 3) / 1200)) * tra15 - 200
tra17 = (1 + ((inf17 + 3) / 1200)) * tra16 - 200
tra18 = (1 + ((inf18 + 3) / 1200)) * tra17 - 200
tra19 = (1 + ((inf19 + 3) / 1200)) * tra18 - 200
tra20 = (1 + ((inf20 + 3) / 1200)) * tra19 - 200
tra21 = (1 + ((inf21 + 3) / 1200)) * tra20 - 200
tra22 = (1 + ((inf22 + 3) / 1200)) * tra21 - 200
tra23 = (1 + ((inf23 + 3) / 1200)) * tra22 - 200
tra24 = (1 + ((inf24 + 3) / 1200)) * tra23 - 200

# month = mt(1 - 12)

mt1 = "Styczeń"
mt2 = "Luty"
mt3 = "Marzec"
mt4 = "Kwiecień"
mt5 = "Maj"
mt6 = "Czerwiec"
mt7 = "Lipiec"
mt8 = "Sierpień"
mt9 = "Wrzesień"
mt10 = "Październik"
mt11 = "Listopad"
mt12 = "Grudzień"

# difference = dif

dif1 = tra - tra1
dif2 = tra1 - tra2
dif3 = tra2 - tra3
dif4 = tra3- tra4
dif5 = tra4- tra5
dif6 = tra5 - tra6
dif7 = tra6 - tra7
dif8 = tra7 - tra8
dif9 = tra8 - tra9
dif10 = tra9 - tra10
dif11 = tra10 - tra11
dif12 = tra11 - tra12
dif13 = tra12 - tra13
dif14 = tra13 - tra14
dif15 = tra14 - tra15
dif16 = tra15 - tra16
dif17 = tra16 - tra17
dif18 = tra17 - tra18
dif19 = tra18 -tra19
dif20 = tra19 - tra20
dif21 = tra20 - tra21
dif22 = tra21 - tra22
dif23 = tra22 - tra23
dif24 = tra23 - tra24


print("Welcome to the bank webside. You can get it information about your loan here.")
input("Please give me your name: ")
print(f"\nTwoja pozostała rata kredytu w miesiącu: \n{mt1}: {tra1} \nTo: {dif1} mniej niż miesiąc temu.")
print(f"\nTwoja pozostała rata kredytu w miesiącu: \n{mt2}: {tra2} \nTo: {dif2} mniej niż miesiąc temu.")
print(f"\nTwoja pozostała rata kredytu w miesiącu: \n{mt3}: {tra3} \nTo: {dif3} mniej niż miesiąc temu.")
print(f"\nTwoja pozostała rata kredytu w miesiącu: \n{mt4}: {tra4} \nTo: {dif4} mniej niż miesiąc temu.")
print(f"\nTwoja pozostała rata kredytu w miesiącu: \n{mt5}: {tra5} \nTo: {dif5} mniej niż miesiąc temu.")
print(f"\nTwoja pozostała rata kredytu w miesiącu: \n{mt6}: {tra6} \nTo: {dif6} mniej niż miesiąc temu.")
print(f"\nTwoja pozostała rata kredytu w miesiącu: \n{mt7}: {tra7} \nTo: {dif7} mniej niż miesiąc temu.")
print(f"\nTwoja pozostała rata kredytu w miesiącu: \n{mt8}: {tra8} \nTo: {dif8} mniej niż miesiąc temu.")
print(f"\nTwoja pozostała rata kredytu w miesiącu: \n{mt9}: {tra9} \nTo: {dif9} mniej niż miesiąc temu.")
print(f"\nTwoja pozostała rata kredytu w miesiącu: \n{mt10}: {tra10} \nTo: {dif10} mniej niż miesiąc temu.")
print(f"\nTwoja pozostała rata kredytu w miesiącu: \n{mt11}: {tra11} \nTo: {dif11} mniej niż miesiąc temu.")
print(f"\nTwoja pozostała rata kredytu w miesiącu: \n{mt12}: {tra12} \nTo: {dif12} mniej niż miesiąc temu.")
print(f"\nTwoja pozostała rata kredytu w miesiącu: \n{mt1}: {tra13} \nTo: {dif13} mniej niż miesiąc temu.")
print(f"\nTwoja pozostała rata kredytu w miesiącu: \n{mt2}: {tra14} \nTo: {dif14} mniej niż miesiąc temu.")
print(f"\nTwoja pozostała rata kredytu w miesiącu: \n{mt3}: {tra15} \nTo: {dif15} mniej niż miesiąc temu.")
print(f"\nTwoja pozostała rata kredytu w miesiącu: \n{mt4}: {tra16} \nTo: {dif16} mniej niż miesiąc temu.")
print(f"\nTwoja pozostała rata kredytu w miesiącu: \n{mt5}: {tra17} \nTo: {dif17} mniej niż miesiąc temu.")
print(f"\nTwoja pozostała rata kredytu w miesiącu: \n{mt6}: {tra18} \nTo: {dif18} mniej niż miesiąc temu.")
print(f"\nTwoja pozostała rata kredytu w miesiącu: \n{mt7}: {tra19} \nTo: {dif19} mniej niż miesiąc temu.")
print(f"\nTwoja pozostała rata kredytu w miesiącu: \n{mt8}: {tra20} \nTo: {dif20} mniej niż miesiąc temu.")
print(f"\nTwoja pozostała rata kredytu w miesiącu: \n{mt9}: {tra21} \nTo: {dif21} mniej niż miesiąc temu.")
print(f"\nTwoja pozostała rata kredytu w miesiącu: \n{mt10}: {tra22} \nTo: {dif22} mniej niż miesiąc temu.")
print(f"\nTwoja pozostała rata kredytu w miesiącu: \n{mt11}: {tra23} \nTo: {dif23} mniej niż miesiąc temu.")
print(f"\nTwoja pozostała rata kredytu w miesiącu: \n{mt12}: {tra24} \nTo: {dif24} mniej niż miesiąc temu.")