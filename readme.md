# 自动填写问卷星脚本

相信同学们都为校园抢表单活动而烦恼过，尤其是几百人抢几十个名额的时候，不到十秒就抢光了，痛苦的是别人可能有工具而暗恨自己没有，脚本已过实战，一秒内能秒杀。

## 使用方法

（1）修改：url_survey = 'https://www.wjx.cn/XXXXX'，在此添加问卷星的问卷地址

（2）修改：googleExe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

Chrome浏览器可执行文件路径，以上是我电脑上的位置可供参考，具体位置需要自己找一下，安装了Google的肯定有这个路径

（3）修改：googleExe = r"C:\Program Files\Google\Chrome\Application\chromedriver.exe"

ChromeDriver可执行文件路径，需要检查Chrome浏览器的版本，下载符合自己版本的，将下载的ChromeDriver压缩文件解压缩到浏览器的安装目录下。

关于ChromeDriver最新下载地址：<https://googlechromelabs.github.io/chrome-for-testing/>

（4）修改：fill_data = {1: '1', 2: '2', 3: '3'}，里面的数据根据具体情况修改，前面是题号，后面是要填的内容，如果是要上传文件，请直接写路径在里面，同时确保文件路径格式正确如1: r"E:\main\1.jpg"。注意这里不考虑有选择题的情况，如有将随机选择一个选项或者会报错。

（5）修改：time.sleep(1)，run函数中的第一个，改里面的数字，因为太快了的话，大家懂的，这不正常，不是人类的手速了

（6）使用pip install selenium安装需要的包

（7）这里我测试的问卷星链接就不关闭了，相信大家如果没遇到什么麻烦的话是可以直接运行的。