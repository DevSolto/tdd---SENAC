class CarrinhoDeCompras:
    def __init__(self):
        self._itens = {}

    def adicionar_item(self, nome: str, preco: float, quantidade: int = 1):
        if preco < 0 or quantidade <= 0:
            raise ValueError("Preço ou quantidade inválidos.")
        if nome in self._itens:
            self._itens[nome]["quantidade"] += quantidade
        else:
            self._itens[nome] = {"preco": preco, "quantidade": quantidade}

    def remover_item(self, nome: str):
        if nome not in self._itens:
            raise KeyError(f"Item '{nome}' não encontrado no carrinho.")
        del self._itens[nome]

    def calcular_total(self) -> float:
        return sum(v["preco"] * v["quantidade"] for v in self._itens.values())

    def aplicar_desconto(self, percentual: float) -> float:
        if percentual < 0 or percentual > 20:
            raise ValueError("Desconto deve ser entre 0% e 20%.")
        total = self.calcular_total()
        return total * (1 - percentual / 100)

    def listar_itens(self) -> dict:
        return dict(self._itens)
