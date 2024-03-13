# Nom: validation.py
# Description: Ce fichier sert à la validation des paramètres fournis dans le fichier de configuration.
# Si un des paramètres fournis est mauvais, un message d'erreur s'affiche et le programme s'arrête.
# Il est importé dans la classe RunProg.py 
# Date: 14/02/2024
# Version: 1.0
# -------------------------------------------------------------------------------------------------------

import sys
import re
import os

def quitterProgramme(message):
    print(message)
    sys.exit(0)

# Fichier de configuration doit contenir:
# - infile
# - au moins 1 [parameters] de seq-gen
# - outfile (output.txt sera utilisé par défaut si il n'est pas fourni)
def filePresent(parametres):
    if 'infile' not in parametres:
        quitterProgramme(f"Paramètre 'infile' n'est pas fourni dasn le fichier de configuration.\nProgramme a quitté")
    if 'outfile' not in parametres:
        parametres['outfile'] = 'output.txt'
    if not any(key in parametres for key in ['-m','-l','-n','-p','-s','-d','-c','-a', '-g','-i','-f','-t','-r','-k','-z','-x','-fe','-op','-or','-on','-wa','-wr','-q','-h']):
        quitterProgramme(f"Aucun [parameters] fourni dans le fichier de configuration.\nProgramme a quitté.")
    return parametres

def modelValide(value):
    model = ['HKY','F84','GTR','JTT','WAG','PAM','BLOSUM','MTREV','CPREV','GENERAL','REV']
    if value not in model:
        quitterProgramme(f"Paramètre -m{value} ne contient pas un modèle valide.\nProgramme a quitté.")
    return

def estEntier(key,value):
    if key == '-g':
        if not value.isdigit() or not 2 <= float(value) <= 32:
            quitterProgramme(f"Paramètre -g{value} invalide. NUM_CATEGORIES doit être un entier entre 2 et 32.\nProgramme a quitté.")
    else:
        if not value.isdigit() or float(value) <= 0:
            quitterProgramme(f"Paramètre {key}{value} invalide. Il doit être un entier > 0.\nProgramme a quitté.")
    return

def estDecimal(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def estDecimalPos(key,value):
    if estDecimal(value):
        if float(value) <= 0:
            quitterProgramme(f"Paramètre {key}{value} invalide. Il doit être un décimal > 0.\nProgramme a quitté.")
    else:
        quitterProgramme(f"Paramètre {key}{value} invalide. Il doit être un décimal > 0.\nProgramme a quitté.")
    return

def estProportionInvariable(value):
    if estDecimal(value):
        if not 0.0 <= float(value) < 1.0:
            quitterProgramme(f"Paramètre -i{value} invalide. Il doit être un décimal [0.0, 1.0[.\nProgramme a quitté.")
    else:
       quitterProgramme(f"Paramètre -i{value} invalide. Il doit être un décimal [0.0, 1.0[.\nProgramme a quitté.") 
    return

def estDecimalRepete(key,value):
    if ',' in value or ' ' in value:
        valeurs = re.split(r'[,\s]+',value)
    else:
        quitterProgramme(f"Paramètre {key}{value} invalide. Il doit être une série de nombres décimaux > 0 séparée par des espaces ou virgules.\nProgramme a quitté.")
    for i in range(len(valeurs)):
        if estDecimal(valeurs[i]) and float(valeurs[i]) <= 0:
            quitterProgramme(f"Paramètre {key}{value} invalide. Il doit être une série de nombres décimaux > 0 séparée par des espaces ou virgules.\nProgramme a quitté.")
        if estDecimal(valeurs[i]) == False:
            quitterProgramme(f"Paramètre {key}{value} invalide. Il doit être une série de nombres décimaux > 0 séparée par des espaces ou virgules.\nProgramme a quitté.")
        return

def estString(value):
    if value == "" or not any(caractere.isalnum() for caractere in value):
        quitterProgramme(f"Paramètre -x{value} invalide. Il doit être une chaîne de caractère.\nProgramme a quitté.")
    return

# Pour vérifier tous les paramètres qui contiennent soi des entiers ou décimaux
def nombreValide(key,value):
    if key in ['-l','-n','-p','-k','-z','-g']:
        estEntier(key,value)
    if key in ['-a','-s','-d','-t']:
        estDecimalPos(key,value)
    if key in ['-c','-f','-r']:
        estDecimalRepete(key,value)
    return

# Pour vérifier les premiers paramètres avant '<infile> outfile'
def premierParamValide(key,value):
    if key == '-m':
        modelValide(value)
    if key in ['-l','-n','-p','-k','-z','-g','-a','-s','-d','-t','-c','-f','-r']:
        nombreValide(key, value)
    if key == '-i':
        estProportionInvariable(value)
    if key == '-x':
        estString(value)
    return

# Vérifie que infile existe et outfile est un nom de fichier qui contient au moins un caractère alphanumérique.
def fileValide(key,value):
    if key == 'infile':
        if not os.path.exists(value):
            quitterProgramme(f"Infile '{value}' n'existe pas.\nProgramme a quitté.")
    else:
        if any(caractere.isalnum() for caractere in value):
            return
        else:
            quitterProgramme(f"Outfile '{value}' format invalide.\nProgramme a quitté.")
    return

# Appeler dans RunProg.py pour la validation des paramètres.
def validerConfig(parametres):
    parametres = filePresent(parametres)
    for key,value in parametres.items():
        if key in ['-m','-l','-n','-p','-s','-d','-c','-a', '-g','-i','-f','-t','-r','-k','-z','-x','-fe','-op','-or','-on','-wa','-wr','-q','-h']:
            premierParamValide(key,value)
        elif key in ['infile','outfile']:
            fileValide(key,value)
        else:
            quitterProgramme(f"{key}{value} n'est pas un paramètre valide.\nProgramme a quitté.")
    return