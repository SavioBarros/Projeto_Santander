"""Descrição
Crie um sistema de carrinho de compras que permita adicionar produtos e calcular o valor total da compra.

Entrada
Lista de produtos adicionados ao carrinho (cada um com nome e preço).
Saída
Lista dos produtos adicionados e o total da compra."""


def compras():

# Lista para armazenar os produtos e preços
  carrinho = []
  total = 0.0

# Entrada do número de itens
  n = int(input().strip())


# Loop para adicionar itens ao carrinho
  for _ in range(n):
      linha = input().strip()
    
    # Encontra a última ocorrência de espaço para separar nome e preço
      posicao_espaco = linha.rfind(" ")
    
    # Separa o nome do produto e o preço
      item = linha[:posicao_espaco]
      preco = float(linha[posicao_espaco + 1:])
    
    # Adiciona ao carrinho
      carrinho.append((item, preco))
      total += preco

  for itens in carrinho:
      print(f"{itens[0]}: R${itens[1]:.2f}")

  print(f"Total: R${total:.2f}")

compras()