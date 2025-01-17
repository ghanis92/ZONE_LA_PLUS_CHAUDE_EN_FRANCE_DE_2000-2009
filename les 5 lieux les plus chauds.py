import csv
from datetime import datetime
import matplotlib.pyplot as plt

# Liste des fichiers à analyser
# les chemins des fichiers contenant les données météorologiques
chemins_fichiers = [
    "H_01_2000-2009.csv"  # on peut ajouter d'autres fichiers si besoin
]

# Paramètres modifiables
# la résolution temporelle : "hour", "day", "month", ou "year"
resolution_temps = "day"
# le type de région : "station" ou "latitude_longitude"
type_region = "station"
# Définir la plage temporelle pour l'analyse
date_debut = "2004-03-17"  # Date de début
date_fin = "2004-03-17"  # Date de fin (même jour si analyse unique)

# Conversion des dates en objets datetime pour les comparaisons
objet_date_debut = datetime.strptime(date_debut, "%Y-%m-%d")
objet_date_fin = datetime.strptime(date_fin, "%Y-%m-%d")

# Initialisation une liste pour stocker les statistiques par région
statistiques_par_region = []

# Lecture et traitement des fichiers
for chemin_fichier in chemins_fichiers:
    with open(chemin_fichier, mode='r') as fichier:
        lecteur_csv = csv.DictReader(fichier, delimiter=';')

        # Parcours de chaque ligne du fichier CSV
        for ligne in lecteur_csv:
            try:
                # Extraction des informations nécessaires depuis chaque ligne
                nom_station = ligne["NOM_USUEL"]  # Nom de la station
                latitude = float(ligne["LAT"])  # Latitude
                longitude = float(ligne["LON"])  # Longitude
                date_heure_str = ligne["AAAAMMJJHH"]  # Date et heure au format AAAAMMJJHH
                temperature = float(ligne["T"]) if ligne["T"] != "mq" else None  # Température, "mq" = valeur manquante

                # on ignore les relevés sans température valide
                if temperature is not None:
                    # Convertion de la chaîne de date en objet datetime
                    objet_date = datetime.strptime(date_heure_str, "%Y%m%d%H")

                    # Vérification si la date est dans la plage définie
                    if objet_date_debut <= objet_date <= objet_date_fin:
                        # Création une clé unique pour chaque région
                        if type_region == "station":
                            cle_region = nom_station
                        elif type_region == "latitude_longitude":
                            cle_region = f"{latitude},{longitude}"
                        else:
                            raise ValueError("Type de région invalide spécifié.")

                        # Recherche si la région existe déjà dans les statistiques
                        trouve = False
                        for stats in statistiques_par_region:
                            if stats["region"] == cle_region:
                                # Mettre à jour les statistiques existantes
                                stats["compteur"] += 1
                                stats["somme_temp"] += temperature
                                stats["temp_max"] = max(stats["temp_max"], temperature)
                                trouve = True
                                break

                        # Si la région n'existe pas, ajoute une nouvelle entrée
                        if not trouve:
                            statistiques_par_region.append({
                                "region": cle_region,
                                "compteur": 1,
                                "somme_temp": temperature,
                                "temp_max": temperature
                            })

            except Exception as e:
                # Ignore les erreurs (par exemple, lignes malformées)
                continue

# Trie des régions par température maximale pour trouver les 5 plus chaudes
# Les régions sont triées en ordre décroissant par leur température maximale
regions_triees = sorted(statistiques_par_region, key=lambda x: x["temp_max"], reverse=True)
# Sélection des 5 régions les plus chaudes
regions_top_5 = regions_triees[:5]

# Préparation des données pour le graphique
# Les noms des régions et leurs températures maximales
noms_regions = [region["region"] for region in regions_top_5]
temperatures_max = [region["temp_max"] for region in regions_top_5]

# Création d'un diagramme en barres pour représenter les 5 lieux les plus chauds
plt.figure(figsize=(10, 6))
plt.bar(noms_regions, temperatures_max)
plt.xlabel("Régions ou Stations")  #axe des x
plt.ylabel("Température Maximale (°C)")  # axe des y
plt.title(f"Top 5 des lieux les plus chauds le {date_debut}")  # Titre du graphique
plt.xticks(rotation=45)  # Rotation des noms des régions pour une meilleure lisibilité
plt.tight_layout()  # Ajustement des marges pour un affichage clair
plt.show()  # Affichage du graphique
