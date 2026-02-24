import random

deck=[]


def create_deck():
    suits=["Hearts","Spades","Diamonds","Clubs"]
    ranks=["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]

    for suit in suits:
        for rank in ranks:
            deck.append(f"{rank} of {suit}")

    return deck


def shuffle_deck():
    random.shuffle(deck)
 

def display_deck():
    for card in deck:
        print(card) 


def main():
    print("-----Creating a new deck of cards-----")

    create_deck()

    print("Deck before shuffling:\n")
    display_deck()

    input("\nPress Enter to shuffle the deck...")

    shuffle_deck()

    print("\nDeck after shuffling:\n")
    display_deck()
    
if __name__ == "__main__":
    main()
 
        
