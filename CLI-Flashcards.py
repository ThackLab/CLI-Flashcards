#!/usr/bin/env python3

import os, sys, random

GREEN = "\033[92m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"

SAVE_DIR = ".GotchuBro"
CHECK_DIR = "Checkpoint"
os.makedirs(SAVE_DIR, exist_ok=True)
os.makedirs(CHECK_DIR, exist_ok=True)


def banner():
    art = f"""{GREEN}{BOLD}
                         __    _                                   
                    _wr""        "-q__                             
                 _dP                 9m_     
               _#P                     9#_                         
              d#@                       9#m                        
             d##                         ###                       
            J###                         ###L                      
            {{###K                       J###K                      
            ]####K      ___aaa___      J####F                      
        __gmM######_  w#P""   ""9#m  _d#####Mmw__                  
     _g##############mZ_         __g##############m_               
   _d####M@PPPP@@M#######Mmp gm#########@@PPP9@M####m_             
  a###""          ,Z"#####@" '######"\\g          ""M##m           
 J#@"             0L  "*##     ##@"  J#              *#K          
 #"               `#    "_gmwgm_~    dF               `#_         
7F                 "#_   ]#####F   _dK                 JE         
]                    *m__ ##### __g@"                   F         
                       "PJ#####LP"                                
 `                       0######_                      '          
                       _0########_                                 
     .               _d#####^#####m__              ,              
      "*w_________am#####P"   ~9#####mw_________w*"                  
          ""9@#####@M""  
{RESET}"""
    print(art)
    print(
        f"{GREEN}{BOLD}"
        "########################################\n"
        "#      CLI Flashcard Trainer v6.4      #\n"
        "########################################"
        f"{RESET}"
    )


def parse_deck(path):
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()
    blocks = [b.strip().splitlines() for b in raw.split("\n\n") if b.strip()]
    return [(b[0].strip(), b[1].strip()) for b in blocks if len(b) >= 2]


