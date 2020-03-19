import json
import requests


def lister_parties(idul):
    """
    La fonction permet de lister les parties en ayant comme entrée un idul
    et affiche le dictionnaire ayant pour clé
    les parties jouées listées (max 20) et un message en cas d'erreur
    """
    url_lister = 'https://python.gel.ulaval.ca/quoridor/api/lister/'
    try:
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
    except RuntimeError as error:
        print(error)

def initialiser_parties(idul):
    """
    La fonction permet de débuter la partie en ayant comme entrée un idul
    et dont la sortie est un tuple constitué de l'identifiant de la partie
     et de l'état initial du jeu.
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
    """
    La fonction permet de jouer un coup, c'est-à-dire de déplacer son pion sur une case adjacente
    en ayant comme entrée l'identifiant de la partie, le type de coup, soit un déplacement, un ajout
    de mur horizontal ou vertical et la position, soit du mur ou de la case
    où on veut déplacer le pion. La sortie retourne un dictionnaire soit de 3 clés:
    l'état, un message et le gagnant ou: d'un message dans la réponse en cas d'erreur.
    """
    url_coup = 'https://python.gel.ulaval.ca/quoridor/api/jouer/'
    try:
        rep = requests.post(url_coup, data={'id': id_partie, 'type': type_coup, 'pos': position})
        if rep.status_code == 200:
            json_rep = rep.json()
            if 'gagnant' in json_rep:
                raise StopIteration(json__rep['gagnant'])
            elif 'message' in json_rep:
                print(json_rep['message'])
            else:
                return json_rep
        else:
            print("Le POST sur '{}' a produit le code d'erreur {}.".format(
                url_coup, rep.status_code)
            )
    except RuntimeError as error:
        print(error)
