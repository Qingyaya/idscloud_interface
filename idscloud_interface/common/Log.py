# coding:utf-8
import logging, time
import os
from  datetime import datetime
# log_path是存放日志的路径
filepath=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_path = os.path.join(filepath, 'log')


# 如果不存在这个logs文件夹，就自动创建一个
if not os.path.exists(log_path):os.mkdir(log_path)

class Log():
    def __init__(self):
        # 文件的命名
        self.logname = os.path.join(log_path, '%s.log'%time.strftime('%Y_%m_%d'))
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # 日志输出格式
        self.formatter = logging.Formatter('[%(asctime)s] - %(filename)s] - %(levelname)s: %(message)s')

    def __console(self, level, message):
        # 创建一个FileHandler，用于写到本地
        # fh = logging.FileHandler(self.logname, 'a')  # 追加模式  这个是python2的
        fh = logging.FileHandler(self.logname, 'a', encoding='utf-8')  # 这个是python3的
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # 创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
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

    def build_start_line(self, case_no):
        """
        write start line
        :return:
        """
        self.__console('info',"--------" + case_no + " START--------")

    def build_end_line(self, case_no):
        """
        write end line
        :return:
        """
        self.__console('info',"--------" + case_no + " END--------")

    def build_case_line(self, case_name, code, msg):
        """
        write test case line
        :param case_name:
        :param code:
        :param msg:
        :return:
        """
        self.__console('info',case_name+" - Param:"+code+" - msg:"+msg)


    def get_report_path(self):
        """
        get report file path
        :return:
        """
        report_path = os.path.join(filepath, "report")
        if not os.path.exists(report_path):
            os.mkdir(report_path)
        report_path = os.path.join(report_path, str(datetime.now().strftime("%Y%m%d")))
        if not os.path.exists(report_path):
            os.mkdir(report_path)

        report_path = os.path.join(report_path,str(datetime.now().strftime("%Y%m%d%H%M%S"))+'.html')
        return report_path

    def get_result_path(self):
        """
        get test result path
        :return:
        """
        return log_path

    def write_result(self, result):
        """

        :param result:
        :return:
        """
        result_path = os.path.join(filepath, "report.txt")
        fb = open(result_path, "a+")
        try:
            fb.writelines(result)
        except FileNotFoundError as ex:
            self.__console('error',str(ex))



if __name__ == "__main__":
   log = Log()
   name =log.get_data_name(os.path.abspath(__file__))
   print(name)