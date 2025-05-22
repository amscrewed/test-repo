import random

SUITES = ["diamonds", "clubs", "spades", "hearts"]
NAMEDC = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}

def main():
    DECK = [(card if 2 <= card <= 10 else NAMEDC[card], suit)
            for card in range(1, 14) for suit in SUITES]
    random.shuffle(DECK)
    
    print("^v^v^=== CARD PRINTER ===^v^v^\n")
    
    for ROUND, card in enumerate(DECK, start=1):
        print(f"[ ROUND {ROUND} ] {card[0]} of {card[1]}\n")
        query = input("Hit 'enter' to pull the next card, or type 'q' to quit.\n")
        if query.lower() == 'q':
            break
            
    print("Thanks for playing.")

if __name__ == "__main__":
    main()