# Test Technique Leviatan

> - Merci de bien lire les consignes
> - Les différents exercices doivent être push sur un dépôt git
> - Les bonus ne sont pas obligatoires
> - Les outils de génération de code sont interdits

## Exercice 1
#### Description :
Dans le langage de votre choix, écrire un programme, pour les nombres entre 1 et 101 inclus :
- **si le nombre est divisible par 3** : on écrit Levia
- **si le nombre est divisible par 5** : on écrit Tan
- **si le nombre est divisible par 3 et par 5** : on écrit LeviaTan
- **sinon** : on écrit le nombre

#### Contraintes :
- Les librairies sont interdites.

### Exemple :
**Entrée**
```sh
N/A
```

**Sortie**
```sh
["1", "2", "Levia", "4", "Tan", "Levia", "7", "8", "Levia", "Tan", "11", "Levia", "13", "14", "LeviaTan".........]
```


-----------------------------------------------------------------------------------------------------------------------


## Exercice 2
#### Description :
Dans le langage de votre choix, écrire un programme qui prend en entrée une liste de nombres entiers positifs et qui renvoie la somme des nombres pairs de cette liste.

#### Contraintes :
- Les librairies sont interdites.
- Ne pas utiliser de bibliothèques externes ou de fonctions pré-définies pour calculer la somme des nombres pairs.

### Exemple :
**Entrée**
```sh
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

**Sortie**
```sh
30
```


-----------------------------------------------------------------------------------------------------------------------


## Exercice 3
#### Description : 
Dans le langage de votre choix, écrire un programme qui prend en entrée une chaîne de caractères et retourne cette chaîne inversée.

#### Contraintes :
- Les librairies sont interdites.
- Ne pas utiliser de méthodes ou fonctions intégrées pour inverser la chaîne.

#### Exemple : 
**Entrée**
```sh
hello
```
**Sortie**
```sh
olleh
```


-----------------------------------------------------------------------------------------------------------------------


## Exercice 4
#### Description:
En **PHP**, écrire un programme qui prend en entrée une chaîne de caractères et retourne True si la chaîne est un palindrome, et False sinon.
> Note : Un palindrome est un mot, une phrase ou une autre séquence de caractères qui se lit de la même manière à l'endroit et à l'envers, en ignorant la casse, la ponctuation, les accents et les espaces (par exemple : radar ou Ève rêve).

#### Contraintes :
- Les librairies sont interdites.
- Ne pas utiliser de méthodes ou fonctions intégrées pour déterminer si la chaîne est un palindrome.
- Ignorer la casse, la ponctuation, les accents et les espaces

#### Exemple :
**Entrée**
```sh
rAdar
```
**Sortie**
```sh
True
```


-----------------------------------------------------------------------------------------------------------------------


## Exercice bonus
#### Description :
Dans le langage de votre choix, écrire un programme qui prend en entrée une liste d'entiers et un nombre entier K. La fonction doit retourner True si deux nombres distincts de la liste peuvent être additionnés pour obtenir K, et False sinon.

#### Contraintes :
- Les librairies sont interdites.

#### Exemple 1 :
**Entrée**
```php
my_function([1, 2, 3, 4, 5], 9)
```
**Sortie**
```sh
True
```

#### Exemple 2 :
**Entrée**
```php
my_function([1, 2, 3, 4, 5], 10)
```
**Sortie**
```sh
False
```


-----------------------------------------------------------------------------------------------------------------------


## Exercice 5
#### Description :
Créer une API REST pour gérer une collection d'articles. Les articles doivent avoir un id, un titre, un contenu et une date de création.
Un article peut être lié à une ou plusieurs catégories. Une catégorie est simplement définie par un nom.

#### Contraintes :
- L'API doit être développée avec un framework **PHP** de votre choix (le framework est obligatoire).
- Fonctions à développer:
  * GET /articles: Récupérer tous les articles.
  * GET /articles/<id>: Récupérer un article par son ID.
  * POST /articles: Ajouter un nouvel article.
  * PUT /articles/<id>: Mettre à jour un article par son ID.
  * DELETE /articles/<id>: Supprimer un article par son ID.
  * POST /categories: Ajouter une nouvelle catégorie.
  * DELETE /categories/<id>: Supprimer une catégorie par son ID.
- La mise en place d'une base de données est obligatoire.
- Toutes les librairies sont autorisées.
- Une gestion d'erreur complète doit être faite.

### Bonus 1 :
Ajouter une authentification avec un système JWT.

#### Contraintes :
- Seuls les utilisateurs authentifiés peuvent créer, mettre à jour ou supprimer des articles.
- Tout le monde peut lire les articles

### Bonus 2 :
Ajouter une interface graphique responsive.
Cette interface sera idéalement développée avec un framework javascript (angular, vuejs, react, etc.)

### Bonus 3 :
Ajouter une fonctionnalité permettant d'exporter tous les articles au format CSV.

-----------------------------------------------------------------------------------------------------------------------