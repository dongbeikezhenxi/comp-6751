import nltk
from nltk.corpus import rte as rte_corpus
import math
from nltk.tokenize import RegexpTokenizer
import test as treedis
#######################################################
rte_10 = nltk.corpus.reader.rte.RTECorpusReader("/Users/yuhaomao/Downloads/rte/rte10.xml", "rte_10.xml")
rte_30 = nltk.corpus.reader.rte.RTECorpusReader("/Users/yuhaomao/Downloads/rte/rte10.xml", "rte_30.xml")
test_pair_rte10 = rte_corpus.pairs(['/Users/yuhaomao/Downloads/rte/rte10.xml'])
test_pair_rte30 = rte_corpus.pairs(['/Users/yuhaomao/Downloads/rte/rte30.xml'])

#######################################################

test_pair = rte_corpus.pairs(['rte1_test.xml'])
rte_pair = rte_corpus.pairs(['rte1_dev.xml','rte2_dev.xml','rte3_dev.xml'])
for pair in rte_pair:
    # print "2222222222",pair.text
    text_tokenize = []
    hyp_token = []
    extractor=nltk.RTEFeatureExtractor(pair)
    text_tokenize.append(list(extractor.text_words))
    hyp_token.append(extractor.hyp_words)
# print "1111111",type(text_tokenize)
# print text_tokenize
# print "2222222",type(hyp_token)
# print hyp_token
# print "......................",rte_corpus.pairs(['rte1_dev.xml'])[8].text
# print "......................",rte_corpus.pairs(['rte1_dev.xml'])[8].hyp
tokenizer = RegexpTokenizer('[\w.@:/]+|\w+|\$[\d.]+')

#######################################################
def cos_sim(post):
    final_text_tokenize = tokenizer.tokenize(post.text)
    final_hyp_takenize = tokenizer.tokenize(post.hyp)

    word_set = set(final_text_tokenize).union(set(final_hyp_takenize))
    # print type(word_set)
    word_dict = dict()
    i = 0
    for word in word_set:
        word_dict[word] = i
        i += 1
    s1_cut_code = [word_dict[word] for word in final_text_tokenize]
    # print s1_cut_code
    s1_cut_code = [0]*len(word_dict)

    for word in final_text_tokenize:
        s1_cut_code[word_dict[word]]+=1
    # print s1_cut_code

    s2_cut_code = [word_dict[word] for word in final_hyp_takenize]
    # print s2_cut_code
    s2_cut_code = [0]*len(word_dict)
    for word in final_hyp_takenize:
        s2_cut_code[word_dict[word]]+=1
    # print s2_cut_code
    sum = 0
    sq1 = 0
    sq2 = 0
    for i in range(len(s1_cut_code)):
        sum += s1_cut_code[i] * s2_cut_code[i]
        sq1 += pow(s1_cut_code[i], 2)
        sq2 += pow(s2_cut_code[i], 2)

    result = float(sum / (math.sqrt(sq1) * math.sqrt(sq2)))
    return result




#######################################################
def negtivewords(words):
    list = []
    for word in words:
        if word in set(['no', 'not', 'never', 'failed', 'rejected','denied','discount','hardly','barely','seldom','rarely','fail','nor','stop','decline','ignore','off','dislike','reject']):
            list.append(word)
        else:
            pass
    return list


def rte_features(rtepair):
    extractor = nltk.RTEFeatureExtractor(rtepair)
    features = {}
    features['word_overlap'] = len(extractor.overlap('word'))
    features['word_hyp_extra'] = len(extractor.hyp_extra('word'))
    # print "1111111",extractor.hyp_extra('word')
    features['ne_overlap'] = len(extractor.overlap('ne'))
    # print "ne repeat\t\t\t",extractor.overlap('ne')
    features['ne_hyp_extra'] = len(extractor.hyp_extra('ne'))
    # print "ne extraeeeeeeeee\t",extractor.hyp_extra('ne')
    features['dif_length']= len(extractor.text_tokens)-len(extractor.hyp_tokens)
    features['result'] = cos_sim(rtepair)
    features['neg_'] = len(negtivewords(list(extractor.text_words))) - len(negtivewords(list(extractor.hyp_words)))
    # features['td'] = treedis.cal(treedis.buildtree(rtepair.text), treedis.buildtree(rtepair.hyp))
    return features

