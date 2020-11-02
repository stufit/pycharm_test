

def file_read():
    myfile = open('yesterday.txt','r')
    yesterday_lyric = ""
    while 1:
        line=myfile.readline()
        #print(line)
        if not line:
            break
        yesterday_lyric = yesterday_lyric+line.strip()+"\n"

    myfile.close()
    return yesterday_lyric

result = file_read()
print(result)



small_yesterday_cnt = result.count('yesterday')
title_yesterday_cnt = result.count('Yesterday')
#print("Number of a word yesterday : ",small_yesterday_cnt)
#print("Number of a word Yesterday : ",title_yesterday_cnt)

#with open('yesterday.txt','r') as file:
 #   lyric = file.read()

#print(lyric)