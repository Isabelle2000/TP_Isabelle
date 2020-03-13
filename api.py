import requests
import json


def lister_parties(idul):
    """ 
    Quest-ce que fais ma fonction? La fonction permet de lister les parties
    Quels sont les paramètres en entré de ma fonction? Un idul
    Quelle est la sortie et/ou le retour de ma fonction? Permet de sortir le dictionnaire
    """
    url_lister = 'https://python.gel.ulaval.ca/quoridor/api/lister/'
    rep = requests.get(url_lister, params={'idul': 'islev54'})
    if rep.status_code == 200:
        rep = rep.text
        json_var = json.loads(rep)
        json_str = json.dumps(json_var, indent=2)
        print(json_str)    
    else:
        print("Le GET sur '{}' a produit le code d'erreur {}.".format(
            url_lister, rep.status_code)
        )

lister_parties('islev54')
