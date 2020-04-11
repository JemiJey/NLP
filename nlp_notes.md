#### Notes

- when we do tokenizer in train data set the same dictionary or word index should be used for test data as well

- use oov_token to specify if the word is out of token in the test data

- pad_sequences has paarameters as sequences and before or after the sentence and max_length 
  padded = pad_sequences(sequences, padding = 'post', max_length=5)

- imdb, info = tfds.load("imdb_reviews", with_info = True, as_supervised=True)
  this code will download the data and give the meta data 