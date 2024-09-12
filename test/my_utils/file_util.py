def print_file_info(file_name):
    """
    接收传入的文件路径
    打印文件全部内容，如文件不存在则捕获异常，输出提示信息，通过finally关闭文件
    :param file_name: 接收的文件路径
    """
    f = None
    try:
        f = open(file_name,"r",encoding="UTF-8")
        for line in f:
            print(line,end='')
    except FileNotFoundError as fn:
        print(f'文件不存在，错误信息：{fn}')
    finally:
        if f:
            f.close()

def append_to_file(file_name, data):
    """
    接收文件路径以及传入的数据，将数据追加到文件中
    :param file_name: 文件路径
    :param data: 追加的内容
    """
    f = open(file_name,"a",encoding="UTF-8")
    f.write(data)
    f.close()
