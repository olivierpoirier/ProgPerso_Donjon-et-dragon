def calculePieces (monnaieNombre):
    nombreGold = int(monnaieNombre / 100)
    nombreSilver = int((monnaieNombre - (nombreGold * 100)) / 10)
    nombreCopper = int(monnaieNombre - (nombreGold * 100 + nombreSilver * 10))
    return nombreGold,nombreSilver,nombreCopper


print("\n//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n")

print("\t\tBienvenue au calculateur de monnaie de donjon et dragon!\n")

print("//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n")



nombreGold = int(input("Veuillez entrer votre nombre de Gold : "))
nombreSilver = int(input("Veuillez entrer votre nombre de Silver : "))
nombreCopper = int(input("Veuillez entrer votre nombre de Copper : "))
affichageMonnaie = "\nVous avez {} Gold, {} Silver et {} Copper."
messageAjout = "\nVous avez sélectionné l'ajout de {} ."
messageSupprime = "\nVous avez sélectionné la suppression de {} ."
messageAjoutCalcul = "\nVeuillez entrer le nombre de {} que vous voulez ajouter : "
messageSupprimeCalcul = "\nVeuillez entrer le nombre de {} que vous devez supprimer : "
messageErreur = "\nVous avez entré un nombre invalide de pièces. Veuillez réessayer."
nombreModificateur = 0
calculMonnaie = 0
choix = "1"

while choix != "F" :

    if choix >= "1" and choix <= "6":
        monnaieNombre =  nombreGold * 100 + nombreSilver * 10 + nombreCopper 
        nombreGold,nombreSilver,nombreCopper=calculePieces (monnaieNombre)
        
        print(affichageMonnaie.format(nombreGold,nombreSilver,nombreCopper))


    print("Voici les choix des programmes : \n\n")
    print("[1] Ajouter des pièces de Gold")
    print("[2] Supprimer des pièces de Gold")
    print("[3] Ajouter des pièces de Silver")
    print("[4] Supprimer des pièces de Silver")
    print("[5] Ajouter des pièces de Copper")
    print("[6] Supprimer des pièces de Copper")
    print("[F] Pour quitter le programme")

    choix = input("\nVeuillez entrez votre choix : ")

    if choix == "1" :
        print(messageAjout.format("Gold"))
        nombreModificateur = int(input(messageAjoutCalcul.format("Gold")))
        nombreGold = nombreGold + nombreModificateur
        
    elif choix == "3" :
        print(messageAjout.format("Silver"))
        nombreModificateur = int(input(messageAjoutCalcul.format("Silver")))
        nombreSilver = nombreSilver + nombreModificateur
        
    elif choix == "5" :
        print(messageAjout.format("Copper"))
        nombreModificateur = int(input(messageAjoutCalcul.format("Copper")))
        nombreCopper = nombreCopper + nombreModificateur


    
    elif choix == "2" :
        print(messageSupprime.format("Gold"))
        nombreModificateur = int(input(messageSupprimeCalcul.format("Gold")))
        if nombreGold < nombreModificateur :
            print(messageErreur)
        else :
            nombreGold = nombreGold - nombreModificateur
            
    elif choix == "4" :
        print(messageSupprime.format("Silver"))
        nombreModificateur = int(input(messageSupprimeCalcul.format("Silver")))
        if nombreGold*10 + nombreSilver <  nombreModificateur :
            print(messageErreur)
        else:
            nombreSilver = (nombreGold*10 + nombreSilver) - nombreModificateur
            nombreGold=0
        
    elif choix == "6" :
        print(messageSupprime.format("Copper"))
        nombreModificateur = int(input(messageSupprimeCalcul.format("Copper")))
        if nombreGold*100 + nombreSilver*10 + nombreCopper <  nombreModificateur :
            print(messageErreur)
        else:
            nombreCopper = (nombreGold*100 + nombreSilver*10 + nombreCopper) - nombreModificateur
            nombreGold=nombreSilver=0
        
    elif choix == "F" :
        print("**** Fin de Programme ****")

    else :
        print("Vous n'avez pas entré une entrée valide. Veuillez réessayer.")
            

