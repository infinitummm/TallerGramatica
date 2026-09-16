class ASTNode:
    """Clase base para todos los nodos del Árbol de Sintaxis Abstracta (AST)."""
    def to_sexpr(self) -> str:
        raise NotImplementedError

    def to_ascii_tree(self, prefix: str = "", is_tail: bool = True) -> str:
        raise NotImplementedError

    def evaluate(self, env=None) -> float:
        raise NotImplementedError

    def count_nodes(self) -> int:
        raise NotImplementedError


class BinaryOpNode(ASTNode):
    """Representa una operación binaria ('+' o '*')."""
    def __init__(self, op: str, left: ASTNode, right: ASTNode):
        self.op = op
        self.left = left
        self.right = right

    def to_sexpr(self) -> str:
        return f"({self.op} {self.left.to_sexpr()} {self.right.to_sexpr()})"

    def to_ascii_tree(self, prefix: str = "", is_tail: bool = True) -> str:
        branch = "└── " if is_tail else "├── "
        res = prefix + branch + f"OpBinario ('{self.op}')\n"
        child_prefix = prefix + ("    " if is_tail else "│   ")
        res += self.left.to_ascii_tree(child_prefix, False)
        res += self.right.to_ascii_tree(child_prefix, True)
        return res

    def evaluate(self, env=None) -> float:
        l_val = self.left.evaluate(env)
        r_val = self.right.evaluate(env)
        if self.op == '+':
            return l_val + r_val
        elif self.op == '*':
            return l_val * r_val
        else:
            raise ValueError(f"Operador desconocido: {self.op}")

    def count_nodes(self) -> int:
        return 1 + self.left.count_nodes() + self.right.count_nodes()


class NumNode(ASTNode):
    """Representa un número literal."""
    def __init__(self, value: float):
        self.value = value

    def to_sexpr(self) -> str:
        if self.value == int(self.value):
            return str(int(self.value))
        return str(self.value)

    def to_ascii_tree(self, prefix: str = "", is_tail: bool = True) -> str:
        branch = "└── " if is_tail else "├── "
        val_str = int(self.value) if self.value == int(self.value) else self.value
        return prefix + branch + f"Num ({val_str})\n"

    def evaluate(self, env=None) -> float:
        return float(self.value)

    def count_nodes(self) -> int:
        return 1


class IdNode(ASTNode):
    """Representa un identificador / variable."""
    def __init__(self, name: str):
        self.name = name

    def to_sexpr(self) -> str:
        return self.name

    def to_ascii_tree(self, prefix: str = "", is_tail: bool = True) -> str:
        branch = "└── " if is_tail else "├── "
        return prefix + branch + f"ID ({self.name})\n"

    def evaluate(self, env=None) -> float:
        if env and self.name in env:
            return float(env[self.name])
        return 0.0

    def count_nodes(self) -> int:
        return 1
