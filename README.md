# CLI Flashcards

An interactive **command-line flashcard trainer** built in Python.  
Designed for simplicity: create your own decks with nothing more than a plain text file.

---

## Features

- Uses simple .txt files for flashcards (no CSVs or databases needed)
- Randomized questions to avoid memorization by order
- Progress tracking via .save files
- Weakness review: auto-generates weakness_ files with only the questions you missed
- Mastery rule: clears .save and weakness_ files after 3 clean passes in a row
- Prompts to try another deck after finishing to refresh your brain

---

## Creating Decks

- Decks are just text files (.txt). 
- All you need to do is save a (.txt) file containing all of your questions and answers 
  in the same directory as the CLI-flasher.py and the script will handle the rest.
- Each flashcard is written as a pair of lines seperated by 1 empty space as follows:
-
- 2x2=
- 4
-
- Hello in russian?
- Привет


---

# Development Notes
- I created this flashcard trainer to aid people who need a diverse range of learning needs. In time this will be the ultimate open-source flashcard machine!
