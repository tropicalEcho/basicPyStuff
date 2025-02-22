board = {
    "A1" : "",
    "A2" : "",
    "A3" : "",
    "B1" : "",
    "B2" : "",
    "B3" : "",
    "C1" : "",
    "C2" : "",
    "C3" : "",
}

def showBoard():
    for key, value in board.items():
        print(f"{value}")

def add2board(userInput, location):
    if userInput in {"x", "o"}:
        for key, value in board.items():
            value = userInput if not value and key else value

def main():
    while True:
        pass
showBoard()