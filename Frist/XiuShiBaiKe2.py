# coding=utf-8
import requests
from bs4 import BeautifulSoup



def down_page(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}
    html = requests.get(url, headers=header)
    return html.text


def get_content(html, page):
    output = """第{}页 作者：{} 性别：{} 年龄：{} 点赞：{} 评论：{}\n{}\n------------\n"""  # 最终输出格式
    soup = BeautifulSoup(html, 'html.parser')
    con = soup.find_all('div', class_='article')
    for item in con:
        author = item.find('h2').string  # 作者
        content = item.find('div', class_='content').find('span').get_text()  # 内容

        vote = item.find('span', class_='stats-vote').find('i', class_='number').string  # 点赞
        comments = item.find('span', class_='stats-comments').find('i', class_='number').string  # 评论
        author_info = item.find('div', class_='articleGender')  # 作者信息
        if author_info is not None:  # 非匿名用户
            class_list = author_info['class']
            if 'manIcon' in class_list:
                gender = '女'
            elif 'womenIcon' in class_list:
                gender = '男'
            else:
                gender = ''
            age = author_info.string
        else:  # 匿名用户
            gender = ''
            age = ''
        save_txt(output.format(page, author, gender, age, vote, comments, content))


def save_txt(*args):
    for i in args:
        with open('qiubai.txt', 'a', encoding='utf-8') as f:
            f.write(i)


def main():
    for i in range(1, 14):
        url = 'https://qiushibaike.com/text/page/{}'.format(i)
        print(url)
        html = down_page(url)
        get_content(html, i)


if __name__ == '__main__':
    main()
