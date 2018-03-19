from gmail import GMail, Message
from random import choice
reason= ["chán", 'buồn ngủ', 'bận chơi','cho mèo ăn']
rand_reason = choice(reason)

gmail = GMail('honganhc4e16@gmail.com','ce4162018')

html_template ="""
<p style="text-align: center;"><strong>Đơn xin nghỉ học</strong></p>
<p style="text-align: left;">Em ch&agrave;o thầy</p>
<p style="text-align: left;">T&ecirc;n em l&agrave; <span style="color: #0000ff;">Vũ Hồng Anh</span></p>
<p style="text-align: left;"><span style="color: #000000;">H&ocirc;m nay e {{sickness}} n&ecirc;n em viết đơn n&agrave;y xin ph&eacute;p thầy cho em nghỉ 1 buổi</span></p>
<p style="text-align: left;"><span style="color: #000000;"></span></p>
<p style="text-align: left;"><span style="color: #000000;">Hồng Anh</span></p>
"""
html_content = html_template.replace('{{sickness}}',rand_reason)

# html_content ="""
# <p style="text-align: center;"><strong>Đơn xin nghỉ học</strong></p>
# <p style="text-align: left;">Em ch&agrave;o thầy</p>
# <p style="text-align: left;">T&ecirc;n em l&agrave; <span style="color: #0000ff;">Vũ Hồng Anh</span></p>
# <p style="text-align: left;"><span style="color: #000000;">H&ocirc;m nay e {} n&ecirc;n em viết đơn n&agrave;y xin ph&eacute;p thầy cho em nghỉ 1 buổi</span></p>
# <p style="text-align: left;"><span style="color: #000000;"></span></p>
# <p style="text-align: left;"><span style="color: #000000;">Hồng Anh</span></p>
# """.format(rand_reason)


msg = Message('html1',to ='techkidsc4e16@gmail.com', html = html_content)
gmail.send(msg)
