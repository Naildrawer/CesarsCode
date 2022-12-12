def isdirection():
  direction = input('Шифруем или дешифруем текст? ')
  while direction.lower() not in ['шифруем', 'дешифруем']:
    print('Введите корректное значение')
    direction = input('Шифруем или дешифруем текст? ')
  return direction  

def language():
  lang = input('Выберите язык (ru/en) ')
  while lang.lower() not in ['ru', 'en']:
    print('Введите корректное значение')
    lang = input('Выберите язык (ru/en) ')
  return lang

def cesarstep():
  step = input("Введите шаг сдвига ")
  while step.isdigit() == False:
    print("Введите корректное значение")
    step = input("Введите шаг сдвига ")
  return step

def inputwords():
  words = input("Введите текст ")
  while words.isspace() == True:
    print('Введен пустой текст')
    words = input("Введите текст ")
  return words  

def coding(lang, step, words, direction):
  upper_eng_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  lower_eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'
  upper_rus_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
  lower_rus_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
  for i in range(len(words)):
    if lang == 'ru':
      rot = 32
      low_alphabet = lower_rus_alphabet
      upp_alphabet = upper_rus_alphabet
    if lang == 'en':
      rot = 26
      low_alphabet = lower_eng_alphabet
      upp_alphabet = upper_eng_alphabet
    if words[i].isalpha():
      if words[i] == words[i].lower():
        place = low_alphabet.index(words[i])
      if words[i] == words[i].upper():
        place = upp_alphabet.index(words[i])
      if direction.lower() == 'дешифруем':
        index = (place - int(step)) % rot
      elif direction.lower() == 'шифруем':
        index = (place + int(step)) % rot
      if words[i] == words[i].lower():
        print(low_alphabet[index], end = '')
      if words[i] == words[i].upper():
        print(upp_alphabet[index], end = '')
    else:
      print(words[i], end = '')
    
  
        
  
direction = isdirection()
lang = language()
step = cesarstep()
words = inputwords()
coding(lang, step, words, direction)
