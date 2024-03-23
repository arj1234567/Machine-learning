
##from nltk.tokenize import word_tokenize
##data = "I pledge to be a data scientist one day"
##tokenized_text=word_tokenize(data)
##print(tokenized_text)
##print(type(tokenized_text))
##
##
##
##from nltk.tokenize import RegexpTokenizer
##tokenizer = RegexpTokenizer(r'\w+')
##result = tokenizer.tokenize("Wow! I am excited to learn data science")
##print(result)




##from nltk.corpus import stopwords
##from nltk.tokenize import word_tokenize
##
##print(stopwords.words('english'))
##
##to_be_removed = set(stopwords.words('english'))
##para="""Cake is a form of sweet food made from flour, sugar, and other ingredients, that is usually baked.
##In their oldest forms, cakes were modifications of bread, but cakes now cover a wide range of preparations 
##that can be simple or elaborate, and that share features with other desserts such as pastries, meringues, custards, 
##and pies."""
##tokenized_para=word_tokenize(para)
##print(tokenized_para)
##
##
##modified_token_list=[word for word in tokenized_para if not word in to_be_removed]
##print(modified_token_list)

##from nltk.corpus import wordnet
##syns = wordnet.synsets("chair") 
##print(syns[0].definition())  
##print(syns[0].examples())


import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
content = """Cake is a form of sweet food made from flour, sugar, and other ingredients, that is usually baked.
In their oldest forms, cakes were modifications of bread, but cakes now cover a wide range of preparations 
that can be simple or elaborate, and that share features with other desserts such as pastries, meringues, custards, 
and pies."""
words= [word_tokenize(i) for i in sent_tokenize(content)]
pos_tag= [nltk.pos_tag(i,tagset="universal") for i in words]
print(pos_tag)
