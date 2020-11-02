
def sameFrequency(a1,a2):
    if(sorted(a1)==sorted(a2)) and (len(a1))==(len(a2)):
        print("matched")
    else:
        print("not matched")

sameFrequency('1233','3133')
sameFrequency('1233','2133')
