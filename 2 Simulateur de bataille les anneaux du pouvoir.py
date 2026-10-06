"""
Rétroaction :
Logique algorithmique :                 5/5 (fait ensemble en classe)
Fonctionnement du programme python :    2/5 (incomplet et comporte des erreurs)
Documentation :                         0/2 (ajouter la documentation des fonctions et des commentaires qui expliquent ton code)
Total :                                 7/12
"""
"""
Entrée: choix_stratégie
Sorties: resultat_combat
Donnée:
               # elfes, nains, humains
armee_galadriel = [250, 150, 500]
              # trolls, worgs, orcs
armee_sauron = [100, 200, 2500]
liste_strategies = [agressive, défensive
Fonctions:
CALCULER_FORCES ( liste_armee)
    force = 1 * nb_humains + 5 * nb_nains + 10 nb_elfes
    retourner force

DETERMINER_RESULTAT_COMBAT (force_galadriel, force_sauron)
    SI force_galadriel > force_sauron
        gagnant = Galadriel
    SINON SI force_sauron > force_galadriel
        gagnant = sauron
    SINON
        gagnant = null
    RETOURNER gagnant
Algo:
INITIALISER les listes
DEMANDER choix_strategies (et valider)
Si choix_strategie = agressive
    éliminer 500 orcs
SINON si choix_stratégie = défensive
    obtenir des renforts de 175 nains
CALCULER_FORCES de Galadriel
CALCULER_FORCES de Sauron
DETERMINER_RESULTAT_COMBAT
AFFICHER resultat_combat

"""
liste_armee_galadriel = [250, 150, 500]
liste_armee_galadriel1 = ["elfes", "nains", "humains"]

liste_armee_sauron = [100, 200, 2500]
liste_armee_sauron1 = ["trolls", "worgs", "orcs"]

def CALCULER_FORCES (liste_armee_galadriel): # Les noms de fonction devraient être en minuscules en pyton.
    force_sauron = 1 * liste_armee_galadriel[2] + 5 * liste_armee_galadriel[1] + 10 * liste_armee_galadriel[0]
    force_galadriel = liste_armee_galadriel[2] + liste_armee_galadriel[1] + liste_armee_galadriel[0] # Ça devait être une fonction générale qui marche pour n'importe quelle armée et qu'on appelle 2 fois, mais à chaque fois, elle calcule une seule force.
    return force_sauron and force_galadriel # Le mot "and" s'utilise entre des conditions, par pour retourner plusieurs choses. Quand on veut retourner plusieurs variables, on les sépare par des virgules.

def DETERMINER_RESULTAT_COMBAT (force_galadriel, force_sauron):

    if force_galadriel > force_sauron:
        Gagnant = "Galadriel"
    elif force_sauron > force_galadriel:
        Gagnant = "sauron"  # Majuscule au début du nom
    else:
        Gagnant = "null"    # En python, tu peux utiliser le mot None
    return Gagnant

strategie = input("Quelle est votre strategie (agressive/ défensive)" ) # La réponse n'est pas validée.
if strategie == "agressive":
    liste_armee_sauron[2] = liste_armee_sauron[2] - 500
    print(f"maintenant l'armée de sauron est {liste_armee_sauron}")

else:
    liste_armee_galadriel[1] = liste_armee_galadriel[1] + 175
    print(f"maintenant l'armée de galadriel est {liste_armee_galadriel}")

# J'ai ajouté ces tests juste pour vérifier tes fonctions.
print(CALCULER_FORCES(liste_armee_galadriel))
print(CALCULER_FORCES(liste_armee_sauron))
print(DETERMINER_RESULTAT_COMBAT(1,2))







