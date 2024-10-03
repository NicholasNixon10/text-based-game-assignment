
def load_game():
    with open('save_data.txt', 'r') as file:
        data = file.read().split()
    return data

def save_game(data):
    savetemp=str(data['health']) + " " +str(data['score'])
    with open('save_data.txt', 'w') as file:
        file.write(savetemp)

def new_game():
    return {"health": 100, "score": 0}

def display_stats(data):
    print(f"Health: {data['health']}, Score: {data['score']}")

def game():
    data={"health": 100, "score": 0}
    print("Welcome to the text-based adventure game!")
    
    choice = input("Do you want to load your previous game? (yes/no): ").lower()
    if choice == "yes":
        temp= load_game()
        data['health'] = int(temp[0])
        data['score'] = int(temp[1])
        print("Game loaded!")
    else:
        data = new_game()
        print("Starting a new game!")
    
    while True:
        display_stats(data)
        print("\nChoose an action:")
        print("1. Fight a monster (+10 score, -20 health)")
        print("2. Rest (+20 health, -5 score)")
        print("3. Save and exit")
        print("4. Exit without saving")
        
        action = input("Enter your choice (1-4): ")
        
        if action == "1":
            data['score'] += 10
            data['health'] -= 20
            print("\nYou fought a monster and gained 10 points, but lost 20 health!")
        elif action == "2":
            data['health'] += 20
            data['score'] -= 5
            print("\nYou took a rest and regained 20 health, but lost 5 points!")
        elif action == "3":
            save_game(data)
            print("\nGame saved! Exiting the game.")
            break
        elif action == "4":
            print("\nExiting the game without saving.")
            break
        else:
            print("\nInvalid choice. Try again.")
        
        if data['health'] <= 0:
            print("\nYou have lost all your health. Game over!")
            break

if __name__ == "__main__":
    game()