"""Kubiks - A library for parsing and interpreting .kbk files."""

from pathlib import Path

from kubiks.serializer import Serializer, Percent
from .lexer import Lexer
from .ast import Parser
from .interpreter import Interpreter

__all__ = ['load', 'Lexer', 'Parser', 'Interpreter', 'parse', 'interpret', 'parse_and_interpret', 'dumps', Percent]

def parse(text: str):
    """
    Parse text into AST (Abstract Syntax Tree).

    Args:
        text: Input text in .kbk format

    Returns:
        FileNode: The root node of the parsed AST
    """
    from .lexer import Lexer
    from .ast import Parser

    tokens = list(Lexer().lex(text))
    parser = Parser(tokens)
    return parser.parse()

def interpret(ast):
    """
    Interpret AST and return the resulting environment.

    Args:
        ast: Abstract Syntax Tree (FileNode)

    Returns:
        dict: The resulting environment dictionary
    """
    from .interpreter import Interpreter
    interpreter = Interpreter()
    return interpreter.eval(ast)

def parse_and_interpret(text: str):
    """
    Parse text and interpret it in one step.

    Args:
        text: Input text in .kbk format

    Returns:
        dict: The resulting environment dictionary
    """
    ast = parse(text)
    return interpret(ast)

def load(file_path: str | Path, strict: bool = True) -> dict:
    """
    Load, parse, and interpret a .kbk file.

    Args:
        file_path: Path to the .kbk file
        strict: Allow only .kbk files

    Returns:
        dict: The resulting environment dictionary after interpretation
    """

    path = Path(file_path)

    if not path.suffix == ".kbk" and strict:
        raise ValueError("Only .kbk files allowed")

    text = path.read_text("utf-8")

    return parse_and_interpret(text)

def loads(text: str) -> dict:
    """
    Parse and interpret a .kbk string.

    Args:
        text: String containing .kbk content

    Returns:
        dict: Parsed configuration
    """

    return parse_and_interpret(text)

def dumps(obj: dict):
    
    return Serializer().dumps(obj)
