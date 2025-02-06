import random, sys, os, time; CHARACTERS = ["ROCK", "PAPER", "SCISSORS", "LIZARD", "SPOCK"]; COMMANDS = ["CLEAR", "CLS", "EXIT", "QUIT", "HELP", "H", "MANUAL", "GUIDE", "SHELDON"]; WINS = {"ROCK": ["SCISSORS", "LIZARD"], "PAPER": ["ROCK", "SPOCK"], "SCISSORS": ["PAPER", "LIZARD"], "LIZARD": ["PAPER", "SPOCK"], "SPOCK": ["SCISSORS", "ROCK"]}; regularHelp = "\nCOMMANDS:\nCLEAR | CLS                  CLEARS THE SCREEN\nEXIT | QUIT                  KILLS THE GAME\nHELP | H                     PRINTS THIS\nMANUAL | GUIDE | SHELDON     SUMMONS SHELDON FOR HELP\n\nGUIDE:\nENTER ( SINGLE | SINGLEPLAYER | 1 | ONE | MONO ) IF YOU WANNA PLAY AGAINST COMPUTER\nENTER ( MULTI | MULTIPLAYER | 2 | TWO | BI | DUO ) IF YOU WANNA PLAY AGAINST A HUMAN\n" ; sheldonHelp = "\nSCISSORS cuts PAPER\nPAPER covers ROCK\nROCK crushes LIZARD\nLIZARD poisons SPOCK\nSPOCK smashes SCISSORS\nSCISSORS decapitates LIZARD\nLIZARD eats PAPER\nPAPER disproves SPOCK\nSPOCK vaporizes ROCK\nand as it always has\nROCK crushes SCISSORS\n"
def clear(): os.system("cls" if os.name == "nt" else "clear")
def handleCommands(c): clear() if c in ["CLEAR", "CLS"] else sys.exit("GOODBYE!") if c in ["EXIT", "QUIT"] else print(regularHelp) if c in ["HELP", "H"] else print(sheldonHelp) if c in ["MANUAL", "GUIDE", "SHELDON"] else None; return c in COMMANDS
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