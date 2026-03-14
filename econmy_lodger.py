# economy_logger.py
import datetime

def log_transaction(transaction_type, amount, player_id="ANON"):
    """
    Records an economic event to a secure, local log file.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Only store the event type, the amount, and a placeholder ID
    log_entry = f"[{timestamp}] TYPE: {transaction_type} | AMOUNT: {amount:.2f} | USER: {player_id}\n"
    
    with open("economy_audit.log", "a") as f:
        f.write(log_entry)

# --- Example Usage ---
# Log a tax collection
log_transaction("GROWTH_TAX", 50.0, "USER_99")
# Log a distribution
log_transaction("NEWCOMER_BONUS", 16.67, "USER_01")
