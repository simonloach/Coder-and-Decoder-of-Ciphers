# -----------------------
# CODE BY SZYMON PISKORZ
# 10.03.2020
# -----------------------


import random
import os
import shutil

try:
    os.chdir(os.getcwd() + "/pliki/")
except:
    os.mkdir("pliki")
    print("Wygenerowano folder 'pliki'")
    os.chdir(os.getcwd() + "/pliki/")


def main():
    try:
        startowy = open("input.txt", "w")
        print("Tworze plik 'input.txt'")
        startowy.write("TUTAJ WPISZ SWOJĄ WIADOMOSC")
        startowy.close()
    except:
        pass
    userChoice = 0
    while userChoice != 4:
        print(
            "\nWybierz co chcesz zrobic: \n1.Wygenerowac koda na podstawie pliku 'probabilities.txt'\n2.Zakodowac wiadomosc zawarta w pliku 'input.txt' do pliku 'outputCoded.txt'\n3.Rozkodowac plik 'outputCoded.txt' do pliku 'outputDecoded.txt'. \n4.Wyjsc z programu.\n    Wpisz poprostu int'a.")
        userChoice = int(input())
        if userChoice == 1:
            generowanie()
        if userChoice == 2:
            kodowanie()
        if userChoice == 3:
            dekodowanie()
        if userChoice == 4:
            shutil.rmtree(os.getcwd())


def generowanie():
    dictionary = {}
    alphabet = [['a', 8167], ['b', 1492], ['c', 2202], ['d', 4253], ['e', 12702], ['f', 2228], ['g', 2015], ['h', 6094],
                ['i', 6966], ['j', 153], ['k', 1292], ['l', 4025], ['m', 2406], ['n', 6749], ['o', 7507], ['p', 1929],
                ['q', 95], ['r', 5987], ['s', 6327], ['t', 9356], ['u', 2758], ['v', 978], ['w', 2560], ['x', 150],
                ['y', 1994], ['z', 77]]
    sum = 0
    print("Lista prawdopodobienstw: \n")
    for el in alphabet:
        sum += el[1]
        print(str(el[0]) + " " + str(el[1] / 1000) + "%")
    print("Wykorzystano liczb:", sum)
    a = ([x for x in range(100000, 100000 + sum)])
    print("Starting to generate pseudorandom code... (This can take a 1-2 minutes)")
    for object in alphabet:
        lista = []
        for i in range(object[1]):
            try:
                item = random.choice(a)
                a.pop(a.index(item))
                lista.append(item)
            except:
                pass
        dictionary[object[0]] = lista
    f = open("wyniki.csv", 'w')
    for key in dictionary.keys():
        f.write(str(key) + "," + str(dictionary[key]).replace("[", "").replace("]", "") + "\n")
    f.close()
    print("Finished generating the code!\n\n")


def kodowanie():
    print(
        "Wybierz czy chcesz uzyc inputu z pliku (zalecane do duzej ilosci znakow) czy wpisac do konsoli: \na. z pliku\nb. z konsoli")
    variable = input()
    if variable == 'a':
        toCode = str(open("input.txt", 'r').read()).replace("\n", "")
    if variable == 'b':
        print("Wprowadz swoj tekst:\n")
        toCode = input().replace("\n", "")
    for x in range(65):
        if x != 32:
            toCode = toCode.replace(chr(x), "")
    for x in range(91, 97):
        toCode = toCode.replace(chr(x), "")
    for x in range(123, 255):
        toCode = toCode.replace(chr(x), "")
    toCodeList = toCode.lower().split(" ")
    slownik = {}
    wynik = ""
    try:
        f = open("wyniki.csv", "r")
    except:
        "Couldnt open file wyniki.csv"
    for line in f:
        lista = line.split(",")
        slownik[str(lista[0])] = lista[1:len(lista) - 1]
    for word in toCodeList:
        if len(word) > 0:
            for litera in word:
                wynik += random.choice(slownik[litera]).replace(" ", "")
            wynik += "  "
    with open("outputCoded.txt", 'w') as f2:
        f2.write(wynik)
        f2.close()
    f.close()
    print("Finished coding your message!\n\n")


def dekodowanie():
    f = open("wyniki.csv", 'r')
    f = f.read().split("\n")
    afterSplitting = []
    slownik = {}
    output = ""
    splitToLetters = []
    for el in f:
        el = el.split(",")
        for x in range(len(el) - 1):
            slownik[el[x + 1].replace(" ", "")] = el[0]
    print(slownik)
    slownik[" "] = " "
    toDecode = open("outputCoded.txt", 'r').read().split(" ")
    for word in toDecode:
        if len(word) > 0:
            afterSplitting.append(word)
    for word in afterSplitting:
        for x in range(int(len(word) / 6)):
            splitToLetters.append(word[0 + 6 * x:6 + 6 * x])
        splitToLetters.append(" ")

    for element in splitToLetters:
        output += slownik[str(element)]

    with open("outputDecoded.txt", 'w') as file:
        file.write(output)
        file.close()
    print("Finished decoding your message!\n\n")


main()
