x = 'C:/lab10/sentences.txt'
f = open(x, "rt")
z = f.read()
print(z)

words=z.split()
word_count = len(words)

rozpovidni_sentences = z.count('.')
pytalni_sentences = z.count('?')
oklychni_sentences = z.count('!')

print("Загальна кількість слів: ", word_count)
print("Кількість розповідних речень: ", rozpovidni_sentences)
print("Кількість питальних речень: ", pytalni_sentences)
print("Кількість окличних речень: ", oklychni_sentences)

f.close
