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

qq_code = "机器人的qq号"
app = Flask(__name__)

openai.api_key = "openai的key，获取方法可以参考bilibili.com的教程"
cffs = "触发方式"
zrqid = 10001  # 主人的qq号

def gpt_reply(msg):
    if "Error" in msg:
        return msg
    msg = msg.replace(f"{cffs} ", "")
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

qid = "空"
rcs = 0
qid1 = "空"
rcs1 = 0
qid2 = "空"
rcs2 = 0
qid3 = "空"
rcs3 = 0
fg = 0

@app.route('/', methods=["POST"])
def post_data():
    global qid, qid1, qid2, qid3, rcs, rcs1, rcs2, rcs3, fg, cffs, zrqid
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
        if data.get('raw_message').startswith(f"{cffs} ") and msg:
            if data.get('user_id') == zrqid:
                send_msg(gpt_reply(msg), uid, gid, mid)
            else:
                if data.get('user_id') == qid:
                    rcs = rcs - 1
                    send_msg(gpt_reply(msg), uid, gid, mid)
                    if rcs < 1:
                        send_msg(msg=f"[CQ:at,qq={qid}]你的使用次数已用尽,已收回授权", uid=None, gid=gid, mid=None)
                        qid = "空"
                else:
                    if data.get('user_id') == qid1:
                        rcs1 = rcs1 - 1
                        send_msg(gpt_reply(msg), uid, gid, mid)
                        if rcs1 < 1:
                            send_msg(msg=f"[CQ:at,qq={qid1}]你的使用次数已用尽,已收回授权", uid=None, gid=gid, mid=None)
                            qid1 = "空"
                    else:
                        if data.get('user_id') == qid2:
                            rcs2 = rcs2 - 1
                            send_msg(gpt_reply(msg), uid, gid, mid)
                            if rcs2 < 1:
                                send_msg(msg=f"[CQ:at,qq={qid2}]你的使用次数已用尽,已收回授权", uid=None, gid=gid, mid=None)
                                qid2 = "空"
                        else:
                            if data.get('user_id') == qid3:
                                rcs3 = rcs3 - 1
                                send_msg(gpt_reply(msg), uid, gid, mid)
                                if rcs3 < 1:
                                    send_msg(msg=f"[CQ:at,qq={qid3}]你的使用次数已用尽,已收回授权", uid=None, gid=gid, mid=None)
                                    qid3 = "空"
                            else:
                                send_msg(msg="你还没有授权哦，无法使用该功能，请授权后再尝试吧", uid=uid, gid=gid, mid=mid)
        if data.get('raw_message').startswith("ctrl "):
            if data.get('user_id') == zrqid:
                ctrl = data.get('raw_message')
                ctrl1 = ctrl.replace("ctrl ", "")
                ctrl2 = ctrl1.replace("&#91;", "[")
                ctrl3 = ctrl2.replace("&#93;", "]")
                ctrl4 = ctrl3.replace("&amp;", "&")
                ctrl5 = ctrl4.replace("&#44;", ",")
                send_msg(msg=ctrl5, uid=None, gid=gid, mid=None)
            else:
                if data.get('user_id') == qid:
                    ctrl = data.get('raw_message')
                    ctrl1 = ctrl.replace("ctrl ", "")
                    ctrl2 = ctrl1.replace("&#91;", "[")
                    ctrl3 = ctrl2.replace("&#93;", "]")
                    ctrl4 = ctrl3.replace("&amp;", "&")
                    ctrl5 = ctrl4.replace("&#44;", ",")
                    send_msg(msg=ctrl5, uid=None, gid=gid, mid=None)
                else:
                    if data.get('user_id') == qid1:
                        ctrl = data.get('raw_message')
                        ctrl1 = ctrl.replace("ctrl ", "")
                        ctrl2 = ctrl1.replace("&#91;", "[")
                        ctrl3 = ctrl2.replace("&#93;", "]")
                        ctrl4 = ctrl3.replace("&amp;", "&")
                        ctrl5 = ctrl4.replace("&#44;", ",")
                        send_msg(msg=ctrl5, uid=None, gid=gid, mid=None)
                    else:
                        if data.get('user_id') == qid2:
                            ctrl = data.get('raw_message')
                            ctrl1 = ctrl.replace("ctrl ", "")
                            ctrl2 = ctrl1.replace("&#91;", "[")
                            ctrl3 = ctrl2.replace("&#93;", "]")
                            ctrl4 = ctrl3.replace("&amp;", "&")
                            ctrl5 = ctrl4.replace("&#44;", ",")
                            send_msg(msg=ctrl5, uid=None, gid=gid, mid=None)
                        else:
                            if data.get('user_id') == qid3:
                                ctrl = data.get('raw_message')
                                ctrl1 = ctrl.replace("ctrl ", "")
                                ctrl2 = ctrl1.replace("&#91;", "[")
                                ctrl3 = ctrl2.replace("&#93;", "]")
                                ctrl4 = ctrl3.replace("&amp;", "&")
                                ctrl5 = ctrl4.replace("&#44;", ",")
                                send_msg(msg=ctrl5, uid=None, gid=gid, mid=None)
                            else:
                                send_msg(msg="你还没有授权哦，无法使用该功能，请授权后再尝试吧", uid=uid, gid=gid, mid=mid)
        if data.get('raw_message') == "查看授权":
            if data.get('user_id') == zrqid:
                send_msg(msg=f"授权位1QQ号:{qid}\n授权位1剩余使用次数:{rcs}\n授权位2QQ号:{qid1}\n授权位2剩余使用次数:{rcs1}\n授权位3QQ号:{qid2}\n授权位3剩余使用次数:{rcs2}\n授权位4QQ号:{qid3}\n授权位1剩余使用次数:{rcs3}", uid=uid, gid=gid, mid=mid)
            else:
                send_msg(msg="抱歉，此权限不开放使用", uid=uid, gid=gid, mid=mid)
        if data.get('raw_message').startswith("授权 "):
            if data.get('user_id') == zrqid:
                sid = data.get('raw_message')
                sid1 = sid.replace("授权 ", "")
                sid2 = sid1.replace("[CQ:at,qq=", "")
                sid3 = sid2.replace("]", "")
                sid4 = int(sid3)
                if qid == "空":
                    qid = sid4
                    rcs = 10
                    send_msg(msg=f"授权成功，已将[CQ:at,qq={qid}]放在第1授权位", uid=None, gid=gid, mid=None)
                else:
                    if qid1 == "空":
                        qid1 = sid4
                        rcs1 = 10
                        send_msg(msg=f"授权成功，已将[CQ:at,qq={qid1}]放在第2授权位", uid=None, gid=gid, mid=None)
                    else:
                        if qid2 == "空":
                            qid2 = sid4
                            rcs2 = 10
                            send_msg(msg=f"授权成功，已将[CQ:at,qq={qid2}]放在第3授权位", uid=None, gid=gid, mid=None)
                        else:
                            if qid3 == "空":
                                qid3 = sid4
                                rcs3 = 10
                                send_msg(msg=f"授权成功，已将[CQ:at,qq={qid3}]放在第4授权位", uid=None, gid=gid, mid=None)
                            else:
                                if fg > 3:
                                    fg = 0
                                if fg == 0:
                                    send_msg(msg=f"[CQ:at,qq={qid}]你的授权即将被覆盖", uid=None, gid=gid,mid=None)
                                    qid = sid4
                                    rcs = 10
                                    send_msg(msg=f"授权成功，已将[CQ:at,qq={qid}]覆盖在第1授权位", uid=None, gid=gid, mid=None)
                                if fg == 1:
                                    send_msg(msg=f"[CQ:at,qq={qid1}]你的授权即将被覆盖", uid=None, gid=gid, mid=None)
                                    qid1 = sid4
                                    rcs1 = 10
                                    send_msg(msg=f"授权成功，已将[CQ:at,qq={qid1}]覆盖在第2授权位", uid=None, gid=gid, mid=None)
                                if fg == 2:
                                    send_msg(msg=f"[CQ:at,qq={qid2}]你的授权即将被覆盖", uid=None, gid=gid, mid=None)
                                    qid2 = sid4
                                    rcs2 = 10
                                    send_msg(msg=f"授权成功，已将[CQ:at,qq={qid2}]覆盖在第3授权位", uid=None, gid=gid, mid=None)
                                if fg == 3:
                                    send_msg(msg=f"[CQ:at,qq={qid3}]你的授权即将被覆盖", uid=None, gid=gid, mid=None)
                                    qid3 = sid4
                                    rcs3 = 10
                                    send_msg(msg=f"授权成功，已将[CQ:at,qq={qid3}]覆盖在第4授权位", uid=None, gid=gid, mid=None)
                                fg = fg + 1
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
            send_msg(msg=text, uid=None, gid=gid, mid=None)
        if "获取彩虹屁" == data.get('raw_message'):
            url = "https://api.shadiao.pro/chp"
            rep = requests.get(url)
            data = rep.json()
            text = data["data"]["text"]
            send_msg(msg=text, uid=None, gid=gid, mid=None)
        if "打开菜单" == data.get('raw_message'):
            send_msg(msg=f"------------菜单------------\n授权((ps:只有指定QQ号才能用)授权方式:授权 +@xxx/QQ号)\n查看授权((ps:只有指定QQ号才能用)授权方式:查看授权)\n1.OpenAI-ChatGPT对话((ps:需要授权,会消耗次数)触发方式:{cffs} +问题)\n2.重复说话((ps:需要授权,不消耗次数,支持CQ码)触发方式:ctrl +要说的话)\n3.网易云音乐搜索歌曲(触发方式:搜索音乐 +歌名/歌名 歌手/歌手/专辑\n4.天气查询(触发方式:xxx天气获取)\n5.一言(触发方式:获取一言)\n6.毒鸡汤(触发方式:获取毒鸡汤)\n7.彩虹屁(触发方式:获取彩虹屁)", uid=None, gid=gid, mid=None)
        if "test" == data.get('raw_message'):
            send_msg(msg="test", uid=None, gid=gid, mid=None)
        if "6" == data.get('raw_message'):
            send_msg(msg="6什么6，有什么好6的", uid=uid, gid=gid, mid=mid)
        if "你干嘛" in data.get('raw_message'):
            send_msg(msg="小黑子被我逮到了吧", uid=uid, gid=gid, mid=mid)
    return 'OK'


if __name__ == '__main__':
    test = input(">>>是否开启cqhttp和网易云音乐api(Y/n):")
    if test == "Y" or test == 'y':
        os.system("explorer.exe C:\QQ bot\mapi\mun.bat")
        os.system("start cmd /K go-cqhttp.exe")
    else:
        quit()
    app.run(host='127.0.0.1', port=5701)
