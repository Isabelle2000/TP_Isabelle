import argparse
import api


def analyser_commande():
    parser = argparse.ArgumentParser(description='Jeu Quoridor - phase 1')
    parser.add_argument('idul', metavar='IDUL', 
                        default='islev54', help="IDUL du joueur")
    parser.add_argument('-l', '--lister', dest='liste',
                        help='Lister les identifiants de vos 20 dernières parties.')
    return parser.parse_args()

def afficher_damier_ascii(etat_de_jeu):
    damier, verticale, horizontale = [], [], []
    for i in range(9):
        matrice_damiier, matrice_verticale, matrice_horizontale = [], [], []
        for j in range(9):
            matrice_damier.append('.')
            matrice_verticale.append(' ')
            matrice_horizontale.append('   ')
        damier.append(matrice_damier)
        verticale.append(matrice_vertical)
        horizontale.append(matrice_horizontal)
    posi_j_1 = etat_de_jeu['joueurs'][0]['pos']
    posi_j_2 = etat_de_jeu['joueurs'][1]['pos']
    damier[posi_j_1[1] - 1][posi_j_1[0] - 1] = '1'
    damier[posi_j_2[1] - 1][posi_j_2[0] - 1] = '2'
    damier.reverse()
    for a, b in etat_de_jeu['murs']['horizontaux']:
        horizontale[b - 1][a - 1] = '---'
    horizontale.reverse()
    for a, b in etat_de_jeu['murs']['verticaux']:
        verticale[b - 1][a - 1] = '|'
    verticale.reverse()
    sortie = "   -----------------------------------\n"
    for i in range(9):
        if i == 8:
            sortie += "1 |"
            sortie += "{}{} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}  ".format(
                verticale[8][0], damier[8][0],
                verticale[8][1], damier[8][1],
                verticale[8][2], damier[8][2],
                verticale[8][3], damier[8][3],
                verticale[8][4], damier[8][4],
                verticale[8][5], damier[8][5],
                verticale[8][6], damier[8][6],
                verticale[8][7], damier[8][7],
                verticale[8][8], damier[8][8],
            )
            sortie = sortie[:-1]
            sortie += "|\n"
        else:
            sortie += "{} |".format(9 - i)
            sortie += "{}{} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}  ".format(
                verticale[i][0] if verticale[i + 1][0] != '|' else '|', damier[i][0],
                verticale[i][1] if verticale[i + 1][1] != '|' else '|', damier[i][1],
                verticale[i][2] if verticale[i + 1][2] != '|' else '|', damier[i][2],
                verticale[i][3] if verticale[i + 1][3] != '|' else '|', damier[i][3],
                verticale[i][4] if verticale[i + 1][4] != '|' else '|', damier[i][4],
                verticale[i][5] if verticale[i + 1][5] != '|' else '|', damier[i][5],
                verticale[i][6] if verticale[i + 1][6] != '|' else '|', damier[i][6],
                verticale[i][7] if verticale[i + 1][7] != '|' else '|', damier[i][7],
                verticale[i][8] if verticale[i + 1][8] != '|' else '|', damier[i][8],
            )
            sortie = sortie[:-1]
            sortie += "|\n"
            sortie += "  |"
            sortie += "{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}".format(
                horizontale[i][0], '-' if horizontale[i][0] == '---' else verticale[i + 1 if i < 8 else 0][1],
                horizontale[i][1] if horizontale[i][0] != '---' else '---', '-' if horizontale[i][1] == '---' else verticale[i + 1 if i < 8 else 0][2],
                horizontale[i][2] if horizontale[i][1] != '---' else '---', '-' if horizontale[i][2] == '---' else verticale[i + 1 if i < 8 else 0][3],
                horizontale[i][3] if horizontale[i][2] != '---' else '---', '-' if horizontale[i][3] == '---' else verticale[i + 1 if i < 8 else 0][4],
                horizontale[i][4] if horizontale[i][3] != '---' else '---', '-' if horizontale[i][4] == '---' else verticale[i + 1 if i < 8 else 0][5],
                horizontale[i][5] if horizontale[i][4] != '---' else '---', '-' if horizontale[i][5] == '---' else verticale[i + 1 if i < 8 else 0][6],
                horizontale[i][6] if horizontale[i][5] != '---' else '---', '-' if horizontale[i][6] == '---' else verticale[i + 1 if i < 8 else 0][7],
                horizontale[i][7] if horizontale[i][6] != '---' else '---', '-' if horizontale[i][7] == '---' else verticale[i + 1 if i < 8 else 0][8],
                horizontale[i][8] if horizontale[i][7] != '---' else '---', '-' if horizontale[i][8] == '---' else verticale[i + 1 if i < 8 else 0][0]
            )
            sortie = sortie[:-1]
            sortie += "|\n"
    sortie += "--|-----------------------------------\n"
    sortie += "  | 1   2   3   4   5   6   7   8   9\n"
    print(sortie)
