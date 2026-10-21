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
    if subtotal <= 30:
      return "Pedido pequeno"
    elif 30 < subtotal <= 100:
      return "Pedido médio"
    else:
      return "Pedido grande"
  def calcular_desconto(self, subtotal, cupom):
    """
    Recebe o cupom já padronizado e retorna o valor do desconto.
    """
    if cupom == "sim":
      desconto = 0.10
    elif cupom == "não":
      desconto = 0
    self.valor_descontado = subtotal * desconto
    return self.valor_descontado
