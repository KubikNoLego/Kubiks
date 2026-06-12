class Node:
    pass

class Key(Node):
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"Key({self.name!r})"


class Integer(Node):
    def __init__(self, value: int):
        self.value = value

    def __repr__(self):
        return f"Integer({self.value})"


class Float(Node):
    def __init__(self, value: float):
        self.value = value

    def __repr__(self):
        return f"Float({self.value})"


class Percent(Node):
    def __init__(self, value: float):
        self.value = value

    def __repr__(self):
        return f"Percent({self.value})"

class Boolean(Node):
    def __init__(self, value: bool):
        self.value = value

    def __repr__(self):
        return f"Boolean({self.value!r})"
    
class Null(Node):
    def __init__(self):
        self.value = None

    def __repr__(self):
        return f"Null()"

class String(Node):
    def __init__(self, value: str):
        self.value = value

    def __repr__(self):
        return f"String({self.value!r})"
    
class ListNode(Node):
    def __init__(self, values: list[Node]):
        self.values = values

    def __repr__(self):
        return f"ListNode({self.values})"


class DictNode(Node):
    def __init__(self, entries: list["AssignmentNode"]):
        self.entries = entries

    def __repr__(self):
        return f"DictNode({self.entries})"
    
class AssignmentNode(Node):
    def __init__(self, key: Key, value: Node):
        self.key = key
        self.value = value

    def __repr__(self):
        return (
            f"AssignmentNode("
            f"key={self.key}, "
            f"value={self.value})"
        )
    
class FileNode(Node):
    def __init__(self, entries: list[AssignmentNode]):
        self.entries = entries

    def __repr__(self):
        return f"FileNode({self.entries})"
    

class Parser:

    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def pick(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None
    
    def advance(self):
        self.pos += 1

    def expect(self, token_type):
        token = self.pick()

        if token is None:
            raise SyntaxError(f"Expected {token_type}, got EOF")

        if token.type == token_type:
            self.advance()
            return token

        raise SyntaxError(f"Expected {token_type}, got {token.type}")
    
    def parse(self):

        if not self.pick():
            raise SyntaxError

        entries = []

        while self.pick():
            entries.append(self.assignment())
        return FileNode(entries)
    
    def assignment(self):
        key = Key(self.expect("KEY").value)

        self.expect("ASSIGNMENT")

        value = self.parse_value()

        return AssignmentNode(key, value)

    def parse_value(self):
        token = self.pick()

        if token is None:
            raise SyntaxError("Unexpected EOF")

        if token.type == "STRING":
            self.advance()
            return String(token.value)

        if token.type == "INTEGER":
            self.advance()
            return Integer(token.value)

        if token.type == "FLOAT":
            self.advance()
            return Float(token.value)

        if token.type == "PERCENT":
            self.advance()
            return Percent(token.value)
        
        if token.type == "BOOLEAN":
            self.advance()
            return Boolean(token.value)
        
        if token.type == "NULL":
            self.advance()
            return Null()

        if token.type == "LBRACK":
            return self.parse_list()

        if token.type == "LBRACE":
            return self.parse_dict()

        raise SyntaxError(f"Unexpected token {token.type}")
    
    def parse_list(self):
        self.expect("LBRACK")

        values = []

        if self.pick() and self.pick().type != "RBRACK":

            values.append(self.parse_value())

            while self.pick() and self.pick().type == "COMMA":
                self.advance()
                values.append(self.parse_value())

        self.expect("RBRACK")

        return ListNode(values)
    
    def parse_dict(self):
        self.expect("LBRACE")

        entries = []

        while self.pick() and self.pick().type != "RBRACE":
            entries.append(self.assignment())

        self.expect("RBRACE")

        return DictNode(entries)