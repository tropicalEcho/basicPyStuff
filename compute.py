import math, os, re, sys, ast

replacement = {
    "^": "**",        
    "√": "math.sqrt", 
    "mod": "%",       
    "÷": "/",    

    "pi": "math.pi",
    "e": "math.e",

    "asin": "math.asin",
    "acos": "math.acos",
    "atan": "math.atan",
    "sin": "math.sin",
    "cos": "math.cos",
    "tan": "math.tan",

    "log": "math.log10", 
    "ln": "math.log",     

    "floor": "math.floor",
    "ceil": "math.ceil",

    "≈": "=="
}

def replaceFactorial(expr):
    pattern = r'(\d+|\([^()]*\))!'
    while re.search(pattern, expr):
        expr = re.sub(pattern, r'math.factorial(\1)', expr)
    return expr

def preprocess(expr):
    expr = re.sub(r'(?<=\d)_(?=\d)', '', expr)
    expr = expr.replace(")(", ")*(")
    expr = re.sub(r'\(\s*\)', '(0)', expr)
    return expr

ALLOWED_NODES = (
    ast.Expression,
    ast.BinOp,
    ast.UnaryOp,
    ast.Call,
    ast.Name,
    ast.Load,
    ast.Attribute,
    ast.Constant,
    ast.Add,
    ast.Sub,
    ast.Mult,
    ast.Div,
    ast.Pow,
    ast.Mod,
    ast.FloorDiv,
    ast.UAdd,
    ast.USub,
    ast.Compare,
    ast.Eq,
    ast.NotEq,
    ast.Lt,
    ast.LtE,
    ast.Gt,
    ast.GtE,
)

def isAstSafe(node):
    if not isinstance(node, ALLOWED_NODES):
        return False
    for child in ast.iter_child_nodes(node):
        if not isAstSafe(child):
            return False
    return True

def safeEval(expression):
    try:
        node = ast.parse(expression, mode="eval")
        if not isAstSafe(node):
            raise ValueError("INVALID OR UNSAFE EXPRESSION!")
        code = compile(node, "<string>", "eval")
        return eval(code, {"__builtins__": None}, {"math": math})
    except Exception as e:
        return f"ERROR: {str(e).upper()}"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

helpText = """
COMMANDS:
  HELP         - Prints this.
  CLEAR | CLS  - Clears screen.
  EXIT | QUIT  - Kills compute.
  <EXPRESSION> - Computes given expression.
"""

def main():
    while True:
        try:
            userInput = input("~\\compute$ ").strip()
        except EOFError:
            print()
            break

        if not userInput:
            continue

        upInput = userInput.upper()
        if upInput in {"CLS", "CLEAR"}:
            clear()
            continue
        elif upInput in {"HELP"}:
            print(helpText)
            continue
        elif upInput in {"EXIT", "QUIT"}:
            sys.exit("GOODBYE!")

        expr = userInput
        for old in sorted(replacement, key=len, reverse=True):
            expr = re.sub(re.escape(old), replacement[old], expr)

        expr = replaceFactorial(expr)

        emptyParenFound = bool(re.search(r'\(\s*\)', expr))

        processed_expr = preprocess(expr)

        result = safeEval(processed_expr)

        if emptyParenFound:
            print("warning: Empty expression in parentheses interpreted as zero.")

        print(f"  {processed_expr} = {result}")

if __name__ == "__main__":
    main()