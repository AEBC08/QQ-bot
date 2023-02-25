# -*- coding:utf-8 -*-
import json
import openai
import os
import random
import re
import requests
import bot
import requests
from flask import Flask, request
import time

qq_code = "114514"  # 机器人QQ号
app = Flask(__name__)

openai.api_key = "sk-xxxxxxxxxxxxxxxxxxxxxxxxx"  # 去OpenAI官网获取api，没有无法使用ChatGPT
gptcf = f"[CQ:at,qq={qq_code}]"  # 触发ChatGPT的方式1，这里默认at触发
gptcf2 = "cxk"  # 触发ChatGPT的方式2，这里默认关键字触发，怎么喜欢怎么来
dcf = 0  # 使用2个触发，1为是，0为否，不使用2个触发只能使用触发方式1
sqxt = 1  # 使用授权系统，1为是，0为否，不使用任何功能将不受限制，推荐开启
zrqq = 1145141919810  # 主人QQ号，使用授权有主人专权
sykunphoto = 1  # 使用坤图，1为是，0为否，娱乐性功能
qdbgm = 0  # 运行时播放bgm，1为是，0为否，娱乐性功能


def gpt_reply(msg):
    if "Error" in msg:
        return msg
    msg = msg.replace(f"{gptcf} ", "")
    msg = msg.replace(f"{gptcf2} ", "")
    completion = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"{msg}",
        max_tokens=2048,
        temperature=0.9,
        top_p=1,
        presence_penalty=0,
        frequency_penalty=0
    )

    if completion.choices[0].text[0:1] == '\n':
        return completion.choices[0].text.strip()
    else:
        return completion.choices[0].text


def send_msg(msg, uid, gid, mid=None):
    if mid is None:
        if uid is None:
            url = "http://127.0.0.1:5700/send_group_msg"
            data = {"group_id": gid, "message": f"{msg}"}
        elif gid is None:
            url = "http://127.0.0.1:5700/send_private_msg"
            data = {"user_id": uid, "message": f"{msg}"}
        else:
            url = "http://127.0.0.1:5700/send_group_msg"
            data = {"group_id": gid, "message": f"[CQ:at,qq={uid}]{msg}"}
        try:
            requests.post(url, data=data, timeout=5)
        except:
            pass
    else:
        url = "http://127.0.0.1:5700/send_group_msg"
        data = {"group_id": gid, "message": f"[CQ:reply,id={mid}]{msg}"}
        try:
            requests.post(url, data=data, timeout=5)
        except:
            pass


