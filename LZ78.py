from optparse import OptionParser
from time import time

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

def compression(filename, output):
  tree = Trie()
  
  with open(filename, 'r') as inputFile:
    with open(output, 'w') as outputFile:
      pattern = ''
      outputFile.write('|')
      while True:
        char = inputFile.read(1)
        if char == '': break

        pattern = pattern + char
        prefixCode = tree.find(pattern)
        if prefixCode != -1:
          continue
        else:
          prefixCode = tree.insert(pattern)
          outputFile.write(f'{prefixCode}~{char}|')
          pattern = ''
      
      if pattern != '':
        outputFile.write(f'{prefixCode}~{char}|')


def decompression(filename, output):
  with open(filename, 'r') as inputFile:
    with open(output, 'w') as outputFile:
      input = inputFile.read().split('|')[1:-1]
      input = [x.split('~') for x in input]

      aux = ['']
      for index, char in input:
        newStr = f'{aux[int(index)]}{char}'
        aux.append(newStr)
        outputFile.write(newStr)

def main():
  parser = OptionParser()
  parser.add_option('-c', action='store', type='string', dest='compression')
  parser.add_option('-x', action='store', type='string', dest='decompression')
  parser.add_option('-o', action='store', type='string', dest='output')

  (options, _) = parser.parse_args()

  if options.compression:
    filename = options.compression
    output = options.output if options.output else filename.replace('.txt', '.z78')
    compression(filename, output)
  elif options.decompression:
    filename = options.decompression
    output = options.output if options.output else filename.replace('.z78', '.txt')
    decompression(filename, output)

if __name__ == '__main__':
  main()