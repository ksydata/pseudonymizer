from pseudonymizer.pseudonymizer import Pseudonymizer
from typing import *

class PhoneNumberMaskingModule(Pseudonymizer):
    """
    연락처(휴대전화번호 혹은 일반전화번호) 마스킹 클래스
    --------------------
    3번째 자리를 복원할 수 없는 비가역성 기법으로 개인의 식별을 방지하는 구체 클래스
    특히 연관된 다른 정보(생년월일, 기념일, 가족 전화번호, 기존 통화내역 등)와 쉽게 결합하여 사용자가 누구인지 식별가능하다는 점에서 개인정보에 해당함
    """   
    def pseudonymizeData(self, phone_number):
        """전화번호의 정규표현식을 기준으로 패턴 매칭이 되는 경우 마스킹을 수행하는 메서드"""
        pattern_match = re.match(r"^\[0-9]-\[0-9]-\d{4}$", phone_number)
        
        if pattern_match:
            front_part, middle_part, rear_part = phone_number.split("-")
            return front_part + middle_part + "*"*4
        # 다만, 전화번호 마지막 4자리는 ****와 같은 기호로 대체하지 않고 전체를 해시값으로 암호화하기도 한다는 점에 유의하여야 함
        # 암호화와 복호화는 알고리즘 및 키 관리 등 복잡한 과정이 필요하므로 높은 보안이 필요한 경우 고려함
        else:
            print("입력받은 { }은 전화번호 패턴에 매칭되지 않아 마스킹할 수 없습니다.".format(phone_number))
            