from pseudonymizer.pseudonymizer import Pseudonymizer
import re
from typing import *

class EmailMaskingModule(Pseudonymizer):
    """
    이메일 마스킹 클래스
    --------------------
    이메일 주소의 메일 발신자 또는 발신기관을 구분할 수 없도록 하는 구체 클래스
    """
    def __init__(self, masking_domain: bool):
        self.masking_domain = masking_domain
        
    def pseudonymizeData(self, email):
        pattern_match = re.match(
            r"^[a-zA-z0-9]([-_\.]?[a-zA-Z0-9])*@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}", email)
            # .: 정확히 1개 문자 매칭
            # * : 앞 패턴이 0개 이상이어야 함
            # ? : 앞 패턴이 없거나 하나이어야 함
            # + : 1회 이상 반복되는 패턴을 매칭
            # \. : 도메인과 최상위 도메인(TLD)에 대한 구분자 마침표 
            # {,} : 중괄호 안에 표기된 범위만큼 반복되는 패턴을 매칭. {3,5}는 3~5회 매칭을 의미함
        if match:
            local_part = pattern_match.group(0)
            domain_part = pattern_match.group(1)
            tld_part = pattern_math.group(2)
            # local_part, domain_part = email.split("@")
            if self.masking_domain:
                masked_local_part = re.sub(r"\S", "*", local_part)
                masked_domain_part = re.sub(r"\S", "*", domain_part)
                return masked_local_part + "@" + masked_domain_part + tld_part
            else:
              # self.masking_domain = False:
                masked_local_part = re.sub(r"\S", "*", local_part)
                return masked_local_part + "@" + domain_part + tld_part

        else:
            print("입력받은 { }은 이메일 패턴에 매칭되지 않아 마스킹할 수 없습니다.".format(email))
    
        # 이메일의 표준은 인터넷 표준 기구(IETF, Internet Engineering Task Force)에서 정의
        # re.sub(pattern, replace, text)
        # @[a-zA-Z0-9]+\.(.[a-zA-Z]{2,3}))