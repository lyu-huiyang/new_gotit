# coding: utf-8
from requests import Session
from bs4 import BeautifulSoup


def check_login(number, passwd):
    login_url = 'http://222.206.65.12/reader/redr_verify.php'
    data = {
        'number': number,
        'passwd': passwd,
        'returnUrl': '',
        'select': 'cert_no'
    }
    url_session = Session()

    temp = url_session.post(login_url, data=data)
    book_list_url = url_session.get('http://222.206.65.12/reader/book_lst.php')
    # book_list_url.recoding = 'utf-8'
    return book_list_url


def library_login(number, passwd):
    book_list_url = check_login(number, passwd)
    # book_list_url.recoding = 'utf-8'
    soup = BeautifulSoup(book_list_url.text, 'html5lib')
    html_td = soup.find_all('td', bgcolor="#FFFFFF")
    j = 0
    books = []
    abook = {}
    print html_td[5].get_text().strip()

    for i in range(0, len(html_td) / 8):
        abook['number'] = html_td[j].get_text().strip()
        abook['name'] = html_td[j + 1].get_text().strip()
        abook['author'] = html_td[j + 2].get_text().strip()
        abook['borrowing_date'] = html_td[j + 3].get_text().strip()
        abook['return_date'] = html_td[j + 4].get_text().strip()
        abook['position'] = html_td[j + 5].get_text().strip()  # 存在乱码问题，未解决
        abook['other'] = html_td[j + 6].get_text().strip()  # 存在乱码问题，未解决
        abook['continue'] = u'续借'
        j += 8
        books.append(abook)
        abook = {}

    return books


if __name__ == '__main__':
    a = library_login('14110543055', '950526')
    # for b in a:
    # print(b)
