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

            match kind:
                case "STRING":
                    value = value[1:-1]

                case "PERCENT":
                    value = round(float(value[:-1]) / 100, 6)

                case "FLOAT":
                    value = float(value)

                case "INTEGER":
                    value = int(value)

                case "BOOLEAN":
                    value = value == "true"

                case "NULL":
                    value = None

                case "COMMENT" | "SKIP" | "NEWLINE":
                    continue
                
                case "MISMATCH":
                    raise SyntaxError(...)

            yield self.Token(kind, value)