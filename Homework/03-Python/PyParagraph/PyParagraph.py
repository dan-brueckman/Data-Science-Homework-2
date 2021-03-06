import os
txt_file = os.path.join(".", "Homework_Python_Word_Counter.txt")
alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
         "S", "T", "U", "V", "W", "X", "Y", "Z"]
with open(txt_file, "r") as tf:
    data = tf.read()
    letter_count = 0
    words = len(data.split())
    sentences = data.count(". ") + 1
    for letter in alpha:
        under = data.count(letter)
        letter_count += under
    avg_letters = (letter_count / words)
    avg_words = words / sentences

print("Paragraph Analysis")
print("------------------")
print("Approximate Word Count: " + str(words))
print("Approximate Sentence Count: " + str(sentences))
print("Average Letter Count: " + str(avg_letters))
print("Average Word Count: " + str(avg_words))


