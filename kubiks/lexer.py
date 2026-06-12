from collections import namedtuple
import re


class Lexer:

    Token = namedtuple("Token",["type","value"])

    TOKEN_SPECIFICATION = [
        # Комментарии
        ("COMMENT", r"\#.*"),

        # Строки
        ("STRING", r'"(?:\\.|[^"\\])*"'),

        # Значения (более специфичные должны идти раньше)
        ("PERCENT", r"-?(?:\d+\.\d+|\d+)%"),
        ("FLOAT", r"-?\d+\.\d+"),
        ("INTEGER", r"-?\d+"),
        ("BOOLEAN", r"(?<!\w)(?:true|false)(?!\w)"),
        ("NULL", r"(?<!\w)null(?!\w)"),

        # Ключи
        ("KEY", r"[A-Za-zА-Яа-я_][A-Za-zА-Яа-я0-9_]*"),

        # Оператор присваивания
        ("ASSIGNMENT", r"\|="),

        # Словари
        ("LBRACE", r"\{"),
        ("RBRACE", r"\}"),

        # Списки
        ("LBRACK", r"\["),
        ("RBRACK", r"\]"),

        # Скобки (на будущее)
        ("LPAREN", r"\("),
        ("RPAREN", r"\)"),

        # Разделители
        ("COMMA", r","),

        # Переводы строк и пробелы
        ("NEWLINE", r"\n"),
        ("SKIP", r"[ \t\r]+"),

        # Любой неизвестный символ
        ("MISMATCH", r"."),
    ]   

    def lex(self, text: str):
        token_regex = "|".join(f"(?P<{name}>{pattern})" 
                    for name, pattern in self.TOKEN_SPECIFICATION)
        
        for match in re.finditer(token_regex, text):
            kind = match.lastgroup
            value = match.group()

            if kind in ("COMMENT", "SKIP", "NEWLINE"):
                continue
            
            elif kind == "STRING":
                yield self.Token(kind, value[1:-1])
            
            elif kind == "PERCENT":
                yield self.Token(kind, round((float(value[:-1])/100), 6))
            
            elif kind == "FLOAT":
                yield self.Token(kind, float(value))

            elif kind == "BOOLEAN":
                yield self.Token(kind, True if value == 'true' else False)
            
            elif kind == "NULL":
                yield self.Token(kind, None)
            
            elif kind == "INTEGER":
                yield self.Token(kind, int(value))
            
            elif kind == "KEY":
                yield self.Token(kind, value)

            elif kind in ("ASSIGNMENT", "LBRACE", "RBRACE",
                            "LBRACK", "RBRACK", "LPAREN", "RPAREN", "COMMA"):
                yield self.Token(kind, value)
            
            elif kind == "MISMATCH":
                raise SyntaxError(f"Unexpected character: {value!r}")