import requests
import json


def lister_parties(idul):
    """ 
    Quest-ce que fais ma fonction? La fonction permet de lister les parties
    Quels sont les paramètres en entré de ma fonction? Un idul
    Quelle est la sortie et/ou le retour de ma fonction? Permet de sortir le dictionnaire
    """
    url_lister = 'https://python.gel.ulaval.ca/quoridor/api/lister/'
    rep = requests.get(url_lister, params={'idul': idul})
    if rep.status_code == 200:
        rep = rep.text
        json_var = json.loads(rep)
        json_str = json.dumps(json_var, indent=2)
        print(json_str)    
    else:
        print("Le GET sur '{}' a produit le code d'erreur {}.".format(
            url_lister, rep.status_code)
        )

def initialiser_parties(idul):
    """ 
    Quest-ce que fais ma fonction? La fonction permet de débuter la partie
    Quels sont les paramètres en entré de ma fonction? Un idul
    Quelle est la sortie et/ou le retour de ma fonction? Permet de sortir un tuple constitué 
    de l'identifiant de la partie et de l'état initial du jeu
    """
    url_initialiser = 'https://python.gel.ulaval.ca/quoridor/api/initialiser/'
    try:
        rep = requests.post(url_initialiser, data={'idul': idul})
        if rep.status_code == 200:
            json_rep = rep.json()
            return json_rep['id'], json_rep['état']
        else:
            print("Le GET sur '{}' a produit le code d'erreur {}.".format(
                url_initialiser, rep.status_code)
            )
    except RuntimeError as error:
        print(error)

def jouer_coup(id_partie, type_coup, position):
    url_coup = 'https://python.gel.ulaval.ca/quoridor/api/jouer/'
    try:
        rep = requests.post(url_coup, data={'id': id_partie, 'type': type_coup, 'pos': position})
        if rep.status_code == 200:
            json_rep = rep.json()
            if 'gagnant' in json_res:
                raise StopIteration(json__rep['gagnant'])
            else:
                return json_rep
        else:
            print("Le POST sur '{}' a produit le code d'erreur {}.".format(
                url_coup, rep.status_code)
            )
    except RuntimeError as error:
        print(error)
