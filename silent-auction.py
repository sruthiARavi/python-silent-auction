import logo

print(logo.gavel_art)
print("Welcome to the silent auction program.")

# Same name and same bid cases are not handled
def find_auction_winner(user_bids):
    winner = ""
    winner_bid = -1

    for bidder in user_bids:
        bid = user_bids[bidder]
        winner_bid = max(winner_bid, bid)
        if winner_bid == bid:
            winner = bidder

    print(f"The winner is {winner} with a bid of ${winner_bid}")

user_bids = {}
should_continue = "yes"

while should_continue == "yes":
    user_name = input("What is your name?: ")
    user_bid = input("What is your bid?: $")
    user_bids[user_name] = int(user_bid)
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    print("\n" * 20)  # For clearing the screen. We can instead multiply by 100 if needed.

find_auction_winner(user_bids)
