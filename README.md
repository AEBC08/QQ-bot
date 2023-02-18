# QQ-bot
一个使用python搭建基于go-cqhttp的QQ机器人
# 安装环境
安装python3.8以上的版本
安装依赖库
pip install openai
pip install requests
pip install flask
# 安装ffmpeg
访问 https://ffmpeg.org/download.html 下载
解压到C:\Program Files目录下
添加环境变量C:\Program Files\ffmpeg\bin
以管理员身份运行cmd或者power shell
运行ffmpeg -version
再次运行setx /M PATH "C:\Program Files\ffmpeg\bin;%PATH%"
# 运行
解压文件到C:\根目录
记事本打开C:\QQ bot\QQ bot\config.yml 将账号密码改成你机器人的账号密码，保存更改
记事本打开C:\QQ bot\QQ bot\bot.py 将机器人账号和你自己的账号还有OpenAIkey填入，没有OpenAIkey将无法使用ChatGPT，获取api的教程去 https://bilibili.com 一大堆，触发方式看个人，作用就是触发ChatGPT
最后双击C:\QQ bot\QQ bot\run.bat就可以启动了
# 实现功能
授权((ps:只有指定QQ号才能用)授权方式:授权 +@xxx/QQ号)查看授权((ps:只有指定QQ号才能用)授权方式:查看授权)1.OpenAI-ChatGPT对话((ps:需要授权,会消耗次数)触发方式:触发方式 +问题)2.重复说话((ps:需要授权,不消耗次数,支持CQ码)触发方式:ctrl +要说的话)3.网易云音乐搜索歌曲(触发方式:搜索音乐 +歌名/歌名 歌手/歌手/专辑4.天气查询(触发方式:xxx天气获取)5.一言(触发方式:获取一言)6.毒鸡汤(触发方式:获取毒鸡汤)7.彩虹屁(触发方式:获取彩虹屁)
