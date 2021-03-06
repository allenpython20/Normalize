
import inflect
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import re
import unicodedata
import datetime
from googletrans import Translator
from mtranslate import translate
from bs4 import BeautifulSoup
import string 

class PreProcessing:
    def __init__(self):
        pass

    def remove_non_ascii(self,words):
        """Remove non-ASCII characters from list of tokenized words"""
        new_words = []
        for word in words:
            new_word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')
            new_words.append(new_word)
        return new_words


    def to_lowercase(self,words):
        """Convert all characters to lowercase from list of tokenized words"""
        new_words = []
        for word in words:
            new_word = word.lower()
            new_words.append(new_word)
        return new_words

    def remove_space(self,words):
        new_words = []
        for word in words:
            new_word = word.strip()
            new_words.append(new_word)
        return new_words

    def remove_incomplete_tags_html(self,words):
        new_words = []
        rep = {"<STRONG": "", "STRONG>": "","ENDIF":""} # define desired replacements here
        for word in words:
            rep = dict((re.escape(k), v) for k, v in rep.items()) 
            pattern = re.compile("|".join(rep.keys()))
            new_word = pattern.sub(lambda m: rep[re.escape(m.group(0))], word)
            new_words.append(new_word)
        return new_words

    def remove_tags_html(self,words):
        new_words = []
        for word in words:
            new_word = BeautifulSoup(word, "lxml").text
            new_words.append(new_word)
        return new_words


    def remove_punctuation_space_start(self,words):
        new_words = []
        for word in words:
            word = word.lower()
            #\$%&\'\(\)\*\+,\-./:;<=>\?@\[\\\]\^_\`\{\|\}~
            #new_word =  re.sub('^[0-9#!\$\?\.\*\|\{\}\+_:\-=?? ]*','',word)
            new_word =  re.sub('^[0-9#!$???.*<>()|,+_:=??\- ]*','',word)
            #new_word =  re.sub('^[#!\$\?\.\*\|\{\}\+-_:=????? ]*','',word)
            new_word = new_word.upper()
            new_words.append(new_word)
        return new_words

    def remove_punctuation_space_start2(self,words):
        new_words = []
        for word in words:
            word = word.lower()
            #\$%&\'\(\)\*\+,\-./:;<=>\?@\[\\\]\^_\`\{\|\}~
            #new_word =  re.sub('^[0-9#!\$\?\.\*\|\{\}\+_:\-=?? ]*','',word)
            new_word =  re.sub('^([0-9#!\$??\?\.\*<>\)\|,\-\+_:=\??]|[a-z]\.)*','',word)
            #new_word =  re.sub('^[#!\$\?\.\*\|\{\}\+-_:=????? ]*','',word)
            new_word = new_word.upper()
            new_words.append(new_word)
        return new_words

    def prueba(self,words):
        new_words = []
        for word in words:
            word = word.lower()
            #\$%&\'\(\)\*\+,\-./:;<=>\?@\[\\\]\^_\`\{\|\}~
            new_word =  re.sub('^[0-9#!$??.*()|+_:=??- ]*','',word)
            new_word = new_word.upper()
            new_words.append(new_word)
        return new_words

    def remove_punctuation_space_end(self,words):
        new_words = []
        cadena = string.punctuation
        for word in words:
            #\$%&\'\(\)\*\+,\-./:;<=>\?@\[\\\]\^_\`\{\|\}~
            word = word.lower()
            #new_word =  re.sub('[!\?\.\*\|\{\}\+_:-=?? ]*$','',word)
            new_word =  re.sub('[!$?.,<>*(|_:=??\- ]*$','',word)
            new_word = new_word.upper()
            new_words.append(new_word)
        return new_words

    def remove_punctuation_start(self,words):
        new_words = []
        for word in words:
            #new_word = word.strip(".:_-")
            new_word = word.lstrip(string.punctuation)
            new_words.append(new_word)
        return new_words

    def remove_punctuation_end(self,words):
        new_words = []
        cadena = string.punctuation
        cadena = cadena.replace('+','').replace('#','')
        for word in words:
            new_word = word.rstrip(cadena)
            new_words.append(new_word)
        return new_words

    def remove_space_start_end(self,words):
        """Convert all characters to lowercase from list of tokenized words"""
        new_words = []
        for word in words:
            new_word = word.strip()
            new_words.append(new_word)
        return new_words


    def remove_punctuation(self,words):
        """Remove punctuation from list of tokenized words"""
        new_words = []
        for word in words:
            new_word = re.sub(r'[^\w\s]', '', word)
            if new_word != '':
                new_words.append(new_word)
        return new_words


    def replace_numbers(words):
        """Replace all interger occurrences in list of tokenized words with textual representation"""
        p = inflect.engine()
        new_words = []
        for word in words:
            if word.isdigit():
                new_word = p.number_to_words(word)
                new_words.append(new_word)
            else:
                new_words.append(word)
        return new_words


    def remove_stopwords(words):
        """Remove stop words from list of tokenized words"""
        new_words = []
        for word in words:
            if word not in stopwords.words('spanish'):
                new_words.append(word)
        return new_words


    def stem_words(words):
        """Stem words in list of tokenized words"""
        stemmer = LancasterStemmer()
        stems = []
        for word in words:
            stem = stemmer.stem(word)
            stems.append(stem)
        return stems


    def lemmatize_verbs(words):
        """Lemmatize verbs in list of tokenized words"""
        lemmatizer = WordNetLemmatizer()
        lemmas = []
        for word in words:
            lemma = lemmatizer.lemmatize(word, pos='v')
            lemmas.append(lemma)
        return lemmas


    def delete_irrelevantwords(words):
        irrelevantwords = ['beneficios', 'requisitos', 'objetivos', 'competencias', 'funciones']
        new_words = []
        for word in words:
            if word not in irrelevantwords:
                new_words.append(word)
        return new_words


    def stemmer_english(words):
        stemmer = SnowballStemmer('spanish')
        wordsStemmer = []
        for word in words:
            element = stemmer.stem(word)
            wordsStemmer.append(element)
        return wordsStemmer


    def delete_empty(words):
        elements = []
        for word in words:
            if word is not None and word.strip() != "":
                elements.append(word)
        return elements

    def delete_sentence_one_word(sentences):
        elements = []
        for sentence in sentences:
            if sentence is not None and sentence.strip() != "" and len(sentence.split()):
                elements.append(sentence)
        return elements

    def translate_english(text):
        translator = Translator()
        textEnglish = translator.translate(text).text
        return textEnglish


    def translate_english_sentences(sentences):
        translator = Translator()
        sentencesTranslate = []
        for sentence in sentences:
            print("===================")
            print(len(sentence))
            print(sentence)
            sentenceEnglish = translate(sentence)
            print(sentenceEnglish)
            sentencesTranslate.append(sentenceEnglish)
        return sentencesTranslate

    def normalize_words(words):
        words = remove_non_ascii(words)
        words = to_lowercase(words)
        words = remove_punctuation(words)
        words = replace_numbers(words)
        words = remove_stopwords(words)
        words = delete_irrelevantwords(words)  # elimina palabras irrelevantes
        # words = stemmer_spanish(words)#elimina palabras irrelevantes
        return words

    def normalize_sentences(sentences):
        sentences = translate_english_sentences(sentences)
        #sentences = delete_sentence_one_word(sentences)
        sentencesNormalize = []
        for sentence in sentences:
            listWords = normalize_words(word_tokenize(sentence))
            print(listWords)
            listWords = delete_empty(listWords)
            print(listWords)
            words = " ".join(listWords)
            sentencesNormalize.append(words)
        return sentencesNormalize

    def normalize_total(lista):
        print("========================INICIA TRADUCCION==============================")
        print(datetime.datetime.now())
        print(len(lista))
        corpus = []
        count = 1
        for element in lista:
            print("Aviso " + str(count))
            print(datetime.datetime.now())
            listaDescripcion = element["listaDescripcion"]
            print(len(listaDescripcion))
            print(listaDescripcion)
            corpus.extend(normalize_sentences(listaDescripcion))
            count = count + 1
        return corpus


