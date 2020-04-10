import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer

sentences = [
    'I love Python',
    'I love Java too' ]


tokenizer = Tokenizer(num_words=100) # num of words to tokenize here we pass 100
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index

print(word_index)
'''results: {'i': 1, 'love': 2, 'python': 3, 'java': 4, 'too': 5}'''