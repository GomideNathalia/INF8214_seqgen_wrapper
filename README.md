# INF8214_TP1

Ce programme permet de créer un objet pour encapsuler le programme Seq-Gen

Auteures:   Fatima Mawassi,
            Mathura Kanapathippillai,
            Nathalia Gomide Cruz 

Date: 14/02/2024

Cours: INF8214 Hiver 2024

## Utilisation de RunProg.py
RunProg.py est une classe Python qui permet de prendre en paramètre le chemin d'un fichier de configuration contenant toutes les informations nécessaires pour bâtir une commande d'execution du programme Seq-Gen. Elle fait aussi une validation des paramètres fournis dans le fichier de configuration qui permet de quitter le programme dans la présence d'un mauvais paramètre. 

RunProg offre les fonctionalités décrites en bas suivantes: run(), status(), reset(), view() et read()

Un exemple d’utilisation peut être trouvé dans le fichier tester.py

Référence à Seq-Gen:

Rambaut, A. and Grassly, N. C. (1997) Seq-Gen: An application for the Monte Carlo simulation of DNA sequence evolution along phylogenetic trees. _Comput. Appl. Biosci._ **13**: 235-238.

## Étapes préalables à l'utilisation de RunProg
- Il faut visiter la [documentation de Seq-Gen](https://snoweye.github.io/phyclust/document/Seq-Gen.v.1.3.2/Seq-Gen.Manual.html) pour le guide d'utilsation de celui-ci et des informations supplémentaires.
- Il faut avoir un fichier de configuration suivant le format ci-dessous.
  - Chaque ligne correspond à un seul paramètre et il ne doit pas avoir de lignes vides.
  - Le fichier doit contenir: _infile=[chemin du fichier d'entrée]_ et _outfile=[chemin du fichier de sortie]_
  - Si aucun _outfile_ est fourni, _output.txt_ sera généré par défaut.
  - Le fichier doit contenir au moins un [parameters](https://snoweye.github.io/phyclust/document/Seq-Gen.v.1.3.2/Seq-Gen.Manual.html) Seq-Gen valide de la liste suivante: ['-m','-l','-n','-p','-s','-d','-c','-a', '-g','-i','-f','-t','-r','-k','-z','-x','-fe','-op','-or','-on','-wa','-wr','-q','-h']
```
infile=example.tree
outfile=output.txt
l=1000
m=HKY
```
- Les paramètres dans le fichier de configuration permet de construire une commande d'exécution de Seq-Gen similaire à celui-ci:
```
./seq-gen -mHKY -l1000 <example.tree> output.txt
```
- Le fichier du program seq-gen doit être dans le même dossier que RunProg.py. Le chemin du fichier  est: ./seq-gen

## Fonctions

### \_\_init\_\_(self, paramsFile): [RunProg.py]
Constructeur de la classe, prend en paramètre le chemin à un fichier de configuration (type string).

### \_\_parametresValides\_\_(self): [RunProg.py]
Valide les paramètres dans le fichier de configuration avant de rouler seq-gen.

- Si aucun \[parameters\] Seq-Gen ou un \[parameters\] invalide est fourni, le programme quittera en affichant un message d'erreur indiquant le paramètre fautif.
- Chaque paramètre et sa valeur associé est validé par la fonction importée _validerConfig(parametres)_

### run(self): [RunProg.py]
Lance l'exécution non bloquante de Seq-Gen. Il génère deux fichiers dans le même dossier que RunProg.py:
- un fichier de sortie de Seq-Gen précisé par _outfile=[chemin du fichier de sortie]_
- un fichier log de Seq-Gen avec l'affichage généré par Seq-Gen: _seqgen.log_

### status(self): [RunProg.py]
Retourne le status d'exécution: 

(0) non commencée 

(1) en cours 

(2) terminée avec succès 

(3) terminée avec un échec

### reset (self): [RunProg.py]
Interrompe l'exécution du programme

### view (self): [RunProg.py]
Retourne la liste des fichiers générés (type liste).

### read (self, fichier): [RunProg.py]
Retourne le contenu du fichier (s'il existe). Il prend en paramètre le chemin du fichier (type string) tel que affiché par _view()_.

### extraireParametres(paramFile): [genereCommande.py]
Crée un dictionaire des paramètres à partir du fichier de configuration.

### genereCommande(parametres): [genereCommande.py]
Génère la ligne de commande pour seq-gen à partir des paramètres extraits.

```
./seq-gen -mHKY -l1000 <example.tree> output.txt
```

### validerConfig(parametres): [validation.py]
Valide les paramètres extraits. Si l'un des paramètres fournis est mauvais, un message d'erreur s'affiche et le programme s'arrête. Les conditions de validité pour chaque paramètre se retrouve dans la [documentation de Seq-Gen](https://snoweye.github.io/phyclust/document/Seq-Gen.v.1.3.2/Seq-Gen.Manual.html).

Par exemple: dans le paramètre _g=18_, 18 doit être un entier entre 2 et 32.

# INF8214_seqgen_wrapper
