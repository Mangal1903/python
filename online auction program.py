import random

class AuctionItem:
    def _init_(self, name, starting_price):
        self.name = name
        self.starting_price = starting_price
        self.current_bid = starting_price
        self.winner = None

    def place_bid(self, bidder, bid_amount):
        if bid_amount > self.current_bid:
            print(f"{bidder} placed a bid of ${bid_amount} on {self.name}")
            self.current_bid = bid_amount
            self.winner = bidder
        else:
            print(f"Sorry, {bidder}, your bid of ${bid_amount} is too low. The current bid is ${self.current_bid}")

    def _str_(self):
        if self.winner:
            return f"{self.name} - Winning bid: ${self.current_bid} by {self.winner}"
        else:
            return f"{self.name} - Current bid: ${self.current_bid}"

class AuctionHouse:
    def _init_(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def conduct_auction(self):
        print("Auction House - Online Auction")
        print("Items for Auction:")
        for item in self.items:
            print(item)

        print("\nLet the auction begin!")
        for item in self.items:
            print(f"\nAuctioning {item.name}...")
            bidders = ["Bidder1", "Bidder2", "Bidder3"]
            for _ in range(3):  # Simulate three rounds of bidding
                bidder = random.choice(bidders)
                bid_amount = random.randint(item.current_bid + 1, item.current_bid + 10)
                item.place_bid(bidder, bid_amount)
            print(f"The winner of {item.name} is {item.winner} with a bid of ${item.current_bid}")

if _name_ == "_main_":
    house = AuctionHouse()

    item1 = AuctionItem("Item 1", 10)
    item2 = AuctionItem("Item 2", 20)
    item3 = AuctionItem("Item 3", 30)

    house.add_item(item1)
    house.add_item(item2)
    house.add_item(item3)

    house.conduct_auction()