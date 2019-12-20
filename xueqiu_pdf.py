import requests

def get_data(url):
    try:
        headers = {
            'cookie': 'device_id=b9d8c77adb9fe9ad5b91028c0e1fc10e; s=cx1146v37f; bid=a197bac568ee7dfe1fcb74c4bea7ade5_jxndp674; __utmz=1.1562166667.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); xq_token_expire=Sat%20Nov%2030%202019%2021%3A15%3A23%20GMT%2B0800%20(China%20Standard%20Time); xq_is_login=1; u=4069490025; __utma=1.1965739988.1562166667.1571416701.1572960143.9; aliyungf_tc=AQAAAKosMxwOrAIAbj8hc0qlVMzxSem/; xq_is_login.sig=J3LxgPVPUzbBg3Kee_PquUfih7Q; u.sig=xaa2S066wQUw-eI_B7dEAAoO8CQ; xqat=f4593705aca12dfbcadf88d54aea15a050b82e08; xqat.sig=8jPbaQG9rr7niyeqh1rREillzT4; xq_a_token=f4593705aca12dfbcadf88d54aea15a050b82e08; xq_a_token.sig=QjVhHz1nZq8GsSYF9lX_N_yMfdI; xq_r_token=dbd95ddf16ca9357012d887cb83c6ac1731c78f0; xq_r_token.sig=KazQwMBeNaheg0v1CHBbr9n9Evw; snbim_minify=true; Hm_lvt_1db88642e346389874251b5a1eded6e3=1574005939,1574006218,1574006492,1574006643; acw_tc=2760821c15747463383238530eb64473b96b0c05f0928a8d5f7670f50ea4eb; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1575021010',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        }
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        response = r.json()
        print(response)
        return dict(response)
    except:
        return 'error'

def get_content(url):

    comments = []
    content = get_data(url)
    data_list = content['list']

    for data in data_list:
        comment = {}
        print(data)
        try:
            comment['title'] = data['title']
            comment['link'] = 'https://xueqiu.com' + data['target']
            comment['description'] = data['description']
            comment['count'] = data['view_count']
            comment['mark'] = data['mark']
            comment['time'] = data['timeBefore']

            comments.append(comment)
        except:
            print('error')

    return comments

def Out2File(dict):
    '''
    将爬取到的文件写入到本地
    保存到当前目录的 TTBT.txt文件中。

    '''
    with open('dou_gua_xueqiu.txt', 'a+') as f:
        for comment in dict:
            f.write('标题： {} \t 链接：{} \t 描述：{} \t 发帖时间：{} \t 查看数量： {} \n'.format(comment['title'], comment['link'], comment['description'], comment['time'], comment['count']))

        print('当前页面爬取完成')


def main(base_url, deep):
    url_list = []
    for i in range(1, deep + 1):
        url_list.append(base_url + str(i))
    print(url_list)

    for url in url_list:
        content = get_content(url)
        print(content)
        Out2File(content)



base_url = 'https://xueqiu.com/statuses/original/timeline.json?user_id=6028781397&page='
deep = 55

def get_tianqi():
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'cookie': 'cityPy=beijing; cityPy_expire=1575895438; Hm_lvt_ab6a683aa97a52202eab5b3a9042a8d2=1575290640; UM_distinctid=16ec6a3987d4f6-0570511e529788-3964720e-384000-16ec6a3987e2ed; CNZZDATA1275796416=684916782-1575285602-%7C1575285602; CNZZDATA1277722738=1600153008-1575290479-null%7C1575290479; Hm_lpvt_ab6a683aa97a52202eab5b3a9042a8d2=1575290660; CNZZDATA1268732535=1876818844-1575286820-https%253A%252F%252Fwww.tianqi.com%252F%7C1575295622',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    }
    response = requests.get('http://www.tianqi.com/beijing/30/', headers=headers)
    response.raise_for_status()
    response.encoding = response.apparent_encoding

    print(response.text)

if __name__ == '__main__':
    # main(base_url, deep)
    get_tianqi()
