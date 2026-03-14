# game_economy.py

def calculate_realized_money(treasure_amount, player_balance):
    # 1. Conversion Rate: Treasure to Money
    conversion_rate = 0.8
    realized_amount = treasure_amount * conversion_rate
    
    # 2. Majority Stack Logic (The "Growth Tax")
    # If the player is already wealthy (e.g., > 1000), tax the new money by 5%
    if player_balance > 1000:
        tax = realized_amount * 0.05
        realized_amount -= tax
        print(f"Majority Stack Tax applied: {tax:.2f} deducted.")
    
    return realized_amount

# --- Example Usage ---
current_treasure = 500
current_wallet = 1200 # This player is a "Top Earner" (over 1000)

final_money = calculate_realized_money(current_treasure, current_wallet)
print(f"Treasure converted! You received: {final_money:.2f}")
