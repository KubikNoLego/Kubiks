from .ast import (
    Node, AssignmentNode, ListNode, DictNode, String, FileNode, Float, Percent,
    Integer, Key, Boolean, Null
)

class Interpreter:

    def __init__(self):
        self.env = {}

    def eval(self, node):
        if isinstance(node, FileNode):
            return self._eval_file(node)
        if isinstance(node, AssignmentNode):
            return self._eval_assignment(node)

        if isinstance(node, Float):
            return node.value
        if isinstance(node, Integer):
            return node.value
        if isinstance(node, Percent):
            return node.value
        if isinstance(node, String):
            return node.value
        if isinstance(node, Boolean):
            return node.value
        if isinstance(node, Null):
            return node.value

        if isinstance(node, ListNode):
            return self._eval_list(node)

        if isinstance(node, DictNode):
            return self._eval_dict(node)

        raise TypeError(f"Unknown node: {type(node).__name__}")
    
    def _eval_file(self, node: FileNode):
        for entry in node.entries:
            self.eval(entry)
        return self.env
    def _eval_assignment(self, node: AssignmentNode):
        value = self.eval(node.value)
        self.env[node.key.name] = value
    def _eval_list(self, node: ListNode):
        return [self.eval(value)for value in node.values]
    def _eval_dict(self, node: DictNode):
        result = {}

        for assignment in node.entries:
            result[assignment.key.name] = self.eval(
                assignment.value
            )

        return result