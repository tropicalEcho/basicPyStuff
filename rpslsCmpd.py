import random, sys, os, time; CHARACTERS = ["ROCK", "PAPER", "SCISSORS", "LIZARD", "SPOCK"]; COMMANDS = ["CLEAR", "CLS", "EXIT", "QUIT", "HELP", "MANUAL", "GUIDE", "SHELDON"]; WINS = {"ROCK": ["SCISSORS", "LIZARD"], "PAPER": ["ROCK", "SPOCK"], "SCISSORS": ["PAPER", "LIZARD"], "LIZARD": ["PAPER", "SPOCK"], "SPOCK": ["SCISSORS", "ROCK"]}; regularHelp = "\nCOMMANDS:\n  HELP           - Prints this.\n  MANUAL | GUIDE - Show detailed game instructions.\n  SHELDON        - Summons Sheldon.\n  CLEAR | CLS    - Clears screen.\n  EXIT | QUIT    - Kills rpsls.\n\nGAME MODES:\n  SINGLE | SINGLEPLAYER | 1 | ONE | MONO - Play against randomness.\n  MULTI | MULTIPLAYER | 2 | TWO | DUO    - Play against another player.\n" ; sheldonHelp = "\nSCISSORS cuts PAPER\nPAPER covers ROCK\nROCK crushes LIZARD\nLIZARD poisons SPOCK\nSPOCK smashes SCISSORS\nSCISSORS decapitates LIZARD\nLIZARD eats PAPER\nPAPER disproves SPOCK\nSPOCK vaporizes ROCK\nand as it always has\nROCK crushes SCISSORS\n"
def clear(): os.system("cls" if os.name == "nt" else "clear")
def handleCommands(c): clear() if c in ["CLEAR", "CLS"] else sys.exit("GOODBYE!") if c in ["EXIT", "QUIT"] else print(regularHelp) if c in ["HELP"] else print(sheldonHelp) if c in ["MANUAL", "GUIDE", "SHELDON"] else None; return c in COMMANDS
def getChoice(p): 
    while True: 
        c = input(p).strip().upper()
        if c in CHARACTERS: return c
        elif handleCommands(c): continue
        else: print("INVALID CHOICE!")
def playGame(p1, p2, s): 
    if s: time.sleep(random.uniform(0.6, 1.6)); print(f"COMPUTER: {p2}")
    print("TIE!" if p1 == p2 else ("YOU WON!" if s else "PLAYER 1 WINS!") if p2 in WINS[p1] else ("YOU LOST!" if s else "PLAYER 2 WINS!"))
clear()
while True:
    if handleCommands(m := input("SINGLEPLAYER | MULTIPLAYER: ").strip().upper()): continue
    if m not in ["SINGLE", "1", "MULTI", "2", "DUO", "SINGLEPLAYER", "MULTIPLAYER", "MONO", "ONE", "BI"]: print("INVALID CHOICE!"); continue
    while True: playGame(getChoice("PLAYER: "), random.choice(CHARACTERS), True) if m in ["SINGLE", "1", "SINGLEPLAYER", "ONE", "MONO"] else playGame((p1 := getChoice("PLAYER 1: ")), (clear(), getChoice("PLAYER 2: "))[1], False)