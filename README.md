# CLI Flashcards

- An interactive command-line flashcard trainer built in Python. 
- Designed with user simplicity and memory retention at its core.
- Create your own decks with nothing more than a plain text file.

---

## Features

- Uses simple .txt files for flashcards (no CSVs or databases needed)
- Randomized questions to avoid memorization by order
- Progress tracking via (.save) files
- Weakness review: auto-generates weakness_ files with only the questions you missed
- Mastery rule: clears (.save) and (weakness_) files after 3 clean passes in a row
- Prompts to try another deck after finishing to refresh your brain

---

## Usage

1. Clone the repository:
   ```
   git clone https://github.com/<your-username>/CLI-Flashcards.git
   cd CLI-Flashcards
2. Run the script with Python 3:
   ```
   python3 CLI-Flashcards.py
3. Enter the name of the deck file when prompted:
   ```
   Pick deck by number or name: Linux_command_line_cards.txt
4. Answer flashcards, review mistakes in the "Checkpoint" directory, and repeat until mastery.
   
## Creating Decks

- Decks are just text files (.txt). 
- All you need to do is save a (.txt) file containing all of your questions and answers 
  in the same directory as the CLI-flasher.py and the script will handle the rest.
- Each flashcard is written as a pair of lines seperated by 1 empty space as follows:
```
How do you say spell hello in russian?
Привет

What command lists all files, including hidden ones?
ls -a

How do you show the current working directory?
pwd

What command shows running processes?
ps aux

How do you search text inside files?
grep
```
---
# Requirements

- Python 3.0 or higher
- Runs on any system with Python 3+ installed (Linux, macOS, Windows, BSD, etc.)
---



