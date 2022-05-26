from optparse import OptionParser

class Node:
  def __init__(self, symbol, code):
    self.symbol = symbol
    self.code = code
    self.isLeaf = False
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

def compression(filename, output):
  D = ['']
  out = []
  tree = Trie()
  
  with open(filename, 'r') as inputFile:
    with open(output, 'w') as outputFile:
      pattern = ''
      for char in inputFile.read():
        pattern = pattern + char
        if pattern in D:
          continue
        else:
          D.append(pattern)
          prefixCode = tree.insert(pattern)
          out.append((prefixCode, char))
          outputFile.write(str(prefixCode)+','+char+'|')
          pattern = ''
  
  print(D)
  print(out)

def decompression(filename, output):
  pass

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