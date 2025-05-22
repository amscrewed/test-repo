import random
import time

PULLED_CARDS = set()
SUITES = [ "diamonds", "clubs", "spades", "hearts" ]
NAMEDC = { 1: "ACE", 11: "JACK", 12: "QUEEN", 13: "KING" }

def main():
    ROUND = 1
    random.seed(int(time.time())) # now the fun can begin
    
    query = input("Hit 'enter' to pull a card.\n")
    
    while query != "q" and ROUND =< 52:
        print(f"[ ROUND {ROUND} ]")
        cardno = random.randint(1, 13)
        suitno = random.randint(1, 4) - 1
        cardsu = SUITES[suitno]
        
        if cardno < 2 or cardno > 10: # ace, jack, queen, or king
            cardno = NAMEDC[cardno]
            
        pulled_card = (cardno, cardsu)
        
        if ROUND != 0 and pulled_card in PULLED_CARDS:
            continue
            
        PULLED_CARDS.add(pulled_card)
        
        print(f"{cardno} of {cardsu}")
        
        ROUND += 1
        query = input("Hit 'enter' to pull a card, or type 'q' to quit.\n")
        
        if query.lower() == "q":
            break;
            
    if ROUND >= 52:
        print("That's all the cards! Thanks for playing.")
    else:
        print("Thanks for playing.")
 
if __name__ == "__main__":
     main()