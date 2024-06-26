# Utilisation d'une version de Python compatible avec Django (3.11 n'existe pas, optons pour 3.9 ou 3.10 par exemple)
FROM python:3.10

# Définition de l'environnement pour Python
ENV PYTHONUNBUFFERED=1

# Définition du répertoire de travail
WORKDIR /movies

# Copie des fichiers requirements.txt dans le conteneur
COPY requirements.txt .

# Installation des dépendances
RUN pip install -r requirements.txt

# Exposition du port sur lequel Django va écouter (8000)
EXPOSE 8000

# Commande par défaut pour démarrer le serveur Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
