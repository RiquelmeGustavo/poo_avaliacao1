class Pedido:
  def _init_(self, nome, produto, qtd, preco_unitario, cupom):
    self.nome = nome
    self.produto = produto
    self.qtd = qtd
    self.preco_unitario = preco_unitario
    self.cupom = cupom.lower()
