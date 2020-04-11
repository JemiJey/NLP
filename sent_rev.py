import tensorflow as tf 
print(tf.__version__)
import tensorflow_datasets as tfds
import numpy as np 
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

imdb, info = tfds.load("imdb_reviews", with_info = True, as_supervised=True)

train_data, test_data = imdb['train'], imdb['test']

traiing_sentences = []
training_labels = []

testing_sentences = []
testing_labels = []

for s,l in train_data:
    traiing_sentences.append(str(s.numpy())) #s and l are tensors so calling numpy we can extract the values
    training_labels.append(str(l.numpy()))


for s,l in test_data:
    testing_sentences.append(str(s.numpy()))
    testing_labels.append(str(l.numpy()))

training_labels_final = np.array(training_labels)
testing_labels_final = np.array(testing_labels)

vocab_size = 10000
embedding_dim = 16
max_length = 120
trunc_type = 'post'
oov_tok = "<oov>"


tokenizer = Tokenizer(num_words = vocab_size ,oov_token = oov_tok)
tokenizer.fit_on_texts(traiing_sentences)
word_index = tokenizer.word_index
sequences = tokenizer.texts_to_sequences(traiing_sentences)
padded = pad_sequences(sequences, maxlen = max_length, truncating=trunc_type)


testing_sequences = tokenizer.texts_to_sequences(testing_sentences)
test_padded = pad_sequences(testing_sequences, maxlen = max_length)

model = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length = max_length),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(6, activation = 'relu'),
    tf.keras.layers.Dense(1, activation = 'sigmoid')
])

model.compile(loss='binary_crossentropy', optimizer = 'adam', metrics=['accuracy'])
model.summary()

num_epochs = 10
model.fit(padded, training_labels_final, epochs = num_epochs, validation_data = (test_padded, testing_labels_final))
# print(info)