from collections import Counter
from model import FrenchDeck

def create_players(players_size: int) -> list:
    """
    change me
    """
   
    deck = FrenchDeck()
    deck.shuffle()

    # generate a init for each player
    players = [[] for _ in range(players_size)]

    deal_cards = 52 - 5 * len(players)
    while len(deck) > deal_cards:
        for player in players:
            player.append(deck.deal())

    return players


def _check_straight(hand):
    values = sorted(set([card.value for card in hand]))
    if len(values) < 5:
        return None
    
    straight = [values[0]]
    for i in range(1, len(values)):
        if values[i] == straight[-1] + 1:
            straight.append(values[i])
            if len(straight) == 5:
                straight_cards = [card for card in hand if card.value in straight]
                return {
                    'hand': straight_cards,
                    'combination': 'Straight'
                }
        else:
            straight = [values[i]]
        
    # check for whell straight (A-2-3-4-5)
    whell_straight_list = [2, 3, 4, 5, 14]
    if values == whell_straight_list:
        straight_cards = [card for card in hand if card.value in whell_straight_list]
        return {
            'hand': straight_cards,
            # 'combination': 'Low straight'
            'combination': 'Straight'
        }
    
    return None

def is_royal_flush(hand):
    ranks = [n.value for n in hand]
    suits = [n.suit for n in hand]
    rank_counter = Counter(n.value for n in hand)
    top_ranks = [10, 11, 12, 13, 14]

    flush = len(set(suits)) == 1
    royal_flush_suits = all(True if card.value in top_ranks else False for card in hand)

    if flush and royal_flush_suits:
        return True

    
def check_combinations(hand):
    """Find pairs (including three and four of a kind) in the given hand."""
    ...
    if len(hand) != 5:
        raise ValueError('A hand must contain exactly 5 cards')
    
    ranks = [n.value for n in hand]
    suits = [n.suit for n in hand]
    rank_counter = Counter(n.value for n in hand)

    # check to compare in the card same values by suit
    pairs = [n for n, count in rank_counter.items() if count == 2]
    triples = [n for n, count in rank_counter.items() if count == 3]
    quads = [n for n, count in rank_counter.items() if count == 4]
    flush = len(set(suits)) == 1
    straight = _check_straight(hand)
    royal_flush = is_royal_flush(hand)

    if royal_flush:
        return {
            'hand': hand,
            'combination': 'Royal flush'
        }
    
    if flush and straight:
        return {
            'hand': hand,
            'combination': 'Straight flush'
        }

    if quads:
        quads_rank = quads[0]
        quads_cards = [n for n in hand if n.value == quads_rank]
        kicker_cards = sorted([n for n in hand if n.value != quads_rank], reverse=True)
        return {
            'hand': quads_cards + kicker_cards,
            'combination': 'Four of a kind'
        }
    
    if pairs and triples:
        return {
            'hand': [n for n in hand if n.value == triples[0]] + [n for n in hand if n.value == pairs[0]],
            'combination': 'Full house'
        }
        
    if flush:
        return {
            'hand': hand,
            'combination': 'Flush'
        }

    if straight:
        return straight
    
    if triples:
        triples_rank = triples[0]
        triples_cards = [n for n in hand if n.value == triples_rank]
        kicker_cards = sorted([n for n in hand if n.value != triples_rank], reverse=True)
        return {
            'hand': triples_cards + kicker_cards,
            'combination': 'Three of a kind'
        }

    if pairs:
        pairs_rank = pairs[0]
        pairs_cards = [n for n in hand if n.value == pairs_rank]
        kicker_cards = sorted([n for n in hand if n.value != pairs_rank], reverse=True)
        return {
            'hand': pairs_cards + kicker_cards,
            'combination': 'Two pairs'
        }
    else:
        return {
            'hand': hand,
            'combination': 'No pairs' # add checker to low, high cards it hand
        }
    

def create_combination_map():
    """
    change me
    """
    combinations = 'Two pairs, Three of a kind, Straight, Flush, Full house, Four of a kind, Straight flush, Royal flush'.split(',')
    combinations_map = res_mapping = {comb.strip(): idx + 2 for idx, comb in enumerate(combinations) }
    res_mapping['No pairs'] = 1
    invert_combination_map = {v: k for k, v in res_mapping.items()}

    return combinations_map, invert_combination_map


def load_scores(hand):
    """
    Load a list of players scores from a players hand
    Parameters:
        a list of player cards.

    Returns:
        list: A list of player scores.
    """
    combinations_map, _ = create_combination_map()
    combinations = [check_combinations(player)['combination'] for player in hand]
    scores = [combinations_map[combination] for combination in combinations]
    
    return scores


