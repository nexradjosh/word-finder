#!/usr/bin/env python3
"""
Word Finder

This script finds English words in a grid of letters by taking one letter from each column,
from left to right.
"""

import sys
import os
from typing import List, Set

def load_dictionary() -> Set[str]:
    """
    Load a dictionary of English words.
    Returns a set of uppercase words for faster lookup.
    """
    # Try to find a dictionary file
    dictionary_paths = [
        '/usr/share/dict/words',  # Common on Unix/Linux/macOS
        'words.txt',  # Fallback if user has a local file
    ]
    
    for path in dictionary_paths:
        if os.path.exists(path):
            with open(path, 'r') as f:
                # Convert all words to uppercase for case-insensitive matching
                return {word.strip().upper() for word in f if word.strip().isalpha()}
    
    # If no dictionary file is found, use a small built-in list of common words
    print("Warning: No dictionary file found. Using a limited built-in word list.")
    common_words = """
    ABOUT AFTER AGAIN ALONG ALSO APPLE AWAY BACK BALL BEEN BEFORE BEGIN BEING
    BELOW BETWEEN BOTH BRING BUILD BUILT CALL CAME CANNOT CAUSE CHANGE CHECK
    CHILD CITY CLOSE COME COULD COUNTRY CREATE DARK DAY DEEP DOES DONE DOWN
    DRAW DRIVE EACH EARLY EARTH EAST EASY EIGHT ELSE ENOUGH EVEN EVER EVERY
    FACE FACT FALL FAMILY FAR FAST FATHER FEEL FEET FIELD FIND FIRE FIRST FISH
    FIVE FOOD FORM FOUND FOUR FROM FRONT FULL GAME GAVE GIVE GOES GOOD GREAT
    GREEN GROW HALF HAND HARD HAVE HEAD HEAR HEART HELP HERE HIGH HOLD HOME
    HORSE HOUSE IDEA KEEP KIND KNOW LAND LARGE LAST LATE LEARN LEAVE LEFT LESS
    LIGHT LIKE LINE LIST LITTLE LIVE LONG LOOK MADE MAKE MANY MEAN MIGHT MILE
    MIND MISS MOST MOVE MUCH MUST NAME NEAR NEED NEVER NEW NEXT NIGHT NINE
    NORTH NOTHING NOW NUMBER OFTEN ONCE ONLY OPEN ORDER OTHER OVER OWN PAGE
    PAIR PART PASS PEOPLE PICTURE PLACE PLAN PLAY POINT POWER PULL PUSH PUT
    QUICK QUITE READ READY REAL RIGHT RIVER ROAD ROCK ROOM ROUND RULE SAID SAME
    SCHOOL SECOND SEEM SEEN SEND SENT SEVEN SHAPE SHARE SHOW SIDE SIMPLE SINCE
    SIZE SLEEP SLOW SMALL SNOW SOME SONG SOON SOUND SOUTH SPELL STAND START
    STATE STAY STEP STILL STOP STORY STRONG STUDY SUCH SURE TAKE TALK TELL THAN
    THAT THEIR THEM THEN THERE THESE THEY THING THINK THIS THOSE THOUGHT THREE
    THROUGH TIME TODAY TOGETHER TOLD TOOK TOWN TREE TRUE TRY TURN UNDER UNTIL
    UPON VERY VOICE WAIT WALK WANT WARM WASH WATER WAVE WEEK WELL WENT WERE
    WEST WHAT WHEEL WHEN WHERE WHICH WHILE WHITE WILL WITH WOMAN WOOD WORD
    WORK WORLD WOULD WRITE YEAR YOUNG
    """
    return {word.strip() for word in common_words.split() if word.strip()}

def parse_grid(grid_text: str) -> List[List[str]]:
    """
    Parse a grid of letters from input text.
    Returns the grid as a list of columns (not rows).
    """
    # Split the input text into rows
    rows = [row.strip() for row in grid_text.strip().split('\n') if row.strip()]
    
    # Convert to columns for easier word generation
    num_cols = max(len(row) for row in rows)
    columns = [[] for _ in range(num_cols)]
    
    for row in rows:
        for col_idx, char in enumerate(row):
            if char.strip():  # Skip whitespace
                columns[col_idx].append(char.upper())
    
    return columns

def find_words(columns: List[List[str]], dictionary: Set[str]) -> List[str]:
    """
    Find all valid English words that can be formed by taking one letter
    from each column, from left to right.
    """
    found_words = []
    
    def backtrack(col_idx: int, current_word: str):
        # If we've used all columns, check if the word is valid
        if col_idx == len(columns):
            if current_word in dictionary:
                found_words.append(current_word)
            return
        
        # Try each letter in the current column
        for letter in columns[col_idx]:
            backtrack(col_idx + 1, current_word + letter)
    
    backtrack(0, "")
    return sorted(found_words)

def main():
    # Check if input is provided as a file
    debug_mode = '--debug' in sys.argv
    output_file = None
    input_file = None
    
    # Parse command line arguments
    i = 1
    while i < len(sys.argv):
        if sys.argv[i] == '--output' or sys.argv[i] == '-o':
            if i + 1 < len(sys.argv):
                output_file = sys.argv[i + 1]
                i += 2
            else:
                print(f"Error: Missing filename after {sys.argv[i]}")
                return
        elif not sys.argv[i].startswith('--') and input_file is None:
            input_file = sys.argv[i]
            i += 1
        else:
            i += 1
    
    if input_file:
        try:
            with open(input_file, 'r') as f:
                grid_text = f.read()
        except FileNotFoundError:
            print(f"Error: File '{input_file}' not found.")
            return
    else:
        # Otherwise, prompt for input
        print("Enter your letter grid (press Enter twice when done):")
        grid_lines = []
        while True:
            line = input()
            if not line:
                break
            grid_lines.append(line)
        grid_text = '\n'.join(grid_lines)
    
    # Load dictionary
    dictionary = load_dictionary()
    
    # Parse grid
    columns = parse_grid(grid_text)
    
    # Print column information in debug mode
    if debug_mode:
        print("\nGrid columns:")
        for i, col in enumerate(columns):
            print(f"Column {i+1}: {col}")
        print()
        
        # Generate all possible words for debugging
        print("Checking all possible words...")
        all_possible = []
        
        def generate_words(col_idx, current):
            if col_idx == len(columns):
                all_possible.append(current)
                return
            for letter in columns[col_idx]:
                generate_words(col_idx + 1, current + letter)
        
        generate_words(0, "")
        print(f"Total combinations: {len(all_possible)}")
        print("First 20 combinations:", all_possible[:20])
        print()
        
        # Check for specific words
        test_words = ["APPLE", "HELLO", "WORLD", "TEST"]
        print("Checking for specific test words:")
        for word in test_words:
            possible = True
            for i, letter in enumerate(word):
                if i >= len(columns) or letter not in columns[i]:
                    possible = False
                    print(f"'{word}' cannot be formed: '{letter}' not in column {i+1}")
                    break
            if possible:
                print(f"'{word}' can potentially be formed!")
        print()
    
    # Find words
    words = find_words(columns, dictionary)
    
    # Prepare output
    if words:
        result = f"Found {len(words)} words:\n" + "\n".join(words)
    else:
        result = "No words found."
    
    # Write to output file if specified
    if output_file:
        try:
            with open(output_file, 'w') as f:
                f.write(result)
            print(f"Results written to {output_file}")
        except Exception as e:
            print(f"Error writing to output file: {e}")
    
    # Print results to console
    print(result)

if __name__ == "__main__":
    main()
