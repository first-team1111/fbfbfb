if __name__ == '__main__':
    n = 100_000
    print(" Simulation count:", n)
    print(f" Random play wins: {play_random(n):4.1f}% of simulations")
    print(f"Optimal play wins: {play_optimal(n):4.1f}% of simulations")
