

from common.testdata_utils import TestdataUtils
from common.requests_utils import RequestUtils

#使用excel数据驱动 requests_utils


all_case_info=TestdataUtils().def_testcase_data_list()
# case_info=all_case_info[1].get('case_info')


for case_info in all_case_info:
    RequestUtils().request_by_step(case_info.get('case_info'))
