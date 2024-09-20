"""
从文件中读取数据
并将数据转换为列表类型，列表内为自定义的Source类型
"""
import json

from data_type import Source

# 父类
class FileReader:

    def file_reader(self):
        pass

# 子类实现
class TextFileReader(FileReader):

    # 接收文件路径
    def __init__(self, path):
        self.path = path

    # 解析文件内容
    def file_reader(self) -> list[Source]:
        data_list: list[Source] = []

        f = open(self.path, "r", encoding='UTF-8')
        """将每一行数据读取并分隔，将一行的数据整理为Source类型，都放到一个列表里"""
        for line in f.readlines():
            line = line.strip()
            tmp_list = line.split(",")
            data_list.append(Source(tmp_list[0], tmp_list[1], int(tmp_list[2]), tmp_list[3]))
        f.close()

        return data_list


class JsonFileReader(FileReader):

    # 接收文件路径
    def __init__(self, path):
        self.path = path

    # 解析文件内容
    def file_reader(self) -> list[Source]:
        data_list: list[Source] = []

        f = open(self.path, "r", encoding='UTF-8')
        """将每一行数据读取并分隔，将一行的数据整理为Source类型，都放到一个列表里"""
        for line in f.readlines():
            data_dict = json.loads(line)
            tmp = Source(data_dict["date"], data_dict["order_id"], int(data_dict["money"]), data_dict["province"])
            data_list.append(tmp)
        f.close()

        return data_list


if __name__ == "__main__":
    text1 = TextFileReader("D:/Python_Data/sale/2011年1月销售数据.txt")
    source1 = text1.file_reader()

    json1 = JsonFileReader("D:/Python_Data/sale/2011年2月销售数据JSON.txt")
    source2 = json1.file_reader()
