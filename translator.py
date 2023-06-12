
def main():
  user = input("Word to Translate: ").lower()
  print("Translated: " + translate(user) + "\n")


def translate(word):
  read_txt = open("Dictionary.txt", "rt")
  dictionary = read_txt.readlines()
  read_txt.close()
  clean_test = word
  word_with_nonChar = False

  for k in range(len(word)):
    if word[k].isalpha() == False:
      word_with_nonChar=True
      clean_test = word.replace(word[k], "")

  for x in range(len(dictionary)):
    for p in range(len(dictionary[x])):
      if dictionary[x][p] == ":":
        if clean_test == dictionary[x][:p-1]:
          final = dictionary[x][p+1:].replace("\n", "")
          final = final.replace(" ","")
          if word_with_nonChar:
            return final + word[-1]
          else:
            return final
  return "Couldn't find any instances of that word in the dictionary, sorry."
          

main()




