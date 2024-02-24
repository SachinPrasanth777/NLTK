from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string
example_string = """Muad'Dib learned rapidly because his first training was in how to learn.
 And the first lesson of all was the basic trust that he could learn.
 It's shocking to find how many people do not believe they can learn,
 and how many more believe learning to be difficult."""
def remove_punc(input_string):
    punctuations=string.punctuation
    output="".join(word for word in example_string if word not in punctuations)
    return output
removed_punc=remove_punc(example_string)
words=word_tokenize(removed_punc)
sent=sent_tokenize(removed_punc)
stop_words=set(stopwords.words('english'))
filtered_list=[word for word in sent if word.casefold() not in stop_words]
stemmer=PorterStemmer()
stemmed_words=[stemmer.stem(word) for word in words]
print(stemmed_words)
