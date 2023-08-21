def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    alphabet_size = 26
    grid_size = 5 * 5
    total_possible_keys = factorial(grid_size)
    
    print(f"Total possible keys without considering identical encryption results: {total_possible_keys}")

    approximate_power_of_2 = int(total_possible_keys.bit_length())
    print(f"Approximate number of keys as a power of 2: 2^{approximate_power_of_2}")

if __name__ == "__main__":
    main()
