
import os
import time
import logging
from common.localconfig_utils import local_config

currnet_path=os.path.dirname(__file__)
log_output_path=os.path.join(currnet_path,'..',local_config.LOG_PATH)

class LoUtils():
    def __init__(self,log_path=log_output_path):
        self.log_name=os.path.join(log_output_path,'ApiTest_%s.log'%time.strftime('%Y_%m_%d'))
        self.logger=logging.getLogger('ApiTestlog')
        self.logger.setLevel(local_config.LOG_LEVEL)

        console_handler = logging.StreamHandler()  # 控制台输出
        file_tandler=logging.FileHandler(self.log_name,'a',encoding='utf-8')    #文件输出
        fromatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
        console_handler.setFormatter(fromatter)
        file_tandler.setFormatter(fromatter)

        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_tandler)

        console_handler.close() #防止日志打印重复
        file_tandler.close()

    def get_logger(self):
        return self.logger

logger=LoUtils().get_logger()   #防止日志打印重复

if __name__=='__main__':
    logger.info('hello')