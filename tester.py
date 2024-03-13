from RunProg import RunProg


monRunProg = RunProg("config.txt")
print("0: quitter\n1: run\n2: status\n3: reset\n4: view\n5: read")
choix = ""

while choix != "0":
    choix = input("\nChoix:")

    if choix == "1":
        monRunProg.run()
    elif choix == "2":
        print(f"status: {monRunProg.status()}")
    elif choix == "3":
        monRunProg.reset()
    elif choix == "4":
        print(f"Fichiers générés: {monRunProg.view()}")
    elif choix == "5":
        fichier = input("Choisi un fichier: ")
        print(f"Contenu du fichier: {monRunProg.read(fichier)}")
    elif choix == "0":
        break
    else:
       print("choix invalide.") 
