import re

with open('4-Scratchcards.txt') as file:
    # Part Two
    # Dictionary of all card numbers(key) and their copies(value) 
    cards = {}
    for i in range(205):
        cards[i+1] = 1
    cardnumber = 0
    
    # Part One
    total_points = 0
    for line in file:
        line = re.sub(r'Card\s+\d+:\s', '', line)
        winners, mine = [l.split() for l in line.split(' | ')]
        # Count of winning numbers
        n = 0
        for w in winners:
            if w in mine:
                n += 1
        # Calculate points for the card and add it to the total
        points = 0 if n == 0 else 2**(n-1)
        total_points += points
        
        # Part Two
        # Add copies to the next range n of cards
        cardnumber += 1
        for c in range(cardnumber + 1, cardnumber + 1 + n):
            cards[c] += cards[cardnumber]
    
    # Part Two
    total_cards = sum(cards.values())
    print(f'total_cards = {total_cards}')
    
    print(f'total_points = {total_points}')

