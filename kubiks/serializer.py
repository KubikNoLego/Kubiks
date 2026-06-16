class Percent():
    
    def __init__(self, percent: int | float):
        self.percent = percent

class Serializer:
    def dumps(self, obj, indent=0):
        if obj is None:
            return "null"
        
        if isinstance(obj, Percent):
            return f"{obj.percent}%"

        if isinstance(obj, bool):
            return "true" if obj else "false"

        if isinstance(obj, str):
            return f'"{obj}"'

        if isinstance(obj, int):
            return str(obj)

        if isinstance(obj, float):
            return str(obj)

        if isinstance(obj, list):
            items = ", ".join(self.dumps(x, indent) for x in obj)
            return f"[{items}]"

        if isinstance(obj, dict):
            lines = ["{"]

            for key, value in obj.items():
                lines.append(
                    "    " * (indent + 1)
                    + f"{key} |= "
                    + self.dumps(value, indent + 1)
                )

            lines.append("    " * indent + "}")
            return "\n".join(lines)

        raise TypeError(f"Unsupported type: {type(obj)}")