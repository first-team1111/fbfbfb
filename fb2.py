def play_optimal(n):
    # using 0-99 instead of ranges 1-100
    pardoned = 0
    in_drawer = list(range(100))
    for _round in range(n):
        random.shuffle(in_drawer)
        for prisoner in range(100):
            reveal = prisoner
            found = False
            for go in range(50):
                card = in_drawer[reveal]
                if card == prisoner:
                    found = True
                    break
                reveal = card
            if not found:
                break
        if found:
            pardoned += 1
    return pardoned / n * 100   # %
