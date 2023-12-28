import spacy
import nltk.corpus
from bs4 import BeautifulSoup
import os
import re
from nltk.tokenize import word_tokenize
import nltk
from nltk import word_tokenize, pos_tag


def determine_tense_input(sentence):
    text = word_tokenize(sentence)
    tagged = pos_tag(text)

    tense = {}
    tense["future"] = len([word for word in tagged if word[1] == "MD"])
    tense["present"] = len(
        [word for word in tagged if word[1] in ["VBP", "VBZ", "VBG"]])
    tense["past"] = len([word for word in tagged if word[1] in ["VBD", "VBN"]])
    return(tense)


nlp = spacy.load("en_core_web_sm")


def split_into_sentences(text):
    doc = nlp(text)
    sentences = [sent for sent in doc.sents]
    return sentences


class IsQuestion():

    def __init__(self):
        posts = self.__get_posts()
        feature_set = self.__get_feature_set(posts)
        self.classifier = self.__perform_classification(feature_set)

    def __get_posts(self):
        return nltk.corpus.nps_chat.xml_posts()

    def __get_feature_set(self, posts):
        feature_list = []
        for post in posts:
            post_text = post.text
            features = {}
            words = nltk.word_tokenize(post_text)
            for word in words:
                features['contains({})'.format(word.lower())] = True
            feature_list.append((features, post.get('class')))
        return feature_list

    def __perform_classification(self, feature_set):
        training_size = int(len(feature_set) * 0.1)
        train_set, test_set = feature_set[training_size:], feature_set[:training_size]
        classifier = nltk.NaiveBayesClassifier.train(train_set)
        # print('Accuracy is : ', nltk.classify.accuracy(classifier, test_set))
        return classifier

    def __get_question_words_set(self):
        question_word_list = ['what', 'where', 'when', 'how', 'why', 'did', 'do', 'does', 'have', 'has', 'am', 'is', 'are', 'can', 'could', 'may', 'would', 'will', 'should'
                              "didn't", "doesn't", "haven't", "isn't", "aren't", "can't", "couldn't", "wouldn't", "won't", "shouldn't", '?']
        return set(question_word_list)

    def predict_question(self, text):
        words = nltk.word_tokenize(text.lower())
        if self.__get_question_words_set().intersection(words) == False:
            return 0
        if '?' in text:
            return 1

        features = {}
        for word in words:
            features['contains({})'.format(word.lower())] = True

        prediction_result = self.classifier.classify(features)
        if prediction_result == 'whQuestion' or prediction_result == 'ynQuestion':
            return 1
        return 0


def detect_issues(paragraphs, issue_patterns):
    issue = []
    for j in paragraphs:
        lines = split_into_sentences(j)
        for line in lines:
            if line.text not in issue:
                for i in issue_patterns:
                    pattern = re.compile(i)
                    if pattern.search(line.text.lower()):
                        print("here")
                        issue.append(line.text)
            if line.text not in issue and isQ.predict_question(line.text):
                issue.append(line.text)
    return issue


isQ = IsQuestion()
mypath = os.path.join("SampleCases", "Civil Appeal")
onlyfiles = [f for f in os.listdir(
    mypath) if os.path.isfile(os.path.join(mypath, f))]

for file in onlyfiles:
    path_case = os.path.join(
        'SampleCases', 'Civil Appeal', file)
    soup = BeautifulSoup(open(path_case), 'xml')

    judgement = soup.find("JudgmentText")

    paragraphs = []

    for i in judgement:
        if i not in judgement.find_all("I"):
            if i.text != '':
                paragraphs.append(i.text)

    with open('arg_pet.txt', 'r') as f:
        arg_pet = f.readlines()

    f.close()

    # arg_pet = [i.strip('\n') for i in arg_pet]
    # arg_pet = [re.compile(i) for i in arg_pet]

    # with open('arg_res.txt', 'r') as f:
    #     arg_res = f.readlines()

    # f.close()
    # arg_res = [re.compile(a.strip('\n')) for a in arg_res]

    with open('issues.txt', 'r') as f:
        issues = f.readlines()

    f.close()
    issues = [a.strip('\n') for a in issues]

    # petitioner = []
    # respondent = []
    # for j in paragraphs:
    #     checkIdx = -1
    #     spanIdxPet = 0
    #     spanIdxRes = 0
    #     for i in arg_pet:
    #         if i.search(j):
    #             checkIdx = 0
    #             spanIdxPet = i.search(j).span()[1]-i.search(j).span()[0]
    #             break
    #     for i in arg_res:
    #         if i.search(j):
    #             if checkIdx == -1:
    #                 checkIdx = 1
    #             else:
    #                 checkIdx = 2
    #                 spanIdxRes = i.search(j).span()[1]-i.search(j).span()[0]
    #             break
    #     if checkIdx == 0 and j not in petitioner:
    #         petitioner.append(j)
    #     elif checkIdx == 1 and j not in respondent:
    #         respondent.append(j)
    #     elif checkIdx == 2:
    #         if spanIdxPet < spanIdxRes and j not in petitioner:
    #             petitioner.append(j)
    #         elif j not in respondent:
    #             respondent.append(j)

    issue = detect_issues(paragraphs, issues)

    f = open(f'Output/output_{file}.txt', 'w')
    # f.write('Arugument by Petitioner:\n')
    # for i in petitioner:
    #     f.write(i+'\n')
    # f.write('\n')
    # f.write('Argument by Respondent:\n')
    # for i in respondent:
    #     f.write(i+'\n')
    # f.write('\n')
    f.write('Issues:\n')
    for i in issue:
        f.write(i+'\n')
    f.close()
