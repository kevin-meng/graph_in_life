import time
import requests
import xlsxwriter

"""
提取群聊成员头像及微信号
"""

f = open('../chatroom/information_volunteer/message2.js','r',encoding='utf8')
content = f.read()
content = content.replace('var data = ','')
msg_all_dic = eval(content)

def down_pic(k,url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
    pic = requests.get(url,headers).content
    with open('../data/pic/{}.jpg'.format(str(k)),'wb') as f:
        f.write(pic)
    print('下载成功{}的头像'.format(str(k)))
    # time.sleep(0.2)


def get_member_info_all():
    wb = xlsxwriter.Workbook('../data/信息化志愿者名单.xlsx')
    ws = wb.add_worksheet('namelist')
    headings = ['head','nick_name','wechat_id']
    ws.write_row('A1',headings)
    cell_format = wb.add_format({'bold': 0, 'align': 'center', 'font_name': u'微软雅黑', 'valign': 'vcenter'})

    member_info = msg_all_dic['member']

    i = 1

    for k,v in member_info.items():
        print(v)
        url = v['head'].replace('\x08\x00','').replace('\x08\x03','').replace('\x08\x01','').replace('\x08\x02','')
        name = v['name'].replace('\x1a\x00','')
        print(name)

        if len(url) < 10: continue

        down_pic(k,url)

        ws.set_row(i,40)
        ws.insert_image('A'+str(i+1),'../data/pic/{}.jpg'.format(str(k)),{'x_scale':0.4,'y_scale':0.4})  #
        time.sleep(0.2)
        ws.write(i,1,name,cell_format)
        ws.write(i,2,str(k),cell_format)
        i += 1

if __name__ == '__main__':
    get_member_info_all()