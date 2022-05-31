from optparse import OptionParser
from LZ78 import compression, decompression

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
