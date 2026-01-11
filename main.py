import time

class Pet:
    def __init__(self, name, personality):
        self.name = name
        self.personality = personality
        self.hunger = 50    # 0 = Full, 100 = Starving
        self.happiness = 50 # 100 = Excited, 0 = Sad

    def feed(self):
        print(f"\n Feeding {self.name}...")
        self.hunger = max(0, self.hunger - 20)
        self.happiness = min(100, self.happiness + 5)
        print("Hunger decreased!")

    def play(self):
        if self.hunger > 80:
            print(f"\n {self.name} is too hungry to play!")
        else:
            print(f"\n🎾 Playing with {self.name}...")
            self.happiness = min(100, self.happiness + 20)
            self.hunger = min(100, self.hunger + 10)
            print("Happiness increased!")

    def get_status(self):
        # Determine mood based on levels
        mood = "Happy " if self.happiness > 60 else "Okay "
        if self.happiness < 30: mood = "Sad 😢"
        if self.hunger > 70: mood = "Hungry 🥩"

        print("-" * 30)
        print(f"🐾 PET STATUS: {self.name}")
        print(f"Personality: {self.personality}")
        print(f"Mood: {mood}")
        print(f"Hunger: {self.hunger}/100")
        print(f"Happiness: {self.happiness}/100")
        print("-" * 30)

# --- Game Loop ---
def start_game():
    print("Welcome to Digital Pet Creator!")
    name = input("What is your pet's name? ")
    personality = input("What is their personality (e.g., Grumpy, Energetic)? ")
    
    my_pet = Pet(name, personality)

    while True:
        my_pet.get_status()
        choice = input("\nWhat do you want to do? (feed/play/quit): ").lower()
        
        if choice == "feed":
            my_pet.feed()
        elif choice == "play":
            my_pet.play()
        elif choice == "quit":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again!")

if __name__ == "__main__":
    start_game()