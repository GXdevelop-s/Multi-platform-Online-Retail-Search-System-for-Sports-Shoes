import hashlib
from django.conf import settings


def md5(data_string):
    # 创建一个md5对象，并用secretKEY转换的字符串作为盐值
    obj = hashlib.md5(settings.SECRET_KEY.encode('utf-8'))
    # 将字符串编码为字节类型，并用update方法将字符串添加到哈希对象中
    obj.update(data_string.encode('utf-8'))
    # hexdigest可以获取哈希计算后的结果，会输出一个十六进制的字符串
    return obj.hexdigest()
