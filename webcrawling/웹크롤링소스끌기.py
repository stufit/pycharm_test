import urllib.request as req

imgUrl = "https://cafeptthumb-phinf.pstatic.net/MjAyMDEwMzFfNTcg/MDAxNjA0MTQ2Mzg2NDM0.-4DLkT_jvdE20K-G2d6gWiUVDY2poOzm5NCvGUXiSocg.STeRWgTKj7fTu4Wi8sQFA9Y9YevMyIOXS3uh5g7kpcAg.JPEG/20201031%EF%BC%BF211200.jpg?type=w1600"
htmlUrl = 'https://www.naver.com'

savePath1 = 'iphone12.jpg'
savepath2 = 'main.html'

file1, header1 = req.urlretrieve(imgUrl,savePath1)
file2, header2 = req.urlretrieve(htmlUrl,savepath2)

#예외처리
# try:
#     file1, header1 = req.urlretrieve(imgUrl,savePath1)
#     file2, header2 = req.urlretrieve(htmlUrl,savepath2)
# except Exception as e:
#     print('Download success')
#     print(e)
# else:
#     #Header정보 출력
#     print(header1)
#     print('-------------------------')
#     print(header2)
#     #다운로드된 파일 정보
#     print('FileName1 {}'.format(file1))
#     print('FileName2 {}'.format(file2))
#     print()


print('Dwonload sucess')