@app.route('/', methods=["POST"])
def post_data():
    data = request.get_json()
    uid = data.get('user_id')
    mid = data.get('message_id')
    try:
        msg = re.sub(r"\[(.*?)]", "", data.get('raw_message'))
        print(f"!!!Msg:[{msg}]")
    except Exception as E:
        msg = f"Error:{E}"
    if data.get('message_type') == 'private':
        send_msg(gpt_reply(msg), uid, None)
    if data.get('message_type') == 'group':
        gid = data.get('group_id')
        if data.get('raw_message').startswith(f"{gptcf} ") and msg:
            if data.get('user_id') == zrqq or sqxt == 0:
                send_msg(gpt_reply(msg), uid, gid, mid)
            else:
                sqtxtdq = open('sjktxt\cqQQ.txt', 'r', encoding='utf-8')
                sqtxtdq1 = sqtxtdq.read()
                sqtxtdq2 = re.findall(r"(\d+);", sqtxtdq1)
                ysq = 0
                for sqqq in sqtxtdq2:
                    sqqq1 = int(sqqq)
                    if data.get('user_id') == sqqq1 and msg:
                        send_msg(gpt_reply(msg), uid, gid, mid)
                        ysq = 1
                        break
                sqtxtdq.close()
                if 0 == ysq:
                    send_msg(msg="你还没有授权哦，无法使用该功能，请授权后再尝试吧", uid=uid, gid=gid, mid=mid)
        if data.get('raw_message').startswith(f"{gptcf2} ") and msg and dcf == 1:
            if data.get('user_id') == zrqq or sqxt == 0:
                send_msg(gpt_reply(msg), uid, gid, mid)
            else:
                sqtxtdq = open('sjktxt\cqQQ.txt', 'r', encoding='utf-8')
                sqtxtdq1 = sqtxtdq.read()
                sqtxtdq2 = re.findall(r"(\d+);", sqtxtdq1)
                ysq = 0
                for sqqq in sqtxtdq2:
                    sqqq1 = int(sqqq)
                    if data.get('user_id') == sqqq1 and msg:
                        send_msg(gpt_reply(msg), uid, gid, mid)
                        ysq = 1
                        break
                sqtxtdq.close()
                if 0 == ysq:
                    send_msg(msg="你还没有授权哦，无法使用该功能，请授权后再尝试吧", uid=uid, gid=gid, mid=mid)
        if data.get('raw_message').startswith("ctrl "):
            if data.get('user_id') == zrqq or sqxt == 0:
                ctrl = data.get('raw_message')
                ctrl1 = ctrl.replace("ctrl ", "")
                ctrl2 = ctrl1.replace("&#91;", "[")
                ctrl3 = ctrl2.replace("&#93;", "]")
                ctrl4 = ctrl3.replace("&amp;", "&")
                ctrl5 = ctrl4.replace("&#44;", ",")
                send_msg(msg=ctrl5, uid=None, gid=gid, mid=None)
            else:
                sqdq = open('sjktxt\cqQQ.txt', 'r',encoding='utf-8')
                sqdq1 = sqdq.read()
                sqdq2 = re.findall(r"(\d+);",sqdq1)
                ysq = 0
                for sqqq in sqdq2:
                    sqqq1 = int(sqqq)
                    if data.get('user_id') == sqqq1:
                        ctrl = data.get('raw_message')
                        ctrl1 = ctrl.replace("ctrl ", "")
                        ctrl2 = ctrl1.replace("&#91;", "[")
                        ctrl3 = ctrl2.replace("&#93;", "]")
                        ctrl4 = ctrl3.replace("&amp;", "&")
                        ctrl5 = ctrl4.replace("&#44;", ",")
                        send_msg(msg=ctrl5, uid=None, gid=gid, mid=None)
                        ysq = 1
                        break
                sqdq.close()
                if ysq == 0:
                    send_msg(msg="你还没有授权哦，无法使用该功能，请授权后再尝试吧", uid=uid, gid=gid, mid=mid)
        if data.get('raw_message').startswith("查询授权 ") and sqxt == 1:
            if data.get('user_id') == zrqq:
                cx = data.get('raw_message')
                cx1 = cx.replace("查询授权 ", "")
                cx2 = cx1.replace("[CQ:at,qq=", "")
                cx3 = cx2.replace("]", "")
                sqcx = open('sjktxt\cqQQ.txt', 'r', encoding='utf-8')
                sqcx1 = sqcx.read()
                sqcx2 = re.findall(r"(\d+);", sqcx1)
                cxcg = 0
                for cxsq in sqcx2:
                    if cx3 == cxsq:
                        cxcg = 1
                        send_msg(msg=f"查询成功，QQ:{cx3}已授权", uid=uid, gid=gid, mid=mid)
                        break
                sqcx.close()
                if cxcg == 0:
                    send_msg(msg=f"查询成功，QQ:{cx3}未授权", uid=uid, gid=gid, mid=mid)
            else:
                send_msg(msg="抱歉，此权限不开放使用", uid=uid, gid=gid, mid=mid)
        if data.get('raw_message').startswith("授权 ") and sqxt == 1:
            if data.get('user_id') == zrqq:
                sid = data.get('raw_message')
                sid1 = sid.replace("授权 ", "")
                sid2 = sid1.replace("[CQ:at,qq=", "")
                sid3 = sid2.replace("]", "")
                sid4 = sid3.replace(" ", "")
                sqxr = open('sjktxt\cqQQ.txt', 'r', encoding='utf-8')
                sqxr1 = sqxr.read()
                sqxr2 = re.findall(r"(\d+);", sqxr1)
                xrpd = 0
                for sqqq in sqxr2:
                    if sid4 == sqqq:
                        xrpd = 1
                        send_msg(msg=f"授权失败，QQ:{sid4}已授权", uid=uid, gid=gid, mid=mid)
                        break
                sqxr.close()
                if xrpd == 0:
                    xr = open('sjktxt\cqQQ.txt', 'a', encoding='utf-8')
                    xr.write(f"{sid4};")
                    xr.close()
                    send_msg(msg=f"授权成功，已将QQ:{sid4}写入", uid=uid, gid=gid, mid=mid)
            else:
                send_msg(msg="抱歉，此权限不开放使用", uid=uid, gid=gid, mid=mid)
        if data.get('raw_message').startswith("移除授权 ") and sqxt == 1:
            if data.get('user_id') == zrqq:
                yc = data.get('raw_message')
                yc1 = yc.replace("移除授权 ", "")
                yc2 = yc1.replace("[CQ:at,qq=", "")
                yc3 = yc2.replace("]", "")
                sqyc = open('sjktxt\cqQQ.txt', 'r', encoding='utf-8')
                sqyc1 = sqyc.read()
                sqyc2 = re.findall(r"(\d+);", sqyc1)
                xrpd = 0
                for ycsq in sqyc2:
                    if yc3 == ycsq:
                        xrpd = 1
                        sqyc.close()
                        ycsq2 = sqyc1.replace(f"{yc3};", "")
                        ycxr = open('sjktxt\cqQQ.txt', 'w', encoding='utf-8')
                        ycxr.write(ycsq2)
                        ycxr.close()
                        send_msg(msg=f"移除成功，QQ:{yc3}已移除", uid=uid, gid=gid, mid=mid)
                        break
                sqyc.close()
                if xrpd == 0:
                    send_msg(msg=f"移除失败，QQ:{yc3}未授权", uid=uid, gid=gid, mid=mid)
            else:
                send_msg(msg="抱歉，此权限不开放使用", uid=uid, gid=gid, mid=mid)
        if "获取一言" == data.get('raw_message'):
            url = "https://api.wrdan.com/hitokoto"
            rep = requests.get(url)
            js = rep.json()
            content = js["text"]
            send_msg(msg=content, uid=uid, gid=gid, mid=mid)
        if data.get('raw_message').endswith("天气获取"):
            what = data.get('raw_message')
            place = what.replace("天气获取", "")
            url = "https://xiaoapi.cn/API/zs_tq.php"
            params = {"type": "cytq", "msg": place,"num": 20,"n": 1}
            rep = requests.get(url, params)
            rep1 = rep.json()["name"]
            rep2 = rep.json()["data"]
            send_msg(msg=f"位置:{rep1}\n{rep2}", uid=uid, gid=gid, mid=mid)
        if data.get('raw_message').startswith("搜索音乐 "):
            gq = data.get('raw_message')
            gq1 = gq.replace("搜索音乐 ", "")
            url = "http://localhost:3000/search"
            params = {"keywords": gq1, "limit": 1}
            iyd = requests.get(url, params)
            iyd1 = re.compile("(\{\"id\":)(\d+)(,\"name\":)")
            iyd2 = iyd1.finditer(iyd.text)
            iyd3 = next(iyd2).group(2)
            send_msg(msg=f"[CQ:music,type=163,id={iyd3}]", uid=None, gid=gid, mid=None)
            send_msg(msg=f"音乐直链https://music.163.com/song/media/outer/url?id={iyd3}.mp3", uid=None, gid=gid, mid=None)
        if "获取毒鸡汤" == data.get('raw_message'):
            url = "https://api.shadiao.pro/du"
            rep = requests.get(url)
            data = rep.json()
            text = data["data"]["text"]
            send_msg(msg=text, uid=uid, gid=gid, mid=mid)
        if "获取彩虹屁" == data.get('raw_message'):
            url = "https://api.shadiao.pro/chp"
            rep = requests.get(url)
            data = rep.json()
            text = data["data"]["text"]
            send_msg(msg=text, uid=uid, gid=gid, mid=uid)
        if "机器人制作" in data.get('raw_message') or "机器人怎么做" in data.get('raw_message'):
            send_msg(msg="制作方法:\nGitHub项目地址https://github.com/AEBC08/QQ-bot\nbilibili视频教程https://www.bilibili.com/video/BV1Cb411R7Ei/?spm_id_from=333.999.0.0\nbilibili视频演示https://www.bilibili.com/video/BV1sv4y1W7NK/?spm_id_from=333.999.0.0\n作者:AEBC08", uid=uid, gid=gid, mid=uid)
        if "打开菜单" == data.get('raw_message'):
            if sqxt == 1:
                send_msg(msg="------------菜单------------\n制作教程(触发方式:机器人怎么做的)\n授权((ps:只有指定QQ号才能用.基本上是无上限授权，只要你储存空间够大就行.授权太多会加大响应时间)授权方式:授权 +@xxx/QQ号)\n查询授权((ps:只有指定QQ号才能用)授权方式:查询授权)\n移除授权((ps:只有指定QQ号才能用)移除方式:移除授权)\n1.OpenAI-ChatGPT对话((ps:需要授权,会消耗次数)触发方式:root +问题)\n2.重复说话((ps:需要授权,不消耗次数,支持CQ码)触发方式:ctrl +要说的话)\n3.网易云音乐搜索歌曲(触发方式:搜索音乐 +歌名/歌名 歌手/歌手/专辑\n4.天气查询(触发方式:xxx天气获取)\n5.一言(触发方式:获取一言)\n6.毒鸡汤(触发方式:获取毒鸡汤)\n7.彩虹屁(触发方式:获取彩虹屁)", uid=None, gid=gid, mid=None)
            if sqxt == 0:
                send_msg(
                    msg="------------菜单------------\n制作教程(触发方式:机器人怎么做的)\n授权(ps:授权系统已被关闭)\n查询授权(ps:授权系统已被关闭)\n移除授权(ps:授权系统已被关闭)\n1.OpenAI-ChatGPT对话(ps:授权系统已被关闭)触发方式:root +问题)\n2.重复说话(ps:授权系统已被关闭,支持CQ码)触发方式:ctrl +要说的话)\n3.网易云音乐搜索歌曲(触发方式:搜索音乐 +歌名/歌名 歌手/歌手/专辑\n4.天气查询(触发方式:xxx天气获取)\n5.一言(触发方式:获取一言)\n6.毒鸡汤(触发方式:获取毒鸡汤)\n7.彩虹屁(触发方式:获取彩虹屁)", uid=None, gid=gid, mid=None)
        if "test" == data.get('raw_message'):
            send_msg(msg="test", uid=None, gid=gid, mid=None)
        if "6" == data.get('raw_message'):
            send_msg(msg="6什么6，有什么好6的", uid=uid, gid=gid, mid=mid)
        if sykunphoto == 1 and "你干嘛" in data.get('raw_message') or "坤" in data.get('raw_message') or "鸡" in data.get('raw_message') or "黑子" in data.get('raw_message') or "kun" in data.get('raw_message') or "cxk" in data.get('raw_message') or "唱跳" in data.get('raw_message'):
            folder_path = 'kun photo'
            file_list = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file))]
            random_file = random.choice(file_list)
            send_msg(msg=f"图片相对路径{random_file}\n[CQ:image,file=By AEBC08,subType=0,url=file:///{random_file}]", uid=uid, gid=gid, mid=mid)
    return 'OK'


