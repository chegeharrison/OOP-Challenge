# main.py

from pet import Pet
import time

def main():
    print("🐾 Welcome to the Digital Pet Simulator! 🐾")
    name = input("Give your pet a name: ")
    pet = Pet(name)
    print(f"\n🎉 {name} has been created!\n")
    time.sleep(1)

    while True:
        print("\nWhat would you like to do?")
        print("1. Feed your pet 🍗")
        print("2. Play with your pet 🎾")
        print("3. Teach a new trick 🎓")
        print("4. Show all tricks 🤹‍♂️")
        print("5. Check pet status 📊")
        print("6. Let your pet sleep 💤")
        print("7. Exit simulator ❌")

        choice = input("Enter your choice (1–7): ")

        if choice == "1":
            pet.eat()
        elif choice == "2":
            pet.play()
        elif choice == "3":
            trick = input("What trick would you like to teach? ")
            pet.train(trick)
        elif choice == "4":
            pet.show_tricks()
        elif choice == "5":
            pet.get_status()
        elif choice == "6":
            pet.sleep()
        elif choice == "7":
            print(f"\n👋 Goodbye! {pet.name} will miss you!\n")
            break
        else:
            print("❗ Invalid choice. Please enter a number from 1 to 7.")

        time.sleep(1.5)  # Add delay for a better user experience

if __name__ == "__main__":
    main()
