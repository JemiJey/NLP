import tensorflow as tf 
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer 

sentences = [
    'Don\'t hate anyone',
    'Nothing is permanant',
    'life is too short so be happy and content'
]

tokenizer = Tokenizer(num_words=100, oov_token="<oov>")
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index

sequences = tokenizer.texts_to_sequences(sentences)

print(sequences)
print(word_index)

test_data = [
    'Don\'t be a mediocre',
    'Nothing is impossible'
]

test_data = tokenizer.texts_to_sequences(test_data)
print(test_data)