def choose_deck():
    decks = [
        f
        for f in sorted(os.listdir("."))
        if f.endswith(".txt") and not f.endswith(".save")
    ]
    if not decks:
        print("[!] No .txt decks found.")
        sys.exit(1)
    print("\nAvailable decks:")
    for i, fn in enumerate(decks, 1):
        print(f"  {i}. {fn}")
    if len(decks) == 1:
        print(f"\nAuto-selecting {decks[0]}\n")
        return decks[0]
    while True:
        choice = input("Choose deck number: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(decks):
            return decks[int(choice) - 1]
        print("[!] Invalid choice.")


def update_weaknesses(deck_file, wrongs):
    """Append wrong questions to weaknesses_<deck>.txt and rebuild tally."""
    fname = os.path.join(CHECK_DIR, f"weaknesses_{deck_file}")
    tally = {}

    # Load existing tallies
    if os.path.exists(fname):
        with open(fname, "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("["):
                    num, q = line.strip().split("]", 1)
                    tally[q.strip()] = tally.get(q.strip(), 0) + int(num.strip("["))

    # Merge new wrongs
    for q in wrongs:
        tally[q] = tally.get(q, 0) + 1

    # Sort by frequency
    sorted_tally = sorted(tally.items(), key=lambda x: -x[1])

    # Rewrite full file
    with open(fname, "w", encoding="utf-8") as f:
        f.write("########## WRONG ##########\n")
        for q, n in sorted_tally:
            f.write(f"[{n}] {q}\n")

        if sorted_tally:
            cutoff = max(1, len(sorted_tally) // 10)  # top 10%
            f.write("\n########## SUMMARY ##########\n")
            f.write("Top 10% weakest questions:\n")
            for q, n in sorted_tally[:cutoff]:
                f.write(f"[{n}] {q}\n")


def handle_streak(deck_file, correct, total, wrongs):
    """Track mastery streaks and clean up when a deck is mastered."""
    streak_file = os.path.join(SAVE_DIR, f"streak_{deck_file}.count")

    # Load streak
    streak = 0
    if os.path.exists(streak_file):
        with open(streak_file, "r", encoding="utf-8") as f:
            try:
                streak = int(f.read().strip())
            except:
                streak = 0

    if correct == total and not wrongs:  # perfect run
        streak += 1
        with open(streak_file, "w", encoding="utf-8") as f:
            f.write(str(streak))
        if streak >= 3:
            print(
                f"""{GREEN}{BOLD}


▄▄     ·▄▄▄▄▄▌   ▄▄▄· ▄▄▌ ▐ ▄▌▄▄▌  ▄▄▄ ..▄▄ · .▄▄ ·      ▌ ▐·▪   ▄▄· ▄▄▄▄▄      ▄▄▄   ▄· ▄▌    ▄▄ 
██▌    ▐▄▄·██•  ▐█ ▀█ ██· █▌▐███•  ▀▄.▀·▐█ ▀. ▐█ ▀.     ▪█·█▌██ ▐█ ▌▪•██  ▪     ▀▄ █·▐█▪██▌    ██▌
▐█·    ██▪ ██▪  ▄█▀▀█ ██▪▐█▐▐▌██▪  ▐▀▀▪▄▄▀▀▀█▄▄▀▀▀█▄    ▐█▐█•▐█·██ ▄▄ ▐█.▪ ▄█▀▄ ▐▀▀▄ ▐█▌▐█▪    ▐█·
.▀     ██▌.▐█▌▐▌▐█ ▪▐▌▐█▌██▐█▌▐█▌▐▌▐█▄▄▌▐█▄▪▐█▐█▄▪▐█     ███ ▐█▌▐███▌ ▐█▌·▐█▌.▐▌▐█•█▌ ▐█▀·.    .▀ 
 ▀     ▀▀▀ .▀▀▀  ▀  ▀  ▀▀▀▀ ▀▪.▀▀▀  ▀▀▀  ▀▀▀▀  ▀▀▀▀     . ▀  ▀▀▀·▀▀▀  ▀▀▀  ▀█▄▀▪.▀  ▀  ▀ •      ▀ 

###############################################
       🎉 !3 Flawless runs in a row! 🫦 
 You've  mastered this deck — Move on proudly
and come back in 3 days then 1 week then 1 month 
         to lock into memory for life!!
###############################################{RESET}
"""
            )
            # cleanup all files
            save_file = os.path.join(SAVE_DIR, deck_file + ".save")
            weak_file = os.path.join(CHECK_DIR, f"weaknesses_{deck_file}")
            for f in [save_file, weak_file, streak_file]:
                if os.path.exists(f):
                    os.remove(f)
            return True  # mastered
    else:
        # reset streak
        with open(streak_file, "w", encoding="utf-8") as f:
            f.write("0")
    return False


def run_deck(deck_file, shuffle=False):
    items = parse_deck(deck_file)
    if shuffle:
        random.shuffle(items)

    save_file = os.path.join(SAVE_DIR, deck_file + ".save")
    answered = set()

    if os.path.exists(save_file):
        with open(save_file, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.split("|", 1)
                if parts and parts[0].strip().isdigit():
                    answered.add(int(parts[0].strip()))
        if answered:
            choice = (
                input(f"Found progress in {save_file}. Resume? (y/n): ").strip().lower()
            )
            if choice != "y":
                open(save_file, "w", encoding="utf-8").close()
                answered.clear()

    print(f"\nLoaded {len(items)} items from {deck_file}.\n")

    correct = total_asked = 0
    wrongs = []  # track wrong questions this run

    with open(save_file, "a", encoding="utf-8") as log:
        for idx, (q, a) in enumerate(items, 1):
            if idx in answered:
                continue
            print(f"{BOLD}[{idx}/{len(items)}] {q}{RESET}")
            resp = input("Your answer: ").strip()
            total_asked += 1

            if resp.lower() == a.lower():
                print(f"{GREEN}Correct!{RESET}\n")
                correct += 1
                status = "CORRECT"
            else:
                print(f"{RED}Wrong — answer: {a}{RESET}\n")
                status = "WRONG"
                wrongs.append(q)  # record the wrong question

            print(
                f"{idx} | {q} | user={resp} | expected={a} | {status}",
                file=log,
                flush=True,
            )

    percent = (correct / total_asked) * 100 if total_asked else 0
    print(f"{BOLD}Score this run: {correct}/{total_asked} ({percent:.1f} %){RESET}\n")

    # mastery check first
    if handle_streak(deck_file, correct, total_asked, wrongs):
        return

    if total_asked == len(items):
        if os.path.exists(save_file):
            os.remove(save_file)
        print("Deck completed! Save file removed.")

        # Only update weaknesses on a *clean full run*
        if wrongs:
            update_weaknesses(deck_file, wrongs)
            print(f"Weaknesses logged in Checkpoint/weaknesses_{deck_file}")
    else:
        print(f"Progress saved in {save_file}")


def main():
    banner()
    while True:
        deck_file = choose_deck()
        shuffle = input("Shuffle questions? (y/n): ").strip().lower() == "y"
        run_deck(deck_file, shuffle=shuffle)
        if input("Another deck? (y/n): ").strip().lower() != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nA new idea must never be judged by its initial result. ~Nicola Tesla")
        sys.exit(0)
