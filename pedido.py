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
  def calcular_total(self, subtotal, valor_descontado):
    """
    Retorna o valor total do pedido, com ou sem desconto.
    """
    return subtotal - valor_descontado

  def exibir_resumo(self):
    """
    Exibe um resumo com as informações do pedido.
    """
    print(f"Resumo do Pedido\n")
    print(f"Cliente: {self.nome}")
    print(f"Produto: {self.produto}")
    print(f"Quantidade: {self.qtd}")
    print(f"Preço unitário: R$ {self.preco_unitario:.2f}")
    print(f"Subtotal: R$ {self.calcular_subtotal(self.qtd, self.preco_unitario):.2f}")
    print(f"Desconto: R$ {self.calcular_desconto(self.subtotal, self.cupom):.2f}")
    print(f"Total: R$ {self.calcular_total(self.subtotal, self.desconto):.2f}")
    print(f"Classificação: {self.classificar_pedido(self.subtotal)}")
