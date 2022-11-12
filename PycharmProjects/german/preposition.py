from random import randrange

def pronouns(num):
    Arr = [["Nominatiivi", "y. 1. p.", "ich"],
           ["Nominatiivi", "y. 2. p.", "du"],
           ["Nominatiivi", "y. 3. p. m.", "er"],
           ["Nominatiivi", "y. 3. p. f.", "sie"],
           ["Nominatiivi", "y. 3. p. n.", "es"],
           ["Nominatiivi", "m. 1. p.", "wir"],
           ["Nominatiivi", "m. 2. p.", "ihr"],
           ["Nominatiivi", "m. 3. p.", "sie"],
           ["Nominatiivi", "teitittely", "Sie"],
           ["Akkusatiivi", "y. 1. p.", "mich"],
           ["Akkusatiivi", "y. 2. p.", "dich"],
           ["Akkusatiivi", "y. 3. p. m.", "ihn"],
           ["Akkusatiivi", "y. 3. p. f.", "sie"],
           ["Akkusatiivi", "y. 3. p. n.", "es"],
           ["Akkusatiivi", "m. 1. p.", "uns"],
           ["Akkusatiivi", "m. 2. p.", "euch"],
           ["Akkusatiivi", "m. 3. p.", "sie"],
           ["Akkusatiivi", "teitittely", "Sie"],
           ["Datiivi", "y. 1. p.", "mir"],
           ["Datiivi", "y. 2. p.", "dir"],
           ["Datiivi", "y. 3. p. m.", "ihm"],
           ["Datiivi", "y. 3. p. f.", "ihr"],
           ["Datiivi", "y. 3. p. n.", "ihm"],
           ["Datiivi", "m. 1. p.", "uns"],
           ["Datiivi", "m. 2. p.", "euch"],
           ["Datiivi", "m. 3. p.", "ihnen"],
           ["Datiivi", "teitittely", "Ihnen"]]
    return Arr[num]

def articles(case):
    Arr =  [["Nominatiivi", "Mask.", "ein", "der"],
            ["Nominatiivi", "Fem.", "eine", "die"],
            ["Nominatiivi", "Neutri", "ein", "das"],
            ["Nominatiivi", "Mon.", "-", "die"],
            ["Akkusatiivi", "Mask.", "einen", "den"],
            ["Akkusatiivi","Fem.", "eine", "die"],
            ["Akkusatiivi", "Neutri", "ein", "das"],
            ["Akkusatiivi", "Mon.", "-", "die"],
            ["Datiivi", "Mask.", "einem", "dem"],
            ["Datiivi","Fem.", "einer", "der"],
            ["Datiivi", "Neutri", "einem", "dem"],
            ["Datiivi", "Mon.", "-+n", "den + n"],
            ["Genetiivi", "Mask.", "eines + s", "des + s"],
            ["Genetiivi","Fem.", "einer", "der"],
            ["Genetiivi", "Neutri", "eines + s", "des + s"],
            ["Genetiivi", "Mon.", "-", "der"]]
    return Arr[case]

def prepositions(first):
    Arr = [["durch", "läpi, kautta, halki", "akkusatiivi"],
           ["für", "jonkin puolesta", "akkusatiivi"],
           ["gegen", "vastaan, vasten", "akkusatiivi"],
           ["ohne", "ilman", "akkusatiivi"],
           ["um(herum)", "ympäri, ympärillä, ympärille", "akkusatiivi"],
           ["aus", "jostakin", "datiivi"],
           ["bei", "jonkun luona", "datiivi"],
           ["mit", "kanssa", "datiivi"],
           ["nach", "jälkeen; johonkin", "datiivi"],
           ["seit", "jostakin lähtien", "datiivi"],
           ["von", "jostakin", "datiivi"],
           ["zu", "johonkin, jonkin luokse", "datiivi"],
           ["gegenüber", "jotakin vastapäätä", "datiivi"],
           ["dank", "jonkun/jonkin ansiosta", "datiivi"],
           ["an", "äärellä, äärelle", "jompi kumpi"],
           ["auf", "päällä, päälle", "jompi kumpi"],
           ["hinter", "takana, taakse", "jompi kumpi"],
           ["in", "sisällä, sisälle", "jompi kumpi"],
           ["neben", "vieressä, viereen", "jompi kumpi"],
           ["über", "yllä, ylle", "jompi kumpi"],
           ["unter", "alla, alle", "jompi kumpi"],
           ["vor", "edessä, eteen", "jompi kumpi"],
           ["zwischen", "välissä, väliin", "jompi kumpi"],
           ["während", "jonkun aikana", "genetiivi"],
           ["wegen", "jonkun takia", "genetiivi"],
           ["aufgrund", "jonkun vuoksi, takia", "genetiivi"]]
    return (Arr[first])

