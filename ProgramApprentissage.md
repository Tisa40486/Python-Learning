# 📚 Programme d'apprentissage Python complet
## De débutant à FastAPI Backend Developer

**Durée totale estimée:** 8-12 semaines (30-40h/semaine)  
**Progression:** Scripts simples → Mini-projets → Architecture solide → API FastAPI  

---

## 🎯 Structure générale

### Phase 1: Fondamentaux Python (2-3 semaines)
### Phase 2: Structures de données & OOP (2-3 semaines)
### Phase 3: Outils professionnels (1-2 semaines)
### Phase 4: FastAPI & Backend (3-4 semaines)
### Phase 5: Projets réels (ongoing)

---

# 🔥 PHASE 1 : FONDAMENTAUX PYTHON (2-3 semaines)

## 1.1 - Syntax de base & types

### Concepts à maîtriser
- Variables et typage (int, str, float, bool)
- Opérateurs (arithmétiques, comparaison, logique)
- Print & input
- Commentaires
- Type hints (tu connaîs déjà, c'est comme C#)

### Ressources
- Read: https://docs.python.org/3/tutorial/introduction.html
- Pratiquer sur: https://www.codewars.com (niveau 8-7 kyu)

### Mini-exercices (fais-les)
```python
# 1. Écris un script qui demande nom & âge, puis affiche
# "Bonjour [nom], vous avez [âge] ans"
# → Utilise input() et print()

# 2. Écris un script qui convertit Celsius → Fahrenheit
# Formule: F = (C * 9/5) + 32

# 3. Écris un script qui vérifie si un nombre est pair/impair
# → Utilise if/else et l'opérateur modulo (%)
```

**Checkpoint:** Tu peux faire des scripts basiques avec variables, input/output, et logique simple?

---

## 1.2 - Conditions (if/elif/else)

### Concepts
- If/elif/else
- Opérateurs logiques (and, or, not)
- Ternaire (x if condition else y)

### Exercices
```python
# 1. Calcul de notes scolaires
# Input: note (0-100)
# Output: A (90+), B (80-89), C (70-79), D (60-69), F (<60)

# 2. Vérificateur d'âge
# Input: âge
# Output: "Mineur" ou "Majeur"

# 3. Jeu simple: nombre secret
# Génère un nombre random (1-100)
# L'utilisateur doit deviner
# Feedback: "trop haut", "trop bas", "gagné!"
# Compte les tentatives
```

**Ressource:** `random.randint(1, 100)` pour les nombres random

**Checkpoint:** Tu comprends if/elif/else et peux faire de la logique conditionnelle?

---

## 1.3 - Boucles (for, while)

### Concepts
- For loops (range, itération)
- While loops
- Break, continue
- Nested loops

### Exercices
```python
# 1. Affiche les nombres de 1 à 10
# for i in range(1, 11):
#     print(i)

# 2. Table de multiplication (choix l'utilisateur)
# Input: nombre
# Output: table de multiplication (1x à 10x)

# 3. Somme des nombres (1 à n)
# Input: n
# Output: somme (ex: n=5 → 1+2+3+4+5 = 15)

# 4. Factorielle
# Input: n
# Output: n! (5! = 5*4*3*2*1)

# 5. FizzBuzz classique
# Pour 1 à 100:
# - Multiple de 3 → "Fizz"
# - Multiple de 5 → "Buzz"
# - Multiple des deux → "FizzBuzz"
# - Sinon → le nombre
```

**Checkpoint:** Tu peux faire des boucles et tu comprends range()?

---

## 1.4 - Strings & manipulation

### Concepts
- Strings (immutables)
- Indexing & slicing (s[0], s[1:3])
- Methods (upper(), lower(), strip(), split(), join())
- F-strings (important!)

### Exercices
```python
# 1. Inverse une string
# Input: "hello" → "olleh"

# 2. Compte les voyelles dans une string
# Input: "hello world" → 3

# 3. Capitalise chaque mot
# Input: "hello world" → "Hello World"
# Utilise: .split(), .join(), .capitalize()

# 4. Palyndrome checker
# Input: "racecar" → True
# Input: "hello" → False

# 5. Parser simple
# Input: "nom=Mattis,age=19,ville=Geneva"
# Output: dict {"nom": "Mattis", "age": "19", "ville": "Geneva"}
# → Utilise .split() et .split("=")
```

**F-strings (IMPORTANT!):**
```python
name = "Mattis"
age = 19
print(f"Hello {name}, you are {age} years old")
```

**Checkpoint:** Tu maîtrises les strings et les f-strings?

---

## 1.5 - Listes (très important!)

### Concepts
- Créer une liste
- Indexing & slicing
- Methods: append(), remove(), pop(), insert(), sort(), reverse()
- List comprehension (puissant!)
- Iteration

### Exercices
```python
# 1. Crée une liste de nombres 1-10, affiche-la

# 2. Ajoute des éléments à une liste
numbers = []
# Demande à l'utilisateur 5 nombres, ajoute-les à la liste

# 3. Trouve le max d'une liste (sans utiliser max())

# 4. Inverse une liste (sans utiliser reverse())

# 5. List comprehension - filtre les pairs
# Input: [1, 2, 3, 4, 5, 6]
# Output: [2, 4, 6]
# Code: even = [x for x in numbers if x % 2 == 0]

# 6. Compte les éléments uniques
# Input: [1, 2, 2, 3, 3, 3, 4]
# Output: 4 éléments uniques

# 7. Trie une liste de noms
names = ["Charlie", "Alice", "Bob"]
# Output: ["Alice", "Bob", "Charlie"]
```

**Checkpoint:** Tu peux manipuler les listes et tu comprends list comprehension?

---

## 1.6 - Dictionnaires (très important!)

### Concepts
- Créer un dict
- Accès par clé
- Ajouter/modifier/supprimer
- Iteration (keys(), values(), items())
- get() pour accès sûr

### Exercices
```python
# 1. Crée un dict d'informations utilisateur
user = {
    "name": "Mattis",
    "age": 19,
    "city": "Geneva"
}
# Accède à chaque valeur, affiche-les

# 2. Compteur de mots
# Input: "hello world hello"
# Output: {"hello": 2, "world": 1}
# Itère sur chaque mot, incrémente le compte

# 3. Inverse un dict (keys ↔ values)
# Input: {"a": 1, "b": 2}
# Output: {1: "a", 2: "b"}

# 4. Merge deux dicts
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
# Result: {"a": 1, "b": 2, "c": 3, "d": 4}

# 5. Filtre un dict
# Input: {"name": "Mattis", "age": 19, "city": "Geneva"}
# Garde seulement les clés commençant par 'a'
# Output: {"age": 19}

# 6. JSON-like parser
# Input: {"user": "Mattis", "nested": {"age": 19}}
# Affiche toutes les clés et valeurs (même imbriquées)
```

**Checkpoint:** Tu comprends dicts et tu peux itérer sur eux?

---

## 🔲 FIN PHASE 1 - CHECKPOINT COMPLET

**Fais ce mini-projet pour vérifier:**

```python
# TODO LIST CLI (Command Line Interface)
# Functionalities:
# 1. "add" → ajoute une tâche
# 2. "list" → affiche toutes les tâches
# 3. "remove" → supprime une tâche (par index)
# 4. "quit" → termine le programme

# Structure:
# - Une liste pour stocker les tâches
# - Une boucle while pour le menu
# - If/elif/else pour chaque commande

# Exemple:
# > add
# Task: Buy milk
# Added!
# 
# > list
# 1. Buy milk
# 
# > add
# Task: Learn Python
# Added!
# 
# > list
# 1. Buy milk
# 2. Learn Python
#
# > remove
# Index: 1
# Removed!
```

**Si tu peux faire ça → tu as les fondamentaux.**

---

---

# 🔥 PHASE 2: STRUCTURES DE DONNÉES & OOP (2-3 semaines)

## 2.1 - Fonctions (fondamental!)

### Concepts
- Définir une fonction (def)
- Paramètres & return
- Default parameters
- *args & **kwargs
- Scope (local, global)
- Type hints (TRÈS important en Python moderne)

### Exercices
```python
# 1. Fonction simple
# def greet(name):
#     return f"Hello {name}"
# 
# print(greet("Mattis"))  # "Hello Mattis"

# 2. Calcul avec paramètres
# def add(a, b):
#     return a + b
# 
# print(add(5, 3))  # 8

# 3. Fonction avec default parameter
# def greet(name="World"):
#     return f"Hello {name}"
# 
# print(greet())  # "Hello World"
# print(greet("Mattis"))  # "Hello Mattis"

# 4. Type hints (Python 3.10+)
# def add(a: int, b: int) -> int:
#     return a + b
# 
# Cela aide les erreurs de type!

# 5. *args (multiple arguments)
# def sum_all(*args):
#     return sum(args)
# 
# print(sum_all(1, 2, 3, 4))  # 10

# 6. **kwargs (keyword arguments)
# def print_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# 
# print_info(name="Mattis", age=19, city="Geneva")

# 7. Combine tout
# def process_user(name: str, age: int = 18, **extra) -> dict:
#     return {
#         "name": name,
#         "age": age,
#         "extra": extra
#     }
```

**TYPE HINTS = très important!** C'est comme C#, ça t'aide à éviter des bugs.

### Mini-projets
```python
# 1. Calculatrice
# def add(a, b) -> float
# def subtract(a, b) -> float
# def multiply(a, b) -> float
# def divide(a, b) -> float
# 
# Menu: ask user, call appropriate function

# 2. Password validator
# def is_strong_password(password: str) -> bool:
#     # Vérify: au moins 8 caractères, 1 chiffre, 1 majuscule, 1 caractère spécial
#     # Return True/False

# 3. File reader
# def read_file(filename: str) -> str:
#     # Essaye de lire le fichier
#     # Si erreur → return "File not found"
#     # Sinon → return le contenu
```

**Checkpoint:** Tu peux écrire des fonctions avec type hints et *args/**kwargs?

---

## 2.2 - Fichiers & exceptions

### Concepts
- Lire fichiers (open, read, readlines)
- Écrire fichiers
- Context managers (with statement - très important!)
- Exceptions (try/except/finally)
- Exceptions custom

### Exercices
```python
# 1. Lire un fichier simple
# with open("test.txt", "r") as file:
#     content = file.read()
#     print(content)

# 2. Lire ligne par ligne
# with open("test.txt", "r") as file:
#     for line in file:
#         print(line.strip())

# 3. Écrire dans un fichier
# with open("output.txt", "w") as file:
#     file.write("Hello World\n")
#     file.write("Line 2\n")

# 4. Append (ajouter à la fin)
# with open("log.txt", "a") as file:
#     file.write("New log entry\n")

# 5. Exception handling
# try:
#     number = int(input("Enter a number: "))
#     result = 10 / number
#     print(f"Result: {result}")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# except ValueError:
#     print("Invalid input!")
# finally:
#     print("Done")

# 6. Fichier JSON (très utile!)
import json
# 
# data = {"name": "Mattis", "age": 19}
# 
# # Write JSON
# with open("data.json", "w") as file:
#     json.dump(data, file)
# 
# # Read JSON
# with open("data.json", "r") as file:
#     loaded = json.load(file)
#     print(loaded["name"])
```

### Mini-projets
```python
# 1. Todo list saver
# Sauvegarde les todos dans un fichier JSON
# À chaque démarrage, charge les todos existants

# 2. Log system
# Chaque action → écrite dans log.txt avec timestamp

# 3. CSV parser
# Lit un fichier CSV simple
# Affiche les données formatées
```

**Checkpoint:** Tu peux lire/écrire des fichiers et utiliser try/except?

---

## 2.3 - Programmation orientée objet (OOP)

### Concepts
- Classes & objets
- __init__ (constructeur)
- Méthodes & attributs
- self
- Encapsulation (private attributes)
- Héritage
- Polymorphisme

### Exercices - Partie 1: Classes basiques
```python
# 1. Classe simple
# class User:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age
#     
#     def greet(self) -> str:
#         return f"Hello, I'm {self.name}"
# 
# user = User("Mattis", 19)
# print(user.greet())
# print(user.name)

# 2. Classe avec méthodes
# class Calculator:
#     def __init__(self, starting_value: int = 0):
#         self.value = starting_value
#     
#     def add(self, n: int):
#         self.value += n
#         return self.value
#     
#     def multiply(self, n: int):
#         self.value *= n
#         return self.value
#     
#     def reset(self):
#         self.value = 0
# 
# calc = Calculator(10)
# print(calc.add(5))  # 15
# print(calc.multiply(2))  # 30

# 3. Encapsulation (private attributes)
# class BankAccount:
#     def __init__(self, balance: float):
#         self.__balance = balance  # Private!
#     
#     def deposit(self, amount: float):
#         if amount > 0:
#             self.__balance += amount
#     
#     def get_balance(self) -> float:
#         return self.__balance
# 
# account = BankAccount(1000)
# account.deposit(500)
# print(account.get_balance())  # 1500
```

### Exercices - Partie 2: Héritage
```python
# 1. Héritage simple
# class Animal:
#     def __init__(self, name: str):
#         self.name = name
#     
#     def speak(self):
#         return f"{self.name} makes a sound"
# 
# class Dog(Animal):
#     def speak(self):
#         return f"{self.name} barks!"
# 
# class Cat(Animal):
#     def speak(self):
#         return f"{self.name} meows!"
# 
# dog = Dog("Rex")
# cat = Cat("Whiskers")
# 
# print(dog.speak())  # "Rex barks!"
# print(cat.speak())  # "Whiskers meows!"

# 2. super() pour appeler parent
# class Vehicle:
#     def __init__(self, brand: str):
#         self.brand = brand
#     
#     def info(self):
#         return f"Brand: {self.brand}"
# 
# class Car(Vehicle):
#     def __init__(self, brand: str, model: str):
#         super().__init__(brand)
#         self.model = model
#     
#     def info(self):
#         return f"{super().info()}, Model: {self.model}"
# 
# car = Car("Toyota", "Camry")
# print(car.info())  # "Brand: Toyota, Model: Camry"
```

### Mini-projets
```python
# 1. Système de produits
# class Product:
#     def __init__(self, name: str, price: float, quantity: int)
# 
# class Inventory:
#     def __init__(self):
#         self.products = []
#     
#     def add_product(self, product: Product)
#     def remove_product(self, product_name: str)
#     def get_total_value(self) -> float

# 2. Système d'animaux
# class Animal:
#     - name, age, species
# 
# class Dog(Animal):
#     - breed
#     - speak() → "Woof!"
# 
# class Cat(Animal):
#     - color
#     - speak() → "Meow!"

# 3. Utilisateurs & rôles
# class User:
#     - name, email
#     - can_edit(), can_delete()
# 
# class Admin(User):
#     - permissions = ["edit", "delete", "ban"]
# 
# class Moderator(User):
#     - permissions = ["edit", "delete"]
```

**Checkpoint:** Tu peux créer des classes avec héritage et encapsulation?

---

## 🔲 FIN PHASE 2 - CHECKPOINT COMPLET

**Fais ce mini-projet:**

```python
# MINI BANKING SYSTEM

# Requirements:
# 1. Classe Account:
#    - account_holder (name)
#    - __balance (private)
#    - deposit(amount)
#    - withdraw(amount)
#    - get_balance()
#    - transfer(other_account, amount)

# 2. Classe Bank:
#    - accounts = []
#    - create_account(name) → crée un Account
#    - find_account(name) → trouve un Account
#    - list_accounts() → affiche tous

# 3. Menu CLI:
#    - Create account
#    - Deposit
#    - Withdraw
#    - Check balance
#    - Transfer
#    - List accounts

# Bonus:
#    - Save accounts to JSON
#    - Load accounts from JSON on startup
```

**Si tu peux faire ça → tu as OOP.**

---

---

# 🔥 PHASE 3: OUTILS PROFESSIONNELS (1-2 semaines)

## 3.1 - Virtual Environment & Package Management

### Concepts
- Virtual environment (isoler dépendances)
- pip (installer packages)
- requirements.txt (lister dépendances)
- Poetry (optionnel mais mieux)

### Pratique
```bash
# Créer un venv
python3 -m venv venv

# Activer (Mac/Linux)
source venv/bin/activate

# Désactiver
deactivate

# Installer packages
pip install requests

# Voir les packages installés
pip list

# Sauvegarder dépendances
pip freeze > requirements.txt

# Installer depuis requirements.txt
pip install -r requirements.txt
```

### Mini-projets
```python
# 1. HTTP requests
# Installe: pip install requests
# Fetch data d'une API publique (OpenWeather, JSONPlaceholder, etc.)

# 2. Date/Time
# Installe: pip install python-dateutil
# Parse dates, calcule différences, etc.
```

**Checkpoint:** Tu peux créer un venv et installer des packages?

---

## 3.2 - Modules & imports

### Concepts
- Import de modules (import x)
- From imports (from x import y)
- Créer tes propres modules
- Packages (dossiers avec __init__.py)

### Structure professionnelle
```
mon_projet/
├── venv/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── utils.py
│   └── models.py
├── tests/
│   └── test_main.py
├── requirements.txt
└── README.md
```

### Exercices
```python
# 1. Crée un module utils.py
# def format_currency(amount: float) -> str:
#     return f"${amount:.2f}"
# 
# def calculate_tax(amount: float, rate: float) -> float:
#     return amount * (rate / 100)

# 2. Utilise-le dans main.py
# from src.utils import format_currency, calculate_tax
# 
# price = 100
# print(format_currency(price))

# 3. Crée une structure de packages
# src/
#   calculations/
#     __init__.py
#     tax.py
#     currency.py
```

**Checkpoint:** Tu peux organiser du code en modules?

---

## 3.3 - Testing (pytest)

### Concepts
- Unit tests
- pytest (framework)
- Fixtures
- Assertions

### Exercices
```python
# Installe: pip install pytest

# calculator.py
def add(a: int, b: int) -> int:
    return a + b

def divide(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# test_calculator.py
import pytest
from calculator import add, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_divide():
    assert divide(10, 2) == 5
    
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

# Run tests
# pytest test_calculator.py
```

**Checkpoint:** Tu peux écrire des tests?

---

## 🔲 FIN PHASE 3 - CHECKPOINT COMPLET

**Organise un des projets précédents:**
- Structure propre (src/, tests/)
- requirements.txt
- Tests pour chaque classe/fonction
- Modules bien séparés

---

---

# 🔥 PHASE 4: FASTAPI & BACKEND (3-4 semaines)

## 4.1 - HTTP & REST API basics

### Concepts
- HTTP verbs (GET, POST, PUT, DELETE)
- Status codes (200, 404, 500, etc.)
- Request/Response
- JSON

### Ressource
- Lis: https://restfulapi.net/ (20 min)

**Checkpoint:** Tu comprends GET/POST et status codes?

---

## 4.2 - FastAPI Basics

### Installation
```bash
pip install fastapi uvicorn
```

### First API
```python
# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/users/{user_id}")
def read_user(user_id: int):
    return {"user_id": user_id, "name": "Mattis"}

# Run: uvicorn main:app --reload
# Visit: http://localhost:8000/users/1
# Docs: http://localhost:8000/docs
```

### Concepts clés
- Routes (path operations)
- Méthodes HTTP (@app.get, @app.post, etc.)
- Path parameters ({user_id})
- Query parameters
- Request body (Pydantic models)
- Response models

### Exercices progressifs
```python
# 1. GET simple
@app.get("/items")
def get_items():
    return [{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}]

# 2. GET avec path parameter
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id, "name": f"Item {item_id}"}

# 3. GET avec query parameters
@app.get("/search")
def search(q: str, skip: int = 0, limit: int = 10):
    return {"query": q, "skip": skip, "limit": limit}

# 4. Pydantic model (comme DTOs en C#!)
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    description: str = None  # Optional

# 5. POST avec body
@app.post("/items")
def create_item(item: Item):
    return {"created": True, "item": item}

# 6. PUT (update)
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "updated": True, "item": item}

# 7. DELETE
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"deleted": True, "item_id": item_id}
```

**Checkpoint:** Tu peux créer une API avec GET/POST/PUT/DELETE?

---

## 4.3 - Pydantic Models

### Concepts
- BaseModel
- Validation
- Type hints
- Optional fields
- Nested models

### Exercices
```python
from pydantic import BaseModel, Field
from typing import Optional

# 1. Simple model
class User(BaseModel):
    name: str
    age: int
    email: str

# 2. With optional fields
class UserOptional(BaseModel):
    name: str
    age: int
    email: Optional[str] = None  # Optional!

# 3. With Field (metadata)
class UserWithValidation(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    age: int = Field(..., ge=0, le=150)  # ge=greater or equal, le=less or equal
    email: str = Field(..., pattern=r"^[\w\.-]+@[\w\.-]+\.\w+$")  # Regex!

# 4. Nested models
class Address(BaseModel):
    street: str
    city: str
    country: str

class UserWithAddress(BaseModel):
    name: str
    address: Address  # Nested!

# 5. List in model
class UserList(BaseModel):
    users: list[User]
    total: int

# Usage
user = User(name="Mattis", age=19, email="mattis@example.com")
print(user.dict())  # Convert to dict
print(user.json())  # Convert to JSON
```

**Checkpoint:** Tu peux créer et valider Pydantic models?

---

## 4.4 - Database (SQLAlchemy + SQLite)

### Installation
```bash
pip install sqlalchemy
```

### Setup (déjà connu du .NET!)
```python
# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# models.py
from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    age = Column(Integer)

# main.py
from database import engine, SessionLocal, Base
from models import User

# Create tables
Base.metadata.create_all(bind=engine)

# Create in API
@app.post("/users")
def create_user(user: UserCreate):
    db = SessionLocal()
    db_user = User(name=user.name, email=user.email, age=user.age)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Read from API
@app.get("/users/{user_id}")
def get_user(user_id: int):
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
```

**Checkpoint:** Tu peux créer des models et les utiliser dans FastAPI?

---

## 4.5 - Architecture propre (comme tu aimes)

### Structure recommandée
```
api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── user_schema.py
│   ├── routes/
│   │   ├── __init__.py
│   │   └── users.py
│   └── repositories/
│       ├── __init__.py
│       └── user_repository.py
├── requirements.txt
└── README.md
```

### Exemple: User management
```python
# models/user.py
from sqlalchemy import Column, Integer, String
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)

# schemas/user_schema.py
from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    
    class Config:
        from_attributes = True

# repositories/user_repository.py
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user_schema import UserCreate

class UserRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, user: UserCreate) -> User:
        db_user = User(name=user.name, email=user.email)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
    
    def get_by_id(self, user_id: int) -> User:
        return self.db.query(User).filter(User.id == user_id).first()
    
    def get_all(self) -> list[User]:
        return self.db.query(User).all()

# routes/users.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.user_schema import UserCreate, UserResponse
from app.repositories.user_repository import UserRepository

router = APIRouter(prefix="/users", tags=["users"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    repo = UserRepository(db)
    return repo.create(user)

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    repo = UserRepository(db)
    return repo.get_by_id(user_id)

@router.get("/", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    repo = UserRepository(db)
    return repo.get_all()

# main.py
from fastapi import FastAPI
from app.routes import users
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(users.router)
```

**Checkpoint:** Tu peux organiser une API avec repositories?

---

## 🔲 FIN PHASE 4 - CHECKPOINT COMPLET

**Fais cette API:**

```
REQUIREMENTS:
- 3 ressources: Users, Posts, Comments
- Chaque ressource:
  - GET /resource → list all
  - GET /resource/{id} → get one
  - POST /resource → create
  - PUT /resource/{id} → update
  - DELETE /resource/{id} → delete
- Database SQLite
- Architecture propre (models, schemas, routes, repos)
- Validation Pydantic
```

---

---

# 🔥 PHASE 5: PROJETS RÉELS (ongoing)

Une fois PHASE 4 fini, tu devrais faire des vrais projets:

1. **Blog API** (Users, Posts, Comments)
2. **Todo App Backend** (avec sync avec frontend React)
3. **E-commerce API** (Products, Orders, Users)
4. **Social Media API** (Posts, Comments, Likes, Followers)

Chaque projet t'aidera à:
- Renforcer les concepts
- Apprendre l'authentification (JWT!)
- Gérer les relations complexes (relationships)
- Déployer sur serveur

---

---

# 📋 RÉSUMÉ DE LA ROUTE

| Phase | Durée | Objectif | Checkpoint |
|-------|-------|----------|-----------|
| 1: Fondamentaux | 2-3w | Syntaxe Python | Todo CLI |
| 2: OOP | 2-3w | Classes & héritage | Banking system |
| 3: Outils pro | 1-2w | Modules, tests, pip | Projet organisé |
| 4: FastAPI | 3-4w | API REST complète | Blog/Todo API |
| 5: Projets | ∞ | Solidifier & créer | Vrais projets |

---

---

# 🎯 TIPS POUR RÉUSSIR

1. **Code every day** — 30-60 min minimum
2. **Do the exercises** — pas juste lire
3. **Understand why** — pas juste copy/paste
4. **Make mistakes** — c'est normal et utile
5. **Google when stuck** — c'est normal aussi
6. **Read error messages** — Python messages sont super utiles
7. **Test your code** — pytest c'est ton ami

---

**Ready to start Phase 1? 🚀**

Tu veux commencer par quoi?
- Variables et types?
- Conditions?
- Boucles?
- Strings?

Je te guiderai étape par étape, avec indices plutôt que solutions directes.