# 🚪 Escape the Locked Room - Text Adventure

A logic-based exploration game where players navigate through connected rooms, collect essential items, and solve environmental puzzles to find the exit. This project is a foundational step into game engine design.

This project focuses on teaching:
* **Nested Dictionaries:** Using complex data structures to represent a game world.
* **State Management:** Tracking the player's current location and inventory status.
* **Gatekeeping Logic:** Implementing "lock and key" mechanics using conditional checks.
* **List Manipulation:** Adding and checking for items in a player's inventory.

---

## ✨ Features

* **Dynamic Environments:** Each room has its own unique description and hidden items.
* **Inventory System:** Collect items like keys and maps that stay with you as you move.
* **Puzzle Mechanics:** Specific rooms are "locked" until you possess the correct item in your inventory.
* **Graceful Navigation:** Move between rooms using simple text commands.

---

## 🚀 How to Run the Game

### 1. Prerequisites
You need **Python 3** installed on your system.

### 2. Setup and Execution
1.  **Save the Code:** Save the Python script as `escape_room.py`.
2.  **Open Terminal:** Navigate to the folder where you saved the file.
3.  **Run the Script:**
    ```bash
    python escape_room.py
    ```

### 3. Gameplay Instructions
* **[Grab]:** Pick up any items you see in the current room.
* **[Move]:** Attempt to travel to the next room (some doors require keys!).
* **[Quit]:** Exit the game at any time.
* **Goal:** Reach the "Exit" room by finding the necessary tools to unlock your path.

---

## 🧠 Code Structure Highlights

### Mapping the World
Instead of writing 100 `if` statements, we store our world data in a dictionary. This makes it easy to add more rooms later without breaking the code logic.



### The Inventory Check
The "Gatekeeping" logic ensures that the player cannot progress too quickly. We check the `inventory` list before allowing a change to the `current_room` variable:

```python
if "key" in inventory:
    current_room = room_data['next_room'] # Unlock the door
else:
    print("The door is locked!") # Access denied

