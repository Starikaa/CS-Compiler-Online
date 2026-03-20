import sys
from utils import Tokenizer, Parser, ASTGenerator, Checker, CodeGenerator

def compile_source(code: str):
    # 1. Lexer
    tokenizer = Tokenizer(code)
    tokens = tokenizer.get_tokens_as_string()
    if "error" in tokens.lower():
        return False, f"Lexer error:\n{tokens}"

    # 2. Parser
    parser = Parser(code)
    parse_result = parser.parse()
    if parse_result != "success":
        return False, f"Parser error:\n{parse_result}"

    # 3. Static Checker
    checker = Checker(source=code)
    check_result = checker.check_from_source()
    if check_result != "Static checking passed":
        return False, f"Static Checker error:\n{check_result}"

    # 4. Code Generator
    codegen = CodeGenerator()
    codegen.generate_and_run(code)

    return True, "Compile success"


def main():
    if len(sys.argv) < 2:
        print("Usage: python run.py <source_file>")
        sys.exit(1)

    source_file = sys.argv[1]

    try:
        with open(source_file, "r", encoding="utf-8") as f:
            code = f.read()
    except FileNotFoundError:
        print("Source file not found")
        sys.exit(1)

    ok, msg = compile_source(code)

    print(msg)

    if not ok:
        sys.exit(1)


if __name__ == "__main__":
    main()