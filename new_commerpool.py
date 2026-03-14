# newcomer_pool.py

def distribute_newcomer_bonus(tax_collected, newcomers):
    """
    Distributes the collected tax equally among all newcomers.
    """
    if not newcomers:
        return 0
    
    # Simple redistribution logic
    bonus_per_player = tax_collected / len(newcomers)
    return bonus_per_player

# --- Example Usage ---
total_tax_collected = 50.0  # Money taken from top earners
newcomer_list = ["Player_A", "Player_B", "Player_C"]

bonus = distribute_newcomer_bonus(total_tax_collected, newcomer_list)
print(f"Each newcomer receives a bonus of: {bonus:.2f}")
