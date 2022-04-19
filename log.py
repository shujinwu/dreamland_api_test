import logging
import time

# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s - %(funcName)s - %(message)s',
#     datefmt  = '%Y-%m-%d %A %H:%M:%S'
# )
logger = logging.getLogger()
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(funcName)s - %(message)s')
console.setFormatter(formatter)
logger.addHandler(console)


def loginfo(func):
    # @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = int(time.time())
        logger.info(f'==========开始执行{func.__name__}==========')
        try:
            # request_header = ''
            # request_data = ''
            # respone = ''
            end_time = int(time.time())
            Duration = end_time - start_time
            logger.info(f'执行耗时{Duration}ms')
        except Exception as e:
            logger.error(repr(e))
            raise e
        logger.info(f'=========={func.__name__}执行完毕==========')
    return wrapper

