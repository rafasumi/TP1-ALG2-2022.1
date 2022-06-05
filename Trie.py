# Classe que representa um nó da árvore Trie
class Node:
  def __init__(self, symbol, code):
    self.symbol = symbol # Símbolo armazenado no nó
    self.code = code # Código numérico associado ao nó
    self.children = {} # Dicionário de filhos do nó. A chave é o símbolo armazenado no filho e o valor é o Node filho


# Classe que representa uma árvore Trie tradicional
class Trie:
  def __init__(self):
    # Raiz da Trie. Armazena a string vazia e tem 0 como código
    self.root = Node("", 0)
    # Código do próximo nó a ser armazenado na árvore. Inicialmente é 1
    # Além disso também é equivalente ao número de nós na árvore
    self.nextCode = 1
  
  # Método para inserção de palavra na árvore
  # Retorna o código associado ao nó pai do nó inserido. Ou seja, o código do prefixo da palavra inserida
  def insert(self, word):
    # Primeiramente, é preciso encontrar onde será inserido o nó para representar essa palavra
    # Começa a busca pela raiz da árvore
    node = self.root
    # O valor inicial do código do prefixo é 0, ou seja, o prefixo ""
    prefixCode = 0 

    # Itera pelos caracteres da palavra a ser inserida
    for char in word:
      # Se o caractere atual estiver associado a algum filho do nó atual da busca, então buscará o próximo caractere
      # da palavra neste nó filho
      if char in node.children:
        node = node.children[char]
        prefixCode = node.code
      # Caso contrário, é criado um nó para o caractere atual. É tido como premissa que só se cairá nesse caso quando
      # se estiver no último caractere da palavra, visto que, quando essa função é chamada para palavras com mais de
      # um caractere, o seu prefixo é formado por caracteres de nós na Trie
      else:
        newNode = Node(char, self.nextCode)
        node.children[char] = newNode
        self.nextCode += 1
        return prefixCode
  
  # Método para buscar uma string na Trie
  # Se a palavra for encontrada, retorna o código associado ao nó do último caractere, que é o código associado a essa palavra
  # Caso contrário, retorna -1
  def find(self, word):
    # Começa a busca pela raiz
    node = self.root

    # Itera pelos caracteres da palavra
    for char in word:
      # Se o caractere atual estiver associado a algum filho do nó atual da busca, então buscará o próximo caractere
      # da palavra neste nó filho
      if char in node.children:
        node = node.children[char]
      # Se, em algum momento, o caractere não estiver associado a nenhum nó filho, então indica que a palavra não está na Trie
      else:
        return -1
    
    return node.code
