import csv


# with open('output.csv', "w") as fichier_csv:
#     writer = csv.writer(fichier_csv, delimiter=',')
#     en_tete = ["nom", "salaire"]
#     writer.writerow(en_tete)
# with open('input.csv') as fichier_csv:
#     reader = csv.DictReader(fichier_csv, delimiter=',')
#     for ligne in reader:
#         print(ligne)
#         with open('output.csv', "a") as fichier_csv:
#             writer = csv.writer(fichier_csv, delimiter=',')
#             writer.writerow([ligne["nom"],
#                              15 * int(ligne["heures_travaillees"])])
            
with open('output.csv', "w") as fichier_sortie, open('input.csv') as fichier_entré:
    writer = csv.writer(fichier_sortie, delimiter=',')
    en_tete = ["nom", "salaire"]
    writer.writerow(en_tete)
    reader = csv.DictReader(fichier_entré, delimiter=',')
    for ligne in reader:
        writer = csv.writer(fichier_sortie, delimiter=',')
        writer.writerow([ligne["nom"], 15 * int(ligne["heures_travaillees"])])