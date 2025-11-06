# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string magic = 'abracadabra',
magic = 'abracadabra'
# a. Retrieve the 5th character.
fifth_char = print(magic[4])
# b. Retrieve the second to last character.
second_to_last_char = print(magic[-2])
# c. Find the first occurrence of the letter 'c'.
first_c_index = print(magic.index('c'))
# find the last occurrence of the letter 'a'
last_a_index = print(magic.rindex('a'))


# Advanced Slicing:
# Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
alphabet = "abcdefghijklmnopqrstuvwxyz"
# a. Extract the letters 'hij'.
# hij = print(alphabet[7:10])
hij = print(alphabet.index('hij'))
hij2 = print(alphabet[7:10])
# b. Extract every second letter starting from 'a' to 'm'.
m_index = print(alphabet.index('m')) # ouput: 12
every_second = print(alphabet[0:13:2]) #output: acegikm
# c. Reverse the entire string using slicing.
reversed_alphabet = print(alphabet[ : :-1]) # output
i_have_a_dream = "I have a dream that one day this nation will rise up and live out the true meaning of its creed: We hold these truths to be self-evident, that all men are created equal"
reversed_speech = print(i_have_a_dream[ : :-1])


# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
famous_quote = "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
john_f_kennedy = print(famous_quote.find("John F. Kennedy"))
# output: ninety-eight
extracted_name = print(famous_quote[83: ])



# Manipulating Words:
# Given the string info = "Python is fun. Fun is good. Good is subjective.",
phrase = "Python is fun. Fun is good. Good is subjective."
# a. Extract the word 'subjective' without knowing its exact position.
word = print(phrase.find("subjective"))
extracted_word = print(phrase[36: ])
# b. Extract every third word.
every_three_words = print(phrase[ : :3])
# c. Reverse the positions of the words, but keep the characters in each word in the same order.
words = phrase.split()
print(words)
reversed_words = ' '.join(reversed(words))
print(reversed_words)



# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
statement = "MAY THE FORCE BE WITH YOU."
print(statement.lower())

# String Joining and Splitting:
# Given the list motto = ["Make", "haste", "slowly."],
# a. Convert the list into a single string.
motto = ["Make", "haste", "slowly."]
joined_motto = ' '.join(motto)
print(joined_motto)
joined_motto_split =joined_motto.split('a')
print(joined_motto_split) 
# b. Now, split the string at every occurrence of the letter 'a'.


# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."
sentence = "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
replaced_sentence = print(sentence.replace("busy", "distracted").replace("plans", "mistakes"))
# b. Replace "plans" with "mistakes".

# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.
repeated_word = print("Iteration " * 7)

# Word Search:
# Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
word = "freedom"
quote = "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
word_in_quote = print(word in quote)

# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".
state = "Supercalifragilisticexpialidocious"
length_of_state = print(len(state))
# b. Count the number of times the letter 'i' appears in the same word/phrase.
