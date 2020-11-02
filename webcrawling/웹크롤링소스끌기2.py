import urllib.request as req
from urllib.error import URLError,HTTPError

lstX =['oman.jpg','index.html']
targetUrl = [''
            ,'https://www.google.com']

for i, url in enumerate(targetUrl):
    try:
        #웹 수신 정보 읽
        response = req.urlopen(url)
        #수신 내용
        contents = response.read()
        print('-------------------------')

        #상태 정보 중간 출력
        print('Header info-{} : {}'.format(i,response.info()))
        print('HTTP Status Code : {}'.format(response.getcode()))
        print()
        print('----------------------------')

        #파일 쓰기
        with open(lstX[i],'wb') as f:
            f.write(contents)
    #에러 발생시
    except HTTPError as e:
        print('Download failed')
        print('HTTPError Code : ',e.code)

    # 에러 발생시
    except URLError as e:
        print('Download failed')
        print('URLError Reson : ', e.reason)

    else:
        print()
        print('Download success')



