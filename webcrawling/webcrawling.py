import bs4
import urllib.request

myHtml = """
    <html>
        <table border=1>
            <tr>
                <td>항목</td>
                <td>2013</td>
                <td>2014</td>
                <td>2015</td>
            </tr>
            <tr>
                <td>매출액</td>
                <td>100</td>
                <td>200</td>
                <td>300</td>
            </tr>
        </table>
    </html>
"""

bsObj = bs4.BeautifulSoup(myHtml,'html.parser')
print(bsObj)
print(type(bsObj))
print(bsObj.find('td'))

num = len(bsObj.find_all('td'))
for i in range(0, num):

    print(bsObj.find_all("td")[i].get_text())
url = 'https://www.koita.or.kr/main/main.aspx'
koita = urllib.request.urlopen(url)

bsObj = bs4.BeautifulSoup(koita, 'html.parser')
print(koita.read())








