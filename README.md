
ZONE_LA_PLUS_CHAUDE_EN_FRANCE_DE_2000-2009
# ZONE_LA_PLUS_CHAUDE_EN_FRANCE_DE_2000-2009
### âœï¸ Auteurs
- **Anis Ghouas**
- **Alio Hissein Alio**
- **Groupe : Shannon**
AnnÃ©e universitaire : **2024-2025**
# ðŸŒ¡ï¸ DÃ©termination des zones les plus chaudes
## ðŸ“– Introduction
Ce projet, dÃ©veloppÃ© dans le cadre de **SAE 105 : Traitement des donnÃ©es**, a pour objectif principal dâ€™identifier les zones gÃ©ographiques les plus chaudes Ã  partir de donnÃ©es mÃ©tÃ©orologiques dÃ©taillÃ©es. Il offre une analyse personnalisable en fonction de la pÃ©riode choisie, de la rÃ©solution temporelle, et du type de zone (station ou coordonnÃ©es gÃ©ographiques).  
GrÃ¢ce Ã  ce projet, nous avons explorÃ© des techniques de manipulation et dâ€™analyse de donnÃ©es climatiques, ainsi que leur interprÃ©tation pour en tirer des informations utiles.
---
## ðŸŽ¯ Objectifs du projet
1. Traiter de grandes quantitÃ©s de donnÃ©es climatiques provenant de fichiers CSV.
2. Analyser les tempÃ©ratures maximales en fonction dâ€™une pÃ©riode et dâ€™une rÃ©solution spatiale dÃ©finies par l'utilisateur.
3. Permettre une personnalisation de lâ€™analyse grÃ¢ce Ã  des paramÃ¨tresâ€¯:
   - **DurÃ©e** : PÃ©riode dâ€™analyse sÃ©lectionnÃ©e par lâ€™utilisateur.
   - **RÃ©solution temporelle** : Choix entre une analyse horaire, journaliÃ¨re, mensuelle ou annuelle.
   - **Type de zone** : Analyse par station mÃ©tÃ©orologique ou par coordonnÃ©es gÃ©ographiques.
4. Identifier et afficher la rÃ©gion ou la station ayant enregistrÃ© la tempÃ©rature la plus Ã©levÃ©e.
---
## ðŸ—‚ï¸ Structure des donnÃ©es
Les fichiers utilisÃ©s pour ce projet contiennent des donnÃ©es mÃ©tÃ©orologiques fournies par MÃ©tÃ©o-France. Voici les principales colonnes et mÃ©tadonnÃ©es contenues dans les fichiers CSVâ€¯:
| **Champ**       | **Description**                                                                                              | **UnitÃ©**                   |
|------------------|------------------------------------------------------------------------------------------------------------|-----------------------------|
| **NUM_POSTE**    | NumÃ©ro unique de la station mÃ©tÃ©orologique (8 chiffres).                                                   | -                           |
| **NOM_USUEL**    | Nom usuel de la station mÃ©tÃ©orologique.                                                                    | -                           |
| **LAT**          | Latitude de la station (valeurs nÃ©gatives au sud).                                                         | DegrÃ©s et millioniÃ¨mes      |
| **LON**          | Longitude de la station (valeurs nÃ©gatives Ã  lâ€™ouest de Greenwich).                                        | DegrÃ©s et millioniÃ¨mes      |
| **ALTI**         | Altitude de la station.                                                                                    | MÃ¨tres                      |
| **AAAAMMJJHH**   | Date et heure de la mesure.                                                                                | Format `YYYYMMDDHH`         |
| **T**            | TempÃ©rature enregistrÃ©e (ou `"mq"` si donnÃ©e manquante).                                                  | Â°C                          |
| **PMERM**        | Moyenne quotidienne des pressions au niveau de la mer.                                                    | hPa (1/10)                  |
| **INST**         | DurÃ©e dâ€™ensoleillement quotidienne.                                                                        | Minutes                     |
| **UV_INDICEX**   | Maximum des indices UV horaires.                                                                           | -                           |
### ðŸ” Gestion des donnÃ©es manquantes
- Les tempÃ©ratures marquÃ©es comme `"mq"` sont automatiquement ignorÃ©es dans le traitement.
- Les lignes malformÃ©es ou contenant des incohÃ©rences sont Ã©galement passÃ©es pour garantir lâ€™exÃ©cution du programme.
---
## ðŸ› ï¸ FonctionnalitÃ©s du projet
1. **Lecture et traitement des fichiers CSV** : Extraction des donnÃ©es climatiques pour les stations ou zones gÃ©ographiques.
2. **Personnalisation de lâ€™analyse** :
   - Choix de la pÃ©riode dâ€™analyse via des dates de dÃ©but et de fin.
   - SÃ©lection de la rÃ©solution temporelle (heure, jour, mois ou annÃ©e).
   - PossibilitÃ© dâ€™analyser les donnÃ©es par station.
3. **Calcul des statistiques** :
   - Nombre total de relevÃ©s pour chaque rÃ©gion.
   - TempÃ©rature maximale enregistrÃ©e.
   - TempÃ©rature moyenne pour chaque rÃ©gion.
4. **Identification de la rÃ©gion ou station la plus chaude** :
   - RÃ©gion ayant enregistrÃ© la tempÃ©rature maximale pendant la pÃ©riode analysÃ©e.
   - Affichage de la tempÃ©rature maximale correspondante.
---
###  Conclusion
GrÃ¢ce Ã  ce projet, nous avons pu maÃ®triser les techniques de traitement et dâ€™analyse de donnÃ©es climatiques, tout en rÃ©pondant Ã  des problÃ©matiques concrÃ¨tes comme lâ€™identification des zones les plus chaudes. Les rÃ©sultats obtenus dÃ©montrent la flexibilitÃ© et la prÃ©cision des outils mis en Å“uvre.
