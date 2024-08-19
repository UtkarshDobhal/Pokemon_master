import random

def display_message(message):
    print("\n" + message + "\n")

def generate_random_power(base_power):
    return random.randint(base_power, base_power + 10)

def battle_pokemon(user_power, pokemon_power):
    display_message(f"⚔️ Battle time! Your power: {user_power} vs Pokémon power: {pokemon_power}")
    while True:
        action = input("Choose your action: (A)ttack or (U)se Item: ").strip().upper()
        while action not in ['A', 'U']:
            action = input("Invalid choice! Please enter (A)ttack or (U)se Item: ").strip().upper()

        if action == 'A':
            attack_power = random.randint(1, 10)
            display_message(f"👊 You chose to Attack! Your attack power: {attack_power}")
            user_power += attack_power
            break
        elif action == 'U':
            item_boost = random.randint(1, 5)
            display_message(f"🛡️ You used an Item! Boosted power: {item_boost}")
            user_power += item_boost
            break

    if user_power >= pokemon_power:
        return True, user_power
    else:
        return False, user_power

def play_game():
    display_message("🌟 Welcome to the Pokémon Power Adventure! 🌟")
    display_message("In this game, you'll encounter Pokémon with varying powers. Your goal is to defeat them and become stronger!")

    user_power = 15
    display_message(f"Your starting power is: {user_power} 💪")

    levels = 5
    for level in range(1, levels + 1):
        base_power = level * 10
        pokemon_power = generate_random_power(base_power)
        display_message(f"🔥 Level {level} 🔥")
        display_message(f"🌿 You encountered a Pokémon with power: {pokemon_power}")

        action = input("Do you want to (B)attle or (R)un? ").strip().upper()
        while action not in ['B', 'R']:
            action = input("Invalid choice! Please enter (B)attle or (R)un: ").strip().upper()

        if action == 'B':
            won, user_power = battle_pokemon(user_power, pokemon_power)
            if won:
                user_power += 2
                user_power += 4  
                display_message(f"🎉 You won the battle! Your power increased by 3 and you gained a bonus of 5 points! Your new power is {user_power} 🎉")
            else:
                display_message(f"😢 You lost the battle. Your power remains {user_power}. 😢")
        else:
            display_message("🚶 You chose to run away. Maybe you'll battle the next one!")

    display_message(f"🏆 Congratulations! You completed all levels with a final power of {user_power}. Thanks for playing! 🏆")

play_game()
