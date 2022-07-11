import logging
import sys

if __name__ == '__main__':
    # 输出格式
    format = "%(asctime)s - %(levelname)s - %(message)s - %(filename)s"
    # 日期格式
    date_FORMAT = "%m/%d/%Y %H:%M:%S %p"
    # 我们主动创建不同的句柄来服务不同的需求
    # 文件句柄
    file_handler = logging.FileHandler('easylog_multihandlers.log')
    # 流句柄，我们以标准形式输出
    stream_handler = logging.StreamHandler(sys.stdout)
    # 我们仅仅打印INFO及其以上的内容
    stream_handler.setLevel(logging.INFO)

    logging.basicConfig(
        level=logging.ERROR,
        format=format,
        datefmt=date_FORMAT,
        handlers=[
            file_handler,
            stream_handler
        ]
    )
    logging.debug("This is a logging debug")
    logging.info("This is a logging info")
    logging.warning("This is a logging warning")
    logging.error("This is a logging error")
    print("This is a print")