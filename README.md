# Modélisation du Risque de Crédit et Déploiement API

Ce projet a pour objectif de construire un modèle de machine learning capable de prédire le risque de défaut de paiement de clients pour des cartes de crédit. Le projet couvre l'ensemble du cycle de vie d'un projet de data science, de l'analyse exploratoire des données (EDA) au déploiement du modèle via une API web.

---

## 📊 Données

Le jeu de données utilisé est le **"Default of Credit Card Clients"** provenant du référentiel UCI Machine Learning.

- **Source :** [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients)
- **Description :** Ce dataset contient des informations sur des paiements par défaut, des facteurs démographiques, des données de crédit, l'historique des paiements et des relevés de factures de clients de cartes de crédit à Taïwan en 2005.
- **Variable Cible :** `TARGET` (1 pour un client en défaut, 0 sinon).

---

## Initiales de l'Analyse Exploratoire (EDA)

L'analyse initiale des données a permis de formuler plusieurs hypothèses clés qui guideront la modélisation :

1.  **Le montant du crédit (`LIMIT_BAL`) est un facteur de risque.** Les clients avec une limite de crédit plus faible ont une probabilité de défaut significativement plus élevée que ceux avec une limite de crédit plus importante.

2.  **L'historique des paiements (`PAY_X`) est le prédicteur le plus puissant.** Un simple retard de paiement d'un ou deux mois augmente drastiquement le risque de défaut. Ces variables seront centrales pour le modèle.

3.  **Les variables démographiques (`SEX`, `EDUCATION`, `MARRIAGE`) ont une influence modérée.** Bien qu'il existe de légères différences de taux de défaut entre les catégories, leur pouvoir prédictif semble moins direct que celui des variables comportementales (historique de paiement, montants des factures).

4.  **Le jeu de données est déséquilibré.** Il y a beaucoup plus de clients qui remboursent leur crédit que de clients qui font défaut. Cela devra être pris en compte lors de la phase de modélisation pour éviter que le modèle ne se contente de prédire "pas de défaut" systématiquement.