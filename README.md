# Projet US SBA - Prédiction de Remboursement de Prêts

Ce projet vise à développer un modèle de prédiction permettant à l'United States Small Business Administration (US SBA) de déterminer si une entreprise sera en mesure de rembourser son prêt ou non. L'objectif est d'aider l'US SBA à prendre des décisions éclairées lors de l'octroi de prêts aux petites entreprises, contribuant ainsi à la croissance économique et à la création d'emplois.

## Contexte

L'US SBA a été créée pour aider les petites entreprises à obtenir du crédit, avec pour objectif de stimuler la croissance économique et de réduire le chômage aux États-Unis. Ce projet de prédiction de remboursement de prêts s'inscrit dans cet objectif en utilisant des techniques d'apprentissage automatique pour évaluer la probabilité de remboursement d'un prêt par une entreprise.
Objectifs du Projet

Ce projet se divise en deux grandes parties :

    Nettoyage, Exploration des Données et Modélisation :
        Nettoyage du jeu de données
        Analyse exploratoire des données (EDA)
        Préparation des données pour la modélisation
        Sélection des caractéristiques et génie des caractéristiques
        Choix et entraînement du modèle de prédiction
    Mise en Production avec FastAPI et Django :
        Développement d'une API avec FastAPI pour servir le modèle de prédiction
        Création d'une interface utilisateur conviviale avec Django pour consommer l'API

### Structure du Projet

Le projet est organisé de la manière suivante :

    Notebooks : Contiennent le code pour le nettoyage, l'EDA et la modélisation.
    API : Contient le code pour l'API développée avec FastAPI.
    DjangoApp : Contient le code pour l'application web développée avec Django.

### Cadre Technique

    Langages de programmation : Python, HTML, CSS
    Bibliothèques principales : Pandas, NumPy, Scikit-learn, FastAPI, Django

### Installation

Pour exécuter ce projet localement, assurez-vous d'avoir Docker et Docker Compose installés sur votre machine. Ensuite, suivez ces étapes :

1. Clonez ce dépôt sur votre machine.
2. Accédez au répertoire du projet.
3. Exécutez docker-compose up pour démarrer les conteneurs Docker.

### Déploiement sur Azure

Pour déployer ce projet sur Microsoft Azure, suivez les étapes suivantes :

1. Créez un compte sur Azure si vous n'en avez pas déjà un.
2. Créez un conteneur Docker sur Azure Container Registry pour héberger votre application.
3. Utilisez Azure Kubernetes Service (AKS) pour déployer votre conteneur Docker sur un cluster Kubernetes géré.
4. Assurez-vous de configurer les services appropriés (tels que le stockage, la base de données, etc.) sur Azure selon les besoins de votre application.
5. Utilisez les outils de CI/CD d'Azure DevOps ou d'autres outils similaires pour automatiser le déploiement de votre application sur Azure.


### Auteurs

Ce projet a été développé par Farid et Elie.