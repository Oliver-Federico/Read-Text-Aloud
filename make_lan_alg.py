import random
import os
from name_data_base import find_name
alphabet = [
    "b",
    "c", "d", 
    "f",
    "g", "h",
    "j",
    "k", "l",
    "m", "n",
    "p",
    "q", "r",
    "s", "t",
    "v",
    "w", 
    "z"
]
vowels = ["a","e","i","o","u"]
special_sounds = ["ch","ph","sh", "pl", "th", "fr", "sp", "qu","br", "zh", "lo", "po", "za"]
#middle_sounds =["oo", "qu", "za", "ze", "lo", "po", "re", "go", "de", "te"]
end_letters = ["k", "p", "g", "t", "d", "h", "d", "z", "p"]
end_sounds = ["am","an","all","ang","ank","ing","ink","ong","onk","ung","unk","eed","ck"]

nameEnd = special_sounds[random.randint(0, len(special_sounds)-1)] + end_sounds[random.randint(0, len(special_sounds)-1)]

def main(english_text):
    words_seperated = sperate_words(english_text)
    newlanguagelist = randomizeList(words_seperated)
    return list_to_string(newlanguagelist)

def sperate_words(english_text):
    words_seperated = []
    last_space = 0
    for letters in range(len(english_text)):
        if english_text[letters] == " ":
            words_seperated.append(english_text[last_space:letters].replace(" ","").lower())
            last_space = letters
    return words_seperated

def randomizeList(list_en):
  final = []
  for word in range(len(list_en)):
    if check_in_dictionary(list_en[word]):
      newWord = translate(list_en[word]).replace(" ","")
    else:
      newWord = changeLetter(list_en[word])
      newWord = change_prefixes_and_suffixes(newWord,list_en[word])
    final.append(newWord)
    addToDictionary(list_en[word],newWord)
  return final

def changeLetter(word):
  newWord = word
  for letter in range(len(word)): 
    if word[letter] in vowels:
      rand_num_vowel = random.randint(0,len(vowels)-1)
      rand_letter = vowels[rand_num_vowel]
    elif word[letter].isalpha() == False:
      rand_letter = word[letter]
    else:
      rand_num = random.randint(0,len(alphabet)-1)
      rand_letter = alphabet[rand_num]
    newWord = newWord.replace(word[letter],rand_letter)
  return newWord

def change_prefixes_and_suffixes(newWord,og_word):
    if find_name.findName(og_word):
      newWord = ""
      return og_word + nameEnd

    if len(newWord) >= 3:
      special_start_sound = special_sounds[random.randint(0,len(special_sounds)-1)]
      special_vowel = vowels[random.randint(0, len(vowels)-1)]
      while special_vowel == special_start_sound:
        special_vowel = vowels[random.randint(0, len(vowels)-1)]   
      newWord = newWord.replace(newWord[0:2], special_start_sound)
      newWord = newWord.replace(newWord[2], special_vowel)
      #hello thi schange ajishckasnca;d
      #end sounds
      special_end = end_letters[random.randint(0,len(end_letters)-1)]
      vowel_before_end = vowels[random.randint(0, len(vowels)-1)]
      while special_vowel == vowel_before_end:
        vowel_before_end = vowels[random.randint(0, len(vowels)-1)]
      newWord = newWord.replace(newWord[-1], special_end)
      newWord = newWord.replace(newWord[-2], vowel_before_end)

    if len(newWord) <= 3:
      newWord = newWord.replace(newWord[random.randint(0,len(newWord)-1)], vowels[random.randint(0,len(vowels)-1)])

    return newWord

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

def addToDictionary(word,rand_word):
    clean_word = word
    clean_rand_word = rand_word
    for x in range(len(word)):
       if word[x].isalpha() == False:
          clean_word = word.replace(word[x], "")

    for y in range(len(rand_word)):
       if rand_word[y].isalpha() == False:
          clean_rand_word = rand_word.replace(rand_word[y], "")

    dic = open("Dictionary.txt", "at")
    if check_in_dictionary(clean_word) == False:
      dic.writelines(clean_word + " : " + clean_rand_word + "\n")
    dic.close()
         
def check_in_dictionary(word_to_test):
  read_txt = open("Dictionary.txt", "rt")
  dictionary = read_txt.readlines()
  read_txt.close()
  clean_test = word_to_test
  if len(dictionary) <= 0:
     return False
  else:
    for k in range(len(word_to_test)):
       if word_to_test[k].isalpha() == False:
          clean_test = word_to_test.replace(word_to_test[k], "")
    for x in range(len(dictionary)):
      for o in range(len(dictionary[x])):
        if dictionary[x][o] == ":":
           if clean_test == dictionary[x][:o-1]:
              return True
  return False
    
def list_to_string(new_lan_list):
    final_str = ""
    for l in range(len(new_lan_list)):
      final_str =final_str + new_lan_list[l]+ " "
    print(final_str)
    return final_str
      

  


                

