# Utiliser une image Python de base
FROM python:3.10-slim

# Installer les dépendances système nécessaires
RUN apt-get update && apt-get install -y \
    python3-tk \
    && rm -rf /var/lib/apt/lists/*

# Créer le dossier de travail
WORKDIR /app

# Copier les fichiers du projet dans le conteneur
COPY . /app

# Installer CustomTkinter
RUN pip install customtkinter

# Commande par défaut (sera modifiée pour les tests automatiques)
CMD ["python", "assistant.py"]
