def str_reverse(s):
    """
    逆序字符串
    :param s:接收的字符串
    :return: 逆序后的字符串
    """
    return s[::-1]

def substr(s, x, y):
    """
    字符串切片操作
    :param s: 接收的字符串
    :param x: 起始位置（包括）
    :param y: 结束位置（不包括）
    :return: 切片后的字符串
    """
    return s[x:y]
