# coding:utf-8

import logging
import logging.handlers
import os.path
import sys
import time

'''
一个自定义的logging模板
为项目开发调试过程的检错定位等提供便利
20220628
chris

DEBUG < INFO < WARNING < ERROR < CRITICAL
'''

LOG_FORMAT = logging.Formatter("%(asctime)s - %(name)s% - %(levelname)%s - %(message)s")
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"


class loggerClass:
    def __init__(self, name='myLogger', loglevel='WARNING', save=True, save_level=logging.WARNING,
                 log_path=None, update_frequency='D', save_interval=1):
        """
        初始化自定义loggerClass类
        :param name: logger的名称，会在控制台与log文件中输出
        :param loglevel: 该logger的等级，控制台中只会输出不低于该等级的log信息
        :param save: 是否利用文件句柄进行处理
        :param save_level: 进行存储的日志级别
        :param log_path: 日志存储路路径
        :param update_frequency: 日志更新频率，针对第三类
        :param save_interval: 日志存储间隔
        """
        self.log_path = log_path
        self.name = name
        self.loglevel = loglevel  # 输入的字符串
        self.log_level = None  # 用来判断的标记位
        self.save = save
        self.save_level = save_level
        # 先初始化自定义根logger的名称
        self.logging = logging
        self.log_format = LOG_FORMAT
        self.date_format = DATE_FORMAT
        self.update_frequency = update_frequency
        self.save_interval = save_interval

    def init_streamHan(self, formatter):
        streamHandler = self.logging.StreamHandler(sys.stdout)
        streamHandler.setLevel(self.log_level)
        streamHandler.setFormatter(formatter)
        return streamHandler

    def init_fileHan(self, formatter, log_file_name='mylog.log'):
        fileHandler = self.logging.FileHandler(log_file_name)
        fileHandler.setLevel(self.save_level)
        fileHandler.setFormatter(formatter)
        return fileHandler

    def init_rotatingfileHan(self, formatter, log_file_name='mylog.log'):
        '''
        :param formatter: 格式化模板
        :param log_file_name: 存储在logs目录中的日志名称
        :return: None
        '''
        fh = self.logging.handlers.RotatingFileHandler(
            filename=log_file_name,
            mode='a',
            maxBytes=100,  # 268435456Bytes = 256MB
            backupCount=7  # 允许的备份文件数上限
        )
        fh.setLevel(self.save_level)
        fh.setFormatter(formatter)
        return fh

    def init_timerotatingfileHan(self, formatter, log_file_name='mylog.log'):
        """
        返回一个按照时间自动分割日志文件的句柄
        :param formatter: 格式化目标
        :param log_file_name:日志文件名
        :param update_frequency:分割周期
        :return:
        """
        fh = self.logging.handlers.TimedRotatingFileHandler(
            filename=log_file_name,
            when=self.update_frequency,
            interval=self.save_interval,
            backupCount=7
        )
        fh.setLevel(self.save_level)
        fh.setFormatter(formatter)
        return fh

    def init_logger(self, fh_type='1'):
        """
        fh_type: 需求的filehandler的类型，1 为普通的文件句柄，2 为
        :return: 满足需求的自定义logger
        """
        if self.loglevel == "DEBUG":
            self.log_level = self.logging.DEBUG
        elif self.loglevel == 'INFO':
            self.log_level = self.logging.INFO
        elif self.loglevel == "WARNING":
            self.log_level = self.logging.WARNING
        elif self.loglevel == "ERROR":
            self.log_level = self.logging.ERROR
        else:
            self.log_level = self.logging.CRITICAL

        # 定义格式化工具
        formatter = self.logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

        # 创建logger
        logger = self.logging.getLogger(self.name)
        logger.setLevel(self.log_level)

        # 注意避免句柄的重复创建
        # if not self.logger.handlers:
        logger.addHandler(self.init_streamHan(formatter))

        if self.save:
            log_file = os.path.join(self.log_path, self.name + '.log')
            # 需要保存，我们启用其文件模块
            if not os.path.exists(self.log_path):
                os.mkdir(self.log_path)
            if not os.path.exists(log_file):
                os.system(r"touch {}".format(log_file))

            if fh_type == '1':
                fh = self.init_fileHan(formatter, log_file)
                logger.addHandler(fh)
            elif fh_type == '2':
                fh = self.init_rotatingfileHan(formatter, log_file)
                logger.addHandler(fh)
            elif fh_type == '3':
                fh = self.init_timerotatingfileHan(formatter, log_file)
                logger.addHandler(fh)

        return logger


if __name__ == '__main__':
    # 我们首先要接收参数
    try:
        print("参数个数:{}".format(len(sys.argv)))
        print("参数列表:{}".format(str(sys.argv)))
        print("脚本名称：{}".format(sys.argv[0]))
        for item in range(1, len(sys.argv)):
            print("参数 {} 为： {}".format(item, sys.argv[item]))
    except Exception as err:
        print(err)

    mylogger = loggerClass("the_logger", "DEBUG", True, logging.WARNING, "logs").init_logger('3')
    mylogger.debug("hi")
    mylogger.info("my word tes1t")
    mylogger.warning("how are you")
    # logger.warning("my word test")
