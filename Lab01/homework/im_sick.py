from gmail import GMail, Message
from random import choice
import datetime

reasons = ["bận cho mèo ăn", "bị mệt do ăn quá nhiều","mỏi chân do chạy quá sức"]
rand_reason = choice(reasons)
html_template = """
<h2 style="text-align: center;">ĐƠN XIN NGHỈ&nbsp;</h2>
<p><em><strong>K&iacute;nh gửi:&nbsp;</strong></em><em>&nbsp;</em>Thầy chủ nhiệm lớp C4E16</p>
<p>T&ecirc;n em l&agrave; <span style="color: #0000ff;">A bờ cờ</span></p>
<p>H&ocirc;m nay em {{sickness}} n&ecirc;n em viết đơn n&agrave;y xin ph&eacute;p thầy cho em nghỉ một buổi</p>
<p>Em xin ch&acirc;n th&agrave;nh cảm ơn<img src="http://htmleditor.tools/tinymce465/plugins/emoticons/img/smiley-smile.gif" alt="smile" /></p>
<p>A bờ cờ</p>
"""
html_content = html_template.replace('{{sickness}}',rand_reason)

gmail = GMail('honganhc4e16@gmail.com','c4e162018')
msg = Message('Call in sick',to='techkidsc4e16@gmail.com', html = html_content)

while True:
    now = datetime.datetime.now()
    if now.hour == 7:
    #if now.strftime('%I %p') == '07 AM':
        gmail.send(msg)
        break
