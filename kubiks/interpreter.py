from .ast import (
    AssignmentNode, ListNode, DictNode, String, FileNode, Float, Percent,
    Integer, Boolean, Null
)

class Interpreter:

    def __init__(self):
        self.env = {}

    def eval(self, node):
        handlers = {
            FileNode: self._eval_file,
            AssignmentNode: self._eval_assignment,
            ListNode: self._eval_list,
            DictNode: self._eval_dict,
        }

        literals = (Float, Integer, Percent, String, Boolean, Null)

        if isinstance(node, literals):
            return node.value

        handler = handlers.get(type(node))
        if handler:
            return handler(node)

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