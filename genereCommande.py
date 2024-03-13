# Chaque ligne est séparé en key,value
def parLine(line):
    if '=' in line:
        key, value = map(str.strip, line.split('='))
        return key, value
    else:
        return line.strip(), None

# Crée un dictionaire de key,value des paramètres dans paramFile (fichier de configuration)
def extraireParametres(paramFile):
    parametres = {}
    with open(paramFile, 'r') as f:
        #case for empty paramFile
        for line in f:
            key,value = parLine(line)
            if key != "infile" and key != "outfile":
                key = "-"+key
            parametres[key] = value
    return parametres

# Génère la ligne de commande pour seq-gen
def genereCommande(parametres):
    commande = './seq-gen'
    for key,value in parametres.items():
        if key.startswith('-') and value != None:
            commande += f" {key}{value}"
        if key.startswith('-') and value == None:
            commande += f" {key}"
    commande += f" <{parametres['infile']}> {parametres['outfile']}"
    return commande