from gtts import gTTS
import os
import make_lan_alg
all_things_to_read = []
period = "."
comma = ","
language = "es"

def main():
    file = open("english.txt", "rt")
    all_things_to_read = file.readlines()
    text_to_read = get_lines(all_things_to_read, len(all_things_to_read))
    text_in_AI_lan = make_lan_alg.main(text_to_read.replace("\n",""))
    output_mp3(text_in_AI_lan)
    
def get_lines(all_text_to_read, file_length):
    final_seperation = ""
    for lines in range(file_length):
        final_seperation = final_seperation + all_text_to_read[lines] + " "
    return final_seperation

def output_mp3(text_to_read):
    read = gTTS(text=text_to_read, lang=language, slow=True)
    read.save("text_to_read.mp3")
    os.system("text_to_read.mp3")

main()