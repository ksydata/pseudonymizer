from pseudonymizer.pseudonymizer import Pseudonymizer
from typing import *

class BusinessNumberMaskingModule(Pseudonymizer):
    """
    사업자등록번호 마스킹 클래스
    --------------------
    사업자등록번호의 일부(2번째 혹은 3번째 자리)를 복원할 수 없는 비가역성 기법으로 개인의 식별을 방지하는 구체 클래스
    """
    def __init__(self, masking_part: str):
        self.masking_part = masking_part
        
    def pseudonymizeData(self, business_number):
        """한국 사업자등록번호의 정규표현식을 기준으로 패턴 매칭이 되는 경우 마스킹을 수행하는 메서드"""
        pattern_match = re.match(r"^\d{3}-\d{2}-\d{5}$", business_number)
        # ex) 124-86-23875
        
        if pattern_match:
            front_part, middle_part, rear_part = business_number.split("-")
            
           # 2번째 자리인 법인의 등록지역을 마스킹할 때
            if self.masking_part == "middle":
                return front_part + "*"*2 + rear_part
           # 3번째 자리인 법인의 일련번호를 마스킹할 때
            elif self.masking_part == "rear":
                return front_part + middle_part + "*"*5
           # 1번째 자리인 법인의 유형만을 남기고 마스킹할 때
            elif self.masking_part == "both":
                return front_part + "*"*2 + "-" + "*"*5
        else:
            print("입력받은 { }은 사업자등록번호 패턴에 매칭되지 않아 마스킹할 수 없습니다.".format(business_number))
            