if __name__ == '__main__':
    if qdbgm == 1:
        os.startfile("Audio\Arknights.mp3")
    zybwz = 0
    print("检查资源完整中...")
    print("----检查cqhttp中...")
    if os.path.exists("go-cqhttp.exe"):
        print("--------cqhttp完整.")
    else:
        zybwz = 1
        print("--------cqhttp不存在，请完整的将资源解压指定路径.")
    print("----检查api中...")
    if os.path.exists("mapi\mun.bat"):
        print("--------api完整.")
    else:
        zybwz = 1
        print("--------api资源不完整，请完整的将资源解压指定路径.")
    print("----检查kun photo中...")
    if os.path.exists("kun photo\cz.txt"):
        print("--------kun photo完整.")
    else:
        zybwz = 1
        print("--------kun photo资源不完整，请完整的将资源解压指定路径.")
    print("----检查数据库中...")
    if os.path.exists("sjktxt\cqQQ.txt"):
        print("--------数据库完整.")
    else:
        sjkcz = open('sjktxt\cqQQ.txt', 'w')
        sjkcz.close()
        print("--------数据库文件丢失，已重新创建.")
    print("检查完毕.")
    if zybwz == 1:
        while True:
            print("资源不完整，无法启动，请确认资源完整，解压到指定路径再次尝试.")
            time.sleep(10)
    else:
        gzlj = os.path.abspath('.')
        xrlj = open('mapi\mun.bat', 'w', encoding='utf-8')
        xrlj.write(f"cd {gzlj}\mapi\nnode app.js")
        xrlj.close()
        os.startfile("mapi\mun.bat")
        os.system("start cmd /K go-cqhttp.exe")
        app.run(host='127.0.0.1', port=5701)
