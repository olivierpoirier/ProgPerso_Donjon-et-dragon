import random

listeBatiments = ["Grange", "tour", "maison abandonnée", "champ", "crâne géant", "cimetière", "chateau", "Arbre géant", "Moulin", "Village abandonné", "arbre mort", "charette abandonnée", "camp", "chaise", "corps", "feu éteint", "traces de pas", "ossments", "ruines", "ruisseau asséché", "individus", "fleur géante", "champignon géant", "pyramide", "caverne", "caverne", "squelette", "bande religieuse", "hallucination", "hallucination", "hallucination"]

listeingredients = ["bois", "lame", "bille", "pustule", "lêvre", "poil", "liquide", "gelée", "bière", "pain", "oeil", "ongles","gâteau", "lichen", "poisson", "viande", "patte", "aiguille", "blé", "poudre","métal","noix", "ficelle", "totem", "bâton", "sphère", "riz", "branche", "catalyseur" , "sceau", "champignon", "pleurotte", "rose", "tulipe", "tournesol", "racine", "crâne", "pierre", "baie", "fruit", "crystal", "plume", "dent", "croc", "griffe", "citrouille", "eau", "roche", "gemme", "sel", "graine", "patate", "feuille", "sang", "chair"]

listeArme = ["hache", "épée", "lance", "gourdin", "cimeterre", "dague", "flèche", "arbalète", "arc", "bouclier", "marteau de guerre", "bâton", "espadon", "pioche", "couteau", "ceste", "poings", "pique"]

listeAdjectif = ["attirante", "chaleureuse", "charmante", "enragé", "de rage","de mort", "de putréfaction", "de sang", "de cendre", "de sel", "de feu", "de peste", "de courage", "hallucinante", "de gel", "de soin", "de vie", "de jouvence", "de poison", "de vengeance", "luminescente", "trompeuse", "fortifiante", "de rapidité", "de rêve", "de chaleur", "de puanteur", "puant", "de lave", "magique", "de force", "de faiblesse", "d'amaigrissement", "de crystal", "de vision", "omniscient", "vivante", "tranchante", "de parole", "chantante", "de performance", "d'extinction", "de destruction", "de douceur", "calmante", "de calme", "de tuerie", "de fumée", "fumante", "de brouillard", "savoureuse", "hilarante", "piquante", "épicé", "de peur", "saignante", "brillante", "de sonorité", "musiscienne", "bruyante"]

listeSyllable = ["ba", "ca", "da", "fa", "ga", "ja", "la", "ma", "na", "pa", "ra", "sa", "ta", "va", "za", "bra", "cra", "dra", "fra", "gra", "pra", "tra", "vra", "bla", "cla", "fla", "gla","pla","cha","be", "de", "fe", "je", "le", "me", "ne", "pe", "re", "se", "te", "ve", "ze", "bre", "cre", "dre", "fre", "gre", "pre", "tre", "vre", "ble", "cle", "fle", "gle","ple","che","bi", "ci", "di", "fi", "gi", "ji", "li", "mi", "ni", "pi", "ri", "si", "ti", "vi", "zi", "bri", "cri", "dri", "fri", "gri", "pri", "tri", "vri", "bli", "cli", "fli", "gli","pli","chi","bo", "co", "do", "fo", "go", "jo", "lo", "mo", "no", "po", "ro", "so", "to", "vo", "zo", "bro", "cro", "dro", "fro", "gro", "pro", "tro", "vro", "blo", "clo", "flo", "glo","plo","cho","bu", "cu", "du", "fu", "gu", "ju", "lu", "mu", "nu", "pu", "ru", "su", "tu", "vu", "zu", "bru", "cru", "dru", "fru", "gru", "pru", "tru", "vru", "blu", "clu", "flu", "glu","plu","chu",]