def randomwords(wort):
    wortarray = wort.split("// ");
    wortarray[1] = wortarray[1][:-1]
    return wortarray

def reviewwords(answer, correct, second):
    if answer == correct[abs(second-1)]:
        return "Oikein"
    return "Väärin, oikein olisi ollut " + str(correct[abs(second-1)])

def review(answer, first, second):
    if answer == prepositions(first)[abs(1-second)]:
        return "Oikein!"
    return "Väärin, oikein olisi ollut " + str(prepositions(first)[abs(1-second)])

def reviewpronouns(answer, fourth):
    if answer == pronouns(fourth)[2]:
        return "Oikein!"
    return "Väärin, oikein olisi ollut " + str(pronouns(fourth)[2])

def reviewcase(answer, first):
    if answer == prepositions(first)[2]:
        return "Oikein!"
    return "Väärin, oikein olisi ollut " +  str(prepositions(first)[2])


def reviewarticles(answer,third):
    correctanswer = articles(third)
    if (answer[0] == correctanswer[2] and answer[1] == correctanswer[3]):
        return "Molemmat oikein!"
    elif (answer[0] == correctanswer[2] and answer[1] != correctanswer[3]):
        return "Epämääräinen artikkeli oikein, määräinen artikkeli olisi ollut " + str(correctanswer[3])
    elif (answer[0] != correctanswer[2] and answer[1] == correctanswer[3]):
        return "Epämääräinen olisi ollut " + str(correctanswer[2] + " määräinen artikkeli oikein")
    return "Väärin, epämääräinen artikkeli olisi ollut " + str(correctanswer[2] + " ja määräinen artikkeli olisi ollut " + correctanswer[3])


var = " "
var2 = []
words = open("words.txt", "r")
wordarray = words.readlines()
verbs = open("verbs.txt")
verbarray = verbs.readlines()
others = open("others.txt")
othersarray = others.readlines()

while (var != ""):
    var2 = []
    first = randrange(26)
    second = randrange(2)
    third = randrange(16)
    fourth = randrange(27)


    var = input(str(prepositions(first)[second]) + ": ")
    print(review(var, first, second))

    var = input("Ja sijamuoto tämän sana jälkeen: ")
    print(reviewcase(var, first))

    var2.append(input(str(articles(third)[0] + " " + str(articles(third)[1]) + " epämääräinen artikkeli: ")))
    var2.append(input("Ja määräinen artikkeli: "))
    print(reviewarticles(var2, third))

    var = input(str(pronouns(fourth)[0]) + " " + str(pronouns(fourth)[1]) + ": ")
    print(reviewpronouns(var, fourth))

    for i in range(100):
        fifth = randrange(50)
        sixth = randrange(2)
        splittedword = randomwords(wordarray[fifth])
        var = input(str(splittedword[sixth]) + ": ")
        print(reviewwords(var, splittedword, sixth))

        seventh = randrange(100)
        splittedword = randomwords(verbarray[seventh])
        var = input(str(splittedword[sixth]) + ": ")
        print(reviewwords(var, splittedword, sixth))
        for j in range(3):
            seventh = randrange(312)
            sixth = randrange(2)
            splittedword = randomwords(othersarray[seventh])
            var = input(str(splittedword[sixth]) + ": ")
            print(reviewwords(var, splittedword, sixth))

    print(" ")










