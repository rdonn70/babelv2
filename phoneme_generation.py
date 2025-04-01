import random
import os
import re
import csv

def csv_scraper(csv_file_path="en_US.csv"):
    data = []
    csvfile = open(csv_file_path, 'r', encoding='utf-8', newline='')
    csv_read = csv.reader(csvfile)
    
    for x in csv_read:
        if len(x) >= 2:
            if("," in x[1]):
                temp_x = x[1].split(',')
                data.append((x[0], temp_x[0].replace('/', '').replace('ˈ', '').replace('ˌ', '').replace(' ', '')))
            else:
                data.append((x[0], x[1].replace('/', '').replace('ˈ', '').replace('ˌ', '').replace(' ', '')))
    csvfile.close()
    return data

def character_scraper(string_list=["", ""]):
    unique_chars = set()
    for x in string_list:
        for y in x[1]:
            unique_chars.update(y)
    return unique_chars

def phoneme_mapper(list1=["extracted"], list2=["generated"]):
    while(len(list1) > len(list2)):
        phoneme1 = random.choice(list2)
        phoneme2 = random.choice(list2)
        if(phoneme1 != phoneme2):
            new_phoneme_combo = phoneme1 + phoneme2
            list2.append(new_phoneme_combo)
    list2_new = list2[0:len(list2)]

    return dict(zip(list1, list2_new))

def phoneme_generation(count):
    consonants = ['m̥', 'm', 'ɱ', 'n̼', 'n̥', 'n', 'ɳ̊', 'ɳ', 'ɲ̊', 'ɲ', 'ŋ̊', 'ŋ', 'ɴ̥', 'ɴ', 'p', 'b', 'p̪', 'b̪', 't̼', 'd̼', 't̪', 'd̪', 't', 'd', 'ʈ', 'ɖ', 
                  'c', 'ɟ', 'k', 'g', 'q', 'ɢ', 'ʡ', 'ʔ', 't̪s̪', 'd̪z̪', 'ts', 'dz', 't̠ʃ', 'd̠ʒ', 'tʂ', 'dʐ', 'tɕ', 'dʑ', 'pɸ', 'bβ', 'p̪f', 'b̪v', 't̪θ',
                  'd̪ð', 'tɹ̝̊', 'dɹ̝', 't̠ɹ̠̊˔', 'd̠ɹ̠˔', 'cç', 'ɟʝ', 'kx', 'ɡɣ', 'qχ', 'ɢʁ', 'ʡʜ', 'ʡʢ', 'ʔh', 's', 'z', 'ʃ', 'ʒ', 'ʂ', 'ʐ', 'ɕ', 'ʑ', 'ɸ',
                  'β', 'f', 'v', 'θ̼', 'ð̼', 'θ', 'ð', 'θ̠', 'ð̠', 'ɹ̠̊˔', 'ɹ̠˔', 'ɻ̊˔', 'ɻ˔', 'ç', 'ʝ', 'x', 'ɣ', 'χ', 'ʁ', 'ħ', 'ʕ', 'h', 'ɦ', 'β̞', 'ʋ', 'ð̞',
                  'ɹ', 'ɹ̠', 'ɻ', 'j', 'ɰ', 'ʁ̞', 'ʔ̞', 'ⱱ̟', 'ⱱ', 'ɾ̼', 'ɾ̥', 'ɾ', 'ɽ̊', 'ɽ', 'ɢ̆', 'ʡ̆', 'ʙ̥', 'ʙ', 'r̥', 'r', 'r̠', 'ɽ̊r̥', 'ɽr', 'ʀ̥', 'ʀ', 'ʜ', 'ʢ',
                  'tɬ', 'dɮ', 'tꞎ', 'ɟʎ̝', 'ɡʟ̝', 'ɬ', 'ɮ', 'ꞎ', 'ʎ̝', 'ʟ̝', 'l̪', 'l', 'l̠', 'ɭ', 'ʎ', 'ʟ', 'ʟ̠', 'ɺ̥', 'ɺ', 'ʎ̆', 'ʟ̆']
    vowels = ['i', 'y', 'ɨ', 'ʉ', 'ɯ', 'u', 'ɪ', 'ʏ', 'ʊ', 'e', 'ø', 'ɘ', 'ɵ', 'ɤ', 'o', 'e̞', 'ø̞', 'ə', 'ɤ̞', 'o̞', 'ɛ', 'œ', 'ɜ', 'ɞ', 'ʌ', 'ɔ', 'æ', 'ɐ',
              'a', 'ɶ', 'ä', 'ɑ', 'ɒ']
    
    phoneme_list = []
    x = 1
    while(x <= count):
        if random.randint(0, 1) == 0:
            consonant_choice = random.choice(consonants)
            consonants.remove(consonant_choice)
            phoneme_list.append(consonant_choice)
        else:
            vowel_choice = random.choice(vowels)
            vowels.remove(vowel_choice)
            phoneme_list.append(vowel_choice)
        x += 1
    return phoneme_list

def language(min_phonemes=12, max_phonemes=40):
    number = random.randint(min_phonemes, max_phonemes)
    phonemes = phoneme_generation(number)
    csv_list = csv_scraper()
    phoneme_dict = phoneme_mapper(character_scraper(csv_list), phonemes)
    #print(phoneme_dict)
    new_language = []
    for x in csv_list:
        temp = "/"
        for y in x[1]:
            try:
                temp += phoneme_dict[y]
            except:
                pass
        new_language.append(temp + "/")
    
    old_language = []
    for z in csv_list:
        old_language.append(z[0])
    return dict(zip(old_language, new_language))

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    dictionary = language()
    input_sentence = input("Enter a sentence to translate: ")
    input_sentence = re.sub(r'[^\w\s]','',input_sentence)
    
    sentence = input_sentence.split()
    for x in sentence:
        print(dictionary[x.strip().lower()], end=" ")