listeChosesRetenues = ["Baies de cendre, gelée fortifiante", "bâton de vision", "blé de rage", "sphère de mort", "totem de vision", "catalyseur de soin", "catalyseur de crystal", "bière de brouillard", "crystal fumant", "métal fumant", "sceau enragé" ]

listeD1 = [1]
listeD2 = [1, 2]
listeD3 = [1, 2, 3]
listeD4 = [1, 2, 3, 4]
listeD6 = [1, 2, 3, 4, 5, 6]
listeD8 = [1, 2, 3, 4, 5, 6, 7, 8]
listeD10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listeD12 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
listeD20 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

syllable = syllableFinal = choix = ""
randomSyllable = [2,3,4,5]
fin = "pasFin"
game = "still active"


print("Bienvenue au programme d'aide de donjon et dragon\n\n")
while game == "still active" :

    print("\nVoici les programmes : ")
    print("[1] : Les joueurs trouvent un lieu random")
    print("[2] : Inventer des objets spéciaux à l'aide d'un objet et d'un adjectif")
    print("[3] : Inventer des objets à l'aide de seulement des syllables")
    print("[4] : Inventer des armes spéciales à l'aide d'un objet et d'un adjectif")
    print("[5] : Rouler des dés") 
    print("[6] : Fin du programme")
    choix = input("\nvotre choix : ")
    
    if choix == "1" :
        batiment = random.choice(listeBatiments)
        print(f"\n\nils trouveront un {batiment} ")

    elif choix == "2" :
        nombreFois = int(input("Entrez un nombre de fois pour créer des objets spéciaux : "))
        for indice in range(nombreFois) :
            ingredient = random.choice(listeingredients)
            adjectif = random.choice(listeAdjectif)
            print(f"[{indice + 1}] : {ingredient} {adjectif} ")

    elif choix == "3" :
        nombreFois = int(input("\nCombien de mots veux tu?\n"))             
        for indice1 in range(nombreFois) :
            nombreSyllable = random.choice(randomSyllable)
            for indice in range(nombreSyllable) :
                syllable = random.choice(listeSyllable)
                syllableFinal = syllableFinal + syllable
            print(f"[{indice1 + 1}] : {syllableFinal}")
            syllableFinal = ""

    elif choix == "4" :
        nombreFois = int(input("Entrez un nombre de fois pour créer des armes spéciales : "))
        for indice in range(nombreFois) :
            arme = random.choice(listeArme)
            adjectif = random.choice(listeAdjectif)
            print(f"[{indice + 1}] : {arme} {adjectif} ")

    elif choix == "5" :
        print("\nVoici les dés : ")
        print("[1] : Dé 1")
        print("[2] : Dé 2")
        print("[3] : Dé 3")
        print("[4] : Dé 4")
        print("[6] : Dé 6")
        print("[8] : Dé 8")
        print("[10] : Dé 10")
        print("[12] : Dé 12")
        print("[20] : Dé 20")
        choixDe = input("\nVotre choix : ")

        if choixDe == "1" :
            de = random.choice(listeD1)
            print(de)
        elif choixDe == "2" :
            de = random.choice(listeD2)
            print(de)
        elif choixDe == "3" :
            de = random.choice(listeD3)
            print(de)
        elif choixDe == "4" :
            de = random.choice(listeD4)
            print(de)
        elif choixDe == "6" :
            de = random.choice(listeD6)
            print(de)
        elif choixDe == "8" :
            de = random.choice(listeD8)
            print(de)
        elif choixDe == "10" :
            de = random.choice(listeD10)
            print(de)
        elif choixDe == "12" :
            de = random.choice(listeD12)
            print(de)
        elif choixDe == "20" :
            de = random.choice(listeD20)
            print(de)

    elif choix == "6" :
        game = "end"
        print("Bonne soirée")
        print("****Fin du programme****")

    else :
        print("Erreur")

#mots retenus :
        
#litosme =
#lilioupa = 
#malichou =
#takel = 
#keltama =
#tumati =
#mesasa = 
#tarbourge =
#potimatar = 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
