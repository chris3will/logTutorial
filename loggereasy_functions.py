import logging
import sys

# 输出格式
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")


def init_logger(logger_name='myLogger'):
    '''
    直接引入logging，创建一个对象
    :return:
    '''
    # 创建一个logger，名称为logger_name
    logger = logging.getLogger(logger_name)
    # 我们设定logger的默认级别
    logger.setLevel(logging.DEBUG)

    # 需要先判断句柄是否已经被创建，如果当前句柄为空，则可以添加。这样可以句柄被重复创建，语句多次执行的问题。
    if not logger.handlers:
        logger.addHandler(init_fileHd(formatter))
        logger.addHandler(init_streamHd(formatter))

    return logger


def init_streamHd(myformatter):
    streamHandler = logging.StreamHandler(sys.stdout)
    streamHandler.setLevel(logging.INFO)
    streamHandler.setFormatter(myformatter)
    return streamHandler


def init_fileHd(myformatter, log_file_name='easylog_functions.log'):
    fileHandler = logging.FileHandler(log_file_name)
    fileHandler.setLevel(logging.DEBUG)
    fileHandler.setFormatter(myformatter)
    return fileHandler


if __name__ == '__main__':
    mylogger = init_logger("myLogger")

    mylogger.debug("This is a logging debug")
    mylogger.info("This is a logging info")
    mylogger.warning("This is a logging warning")
    mylogger.error("This is a logging error")
    print("This is a print")
