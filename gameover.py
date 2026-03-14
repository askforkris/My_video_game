# Add these to your initialization
timer = 60.0  # 60 seconds
game_state = "PLAYING" # States: "PLAYING", "GAME_OVER"

# Inside your main while loop:
if game_state == "PLAYING":
    timer -= 1/60  # Subtract 1 second per 60 frames
    
    # Update movement and collision here...
    
    if timer <= 0:
        game_state = "GAME_OVER"

# Drawing logic
if game_state == "PLAYING":
    # Draw player, treasure, and balance...
elif game_state == "GAME_OVER":
    text = font.render(f"GAME OVER! Final Score: {player_balance:.2f}", True, (255, 0, 0))
    screen.blit(text, (200, 300))
