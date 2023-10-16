# JazminEubanks
# Define the rooms and items in those rooms
rooms = {
    'Lobby': {'North': 'Jupiter', 'East': 'Neptune', 'South': 'Mercury', 'West': 'Saturn'},
    'Jupiter': {'South': 'Lobby', 'item': 'Fluorite'},
    'Neptune': {'West': 'Lobby', 'item': 'Amethyst'},
    'Mercury': {'North': 'Lobby', 'item': 'Aventurine'},
    'Saturn': {'East': 'Lobby', 'item': 'Citrine'},
    'Venus': {'West': 'Mars', 'item': 'Carnelian'},
    'Uranus': {'West': 'Mercury', 'item': 'Jade'},
    'Mars': {'East': 'Venus'}  # villain location
}

# display instructions


def show_instructions():
    print("Space Crystal Adventure Game")
    print("Collect all the space crystals to win the game, or be defeated by the Martians.")
    print("Move commands: go North, go East, go South, go West")
    print("Add to Inventory: get [item name]")


# Function to show player's status
def show_status(current_room, inventory):
    print("----------------------")
    print(f"You are in {current_room}")
    print(f"Inventory: {inventory}")
    if 'item' in rooms[current_room]:
        print(f"You see a {rooms[current_room]['item']}")
    print("----------------------")


# Main game loop
def main():
    current_room = 'Lobby'
    inventory = []
    show_instructions()

    while True:
        show_status(current_room, inventory)
        move = input("Enter your move: ").strip()

        # Handling player movement
        if move in ['go North', 'go East', 'go South', 'go West']:
            direction = move.split()[1]
            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
            else:
                print("You can't go that way!")
        elif move.startswith('get '):
            item = move.split()[1]
            if 'item' in rooms[current_room] and rooms[current_room]['item'] == item:
                inventory.append(item)
                del rooms[current_room]['item']
                print(f"{item} collected!")
            else:
                print("There's no such item here!")
        else:
            print("Invalid move!")

        # Check for game win or loss
        if current_room == 'Mars' and len(inventory) == 6:
            print(
                "Congratulations! You have collected all the crystals and defeated the Martians!")
            break
        elif current_room == 'Mars':
            print("Oh no! The Martians defeated you!")
            break


# Run the game
if __name__ == "__main__":
    main()
