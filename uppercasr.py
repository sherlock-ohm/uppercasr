#!/usr/bin/env python3

import sys
import itertools
import argparse
import random

def capitalize_combinations(input_string):
    """
    Generate all possible combinations of capitalization for alphabetic characters in a string.
    Non-alphabetic characters remain unchanged.
    """
    return [
        ''.join(combo)
        for combo in itertools.product(
            *[(char.lower(), char.upper()) if char.isalpha() else (char,) for char in input_string.strip()]
        )
    ]

def process_file(file_path):
    """
    Read input from a file, remove blank lines, and generate capitalization combinations for all strings.
    """
    try:
        with open(file_path, 'r') as infile:
            input_lines = [line.strip() for line in infile if line.strip()]  # Remove blank lines and strip whitespace
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

    results = []
    for line in input_lines:
        results.extend(capitalize_combinations(line))  # Generate combinations directly
    return results

def main():
    parser = argparse.ArgumentParser(
        description="Generate all capitalization combinations for strings provided from a file."
    )
    parser.add_argument(
        "input",
        help="Path to the input file containing strings.",
    )
    parser.add_argument(
        "-o", "--output",
        help="Output file to save the results. If omitted, results are printed to stdout.",
    )
    args = parser.parse_args()

    # Process the input file
    results = process_file(args.input)

    # Shuffle the results for randomization
    random.shuffle(results)

    # Ask the user how many lines they want in the output
    while True:
        try:
            num_lines = int(input(f"Enter the number of lines to output (1-{len(results)}): "))
            if 1 <= num_lines <= len(results):
                break
            print(f"Please enter a valid number between 1 and {len(results)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Limit results to the specified number of lines
    results = results[:num_lines]

    # Write output
    if args.output:
        try:
            with open(args.output, 'w') as outfile:
                outfile.write('\n'.join(results) + '\n')  # Write combinations without blank lines
            print(f"Results saved to {args.output}")
        except IOError as e:
            print(f"Error writing to file '{args.output}': {e}")
            sys.exit(1)
    else:
        print('\n'.join(results))  # Print combinations to stdout

if __name__ == "__main__":
    main()
