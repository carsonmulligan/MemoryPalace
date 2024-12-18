import random
import json

# Define the mappings for persons, actions, and objects
persons = {
    str(i).zfill(2): name for i, name in enumerate([
        "Jack", "Emma", "Liam", "Olivia", "Noah", "Ava", "Ethan", "Sophia", "Mason", "Isabella",
        "Logan", "Mia", "Lucas", "Charlotte", "Aiden", "Amelia", "Elijah", "Harper", "James", "Evelyn",
        "Benjamin", "Abigail", "Sebastian", "Emily", "Alexander", "Ella", "Michael", "Scarlett", "William", "Grace",
        "Henry", "Chloe", "Daniel", "Victoria", "Matthew", "Aria", "Joseph", "Madison", "David", "Luna",
        "Jackson", "Layla", "Samuel", "Zoey", "Levi", "Hannah", "Isaac", "Zoe", "Owen", "Stella",
        "Gabriel", "Ellie", "Julian", "Avery", "Carter", "Aubrey", "Wyatt", "Mila", "Luke", "Camila",
        "Dylan", "Penelope", "Caleb", "Riley", "Nathan", "Aurora", "Ryan", "Lily", "Andrew", "Addison",
        "Theodore", "Violet", "Hunter", "Hazel", "Christian", "Nora", "Isaiah", "Skylar", "Joshua", "Savannah",
        "Anthony", "Lucy", "Thomas", "Paisley", "Charles", "Eliana", "Christopher", "Claire", "Eli", "Bella",
        "Hudson", "Willow", "Adrian", "Caroline", "Aaron", "Anna", "Cooper", "Autumn"
    ], start=1)
}

actions = {
    str(i).zfill(2): action for i, action in enumerate([
        "Running", "Jumping", "Swimming", "Lifting", "Reading", "Writing", "Climbing", "Singing", "Dancing", "Cooking",
        "Driving", "Painting", "Drawing", "Laughing", "Crying", "Sleeping", "Thinking", "Talking", "Throwing", "Catching",
        "Typing", "Digging", "Sewing", "Fishing", "Hunting", "Hiking", "Jogging", "Skipping", "Meditating", "Gardening",
        "Washing", "Cleaning", "Repairing", "Sharpening", "Knitting", "Carving", "Folding", "Rolling", "Hammering", "Sawing",
        "Welding", "Polishing", "Drilling", "Sanding", "Measuring", "Mixing", "Pouring", "Carrying", "Chopping", "Shredding",
        "Grating", "Slicing", "Baking", "Frying", "Grilling", "Boiling", "Stirring", "Whisking", "Peeling", "Pouring",
        "Chewing", "Swallowing", "Sniffing", "Tasting", "Kneeling", "Crawling", "Leaping", "Gliding", "Flying", "Landing",
        "Clapping", "Snapping", "Winking", "Smiling", "Frowning", "Hugging", "Kissing", "Punching", "Kicking", "Tickling",
        "Rubbing", "Scratching", "Petting", "Brushing", "Combing", "Washing", "Shaving", "Folding", "Unpacking", "Packing",
        "Sorting", "Stacking", "Lining", "Pushing", "Pulling", "Sliding"
    ], start=1)
}

objects = {
    str(i).zfill(2): obj for i, obj in enumerate([
        "Book", "Pen", "Apple", "Ball", "Chair", "Table", "Phone", "Laptop", "Bottle", "Hat",
        "Shoes", "Watch", "Gloves", "Scarf", "Bag", "Umbrella", "Key", "Wallet", "Camera", "Map",
        "Lantern", "Candle", "Lamp", "Fan", "Radio", "Drum", "Guitar", "Piano", "Violin", "Flute",
        "Bell", "Clock", "Mirror", "Brush", "Comb", "Basket", "Pillow", "Blanket", "Curtain", "Rug",
        "Towel", "Soap", "Shampoo", "Conditioner", "Toothbrush", "Toothpaste", "Sponge", "Broom", "Mop", "Dustpan",
        "Vacuum", "Iron", "Stove", "Oven", "Microwave", "Fridge", "Freezer", "Dishwasher", "Sink", "Faucet",
        "Knife", "Fork", "Spoon", "Plate", "Bowl", "Cup", "Glass", "Jug", "Tray", "Cutting Board",
        "Pan", "Pot", "Whisk", "Spatula", "Ladle", "Tongs", "Chopsticks", "Strainer", "Colander", "Grater",
        "Rolling Pin", "Measuring Cup", "Scale", "Thermometer", "Timer", "Blender", "Mixer", "Food Processor", "Toaster", "Kettle"
    ], start=1)
}

# Function to encode six-digit codes
def encode_six_digit_code(code):
    person_code = code[:2]
    action_code = code[2:4]
    object_code = code[4:]

    person = persons.get(person_code, "Unknown Person")
    action = actions.get(action_code, "Unknown Action")
    object_ = objects.get(object_code, "Unknown Object")

    return person, action, object_

# Generate a sequential list of six-digit codes
def generate_sequential_codes():
    codes = []
    for i in range(1, 100, 3):
        person_code = str(i).zfill(2)
        action_code = str(i + 1).zfill(2)
        object_code = str(i + 2).zfill(2)
        code = person_code + action_code + object_code
        codes.append(code)
    return codes

# Main function to demonstrate the system
def main():
    print("Mappings:")
    print("Persons:", json.dumps(persons, indent=2))
    print("Actions:", json.dumps(actions, indent=2))
    print("Objects:", json.dumps(objects, indent=2))

    print("\nSequential Six-Digit Codes and Decoded Values:")
    sequential_codes = generate_sequential_codes()
    for code in sequential_codes:
        person, action, object_ = encode_six_digit_code(code)
        print(f"Code: {code} -> {person} {action} {object_}")

if __name__ == "__main__":
    main()
