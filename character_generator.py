import random

species = [
    "Goblin", "Fairy", "Elf", "Gnome", "Dragonling",
    "Mushroom Sprite", "Forest Troll", "Moon Cat", "Pixie"
]

jobs = [
    "Potion Brewer", "Cloud Shepherd", "Treasure Hunter",
    "Moss Gardener", "Dragon Dentist", "Spell Tailor",
    "Star Collector", "Cookie Wizard"
]

traits = [
    "always humming", "terribly clumsy", "laughs at squirrels",
    "collects shiny rocks", "afraid of butterflies",
    "can talk to mushrooms", "never sleeps", "loves riddles"
]

pets = [
    "mini dragon", "floating jellyfish", "enchanted snail",
    "baby phoenix", "glowing frog", "shadow rabbit", "tiny griffin"
]

items = [
    "teacup of endless cocoa", "singing sword", "invisible umbrella",
    "wand made of cinnamon", "sparkly acorn", "magic spoon",
    "pocket-sized castle"
]

print("=== Whimsical Fantasy Character Generator ===\n")

name = input("Character name: ")
color = input("Favorite color: ")

species_choice = random.choice(species)
job = random.choice(jobs)
trait = random.choice(traits)
pet = random.choice(pets)
item = random.choice(items)
age = random.randint(20, 500)

print("\n--- Your Character ---")
print(f"Name: {name}")
print(f"Species: {species_choice}")
print(f"Age: {age}")
print(f"Occupation: {job}")
print(f"Favorite Color: {color}")
print(f"Special Trait: {trait}")
print(f"Companion: {pet}")
print(f"Magic Item: {item}")

print(f"\n{name} is a {age}-year-old {species_choice} who works as a {job}.")
print(f"They adore the color {color}, are known for {trait},")
print(f"travel with a {pet}, and never leave home without their {item}.")