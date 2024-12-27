#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

def limpia_palabra(filename):
  remover=[',',':','.','"',"'",' ','-','´','?','!','(',')','`','*',';']
  archivo_final=[]
  archivo=open(str(filename),'r')
  for linea in archivo:
    linea=linea.split()
    for palabra in linea:
      palabra=[char.lower() for char in palabra]
      palabra=[letra for letra in palabra if letra not in remover]
      palabra_final=''.join(palabra)
      archivo_final.append(palabra_final)
  archivo.close()
  del(archivo)
  return archivo_final

def cuenta_palabras(filename):
  archivo=limpia_palabra(filename)
  palabras={}
  for palabra in archivo:
    if palabra in palabras:
      palabras[palabra]+=1
    else:
      palabras[palabra]=1
  return  palabras


def print_words(filename):
  palabras=cuenta_palabras(filename)
  keys=sorted(palabras.keys())
  for palabra in keys :print(palabra,palabras[palabra])
  return


def print_top(filename):
  palabras=cuenta_palabras(filename)
  palabras_tuplas= sorted(palabras.items(), key= lambda x:x[-1],reverse=True)
  top=1
  for count in palabras_tuplas:
    print(f'Top {top} - {count[0]}', {count[1]})
    top+=1
    if top>20: break
  return



###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
  main()
