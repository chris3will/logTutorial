import logging

if __name__ == '__main__':
    # 输出格式
    format = "%(asctime)s - %(levelname)s - %(message)s - %(filename)s"
    # 日期格式
    date_FORMAT = "%m/%d/%Y %H:%M:%S %p"
    logging.basicConfig(
        filename='easylog_format.log',
        format=format,
        datefmt=date_FORMAT,
        level=logging.DEBUG
    )
    logging.debug("This is a logging debug")
    logging.info("This is a logging info")
    logging.warning("This is a logging warning")
    logging.error("This is a logging error")
    print("This is a print")



