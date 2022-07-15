import glob



POS_FILE_PATTERN = "M03\\data\\aclimdb\\train\\pos\\*.txt"
NEG_FILE_PATTERN = "M03\\data\\aclimdb\\train\\neg\\*.txt"
SPECIAL_CHARACTERS = ".,!?"
pos_files = glob.glob(POS_FILE_PATTERN)
neg_files = glob.glob(NEG_FILE_PATTERN)
pos_words = []
neg_words = []
for file in pos_files:
    with open(file,encoding="utf8") as pos_stream:
        content = pos_stream.read()
        words = content.lower().replace("<br />", " ").split()
        pos_words.append(words)
for file in neg_files:
    with open(file,encoding="utf8") as neg_stream:
        content = neg_stream.read()
        words = content.lower().replace("<br />", " ").split()
        neg_words.append(words)
sentence = input("Podaj komentarz: ")
words_in_sentence = sentence.lower().replace("<br />", " ").replace(".", "").split()
word_sentiment = 0
list_of_sentiments = []
sentiment = 0
for word in words_in_sentence:
    count_of_pos_words = 0
    count_of_neg_words = 0
    for review in pos_words:
        if word in review:
            count_of_pos_words += 1
    for review in neg_words:
        if word in review:
            count_of_neg_words += 1
    sum_of_pos_and_neg = count_of_pos_words + count_of_neg_words
    if sum_of_pos_and_neg > 0:
        word_sentiment = (count_of_pos_words - count_of_neg_words)/sum_of_pos_and_neg
        print(word, word_sentiment)
        list_of_sentiments.append(word_sentiment)
        

    else:
        print(0.0)
sentiment = sum(list_of_sentiments)/len(sentence)
if sentiment > 0:
    print("Sentyment jest pozytywny i wynosi tyle: ", sentiment)
else:
    print("Sentyment jest negatywny i wynosi tyle: ", sentiment)
