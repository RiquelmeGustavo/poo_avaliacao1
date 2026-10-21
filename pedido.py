class Pedido:
  def _init_(self, nome, produto, qtd, preco_unitario, cupom):
    self.nome = nome
    self.produto = produto
    self.qtd = qtd
    self.preco_unitario = preco_unitario
    self.cupom = cupom.lower()
    
  def calcular_subtotal(self, qtd, preco_unitario):
    """
    Retorna o subtotal do pedido.
    """
    self.subtotal = qtd * preco_unitario
    return self.subtotal
def classificar_pedido(self, subtotal):
    """
    Classifica o pedido pelo preço (pequeno, médio e grande).
    """
