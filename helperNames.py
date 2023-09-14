import random


names = ["Anna", "Jan", "Maria", "Piotr", "Katarzyna", "Tomasz", "Magdalena", "Pawel", "Agnieszka", "Michal",
          "Karolina", "Grzegorz", "Ewa", "Marcin", "Aleksandra", "Robert", "Joanna", "Krzysztof", "Natalia", "Wojciech"]

surnames = ["Nowak", "Kowalski", "Wisniewski", "Dabrowski", "Lewandowski", "Wojcik", "Kaminski", "Kowalczyk", "Zielinski", "Szymanski",
            "Wojciechowski", "Kowalewski", "Kaczmarek", "Michalski", "Zawisza", "Pawlak", "Krol", "Jankowski", "Majewski", "Kaczynski"]
def randomName():
    return random.choice(names)

def randomSurname():
    return random.choice(surnames)




