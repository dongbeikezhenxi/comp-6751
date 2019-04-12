# import nltk
# from nltk.corpus import movie_reviews as mr
# from nltk.chunk import ne_chunk as ck
# from nltk.tokenize import sent_tokenize
# from nltk.tokenize import word_tokenize
# from nltk.corpus import treebank
# from nltk import pos_tag, word_tokenize
# import os
# import nltk
# import re
# from nltk.parse import stanford
# os.environ['STANFORD_PARSER']= '/Users/yuhaomao/PycharmProjects/assignment1/parserTools/stanford-parser.jar'
# os.environ['STANFORD_MODELS']= '/Users/yuhaomao/PycharmProjects/assignment1/parserTools/stanford-parser-3.9.1-models.jar'
# java_path = "/Library/Java/JavaVirtualMachines/jdk-10.0.2.jdk/Contents/Home"
# os.environ['JAVAHOME'] = java_path
# parser= stanford.StanfordParser(model_path="/Users/yuhaomao/PycharmProjects/assignment1/parserTools/englishPCFG.ser.gz")
#
# print mr.fileids()
# f = file('out.log', 'w')
# for fileid in mr.fileids()[50:100]:
#         fileid_50 = mr.raw(fileid)
#         # print "5000000",fileid_50
#         file_tn = sent_tokenize(fileid_50)
#         print "8888888",file_tn
#         file_tn = ['Kaew Panjapetchkaew was a Muslim monk.']
#         # f.writelines(mr.raw(mr.fileids()[0]))
#         print "333",type(file_tn) #sent_tokennize for all the file in movie_review
#         #
#         for word_in in file_tn:
#                 word_50 = nltk.word_tokenize(word_in)
#                 print "11111",word_50 #word_tokenize from the movie_review
#                 ptag = nltk.pos_tag(word_50)
#                 print ptag[:100] #pos tagging of the words
#                 print "55555",parser.parse_one(word_50)
#                 # rd_parser = nltk.RecursiveDescentParser()
#                 # for tree in rd_parser.parse(ptag):
#                 #         print (tree)
#                         # tree.draw()
#                 entities = nltk.ne_chunk(ptag)
#                 print entities.draw()
#                 print entities #Name entity recognition
# # ###########################################################################   1111          AAAAAAAAAAAA
# # ###########################################################################   1111          AAAAAAAAAAAA
# # ###########################################################################   1111          AAAAAAAAAAAA
# #
# # for fileid in mr.fileids()[0:1]:
# #         fileid_50 = mr.raw(fileid)
# #         file_tn = sent_tokenize(fileid_50)
# #         print "sentence:",file_tn
# #         for word_in in file_tn:
# #             word_50 = nltk.word_tokenize(word_in)
# #             print "111111111111"
# #             print word_50
# #             print "22222222222"
# #             ptag1 = nltk.pos_tag(word_50)
# #             print ptag1
# #             parser.parse_one(word_50).draw()
# #             ners = nltk.ne_chunk(ptag1)
# #             print ners.draw()
# # ###########################################################################   1A 1B
# # import nltk
# # from nltk.corpus import movie_reviews as mr
# # from nltk.tokenize import sent_tokenize
# # from nltk import pos_tag
# # import os
# # import nltk
# # from nltk.parse import stanford
# # from nltk.chunk import ne_chunk as ck
# # import re
# #
# # os.environ[
# #     'STANFORD_PARSER'] = '/Users/yuhaomao/PycharmProjects/assignment1/parserTools/stanford-parser.jar'
# # os.environ[
# #     'STANFORD_MODELS'] = '/Users/yuhaomao/PycharmProjects/assignment1/parserTools/stanford-parser-3.9.1-models.jar'
# # java_path = "/Library/Java/JavaVirtualMachines/jdk-10.0.2.jdk/Contents/Home"
# # os.environ['JAVAHOME'] = java_path
# # parser = stanford.StanfordParser(
# #     model_path="/Users/yuhaomao/PycharmProjects/assignment1/parserTools/englishPCFG.ser.gz")
# #
# # for fileid in mr.fileids()[0:1]:
# #         fileid_50 = mr.raw(fileid)
# #         file_tn = sent_tokenize(fileid_50)
# #         for word_in in file_tn:
# #                 sentence = str(word_in)
# #                 mat_name = re.findall(
# #                     r"\b([A-Z]\w*\s[A-Z]\.?\w*\s[A-Z]\w*\b|M[r|s|rs].?\s[A-Z]\w*|[A-Z]\w*\s[A-Z]\w*\b)", sentence)
# #                 print "NAME:", mat_name
# #                 mat_org = re.findall(r"[A-Z]{2,}]", sentence)
# #                 print "ORG:", mat_org
# #                 mat_time = re.findall(
# #                     r"\d{4}[.-][0-1]\d[.-][0-3]\d|\b\d{1}:\d{2}\b|\b\d{2}:\d{2}\b|\d{2}[.-]\d{2}[.-]\d{4}|January \d{1,2}"
# #                     r"|March \d{1,2}|February \d{1,2}|April \d{1,2}|May \d{1,2}|June \d{1,2}|July \d{1,2}|August \d{1,2}"
# #                     r"|September \d{1,2}|October \d{1,2}|November \d{1,2}|December \d{1,2}"
# #                     r"|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday", sentence)
# #                 print "TIME:", mat_time
# #                 word_50 = nltk.word_tokenize(word_in)
# #                 print "111111111111"
# #                 print word_50
# #                 print "22222222222"
# #                 ptag1 = nltk.pos_tag(word_50)
# #                 print ptag1
# #                 parser.parse_one(word_50).draw()
# #                 ners = nltk.ne_chunk(ptag1)
# #                 print ners.draw()
# # ###########################################################################   1A 1B nokia version #######module a
# # ###########################################################################   1A 1B nokia version #######module a
# # ###########################################################################   1A 1B nokia version #######module a
# # ###########################################################################   1A 1B nokia version #######module a
# # ###########################################################################   1A 1B nokia version #######module a
# # ###########################################################################   1A 1B nokia version #######module a
# # ###########################################################################   1A 1B nokia version #######module a
# # ###########################################################################   1A 1B nokia version #######module a
# #
# # sentences = """people with bad audio quality have defective phones. i have read a lot of the reviews and my phone does not have a hiss or anything that people are talking about. it is crystal clear. this is one of the nicest phones nokia has made. i do recommend getting the data kit for those geeks. there are a lot of cool websites with games and midi ringtones to download for free.
# #
# # t-mobile ruins an otherwise good phone. nokia makes a great phone, that's clear. with all its complicated features, the menus are easily accessible and the quality of the features is great. the one huge disappointment is that the phones manufactured for t-mobile lack many of the menus and functions that a nokia straight from the manufacturer should have.
# # one of the things t-mobile brags about is the fact that it's a " worldphone " and can be used in europe, etc.
# # yet they've gotten rid of most of the languages that should be in the phone, including italian, german, and dutch. the internet functions of the phone - wap and gprs - will only work through t-mobile's services, because they have deleted the menu options that would enable you to configure the phone to be used on a different network. therefore, if you wanted to travel abroad and pop in a local sim card, even if you unlock the phone, there is no way you can use the local wap browser or internet.
# # after spending hours being transferred from one tech help person to another, i got fed up and have decided to return the phone.
# # bottom line, if you're attracted to this phone because of its tri-band feature so you can take it abroad, forget it. find another phone, or buy this one in its manufacturer-unlocked form."""
# #
# # sentence = nltk.sent_tokenize(sentences)
# # for sent in sentence:
# #     ############################# name
# #     mat_name = re.findall(r"\b([A-Z]\w*\s[A-Z]\.?\w*\s[A-Z]\w*\b|M[r|s|rs].?\s[A-Z]\w*|[A-Z]\w*\s[A-Z]\w*\b)",
# #                           sentences)
# #     print "NAME:", mat_name
# #
# #     ############################# organization
# #     mat_org = re.findall(r"[A-Z]{2,}]", sentences)
# #     print "ORG:", mat_org
# #
# #     ############################# time
# #     mat_time = re.findall(
# #         r"\d{4}[.-][0-1]\d[.-][0-3]\d|\b\d{1}:\d{2}\b|\b\d{2}:\d{2}\b|\d{2}[.-]\d{2}[.-]\d{4}|January \d{1,2}"
# #         r"|March \d{1,2}|February \d{1,2}|April \d{1,2}|May \d{1,2}|June \d{1,2}|July \d{1,2}|August \d{1,2}"
# #         r"|September \d{1,2}|October \d{1,2}|November \d{1,2}|December \d{1,2}"
# #         r"|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday", sentences)
# #     print "TIME:", mat_time
# # ###########################################################################   1A 1B nokia version #######module b
# # ###########################################################################   1A 1B nokia version #######module b
# # ###########################################################################   1A 1B nokia version #######module b
# # ###########################################################################   1A 1B nokia version #######module b
# # ###########################################################################   1A 1B nokia version #######module b
# # ###########################################################################   1A 1B nokia version #######module b
# # ###########################################################################   1A 1B nokia version #######module b
# # ###########################################################################   1A 1B nokia version #######module b
# # ###########################################################################   1A 1B nokia version #######module b
# # ###########################################################################   1A 1B nokia version #######module b
# # sentences = """people with bad audio quality have defective phones. i have read a lot of the reviews and my phone does not have a hiss or anything that people are talking about. it is crystal clear. this is one of the nicest phones nokia has made. i do recommend getting the data kit for those geeks. there are a lot of cool websites with games and midi ringtones to download for free.
# #
# # t-mobile ruins an otherwise good phone. nokia makes a great phone, that's clear. with all its complicated features, the menus are easily accessible and the quality of the features is great. the one huge disappointment is that the phones manufactured for t-mobile lack many of the menus and functions that a nokia straight from the manufacturer should have.
# # one of the things t-mobile brags about is the fact that it's a " worldphone " and can be used in europe, etc.
# # yet they've gotten rid of most of the languages that should be in the phone, including italian, german, and dutch. the internet functions of the phone - wap and gprs - will only work through t-mobile's services, because they have deleted the menu options that would enable you to configure the phone to be used on a different network. therefore, if you wanted to travel abroad and pop in a local sim card, even if you unlock the phone, there is no way you can use the local wap browser or internet.
# # after spending hours being transferred from one tech help person to another, i got fed up and have decided to return the phone.
# # bottom line, if you're attracted to this phone because of its tri-band feature so you can take it abroad, forget it. find another phone, or buy this one in its manufacturer-unlocked form."""
# #
# # sentence = nltk.sent_tokenize(sentences)
# # for sent in sentence:
# #     wordtokenize = nltk.word_tokenize(sent)
# #     ptag = nltk.pos_tag(wordtokenize)
# #
# #     ne_grammar = """TIME: {<NNP><CD>|<CD><NNP>}
# #                     PERSON: {<NNP>{2,3}}
# #                     ORGANIZATION: {<NNP>}
# #                  """
# #     cp = nltk.RegexpParser(ne_grammar)
# #     tree = cp.parse(ptag)
# #     ne_time = [word for word, pos in tree.pos() if pos == "TIME"]
# #     print "TIME:", ne_time
# #     ne_person = [word for word, pos in tree.pos() if pos == "PERSON"]
# #     print "PERSON:", ne_person
# #     ne_org = [word for word, pos in tree.pos() if pos == "ORGANIZATION"]
# #     print "ORGANIZATION:", ne_org
# # ###########################################################################   1A 1B nokia version #######module c
# # ###########################################################################   1A 1B nokia version #######module c
# # ###########################################################################   1A 1B nokia version #######module c
# # ###########################################################################   1A 1B nokia version #######module c
# # ###########################################################################   1A 1B nokia version #######module c
# # ###########################################################################   1A 1B nokia version #######module c
# # ###########################################################################   1A 1B nokia version #######module c
# # ###########################################################################   1A 1B nokia version #######module c
# # ###########################################################################   1A 1B nokia version #######module c
# # sentences = """people with bad audio quality have defective phones. i have read a lot of the reviews and my phone does not have a hiss or anything that people are talking about. it is crystal clear. this is one of the nicest phones nokia has made. i do recommend getting the data kit for those geeks. there are a lot of cool websites with games and midi ringtones to download for free.
# #
# # t-mobile ruins an otherwise good phone. nokia makes a great phone, that's clear. with all its complicated features, the menus are easily accessible and the quality of the features is great. the one huge disappointment is that the phones manufactured for t-mobile lack many of the menus and functions that a nokia straight from the manufacturer should have.
# # one of the things t-mobile brags about is the fact that it's a " worldphone " and can be used in europe, etc.
# # yet they've gotten rid of most of the languages that should be in the phone, including italian, german, and dutch. the internet functions of the phone - wap and gprs - will only work through t-mobile's services, because they have deleted the menu options that would enable you to configure the phone to be used on a different network. therefore, if you wanted to travel abroad and pop in a local sim card, even if you unlock the phone, there is no way you can use the local wap browser or internet.
# # after spending hours being transferred from one tech help person to another, i got fed up and have decided to return the phone.
# # bottom line, if you're attracted to this phone because of its tri-band feature so you can take it abroad, forget it. find another phone, or buy this one in its manufacturer-unlocked form."""
# #
# # def leaves(tree):
# #     """Finds NP (nounphrase) leaf nodes of a chunk tree."""
# #     ll=[]
# #     for subtree in tree.subtrees(filter = lambda t: t.label()=='NP'):
# #            ll.append(' '.join(subtree.leaves()))
# #     return ll
# #
# # file_tn = sent_tokenize(sentences)
# # print "sentence:",file_tn
# # for word_in in file_tn:
# #     word_50 = nltk.word_tokenize(word_in)
# #     print "111111111111"
# #     print word_50
# #     print "22222222222"
# #     ptag1 = nltk.pos_tag(word_50)
# #     parser.parse_one(word_50).draw()
# #     parserpar = parser.parse_one(word_50)
# #
# #     entitylist = leaves(parserpar)
# #     print "entitylist=",entitylist
# #     entitystring = str(entitylist)
# #
# #     mat_name = re.findall(r"\b([A-Z]\w*\s[A-Z]\.?\w*\s[A-Z]\w*\b|M[r|s|rs].?\s[A-Z]\w*|[A-Z]\w*\s[A-Z]\w*\b)",entitystring)
# #     print "PERSON:", mat_name
# #
# #     mat_org = re.findall(r"[A-Z]{2,}]",entitystring)
# #     print "ORG:",mat_org
# #
# #     mat_time= re.findall(r"\d{4}[.-][0-1]\d[.-][0-3]\d|\b\d{1}:\d{2}\b|\b\d{2}:\d{2}\b|\d{2}[.-]\d{2}[.-]\d{4}|January \d{1,2}"
# #                      r"|March \d{1,2}|February \d{1,2}|April \d{1,2}|May \d{1,2}|June \d{1,2}|July \d{1,2}|August \d{1,2}"
# #                      r"|September \d{1,2}|October \d{1,2}|November \d{1,2}|December \d{1,2}"
# #                      r"|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday",entitystring)
# #     print "TIME:",mat_time
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# # ###########################################################################   1111          111111111111
# # ###########################################################################   1111          11         11
# # ###########################################################################   1111          11          11
# # ###########################################################################   1111          11          11
# # ###########################################################################   1111          111111111111
# # ###########################################################################   1111          11          11
# # ###########################################################################   1111          11          11
# # ###########################################################################   1111          11          11
# # ###########################################################################   1111          111111111111
# # # import re
# # #
# # # for fileid in mr.fileids()[:1]:
# # #         fileid_50 = mr.raw(fileid)
# # #         file_tn = sent_tokenize(fileid_50)
# # #         for sentence in file_tn:
# # #                 sentences = sentence
# # #                 print sentences
# # #                 sentences = "Mr. Tom is asda sdasda Mrs Tom birthday Yuhao Mao is Ya Nan Zhu IBM 2014-09-30,Ya N. Zhu 5 January is NOKIA ,Zhu Yanan is January 23, March 23 February 5 he5:50is asd Saturday 2014-02-41  kjd 05-08-2017 kajdls 2014-03-08. mAo-yuh_ao92@gm_ail.net  5:49 "
# # #
# # #                 mat_name = re.findall(r"\b([A-Z]\w*\s[A-Z]\.?\w*\s[A-Z]\w*\b|M[r|s|rs].?\s[A-Z]\w*|[A-Z]\w*\s[A-Z]\w*\b)",sentences)
# # #                 print mat_name
# # #                 mat_org = re.findall(r"[A-Z]{2,}",sentences)
# # #                 print ">>>>>>>>>>>>org"
# # #                 print mat_org
# # #                 mat_time= re.findall(r"\d{4}[.-][0-1]\d[.-][0-3]\d|\b\d{1}:\d{2}\b|\b\d{2}:\d{2}\b|\d{2}[.-]\d{2}[.-]\d{4}|January \d{1,2}"
# # #                                  r"|March \d{1,2}|February \d{1,2}|April \d{1,2}|May \d{1,2}|June \d{1,2}|July \d{1,2}|August \d{1,2}"
# # #                                  r"|September \d{1,2}|October \d{1,2}|November \d{1,2}|December \d{1,2}"
# # #                                  r"|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday",sentences)
# # #                 print ">>>>>>>>>>>>>>>>>>>time"
# # #                 print mat_time
# # # sentences = "Mr. Tom is asda sdasda Mrs Tom birthday Yuhao Mao is Ya Nan Zhu IBM 2014-09-30,Ya N. Zhu 5 January is NOKIA ,Zhu Yanan is January 23, March 23 February 5 he5:50is asd Saturday 2014-02-41  kjd 05-08-2017 kajdls 2014-03-08. mAo-yuh_ao92@gm_ail.net  5:49 "
# # ###################################################################################### part A
# # import re
# # ############################# name
# # # mat_name = re.findall(r"\b([A-Z]\w*\s[A-Z]\.?\w*\s[A-Z]\w*\b|M[r|s|rs].?\s[A-Z]\w*|[A-Z]\w*\s[A-Z]\w*\b)",sentences)
# # # print ">>>>>>>>>>>>>>>>re"
# # # print mat_name
# # #
# # # #################################### orgination ####################
# # # mat_org = re.findall(r"[A-Z]{2,}",sentences)
# # # print ">>>>>>>>>>>>org"
# # # print mat_org
# # #
# # # ##########################   time
# # # mat_time= re.findall(r"\d{4}[.-][0-1]\d[.-][0-3]\d|\b\d{1}:\d{2}\b|\b\d{2}:\d{2}\b|\d{2}[.-]\d{2}[.-]\d{4}|January \d{1,2}"
# # #                  r"|March \d{1,2}|February \d{1,2}|April \d{1,2}|May \d{1,2}|June \d{1,2}|July \d{1,2}|August \d{1,2}"
# # #                  r"|September \d{1,2}|October \d{1,2}|November \d{1,2}|December \d{1,2}"
# # #                  r"|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday",sentences)
# # # print ">>>>>>>>>>>>>>>>>>>time"
# # # print mat_time
# #
# # ################################################################################### part B
# #

from nltk.corpus import stopwords
en_stopwords = stopwords.words('english')
print(sorted(en_stopwords))