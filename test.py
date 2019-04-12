import os
import nltk
from nltk.parse import stanford
from nltk.parse.stanford import StanfordDependencyParser

def tstfmt(tree):
    tree=str(tree).replace("\n","")
    # print tree
    tree=" ".join(tree.split()).replace(" (","{").replace(")","}").replace(" ","{").split("{")
    # print tree
    # print "111",type(tree)
    for i in range(0,len(tree),1):
        if tree[i].find("}")>=0:
            tree[i]=tree[i]+"}"
    # print type(tree)
    # print "tree11111",tree
    tree="{".join(tree).replace("(ROOT","{ROOT")
    return tree

def cal(tree1,tree2):
    # if tree1==None or tree2==None:
    #     return 0
    tree1=tstfmt(tree1)
    tree2=tstfmt(tree2)
    if len(tree1)>len(tree2):
        cmd=os.popen("python -m apted -t "+tree2+" "+tree1+" -mv")
    else:
        cmd=os.popen("python -m apted -t "+tree1+" "+tree2+" -mv")
    try:
        ret=cmd.readlines()[0].replace(" ","")
    except:
        return 0
    ret = ret[ret.rfind(":") + 1:-1]
    print "11"
    return int(ret)

os.environ['STANFORD_PARSER'] = '/Users/yuhaomao/PycharmProjects/assignment1/parserTools/stanford-parser.jar'
os.environ['STANFORD_MODELS'] = '/Users/yuhaomao/PycharmProjects/assignment1/parserTools/stanford-parser-3.9.1-models.jar'

java_path = "/Library/Java/JavaVirtualMachines/jdk-10.0.2.jdk/Contents/Home"
os.environ['JAVAHOME'] = java_path

parser = stanford.StanfordParser(model_path="/Users/yuhaomao/PycharmProjects/assignment1/parserTools/englishPCFG.ser.gz")
dparser = StanfordDependencyParser(model_path="/Users/yuhaomao/PycharmProjects/assignment1/parserTools/englishPCFG.ser.gz")
sentence1 = "Oracle had fought to keep the forms from being released"
sentence2 = "Oracle released a confidential document"
def buildtree(sentence1):
    sent1 = nltk.sent_tokenize(sentence1)
    word1 = nltk.word_tokenize(sent1[0])
    try:
        return parser.parse_one(word1)
    except:
        return None

# sent1 = "Around ten suspected Muslim militants took part in the fifteen minute long attack in the early hours of Sunday morning, leaving the 76-year-old monk, Kaew Panjapetchkaew, with his throat cut."
# sent2 = "Kaew Panjapetchkaew was a Muslim monk."
# features = cal(buildtree(sent1), buildtree(sent2))
# print features

# tree1 =
# tree2 =
# print cal(tree1,tree2)

# import math
#
# final_text_tokenize = ["word1","word2","word3","word1"]
# final_hyp_takenize = ["word2","word4","word5"]
#
# word_set = set(final_text_tokenize).union(set(final_hyp_takenize))
# word_dict = dict()
# i = 0
# for word in word_set:
#     word_dict[word] = i
#     i += 1
#
# s1_cut_code = [word_dict[word] for word in final_text_tokenize]
# s1_cut_code = [0]*len(word_dict)
# for word in final_text_tokenize:
#     s1_cut_code[word_dict[word]]+=1
#
# s2_cut_code = [word_dict[word] for word in final_hyp_takenize]
# s2_cut_code = [0]*len(word_dict)
# for word in final_hyp_takenize:
#     s2_cut_code[word_dict[word]]+=1
#
# # calculate cos xiangsudu
# sum = 0
# sq1 = 0
# sq2 = 0
# for i in range(len(s1_cut_code)):
#     sum += s1_cut_code[i] * s2_cut_code[i]
#     sq1 += pow(s1_cut_code[i], 2)
#     sq2 += pow(s2_cut_code[i], 2)
#
#
# try:
#     result = round(float(sum) / (math.sqrt(sq1) * math.sqrt(sq2)), 2)
# except ZeroDivisionError:
#     result = 0.0
# print result