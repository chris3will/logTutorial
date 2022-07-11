import logging

if __name__ == '__main__':
    logging.basicConfig(
        filename='easylog.log',
        level=logging.DEBUG
    )
    logging.debug("This is a logging debug")
    logging.info("This is a logging info")
    logging.warning("This is a logging warning")
    logging.error("This is a logging error")
    print("This is a print")



