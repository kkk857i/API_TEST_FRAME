
import logging

logger=logging.getLogger('logger')
logger.setLevel(10)  #10，20，30，40，50
handler1=logging.StreamHandler()    #控制台
logger.setLevel(10)
fromatter=logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
handler1.setFormatter(fromatter)
logger.addHandler(handler1)

handler2=logging.FileHandler('./test.log','a',encoding='utf-8')
handler2.setLevel(10)
handler2.setFormatter(fromatter)
logger.addHandler(handler2)

logger.info('hello')
