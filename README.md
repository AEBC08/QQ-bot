# QQ-bot
一个使用python搭建基于go-cqhttp的QQ机器人
# 使用需知
需要一定的动手能力和理解能力
<br>
目前不确定会不会出现问题
# 安装环境
安装python3.8以上的版本 官网 https://www.python.org
<br>
<br>
安装nodejs 官网 https://nodejs.org
<br>
安装依赖库：
<pre><code>
pip install openai
</code></pre>
<pre><code>
pip install requests
</code></pre>
<pre><code>
pip install flask
</code></pre>
# 安装ffmpeg
下载：
<br>
访问官网 https://ffmpeg.org/download.html
<br>
或 https://pan.baidu.com/s/1KtT90Mf42ky6K5vM0oMpdg?pwd=t4vb 提取码: t4vb 
<br>
解压到C:\Program Files目录下
<br>
添加环境变量C:\Program Files\ffmpeg\bin
<br>
以管理员身份运行cmd或者power shell
<br>
运行：
<pre><code>
ffmpeg -version
</code></pre>
再次运行：
<pre><code>
setx /M PATH "C:\Program Files\ffmpeg\bin;%PATH%"
</code></pre>
# 运行
解压压缩包到C:\（根目录，一定要是C盘根目录，文件夹名字不能改，不然会出问题）
<br>
记事本或者其他文本编辑器开C:\QQ bot\QQ bot\config.yml 将账号密码改成你机器人的账号密码，保存更改
<br>
记事本或者其他文本编辑器打开C:\QQ bot\QQ bot\bot.py 将机器人账号和你自己的账号还有OpenAIkey填入，触发方式看个人，作用就是触发ChatGPT
<br>
没有OpenAIkey将无法使用ChatGPT，获取key的教程去 https://bilibili.com 一大堆
<br>
最后双击C:\QQ bot\QQ bot\run.bat就可以启动了
# 实现功能
授权((ps:只有指定QQ号才能用)授权方式:授权 +@xxx/QQ号)
查看授权((ps:只有指定QQ号才能用)授权方式:查看授权)
1.OpenAI-ChatGPT对话((ps:需要授权,会消耗次数)触发方式:触发方式 +问题)
2.重复说话((ps:需要授权,不消耗次数,支持CQ码)触发方式:ctrl +要说的话)
3.网易云音乐搜索歌曲(触发方式:搜索音乐 +歌名/歌名 歌手/歌手/专辑)
4.天气查询(触发方式:xxx天气获取)
5.一言(触发方式:获取一言)
6.毒鸡汤(触发方式:获取毒鸡汤)7.彩虹屁(触发方式:获取彩虹屁)
# 详细视频教程
访问 https://space.bilibili.com/510197857 查看作品
# 更新时间
每星期周末
<br>
大概率更新
