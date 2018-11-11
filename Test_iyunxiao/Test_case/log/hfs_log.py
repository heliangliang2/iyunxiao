
# coding:utf-8
import logging,time,os
# 这个是日志保存本地的路径
log_path = "C:\\Users\\Administrator\\Desktop\\iyunxiao\\iyunxiao\\Test_iyunxiao\\Test_case\\log"
class loger2:
    def __init__(self):
        # 文件的命名
        self.logname = os.path.join(log_path,'%s.log'%time.strftime('%Y_%m_%d_%H_%M_%S'))
        # self.logname = os.path.join(log_path,'%s.log')
        self.loger2 = logging.getLogger()
        self.loger2.setLevel(logging.DEBUG)
        # 日志输出格式
        self.formatter = logging.Formatter('[%(asctime)s] - %(filename)s[line:%(lineno)d] - fuc:%(funcName)s- %(levelname)s: %(message)s')
    def __console(self, level, message):
        # 创建一个FileHandler，用于写到本地
        fh = logging.FileHandler(self.logname, 'a')  # 追加模式
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.loger2.addHandler(fh)
        # 创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.loger2.addHandler(ch)
        if level == 'info':
            self.loger2.info(message)
        elif level == 'debug':
            self.loger2.debug(message)
        elif level == 'warning':
            self.loger2.warning(message)
        elif level == 'error':
            self.loger2.error(message)
        # 这两行代码是为了避免日志输出重复问题
        self.loger2.removeHandler(ch)
        self.loger2.removeHandler(fh)
        # 关闭打开的文件
        fh.close()

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)

if __name__ == "__main__":
   loger2 = loger2()