def count_scores(player_scores: list) -> Counter:
    """
    Count the number of occurrences of each score in a list of player scores.
    
    Parameters:
        player_scores (list): A list of player scores.

    Returns:
        Counter: A Counter object mapping each score to its frequency.
    """
    score_counts = Counter(player_scores
                           )
    return score_counts


def find_highest_score(player_scores: list) -> int:
    """
    Find the highest score in a list of player scores.
    
    Parameters:
        player_scores (list): A list of player scores.

    Returns:
        int: The highest score in the list.
    """
    highest_score = max(player_scores)

    return highest_score


def find_winners(player_scores: list, highest_score: int) -> list:
    """
    Find the indices of the players who achieved the highest score.
    
    Parameters:
        player_scores (list): A list of player scores.
        highest_score (int): The highest score in the list.

    Returns:
        list: A list of indices of players who achieved the highest score.
    """
    winners = [n + 1 for n in range(len(player_scores)) if player_scores[n] == highest_score]

    return winners


def create_header(header_text: str) -> str:
    """
    Create a header string
    
    Parameters:
        header_text (str): The text to display in the header.

    Returns:
        str: The header string.
    """
    header = header_text + '\n' + "=" * len(header_text)

    return header


def announce_winner(winners_score: list, highest_score: int, players: list) -> str:
    """
    Announce the winner or winners of the game.
    
    Parameters:
        winners (list): A list of indices of players whoe achieved the highest score.
        highest_score (int): The highest score in the list.
        players (list): A list of players card in his hand.
    """
    _, invert_combination_map = create_combination_map()
    scores = winners_score # T)DO: cc to params *args to all inits inside
    hs = highest_score
    winners = [n + 1 for n in range(len(scores)) if scores[n] == hs]
        # players_outside_this_def = create_players() # отдельно cuz type a how much players on the table with a table; are at the table;
    # scores = load_scores(players)
    # hs = find_highest_score(winners_score)
    # winners = find_winners(winners_score, highest_score)
    if len(winners) == 1:
        print(create_header("Winner Announcement!"))
        winner = winners[0]
        report = f"Player {winner} is win with the {invert_combination_map[hs]}"
        header = create_header(report)
        print(header)
    else:
        print(create_header("Tie Breaker!"))
        winner_str = ", ".join([str(winner) for winner in winners])
        report = f"Player {winner_str} is win with the {invert_combination_map[hs]}"
        header = create_header(report)
        print(header)

        score_idx = winners
        score_idx = [n - 1 for n in score_idx]
        players_score = pc = [players[n] for n in score_idx]
        # by sum of all card in the hand
        if hs == 1:
            print(create_header("Winner Announcement!"))
            player_sum_map = {score_idx[idx]: sum([n.value for n in hand]) for idx, hand in enumerate(pc)}
            # winner, sum_card_scores = [(player, score) for player, score in player_sum_map.items() if score == max(player_sum_map.values())][0]
            winner, sum_card_scores = [(player + 1, score) for player, score in player_sum_map.items() if score == max(player_sum_map.values())][0]
            winner
            report = f"Player {winner} is win with a sum of score is {sum_card_scores}"
            header = create_header(report)
            print(header)
        else:
            print(create_header("Winner Announcement!"))
            # print('score idx: ', score_idx)
            combination_player_scores_map = {score_idx[idx]: Counter([n.value for n in hand]).most_common()[0][0] for idx, hand in enumerate(pc)}
            # print('comb players scores map:', combination_player_scores_map)
            # winner, score = [(player, score) for player, score in combination_player_scores_map.items() if score == max(combination_player_scores_map.values())][0]
            # cuz tie was with players idx + 1; after cc to -1; to score_idx; to +f real players
            winner, score = [(player + 1, score) for player, score in combination_player_scores_map.items() if score == max(combination_player_scores_map.values())][0]
            report = f"Player {winner} is win with a score of {score}"
            header = create_header(report)
            print(header)

 
def display_combination_cards_distribution(score_counts: Counter):
    """
    Display the distribution of scores in a list of player scores.
    
    Parameters:
        score_counts (Counter): A Counter object mapping each score to its frequency.
    """
    _, invert_combination_map = create_combination_map()
    
    print(create_header('Combination cards distribution:'))
    for score, count in sorted(score_counts.items(), reverse=True):
            print(f"{invert_combination_map[score]}: {count} players")


def determine_winner(player_scores, players):
    """
    Determine the winner or winners of the game and display the score distribution.
    
    Parameters:
        player_scores (list): A list of player scores.
    """
    score_counts = count_scores(player_scores)
    highest_score = find_highest_score(player_scores)
    winners = find_winners(player_scores, highest_score)

    announce_winner(winners, highest_score, players)

    display_score_distribution(score_counts)


        

