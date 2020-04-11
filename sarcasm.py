import json
import tensorflow as tf 
from tensorflow.keras.preprocessing.text import Tokenizer 
from tensorflow.keras.preprocessing.sequence import pad_sequences

data = [json.loads(line) for line in open('data/nlp/Sarcasm_Headlines_Dataset_v2.json', 'r')]
'''with open('data/nlp/Sarcasm_Headlines_Dataset_v2.json', 'r') as f:
    datastore = json.load(f)'''

urls = []
labels = []
sentences = []


for item in data:
    sentences.append(item['headline'])
    urls.append(item['article_link'])
    labels.append(item['is_sarcastic'])

# print(sentences)

tokenizer = Tokenizer(oov_token = "<oov>")
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index
print(word_index)

sequences = tokenizer.texts_to_sequences(sentences)
padded = pad_sequences(sequences, padding = 'post')
print(padded[0])
print(padded.shape)