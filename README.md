# Word Finder

A Python utility that finds English words in a grid of letters by taking one letter from each column, from left to right.

## Description

Word Finder searches for valid English words that can be formed by selecting one letter from each column of a letter grid, moving from left to right. The program uses a dictionary lookup to validate words and can process both user-input grids and grid files.

## Features

- Find all valid English words from a letter grid
- Process input from files or direct user input
- Output results to console or file
- Debug mode for troubleshooting
- Automatic dictionary loading from system or fallback to built-in word list

## Installation

No installation required. Simply download the script and run it with Python 3.

```bash
git clone https://github.com/yourusername/word-finder.git
cd word-finder
```

## Usage

### Basic Usage

```bash
python word_finder.py
```
This will prompt you to enter a letter grid interactively.

### Using a Grid File

```bash
python word_finder.py example_grid.txt
```

### Output to File

```bash
python word_finder.py example_grid.txt --output results.txt
```
or
```bash
python word_finder.py example_grid.txt -o results.txt
```

### Debug Mode

```bash
python word_finder.py example_grid.txt --debug
```

## Input Format

The input grid should be formatted as rows of letters. For example:

```
ABCEF
DPSFJ
IJPKE
DFELF
FIEJF
```

## Example Files

The repository includes several example grid files:
- `example_grid.txt` - A simple example grid
- `thick_grid.txt` - A grid with more rows
- `wagon_grid.txt` - A grid containing the word "WAGON"
- `veritas_grid.txt` - A grid with the word "VERITAS"
- `infinite_grid.txt` - A larger example grid

Corresponding result files are also included for some grids.

## How It Works

1. The program loads a dictionary of English words from the system or uses a built-in list
2. It parses the input grid and converts it to columns
3. Using backtracking, it generates all possible words by taking one letter from each column
4. It checks each generated word against the dictionary
5. It outputs all valid words found, sorted alphabetically

## Requirements

- Python 3.x

## License

This work is licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).

## Author

Josh Todd
