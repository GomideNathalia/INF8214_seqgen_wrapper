import subprocess
import os
import sys
from genereCommande import genereCommande
from genereCommande import extraireParametres
from validation import validerConfig

# Classe pour manipuler le programme seqgen
class RunProg:
    # Constructeur de la classe, prend en paramètre un fichier de configuration 
    def __init__(self, paramsFile):
        self.__processus = None
        self.__paramsFile = paramsFile
        self.__parametresValides__()

    # Valide les paramètres dans le fichier de configuration
    def __parametresValides__(self):
        if os.path.exists(self.__paramsFile) and any(caractere.isalnum() for caractere in self.__paramsFile):
            validerConfig(extraireParametres(self.__paramsFile))
        else:
            print(f"Fichier de configuration: {self.__paramsFile} n'existe pas ou est un format de nom de fichier invalide.")
            sys.exit(0)
        return 
    
    # Lance l'exécution non bloquante de seqgen
    def run(self):
        commande = genereCommande(extraireParametres(self.__paramsFile))

        log_file = open('seqgen.log', 'w')
        self.__processus = subprocess.Popen([commande], shell = True, stdout = log_file, stderr = log_file)

    # Retourne le status d'exécution: 
    # (0) non commencée/ 
    # (1) en cours/ 
    # (2) terminée avec succès/ 
    # (3) terminée avec un échec
    def status(self): 
        if self.__processus == None:
            return 0
        
        if self.__processus.poll() == None:
            return 1
        
        if self.__processus.poll() == 0:
            return 2
        
        return 3
    
    # Interrompe l'exécution
    def reset (self):
        self.__processus.kill()
        self.__processus = None

    # Retourne la liste des fichiers générés
    def view (self):
        parametres = extraireParametres(self.__paramsFile)
        ListeFichiers = [parametres['outfile'], "seqgen.log"]
        return ListeFichiers

    
    # Retourne le contenu du fichier (s'il existe) 
    def read (self, fichier):
        fichier_path = os.path.exists(fichier)
    
        if fichier_path:
         
         with open(fichier, "r") as openFichier:
          return openFichier.read()
      
        else: 
         return  " le fichier spécifié n'existe pas ."
