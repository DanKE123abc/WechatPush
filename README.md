# WechatPush

![Language](https://img.shields.io/badge/Language-Python-yellow)![LICENSE](https://img.shields.io/badge/LICENSE-MIT-red)![Author](https://img.shields.io/badge/Author-DanKe-blue)![Version](https://img.shields.io/badge/Version-0.1.2[beta]-grenn)

# 官方文档：http://wechatpush.danke.ml

Python微信公众号/订阅号/测试号推送库

功能目前还不完善，将逐步完善微信推送所有功能

### 使用教程

直接运行wechat.py或者在脚本中输入以下代码：

```python
import wechatpush
wechatpush.help()
```

需要在setting.py中设置appid与appsecret



#### 引用方法

wechatpush.push_text(openid,message)

​     发送消息

wechatpush.push_textcard(templateid,openid,message,url)

​    发送模板消息，message必须为符合模板的json格式，url一项选填

wechatpush.push_url(openid,url,label,message)
    发送带链接的消息，message可以不填

微信官方文档：https://developers.weixin.qq.com/doc/offiaccount/Getting_Started/Overview.html

#### 待续

todo
