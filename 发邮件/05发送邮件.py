import smtplib
from email.mime.text  import MIMEText

# 163smtp的服务器地址
mail163Server = "smtp.163.com"
# 163smtp服务器端口号
mail163ServerPort = 25

# 登陆邮箱服务器的用户名
mailUser = "wenyucheng8888@163.com"
# 登陆邮箱服务器的 授权密码
mailPasswd = "1qaz2wsx"

# 发件人
fromMail = "wenyucheng8888@163.com"
# 收件人
toMail = "wenyucheng8888@163.com"


# 设置邮件内容
# 创建一个MimeText对象
mimeText = MIMEText("恭喜您,成功聘用为阿里巴巴首席执行官,年薪xxxxw")
# 主题
mimeText["Subject"] = "入职邀请!"
# 收件人
mimeText["To"] = toMail
# 发件人
mimeText["From"] = fromMail
# mimeText["From"] = "阿里巴巴"




# 连接邮箱服务器,并获得邮箱服务器对象
smtpServer = smtplib.SMTP(mail163Server,mail163ServerPort)

# 登陆邮箱服务器
smtpServer.login(mailUser,mailPasswd)

#发送邮件
# 发件人,收件人,内容
smtpServer.sendmail(fromMail,toMail,mimeText.as_string())

# 关闭连接
smtpServer.close()












