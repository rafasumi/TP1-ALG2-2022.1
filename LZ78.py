from Trie import Trie
from os import stat

# Compressão seguindo o LZ78
def compression(filename, output):
  tree = Trie()
  # Armazena o maior código de prefixo usado na saída para ser usado no cálculo da taxa
  # de compressão. A quantidade de bits necessária para armazenar esse código será usada
  # para todos os outros os códigos armazenados
  highestCode = 0

  with open(filename, 'r', encoding='utf-8') as inputFile:
    with open(output, 'w', encoding='utf-8') as outputFile:
      # Padrão que é buscado na Trie
      pattern = ''
      outputFile.write('|')

      # Itera por todos os caracteres da entrada
      while True:
        char = inputFile.read(1)
        if char == '': break # Cláusula para verificar se chegou no final do arquivo

        # Concatena o padrão com o atual caractere lido
        pattern = ''.join((pattern, char))
        prefixCode = tree.find(pattern)

        # Padrão existe na Trie. Acúmula o caractere e vai para a próxima iteração
        if prefixCode != -1:
          continue
        # Padrão não existe na Trie, então deve ser inserido
        else:
          # Insere o padrão na Trie e pega o código do prefixo
          prefixCode = tree.insert(pattern)

          if prefixCode > highestCode: highestCode = prefixCode

          outputFile.write(f'{prefixCode}~{char}|')
          # Define o padrão como a string vazia
          pattern = ''
      
      # É preciso fazer uma última verificação após while para tratar o caso em que
      # o último caractere da entrada for acumulado no padrão, visto que, quando isso
      # ocorre, ele não é gerado na saída no while.
      if pattern != '':
        if prefixCode > highestCode: highestCode = prefixCode
        outputFile.write(f'{prefixCode}~{char}|')
  
  # Gerando o relatório com a taxa de compressão
  with open('./compressionReport.txt', 'w', encoding='utf-8') as reportFile:
    # Obtém o tamanho do arquivo original em bits (tamanho em bytes * 8)
    originalFileBitSize = stat(filename).st_size * 8

    # Número de nós na Trie (sem contar a raiz)
    trieNodeCount = tree.nextCode - 1

    # O cálculo do tamanho teórico do arquivo de saída é feito considerando que, para cada nó na Trie, será 
    # salvo o código numérico do seu prefixo e o caractere associado ao nó. Dessa forma, para cada nó serão 
    # gastos o número de bits necessário para armazenar o código mais 1 byte (8 bits) para o caractere
    outputFileBitSize = trieNodeCount * (highestCode.bit_length() + 8)

    # A taxa de compressão considerada é a razão entre o tamanho do arquivo de saída e o arquivo de entrada
    compressionRate = outputFileBitSize / originalFileBitSize

    reportFile.write(f'Input: {filename} - Bit size: {originalFileBitSize}\n')
    reportFile.write(f'Output: {output} - Bit size: {outputFileBitSize}\n')
    reportFile.write(f'Taxa de compressão: {round(compressionRate, 2)}\n')

# Descompressão seguindo o LZ78
def decompression(filename, output):
  with open(filename, 'r', encoding='utf-8') as inputFile:
    with open(output, 'w', encoding='utf-8') as outputFile:
      # Faz o split da entrada (sem considerar o primeiro e o último caracteres)
      input = inputFile.read().split('|')[1:-1]
      # Aplica um novo split em cada elemento da lista gerada pelo primeiro split
      # para separar os códigos dos caracteres
      input = [x.split('~') for x in input]

      # Lista auxiliar que contém os prefixos computados ao longo do for
      aux = ['']
      for index, char in input:
        # A string gerada será o prefixo do elemento atual concatenado com o caractere associado a ele
        newStr = f'{aux[int(index)]}{char}'
        aux.append(newStr)
        outputFile.write(newStr)