def accuracy_(classifier, gold):
    TP = 0.0
    FN = 0.0
    TN = 0.0
    FP = 0.0
    result = []
    gold_list = []
    result_list = []
    results = classifier.classify_many([fs for (fs, l) in gold])
    correct = [l == r for ((fs, l), r) in zip(gold, results)]
    # print "gold",gold
    # print "result",results
    for gold_result in gold:
        gold_list.append(int(gold_result[-1]))
    result_list = results
    for i in range(len(gold_list)):
        if gold_list[i] ==1 and result_list[i] == 1:
            TP += 1
        elif gold_list[i] == 1 and result_list[i] == 0:
            FN += 1
        elif gold_list[i] == 0 and result_list[i] == 0:
            FP += 1
        else:
            TN += 1

    precision = TP / (TP + FP)
    recall = TP / (TP + FN)
    f_measure = 2 * precision * recall / (precision + recall)
    result.append(precision)
    result.append(recall)
    result.append(f_measure)
    if correct:
        result.append(float(sum(correct)) / float(len(correct)))
        return result
    else:
        return 0


# def accuracy_(classifier, gold):
#     results = classifier.classify_many([fs for (fs, l) in gold])
#     correct = [l == r for ((fs, l), r) in zip(gold, results)]
#     if correct:
#         return sum(correct) / len(correct)
#     else:
#         return 0

train_set = [(rte_features(post), post.value) for post in rte_pair]
test_set  = [(rte_features(post), post.value) for post in test_pair]


classifier = nltk.NaiveBayesClassifier.train(train_set)


print "############test_set############"
print "Accuracy:\t", accuracy_(classifier, test_set)[3]
print "Recall:\t\t", accuracy_(classifier, test_set)[1]
print "Percision:\t",accuracy_(classifier, test_set)[0]
print "f_measure:\t",accuracy_(classifier, test_set)[2]
print
rte_10_testset = [(rte_features(post), post.value) for post in test_pair_rte10]
rte_30_testset = [(rte_features(post), post.value) for post in test_pair_rte30]
print "############rte_10############"
print "Accuracy:\t", accuracy_(classifier, rte_10_testset)[3]
print "Recall:\t\t", accuracy_(classifier, rte_10_testset)[1]
print "Percision:\t",accuracy_(classifier, rte_10_testset)[0]
print "f_measure:\t",accuracy_(classifier, rte_10_testset)[2]
print
print "############rte_30############"
print "Accuracy:\t", accuracy_(classifier, rte_30_testset)[3]
print "Recall:\t\t", accuracy_(classifier, rte_30_testset)[1]
print "Percision:\t",accuracy_(classifier, rte_30_testset)[0]
print "f_measure:\t",accuracy_(classifier, rte_30_testset)[2]
print "########################################################"


#####################################
for i in range (18):
    # test = rte_corpus.pairs(['rte2_test.xml'])[i]
    test = rte_corpus.pairs('/Users/yuhaomao/Downloads/rte/rte30.xml')[i]
    extractor = nltk.RTEFeatureExtractor(test)
    if test.value == classifier.classify(rte_features(test)):
        print 'Example:', i+1, ' Correct! Both are ', test.value
        print test.text
        print test.hyp
        print "overlap_word:", extractor.overlap('word')
        print "overlap_ne:", extractor.overlap('ne')
        print "hyp_extra_word:", extractor.hyp_extra('word')
        print "hypro_extra_ne:", extractor.hyp_extra('ne')
        print "cos_sim:", cos_sim(test)
        print "dif_length:", len(extractor.text_tokens) - len(extractor.hyp_tokens)
        print "neg_",len(negtivewords(list(extractor.text_words))) - len(negtivewords(list(extractor.hyp_words))),'\n'

    else:
        print 'Example:', i+1, ' Wrong! True value is ', test.value, 'Classify as ', classifier.classify(rte_features(test))
        print test.text
        print test.hyp
        print "overlap_word:",extractor.overlap('word')
        print "overlap_ne:",extractor.overlap('ne')
        print "hyp_extra_word:",extractor.hyp_extra('word')
        print "hypro_extra_ne:",extractor.hyp_extra('ne')
        print "cos_sim:", cos_sim(test)
        print "dif_length:", len(extractor.text_tokens) - len(extractor.hyp_tokens)
        print "neg_",len(negtivewords(list(extractor.text_words))) - len(negtivewords(list(extractor.hyp_words))),'\n'

print nltk.classify.accuracy(classifier, test_set)
#####################################