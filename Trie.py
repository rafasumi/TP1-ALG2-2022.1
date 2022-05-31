class Node:
  def __init__(self, symbol, code):
    self.symbol = symbol
    self.code = code
    self.children = {}

class Trie:
  def __init__(self):
    self.root = Node("", 0)
    self.nextCode = 1
  
  def insert(self, word):
    node = self.root
    prefixCode = 0

    for char in word:
      if char in node.children:
        node = node.children[char]
        prefixCode = node.code
      else:
        newNode = Node(char, self.nextCode)
        node.children[char] = newNode
        self.nextCode += 1
        return prefixCode
  
  def find(self, word):
    node = self.root

    for char in word:
      if char in node.children:
        node = node.children[char]
      else:
        return -1
    
    return node.code
