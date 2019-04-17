from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from smtplib import SMTP_SSL

from config.cif import *


class SendEmail(object):
    # 使用Python发送文本格式的邮件
    def send_email_text(self):
        # 邮件服务信息：邮件服务+发件人QQ邮箱信息+发件人邮箱+收件人邮箱
        smtp_server = 'smtp.qq.com'
        sender_qq = '2969775177@qq.com'
        password = 'wsvhdwastvlndcjg'
        sender_email = '2969775177@qq.com'
        receiver = '13021117364@163.com'
        # receiver = ['1@123.com','2@123.com','3@123.com']  # 给多人发送邮件

        # 邮件内容：正文+标题
        mail_content = '您好，这是一封使用python登录QQ邮箱发送文本邮件的测试'
        mail_title = '发送文本格式邮件测试'

        # 登录smtp服务器并发送邮件
        smtp = SMTP_SSL(smtp_server)
        smtp.ehlo(smtp_server)  # 由客户端发送，指示 ESMTP 会话开始
        smtp.login(sender_qq, password)

        msg = MIMEText(mail_content, 'plain', 'utf-8')  # 构建纯文本邮件对象，plain为纯文本格式，以utf-8编码
        msg['Subject'] = Header(mail_title, 'utf-8')  # 邮件主题中包含中文，需要通过Header对对象进行编码
        msg['From'] = sender_email
        msg['To'] = receiver

        smtp.sendmail(sender_email, receiver, msg.as_string())
        smtp.close()

    # 使用Python发送HTML格式的邮件
    def send_email_html(self):
        # 邮件服务信息：邮件服务+发件人QQ邮箱信息+发件人邮箱+收件人邮箱
        smtp_server = 'smtp.qq.com'
        sender_qq = '2969775177@qq.com'
        password = 'wsvhdwastvlndcjg'
        sender_email = '2969775177@qq.com'
        receiver = '13021117364@163.com'
        # receiver = ['1@123.com','2@123.com','3@123.com']  # 给多人发送邮件

        # 邮件内容：正文+标题
        # 传入Html格式的邮件内容
        mail_content = '<html><body><h2>您好</h2>，<p>这是一封使用python登录QQ邮箱发送网页格式邮件的测试</p></body></html>'
        mail_title = '发送网页格式邮件测试'

        # 登录smtp服务器并发送邮件
        smtp = SMTP_SSL(smtp_server)
        smtp.ehlo(smtp_server)  # 由客户端发送，指示 ESMTP 会话开始
        smtp.login(sender_qq, password)

        msg = MIMEText(mail_content, 'html', 'utf-8')  # 构建邮件对象，指定为html格式，以utf-8编码
        msg['Subject'] = Header(mail_title, 'utf-8')  # 邮件主题中包含中文，需要通过Header对对象进行编码
        msg['From'] = sender_email
        msg['To'] = receiver

        smtp.sendmail(sender_email, receiver, msg.as_string())
        smtp.close()

    # 使用Python发送带附件的邮件
    def send_email_mixture(self, report_file):
        # 邮件服务信息：邮件服务+发件人QQ邮箱信息+发件人邮箱+收件人邮箱
        smtp_server = 'smtp.qq.com'
        sender_qq = '2969775177@qq.com'
        password = 'wsvhdwastvlndcjg'
        sender_email = '2969775177@qq.com'
        receiver = '13021117364@163.com'
        # receiver = ['1@123.com','2@123.com','3@123.com']  # 给多人发送邮件

        # 邮件内容：正文+标题
        # 传入Html格式的邮件内容
        mail_content = '<html><body><h2>您好</h2>，<p>这是一封使用python登录QQ邮箱发送网页格式带附件邮件的测试</p></body></html>'
        mail_title = '发送网页格式带附件的邮件测试'

        # 登录smtp服务器并发送邮件
        smtp = SMTP_SSL(smtp_server)
        smtp.ehlo(smtp_server)  # 由客户端发送，指示 ESMTP 会话开始
        smtp.login(sender_qq, password)

        msg = MIMEMultipart()  # 构建混合格式邮件对象
        msg.attach(MIMEText(mail_content, 'html', 'utf-8'))  # 邮件正文
        msg['Subject'] = Header(mail_title, 'utf-8')  # 邮件主题中包含中文，需要通过Header对对象进行编码
        msg['From'] = sender_email
        msg['To'] = receiver

        # 加载附件
        att = MIMEText(open(report_file, 'rb').read(), 'base64', 'utf-8')  # 打开文件并以二进制方式读取，以base64位加密，utf-8编码保存作为附件
        att['Content-Type'] = 'application/octet-stream'  # 声明附件内容类型
        att['Content-Disposition'] = 'attachment; filename="report.html"'   # 声明附件描述及附件名称
        msg.attach(att)

        smtp.sendmail(sender_email, receiver, msg.as_string())
        smtp.close()

        # 发送HTML文本中带图片的邮件
    def send_email_html_img(self, data_file):
        # 邮件服务信息：邮件服务+发件人QQ邮箱信息+发件人邮箱+收件人邮箱
        smtp_server = 'smtp.qq.com'
        sender_qq = '2969775177@qq.com'
        password = 'wsvhdwastvlndcjg'
        sender_email = '2969775177@qq.com'
        receiver = '13021117364@163.com'
        # receiver = ['1@123.com','2@123.com','3@123.com']  # 给多人发送邮件

        # 邮件内容：正文+标题
        # 传入Html格式的邮件内容
        mail_content = '''
                    <html><body>
                    <h2>您好</h2>，
                    <p>这是一封使用python登录QQ邮箱发送网页格式带图片邮件的测试</p>,
                    <p>图片演示：</p>,
                    <p><img src="cid:01"></p>
                    </body></html>
                    '''
        mail_title = '发送网页格式带图片邮件测试'

        # 登录smtp服务器并发送邮件
        smtp = SMTP_SSL(smtp_server)
        smtp.ehlo(smtp_server)  # 由客户端发送，指示 ESMTP 会话开始
        smtp.login(sender_qq, password)

        msg = MIMEMultipart('alternative')  # 同时支持HTML和Plain格式
        msg.attach(MIMEText(mail_content, 'html', 'utf-8'))  # 构建邮件对象，指定为html格式，以utf-8编码
        msg['Subject'] = Header(mail_title, 'utf-8')  # 邮件主题中包含中文，需要通过Header对对象进行编码
        msg['From'] = sender_email
        msg['To'] = receiver

        # 指定图片
        img = MIMEImage(open(data_file, 'rb').read())

        # 定义图片ID
        img.add_header('Content-ID', '0')
        msg.attach(img)

        smtp.sendmail(sender_email, receiver, msg.as_string())
        smtp.close()


if __name__ == '__main__':
    e = SendEmail()
    # e.send_email_text()
    # e.send_email_html()
    # e.send_email_mixture(report_file)
    e.send_email_html_img(data_file)



