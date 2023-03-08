import settings1


def main():
    players = settings1.create_players(size)
    scores = settings1.load_scores(players)

    highest_score = settings1.find_highest_score(scores)
    score_counts = settings1.count_scores(scores)

    settings1.announce_winner(scores, highest_score, players)
    settings1.display_combination_cards_distribution(score_counts)
    

if __name__ == "__main__":
    size = int(input('Type a count of players (2-10) at the poker table: '))
    main()
