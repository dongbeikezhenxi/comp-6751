import re
# import nltk
# def open_ie():
#     PR = re.compile(r'.*\president\b')
#     for doc in nltk.corpus.ieer.parsed_docs():
#         for rel in nltk.sem.extract_rels('PER', 'ORG', doc, corpus='ieer', pattern=PR):
#             return nltk.sem.rtuple(rel)
#

########################### time RE#################|(January\s\d{1,2}|February\s\d{1,2}|March\s\d{1,2}|April\s\d{1,2})
from datetime import datetime
test_date = "Mr. Tom is asda SSSS sdasda Mrs Tom birthday Yuhao Mao is Ya Nan Zhu IBM 2014-09-30,Ya N. Zhu 5 January NOKIA ,Zhu Yanan is January 23, March 23 February 5 he5:50is asd Saturday 2014-02-41  kjd 05-08-2017 kajdls 2014-03-08. mAo-yuh_ao92@gm_ail.net  5:49 "
# mat = re.findall(r"(\d{4}-\d{1,2}-\d{1,2})",test_date)
###########################################      re_ time       ##################################finish
# mat = re.findall(r"\d{4}[.-][0-1]\d[.-][0-3]\d|\b\d{1}:\d{2}\b|\b\d{2}:\d{2}\b|\d{2}[.-]\d{2}[.-]\d{4}|January \d{1,2}"
#                  r"|March \d{1,2}|February \d{1,2}|April \d{1,2}|May \d{1,2}|June \d{1,2}|July \d{1,2}|August \d{1,2}"
#                  r"|September \d{1,2}|October \d{1,2}|November \d{1,2}|December \d{1,2}"
#                  r"|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday",test_date)
# mat  = re.findall(r"(M(r|s|rs)\.?\s[A-Z]\w*|[A-Z]\w*\s[A-Z]\w*|[A-Z]\w*\s[A-Z]\.?\w*\s[A-Z]\w*)",test_date)##############name


#############################################       name ############################################
# mat2 = re.findall(r"\b[A-Z]\w*\s[A-Z]\.?\w*\s[A-Z]\w*\b",test_date) ################Ya Nan Zhu and Ya N. Zhu
# mat3 = re.finditer(r"\b(M(r|s|rs)\.?\s[A-Z]\w*\b)",test_date)
# mat3 = re.findall(r"(M[r|s|rs].?\s[A-Z]\w*)",test_date) #################### Mr. Tom and Mrs Tom
# mat4 = re.findall(r"\b[A-Z]\w*\s[A-Z]\w*\b",test_date)#############Yuhao Mao (but recignized Ya Nan and Ya N)#######
# mat5 = re.findall(r"([A-Z]\w*\s+[A-Z]\w*\s+[A-Z]\w*\s)", test_date)############Yu Hao Mao##########
# mat6 = re.findall(r"(([A-Z][a-z]*\s){2,3})",test_date)###############repeat Yuhao############
# mat = mat2 + mat3 + mat4
# mat = re.findall(r'([a-zA-Z0-9._-]+[@][a-zA-Z0-9._-]*\.[a-zA-Z0-9]*)',test_date)##############email####finish
# mat = re.findall(r"(\d{4}-\d{1,2}-\d{1,2})",test_date)
# print mat
######################### final name############
mat_name = re.findall(r"\b([A-Z]\w*\s[A-Z]\.?\w*\s[A-Z]\w*\b|M[r|s|rs].?\s[A-Z]\w*|[A-Z]\w*\s[A-Z]\w*\b)",test_date)
# print mat2
# print mat3
# for i in mat3:
#     list = i.group().split()
#     print list
# print mat4
# for i in mat6:
#     print i[0]
# print mat6

print mat_name


##################################### orgination ####################
mat_org = re.findall(r"[A-Z]{2,}",test_date)
print mat_org

