from Cards.Card import Card, Rank

# DONE (TASK 3): Implement a function that evaluates a player's poker hand.
#   Loop through all cards in the given 'hand' list and collect their ranks and suits.
#   Use a dictionary to count how many times each rank appears to detect pairs, three of a kind, or four of a kind.
#   Sort these counts from largest to smallest. Use another dictionary to count how many times each suit appears to check
#   for a flush (5 or more cards of the same suit). Remove duplicate ranks and sort them to detect a
#   straight (5 cards in a row). Remember that the Ace (rank 14) can also count as 1 when checking for a straight.
#   If both a straight and a flush occur in the same suit, return "Straight Flush". Otherwise, use the rank counts
#   and flags to determine if the hand is: "Four of a Kind", "Full House", "Flush", "Straight", "Three of a Kind",
#   "Two Pair", "One Pair", or "High Card". Return a string with the correct hand type at the end.
def evaluate_hand(hand: list[Card]):

    rank_list = []
    suit_list = []
    rank_counts = dict()
    suit_counts = dict()

    is_flush = False
    flush_suit = ""

    is_straight = False

    flush_ranks = []

    temp_ranks = dict()
    two = False
    three = False


    for card in hand:
        rank_list.append(card.rank.value)
        suit_list.append(card.suit)
        rank_counts[card.rank] = rank_counts.get(card.rank, 0) + 1
        suit_counts[card.suit] = suit_counts.get(card.suit, 0) + 1
    rank_counts = dict(sorted(rank_counts.items(),key=lambda item: (item[1], item[0].value), reverse=True))

    for suit in suit_counts:
        if suit_counts[suit] >= 5:
            is_flush = True
            flush_suit = suit
            break

    unique_ranks = sorted(set(rank_list))
    for i in range(len(unique_ranks) -  4):
        possible_straight = unique_ranks[i:(i + 5)]
        if max(possible_straight) - min(possible_straight) == 4 and len(set(possible_straight)) == 5:
            is_straight = True
            break
    if {Rank.ACE.value, Rank.TWO.value, Rank.THREE.value, Rank.FOUR.value, Rank.FIVE.value}.issubset(unique_ranks):
        is_straight = True

    if is_straight and is_flush:
        for card in hand:
            if card.suit == flush_suit:
                flush_ranks.append(card.rank.value)
        unique_flush_ranks = sorted(set(flush_ranks))
        for i in range(len(unique_flush_ranks) - 4):
            possible_straight = unique_flush_ranks[i:(i + 5)]
            if max(possible_straight) - min(possible_straight) == 4 and len(set(possible_straight)) == 5:
                return "Straight Flush"
        if {Rank.ACE.value, Rank.TWO.value, Rank.THREE.value, Rank.FOUR.value, Rank.FIVE.value}.issubset(unique_flush_ranks):
                return "Straight Flush"

    if 4 in rank_counts.values():
        return "Four of a Kind"
    else:
        for card in hand:
            saved_rank = card.rank
            temp_ranks[saved_rank] = temp_ranks.get(saved_rank, 0) + 1
        for rank in temp_ranks:
            if temp_ranks[rank] == 2:
                two = True
            elif temp_ranks[rank] == 3:
                three = True
        if two and three:
            return "Full House"

    if is_flush:
        return "Flush"
    elif is_straight:
        return "Straight"
    elif 3 in rank_counts.values():
        return "Three of a Kind"
    else:
        counter = 0
        for rank in rank_counts:
            if rank_counts[rank] == 2:
                counter += 1
        if counter == 2:
            return "Two Pair"
        elif counter == 1:
            return "One Pair"

    return "High Card" # If none of the above, it's High Card
# DONE (TASK 3) (Teammate A: Adrián E. Quiñones Pérez)
