from Trie import Trie

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
