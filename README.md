# WechatPush

![Language](https://img.shields.io/badge/Language-Python-yellow)![LICENSE](https://img.shields.io/badge/LICENSE-MIT-red)![Author](https://img.shields.io/badge/Author-DanKe-blue)

Python微信公众号/订阅号/测试号推送库

功能目前还不完善，将逐步完善微信推送所有功能



# 文档

# <span id="about">介绍</span>

*欢迎关注作者微信公众号【蛋壳的窝】*

> 什么是WechatPush

**WechatPush** 是一个基于微信公众号开发接口实现的微信通知推送服务，你可以通过你自己的微信公众号/订阅号/测试号实现你自己的微信推送服务。配置完成后，只需要一段代码即可把信息推送到微信上，无需安装额外的软件即可做到信息实时通知。你可以使用**WechatPush**来做服务器报警通知、抢课通知、抢票通知、信息更新提示等。


# <span id="open">开源地址</span>

> 记得在Github上把星星点亮哦

![Language](https://img.shields.io/badge/Language-Python-yellow)![LICENSE](https://img.shields.io/badge/LICENSE-MIT-red)![Author](https://img.shields.io/badge/Author-DanKe-blue)

[WechatPush: Python微信公众号/订阅号/测试号推送库](https://github.com/DanKE123abc/WechatPush)



# <span id="see">效果预览</span>

> 下面是效果预览

|          |                          |                          |
| -------- | ------------------------ | ------------------------ |
| **类型** | **普通消息**             | **模板消息**             |
| 预览     | ![普通消息](.\img\1.jpg) | ![模板消息](.\img\2.jpg) |
| **类型** | **带链接的消息**         | **TTS伪语音**            |
| 预览     | ![3](.\img\3.jpg)        | ![4](.\img\4.jpg)        |


# <span id="words">参数解释</span>

### appid

你的微信公众号开发者接口中的appID

### appsecret

你的微信公众号开发者接口中的appsecret

### openid

你要发信息给的人的用户标识（独一无二，类似于微信号）

### templateid

发送模板消息时的模板id

### message

发送的信息，发送普通消息时为字符串，发送模板消息时为json

发送带链接的消息时，可以不填

发送TTS伪语音时为语音朗读文本

### url

发送模板消息时，点击“详情”后跳转到的网页，不填则发送的消息没有“详情”一栏

发送带链接的消息时，点击链接标签跳转到的网页，不填则跳转到微信官网

### label

发送带链接的消息时，链接标签显示的信息，不填则显示”点击查看链接“

### person

发送TTS伪语音时的音色，默认为0

| 音色码 | 实际音色 |
| ------ | -------- |
| 0      | 标准女音 |
| 1      | 标准男音 |
| 3      | 斯文男音 |

### volume

发送TTS伪语音时的音量，默认为2

# <span id="import">快速接入</span>

> #### 我们推荐您使用[微信测试号](https://mp.weixin.qq.com/debug/cgi-bin/sandboxinfo?action=showinfo&t=sandbox/index)进行调试，无需注册，扫码登录即可使用！

这里提供了一段源码帮你更好地理解使用方法

```python
import wechatpush
wechatpush.push_text("xxxx这里是用户的openidxxxx","Hello World！TEXT")
wechatpush.push_url("xxxx这里是用户的openidxxxx","http://danke.ml","蛋壳的小站","Hello World URL")

#msg消息必须按照模板配置！
msg = {
    "Title": {
                "value":"Hello World! TEXTCARD"
            },
}
wechatpush.push_textcard("vvvv这里是模板idvvvv","xxxx这里是用户的openidxxxx",msg)
wechatpush.push_voice("xxxx这里是用户的openidxxxx","Hello World！TTS",3,5)
```

>  wechatpush启动流程：

1.调用wechatpush --> 2.获取AccessToken --> 3.检查setting.py是否存在 --> 4.导入appid与appsecret --> 5.返回AccessToken --> 6.解析信息 --> 7.发送消息

## <span id="one">1.安装WechatPush库</span>

##### 运行以下命令：

```python
pip install py-WechatPush
```

*或者从仓库下载wechatpush.py放入项目文件夹内*



```python
import wechatpush
```

## <span id="two">2.配置setting</span>

在与软件同目录下创建setting.py文件，填入下面的代码：

```python
#--------------------wechatpush-----------------------

APPID = '你自己的appid'
APPSECRET = '你自己的appsecret'
```

## <span id="three">3.发送消息</span>

##### 一：普通消息

```python
import wechatpush
wechatpush.push_text("你要接收消息的openid","你要发的消息")
```

##### 二：模板消息

```python
import wechatpush
wechatpush.push_textcard("你要用的模板id","你要接收消息的openid","模板参数（json）","详情页url（选填）")
```

##### 三：带链接的消息

```python
import wechatpush
wechatpush.push_url("你要接收消息的openid","标签跳转的链接","标签显示","你要发的消息")
```

##### 四：TTS伪语音

```python
import wechatpush
wechatpush.push_voice("你要接收消息的openid","你要发送的语音文本")
```

如果一切正常的话，errcode的值是0

## <span id="qa">常见问题：</span>

**1.软件报告 “setting.py not found”和“setting.py is created. Please re run it after configuration”**

没有找到setting.py文件，自动生成了一个，需要您手动在setting.py中填写后重新启动。

**2.软件报告 “appid or appsecret not found”**

无法从setting.py读取appid或者appsecret，请检测setting.py是否已有此项。

**3.软件报告 ”errcode = xxxxx“**

见下表

| 返回码 | 说明                         |
| ------ | ---------------------------- |
| -1     | 系统繁忙                     |
| 0      | 请求成功                     |
| 40001  | 验证失败                     |
| 40002  | 不合法的凭证类型             |
| 40003  | 不合法的OpenID               |
| 40004  | 不合法的媒体文件类型         |
| 40005  | 不合法的文件类型             |
| 40006  | 不合法的文件大小             |
| 40007  | 不合法的媒体文件id           |
| 40008  | 不合法的消息类型             |
| 40009  | 不合法的图片文件大小         |
| 40010  | 不合法的语音文件大小         |
| 40011  | 不合法的视频文件大小         |
| 40012  | 不合法的缩略图文件大小       |
| 40013  | 不合法的APPID                |
| 41001  | 缺少access_token参数         |
| 41002  | 缺少appid参数                |
| 41003  | 缺少refresh_token参数        |
| 41004  | 缺少secret参数               |
| 41005  | 缺少多媒体文件数据           |
| 41006  | access_token超时             |
| 42001  | 需要GET请求                  |
| 43002  | 需要POST请求                 |
| 43003  | 需要HTTPS请求                |
| 44001  | 多媒体文件为空               |
| 44002  | POST的数据包为空             |
| 44003  | 图文消息内容为空             |
| 45001  | 多媒体文件大小超过限制       |
| 45002  | 消息内容超过限制             |
| 45003  | 标题字段超过限制             |
| 45004  | 描述字段超过限制             |
| 45005  | 链接字段超过限制             |
| 45006  | 图片链接字段超过限制         |
| 45007  | 语音播放时间超过限制         |
| 45008  | 图文消息超过限制             |
| 45009  | 接口调用超过限制             |
| 45015  | 响应超出时间限制或订阅被取消 |
| 46001  | 不存在媒体数据               |
| 47001  | 解析JSON/XML内容错误         |

# <span id="danke">使用须知</span>

1.本库原作者为[蛋壳](https://github.com/DanKE123abc)，本项目遵循MIT开源协议，请遵守协议！

2.本库是作为工具类而不是服务类，您的一切信息不会被泄露给作者，作者不负任何法律责任。

3.本库是为了方便开发者朋友，与腾讯，微信及其他第三方服务无关。

4.当您因使用本库造成任何重大事故时，作者不负任何责任！

5.请勿使用本库进行一切违法国家法律法规的事情！

# <span id="help">帮助作者</span>

您的支持就是对我最大的鼓励！

| 支付宝                | 微信                 |
| --------------------- | -------------------- |
| ![zfb](.\img\zfb.jpg) | ![zfb](.\img\wx.jpg) |

# <span id="logs">更新日志</span>

#### v0.1.5

上传到pypi

现在可以使用 pip install py-wechatpush 安装

#### v0.1.4

修复了一些Bug

支持发送TTS伪语音（实际上就是带链接的文本消息，TTS用的是百度的接口）

**注意：TTS伪语音只是一个测试，将来可能会下线*

#### v0.1.2

支持发送带链接的消息

#### v0.1.1

模板消息支持自定义url

#### v0.1.0

第一个版本，支持发送普通消息和模板消息

