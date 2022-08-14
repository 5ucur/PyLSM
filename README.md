# PyLSM

**PyLSM** - Language Style Matching in Python. Compare two bodies of text and get their LSM ratio. Higher ratio means more similar.

# How it works

PyLSM is based on the research by Ireland, Eastwick, Slatcher, and Scissors in 2011. The program first generates a list of part of speech (POS) tags in each of the given texts, counts the occurences of each POS tag, and determines the ratio for each tag as compared to the total word count. Then it compares the tag proportions between the texts.  

# Why the Serbian Cyrillic version

For fun. There is a version in Latin (English) as well. Both should work the same.

# Installation

After installing spacy (pip install -r requirements.txt), validate it by running  
`python -m spacy validate`  
and if need be (especially if the validation command does not report en_core_web_sm being installed), run  
`python -m spacy download en_core_web_sm`

## Arch Linux

On Arch, install spacy from AUR (yay python-spacy), then run  
`python -m spacy download en_core_web_sm`

# Special thanks

Special thanks to my friend and fellow programmer, [@grishatop1](https://github.com/grishatop1), for testing this program. I have helped develop some of his programs, and tested others. I am thankful he was able to test PyLSM for me. Go check out his work!

--------

# ПајПЈС

**ПајПЈС** - Подударање језичких стилова у Пајтону. Пореди два комада текста и даје њихов ПЈС однос. Већи износ означава већу сличност.

# Како овај програм ради

ПајПЈС је заснован на истраживању које су вршили Ајерланд, Иствик, Слечер и Сизорс 2011. године. Програм прво направи списак свих врста ријечи у оба текста, преброји колико се пута појављује која врста ријечи, те одреди однос између тог броја и укупног броја ријечи. Затим се ти односи из оба текста успоређују.   

# Зашто српска ћирилична верзија

Из чисте забаве. Постоји и верзија на латиници, на енглеском. Обје би верзије требало да раде подједнако.

# Инсталација

Након што инсталирате библиотеку spacy (pip install -r requirements.txt), потврдите је командом  
`python -m spacy validate`  
те ако има потребе (нарочито ако команда за потврду не пријави постојање en_core_web_sm на Вашем уређају), извршите команду   
`python -m spacy download en_core_web_sm`

## Арч Линукс

На Арчу, инсталирајте spacy преко AUR-a (yay python-spacy), затим извршите команду  
`python -m spacy download en_core_web_sm`

# Посебна захвалност

Посебно хвала мом пријатељу и колеги програмеру, [@grishatop1](https://github.com/grishatop1), што је тестирао овај програм. Помогао сам му у развоју неких од његових програма, а друге сам тестирао. Захвалан сам што је он могао да издвоји времена и тестира ПајПЈС. Погледајте његов рад!
