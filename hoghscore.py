if game_state == "GAME_OVER":
    # 1. Update the record
    update_high_score(player_balance)
    
    # 2. Render UI
    screen.fill((0, 0, 0))
    score_text = font.render(f"Final Score: {player_balance:.2f}", True, (255, 255, 255))
    high_text = font.render(f"High Score: {high_score:.2f}", True, (255, 215, 0))
    screen.blit(score_text, (200, 250))
    screen.blit(high_text, (200, 300))
    
    # 3. Add a restart instruction
    restart_text = font.render("Press 'R' to Restart", True, (200, 200, 200))
    screen.blit(restart_text, (200, 400))
