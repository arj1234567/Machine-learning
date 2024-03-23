import nltk
##nltk.download()

from nltk.tokenize import word_tokenize
##data = "Hello how are you, where are you going ?"
##tokenized_text = word_tokenize(data)
##print(tokenized_text)
##print(type(tokenized_text))
##
##from nltk.tokenize import RegexpTokenizer
##tokenizer = RegexpTokenizer(r'\w+')
##result = tokenizer.tokenize("Hello how are you, where are you going ?")
##print(result)

##from nltk.corpus import stopwords
##from nltk.tokenize import word_tokenize
##to_be_removed = set(stopwords.words('english'))
##para =""" Cricket is a bat-and-ball game played between two teams of eleven players
##on a field at the centre of which is a 22-yard (20-metre) pitch with a
##wicket at each end, each comprising two bails balanced on three stumps."""
##tokenized_para = word_tokenize(para)
##print(tokenized_para)
##modified_token_list = [word for word in tokenized_para if not word in to_be_removed]
##print(modified_token_list)

##from nltk.corpus import wordnet
##syns = wordnet.synsets("hat")
##print(syns[0].definition())
##print(syns[0].examples())

from nltk.tokenize import sent_tokenize,word_tokenize
content = """ Cricket is a bat-and-ball game played between two teams of eleven players
on a field at the centre of which is a 22-yard (20-metre) pitch with a
wicket at each end, each comprising two bails balanced on three stumps.  """
words = [word_tokenize(i) for i in sent_tokenize(content)]
pos_tag = [nltk.pos_tag(i,tagset = "universal") for i in words]
print(pos_tag)
