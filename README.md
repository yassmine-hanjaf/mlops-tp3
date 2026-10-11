# MLOps Chapitre 2 : Boîte à outils MLOps

Chaîne réalisée : **Git → GitHub Actions (tests) → Docker → Docker Hub**

## Application
API Flask avec deux routes : `/` (statut) et `/health`.

## Choix technologiques
| Besoin | Choix | Raison |
|---|---|---|
| Code | GitHub | Gratuit, intégré à la CI |
| CI/CD | GitHub Actions | Aucun serveur à maintenir |
| Conteneurs | Docker | Standard, portable |
| Registry | Docker Hub | Gratuit, simple |
| Tests | pytest | Simple et standard |

## Lancer l'image
docker pull 1yassmine12/mon-projet-python:latest
docker run -d --name mon-projet-python -p 5000:5000 1yassmine12/mon-projet-python:latest

## Pipeline
Chaque push sur `main` lance les tests (`pytest`), puis, s'ils passent, construit et publie l'image sur Docker Hub.