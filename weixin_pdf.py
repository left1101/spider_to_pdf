import requests
import pdfkit
import os
from PyPDF2 import PdfFileReader, PdfFileWriter

def get_data(url, data):
    try:
        headers = {
            'cookie': 'pgv_pvi=9353552896; RK=qa7YO9J9Yp; ptcz=80abfef4de76da1385a3d90662b89b5b3645d5ed3116c63dd17ace386a29c53a; pgv_pvid=5292434730; tvfe_boss_uuid=77711f62bc4474ff; o_cookie=1004212394; pac_uid=1_1004212394; wxuin=63863755212101; eas_sid=e1R5u645D0E7H2w9p9j9b5W7W7; _mta_closed_sysmsg=/--20180926/--20190816; aics=H81xkjyviwG9v7VAqh89NniMWcVRWSe1Cse6ElNl; ptui_loginuin=1666154330; rewardsn=; wxtokenkey=777; pgv_info=ssid=s8006791740; uin=o1004212394; skey=@rLcmrxyIM; ptisp=cnc; qqmusic_uin=; qqmusic_key=; qqmusic_fromtag=',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
            'referer': 'http://mp.weixin.qq.com/mp/homepage?__biz=MzI3NzMwNjU3MQ==&hid=2&sn=9364e4b30e1c9e45a0e87420aac17e6a&scene=18',
        }
        r = requests.post(url, headers=headers, data=data)
        r.raise_for_status()
        response = r.json()
        print(response)
        return dict(response)
    except:
        return 'error'

def get_content(url, _data):

    comments = []
    content = get_data(url, _data)
    data_list = content['appmsg_list']

    for data in data_list:
        comment = {}
        print(data)
        try:
            comment['title'] = data['title']
            comment['link'] = data['link']
            comment['cover'] = data['cover']
            comment['digest'] = data['digest']

            comments.append(comment)
        except:
            print('error')

    return comments


def save_pdf(html, filename):
    """
    把所有html文件保存到pdf文件
    :param html:  html内容
    :param file_name: pdf文件名
    :return:
    """
    options = {
        'page-size': 'Letter',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'custom-header': [
            ('Accept-Encoding', 'gzip')
        ],
        'cookie': [
            ('cookie-name1', 'cookie-value1'),
            ('cookie-name2', 'cookie-value2'),
        ],
        'outline-depth': 10,
    }
    pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')
    pdfkit.from_string(html, filename, options=options)

def merge_pdf(infnList, outfn):
    """
    合并pdf
    :param infnList: 要合并的PDF文件路径列表
    :param outfn: 保存的PDF文件名
    :return: None
    """
    pagenum = 0
    pdf_output = PdfFileWriter()

    for pdf in infnList:
        # 先合并一级目录的内容
        title = pdf['title']
        pdf_path = '{}_weixin.pdf'.format(title)

        pdf_input = PdfFileReader(open(pdf_path, 'rb'))
        # 获取 pdf 共用多少页
        page_count = pdf_input.getNumPages()
        for i in range(page_count):
            pdf_output.addPage(pdf_input.getPage(i))

        # 添加书签
        pdf_output.addBookmark(title, pagenum=pagenum)

        # 页数增加
        pagenum += page_count

        os.remove(pdf_path)

    # 合并
    pdf_output.write(open(outfn, 'wb'))
    # 删除所有章节文件
    # shutil.rmtree(os.path.join(os.path.dirname(__file__), 'gen'))

def get_html(url):
    try:
        headers = {
            'cookie': 'pgv_pvi=9353552896; RK=qa7YO9J9Yp; ptcz=80abfef4de76da1385a3d90662b89b5b3645d5ed3116c63dd17ace386a29c53a; pgv_pvid=5292434730; tvfe_boss_uuid=77711f62bc4474ff; o_cookie=1004212394; pac_uid=1_1004212394; ua_id=UcZLij3wJqMvQDRdAAAAAKqnNKYWE2sg9vvE6PIYdnE=; xid=3a99c47f7ff5d93c5e3c4cc765b2e035; mm_lang=zh_CN; wxuin=63863755212101; eas_sid=e1R5u645D0E7H2w9p9j9b5W7W7; _mta_closed_sysmsg=/--20180926/--20190816; aics=H81xkjyviwG9v7VAqh89NniMWcVRWSe1Cse6ElNl; ptui_loginuin=1666154330; rewardsn=; wxtokenkey=777; pgv_info=ssid=s8006791740; uin=o1004212394; skey=@rLcmrxyIM; ptisp=cnc; qqmusic_uin=; qqmusic_key=; qqmusic_fromtag=',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
            'referer': 'https://mp.weixin.qq.com/s?__biz=MzI3NzMwNjU3MQ==&mid=2247483883&idx=1&sn=84d9a790f8334f4b280c31e6381fc650&scene=19',
            'origin': 'https://mp.weixin.qq.com',
        }
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        content = r.text

        return content
    except:
        return 'error'

def main():
    url = 'http://mp.weixin.qq.com/mp/homepage'
    data = {
        '__biz': 'MzIwMTA4MDQzMA==',
        'hid': 2,
        'sn': '56b47e7dc7aa093198c37fb2a052a0a6',
        'scene': 18,
        'cid': 0,
        'begin': 0,
        'count': 50,
        'action': 'appmsg_list',
        'f': 'json',
        'r': 0.7331783003369596,
    }
    contents = get_content(url, data)

    print(contents)

    for content in contents:
        print('content')
        print(content)
        pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')
        pdfkit.from_url(content['link'], '{}_weixin.pdf'.format(content['title']))
        # pdfkit.from_string(html, filename, options=options)
        # html = get_html(content['link'])
        # save_pdf(html, '{}_weixin.pdf'.format(content['title']))

    merge_pdf(contents, '民工-投资-了解民工.pdf')


if __name__ == '__main__':
    main()
