def print_words_by_length(filename , length):
  file = open("python.txt" , "p")
  text = file.read()
  file.close()
  words = text.split()
  print(f"Words of length {length}: ")
  for word in words:
    if len(word) == length:
      print (word)
# user input
fname = input("Enter file name: ")
1 = int(input("Enter word length: "))
print_words_by_length (fname, 1)
