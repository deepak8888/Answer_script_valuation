import os
from lseg import lineseg
from semantic3 import semantic_main,wos
def wordrecogn():
    pathofak=input("enter path of answer key?\n")
    pathofas=input("enter path of answer sheet?\n")
    if not os.path.exists(pathofak) or not os.path.exists(pathofas):
        print("Invalid Directory")
        wordrecogn()
    reckey=lineseg(pathofak)
    recanspaper=lineseg(pathofas)
    print("\nRecognised key:\n",reckey)
    print("\nRecognised Answer Sheet:\n",recanspaper)
    s = input("Do you want to evaluate semantic and word order similiarity?(Y/N)")
    while(1):
        if s=="Y" or s=="N":
            break
        else:
            print("\nInvalid Input\n")
            s = input("Do you want to evaluate semantic and word order similiarity?(Y/N)")

    if(s=="Y"):
        print("Semantic similiarity is:",semantic_main(reckey,recanspaper))
        print("Word order similiarity is:",wos(reckey,recanspaper))



wordrecogn()












