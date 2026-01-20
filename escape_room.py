def escape_room():
    # 1. Game Setup
    # The 'rooms' dictionary holds the data for our world
    rooms = {
        "Hallway": {
            "description": "a long, dimly lit hallway with a heavy door to the North.",
            "item": "key",
            "next_room": "Vault"
        },
        "Vault": {
            "description": "a cold, steel room filled with gold. You see a window to the East.",
            "item": "map",
            "next_room": "Exit"
        }
    }
    
    current_room = "Hallway"
    inventory = []
    
    print("--- 🚪 Escape the Locked Room 🚪 ---")
    print("Find items and move through rooms to reach the exit!")

    # 2. Main Game Loop
    while True:
        room_data = rooms[current_room]
        print(f"\nYou are in the {current_room}. It is {room_data['description']}")
        
        # Check for items
        if room_data["item"] and room_data["item"] not in inventory:
            print(f"🔍 You see a {room_data['item']} here!")

        action = input("\nWhat do you want to do? [grab / move / quit]: ").lower().strip()

        if action == "quit":
            break
        
        # 3. Game Logic
        elif action == "grab":
            item = room_data["item"]
            if item and item not in inventory:
                inventory.append(item)
                print(f"✅ You picked up the {item}!")
            else:
                print("❌ Nothing left to grab here.")

        elif action == "move":
            # Check if player has the required item to move forward
            if "key" in inventory:
                if current_room == "Vault":
                    print("🎉 You used the map to find the exit! YOU ESCAPED!")
                    break
                else:
                    current_room = room_data["next_room"]
                    print(f"🏃 You move into the {current_room}...")
            else:
                print("🔒 The door is locked! You need a 'key' to move.")
        
        else:
            print("Invalid command.")

# Start the game
escape_room()
