from Trie import Trie
from os import stat

def compression(filename, output):
  tree = Trie()
  highestCode = 0

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

          if prefixCode > highestCode: highestCode = prefixCode

          outputFile.write(f'{prefixCode}~{char}|')
          pattern = ''
      
      if pattern != '':
        if prefixCode > highestCode: highestCode = prefixCode
        outputFile.write(f'{prefixCode}~{char}|')
  
  with open('./compressionReport.txt', 'w') as reportFile:
    originalFileBitSize = stat(filename).st_size * 8

    trieNodeCount = tree.nextCode - 1
    outputFileBitSize = trieNodeCount * (highestCode.bit_length() + 8)

    compressionRate = outputFileBitSize / originalFileBitSize

    reportFile.write(f'Input: {filename} - Bit size: {originalFileBitSize}\n')
    reportFile.write(f'Output: {output} - Bit size: {outputFileBitSize}\n')
    reportFile.write(f'Taxa de compressão: {round(compressionRate, 2)}\n')

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
