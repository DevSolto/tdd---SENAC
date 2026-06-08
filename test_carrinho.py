import pytest
from carrinho import CarrinhoDeCompras


# ──────────────────────────────────────────
# ADICIONAR ITEM
# ──────────────────────────────────────────

def test_adicionar_item_simples():
    """GREEN: adiciona um item e verifica se está no carrinho."""
    carrinho = CarrinhoDeCompras()
    carrinho.adicionar_item("Camiseta", 49.90)
    assert "Camiseta" in carrinho.listar_itens()


def test_adicionar_item_incrementa_quantidade():
    """GREEN: adicionar o mesmo item duas vezes soma as quantidades."""
    carrinho = CarrinhoDeCompras()
    carrinho.adicionar_item("Camiseta", 49.90, 2)
    carrinho.adicionar_item("Camiseta", 49.90, 3)
    assert carrinho.listar_itens()["Camiseta"]["quantidade"] == 5


def test_adicionar_item_preco_negativo_levanta_erro():
    """RED→GREEN: preço negativo deve levantar ValueError."""
    carrinho = CarrinhoDeCompras()
    with pytest.raises(ValueError):
        carrinho.adicionar_item("Produto", -10.0)


def test_adicionar_item_quantidade_zero_levanta_erro():
    """RED→GREEN: quantidade zero deve levantar ValueError."""
    carrinho = CarrinhoDeCompras()
    with pytest.raises(ValueError):
        carrinho.adicionar_item("Produto", 10.0, 0)


# ──────────────────────────────────────────
# REMOVER ITEM
# ──────────────────────────────────────────

def test_remover_item_existente():
    """GREEN: remove item e ele não deve mais estar no carrinho."""
    carrinho = CarrinhoDeCompras()
    carrinho.adicionar_item("Calça", 89.90)
    carrinho.remover_item("Calça")
    assert "Calça" not in carrinho.listar_itens()


def test_remover_item_inexistente_levanta_erro():
    """RED→GREEN: remover item que não existe deve levantar KeyError."""
    carrinho = CarrinhoDeCompras()
    with pytest.raises(KeyError):
        carrinho.remover_item("Fantasma")


# ──────────────────────────────────────────
# CALCULAR TOTAL
# ──────────────────────────────────────────

def test_calcular_total_carrinho_vazio():
    """GREEN: carrinho vazio deve retornar total zero."""
    carrinho = CarrinhoDeCompras()
    assert carrinho.calcular_total() == 0.0


def test_calcular_total_correto():
    """GREEN: total deve ser a soma de preco * quantidade de cada item."""
    carrinho = CarrinhoDeCompras()
    carrinho.adicionar_item("Camiseta", 50.0, 2)   # 100
    carrinho.adicionar_item("Tênis", 200.0, 1)      # 200
    assert carrinho.calcular_total() == 300.0


# ──────────────────────────────────────────
# APLICAR DESCONTO
# ──────────────────────────────────────────

def test_aplicar_desconto_valido():
    """GREEN: desconto de 10% sobre 200 deve retornar 180."""
    carrinho = CarrinhoDeCompras()
    carrinho.adicionar_item("Tênis", 200.0)
    assert carrinho.aplicar_desconto(10) == 180.0


def test_aplicar_desconto_maximo():
    """GREEN: desconto de exatamente 20% deve ser aceito."""
    carrinho = CarrinhoDeCompras()
    carrinho.adicionar_item("Tênis", 200.0)
    assert carrinho.aplicar_desconto(20) == 160.0


def test_aplicar_desconto_acima_do_limite_levanta_erro():
    """RED→GREEN: desconto > 20% deve levantar ValueError."""
    carrinho = CarrinhoDeCompras()
    carrinho.adicionar_item("Tênis", 200.0)
    with pytest.raises(ValueError):
        carrinho.aplicar_desconto(21)


def test_aplicar_desconto_negativo_levanta_erro():
    """RED→GREEN: desconto negativo deve levantar ValueError."""
    carrinho = CarrinhoDeCompras()
    carrinho.adicionar_item("Tênis", 200.0)
    with pytest.raises(ValueError):
        carrinho.aplicar_desconto(-5)
