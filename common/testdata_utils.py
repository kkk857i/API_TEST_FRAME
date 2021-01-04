
import os
from common.excel_utils import ExcelUtils
from common import config
from common.localconfig import local_config

current_path=os.path.dirname(__file__)
test_data_path=os.path.join(current_path,'..',local_config.CASE_DATA_PATH)

class TestdataUtils():
    def __init__(self,test_data_path=test_data_path):
        self.test_data_path=test_data_path
        self.test_data=ExcelUtils(test_data_path,'Sheet1').get_sheet_data_by_dict()

    def __get_testcase_data_dict(self):
        testcase_dict={}
        for rwo_data in self.test_data:
            testcase_dict.setdefault(rwo_data['测试用例编号'],[]).append(rwo_data)
        return testcase_dict

    def def_testcase_data_list(self):
        testcase_list=[]
        for k,v in self.__get_testcase_data_dict().items():
            one_case_dict={}
            one_case_dict['case_name']=k
            one_case_dict['case_name']=v
            testcase_list.append(one_case_dict)
        return testcase_list


if __name__=="__main__":
    testdataUtils=TestdataUtils()
    for i in testdataUtils.def_testcase_data_list():
        print(i)