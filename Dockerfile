# 1. Partir d'une image Python officielle et légère
FROM python:3.9-slim

# 2. Définir le répertoire de travail à l'intérieur du conteneur
WORKDIR /app

# 3. Copier le fichier des dépendances
COPY requirements.txt .

# 4. Installer les dépendances
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copier tout le reste du code du projet dans le conteneur
COPY . .

# 6. Exposer le port 80 pour que le monde extérieur puisse communiquer avec l'API
EXPOSE 80

# 7. La commande à exécuter lorsque le conteneur démarre
# On utilise --host 0.0.0.0 pour rendre l'API accessible depuis l'extérieur du conteneur
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"] 
