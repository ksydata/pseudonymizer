from pseudonymizer.pseudonymizer import Pseudonymizer
from typing import *

class RandomRoundingPseudonymizer(Pseudonymizer):
    """
    랜덤라운딩 구체 클래스
    ----------------------
    데이터의 길이가 일정하지 않은 경우 값의 크기에 따라 처리 단위를 다르게 올림, 내림, 반올림하는 가명처리기법"""
    def __init__(self, rounding_type):
        self.rounding_type = rounding_type
        
    def pseudonymizeData(self, numeric):
        """수치데이터를 실제 수 기준으로 자릿수 올림 또는 내림하여 일반화(범주화)하는 메서드"""
        if self.rounding_type == "round_up":
            return numeric if numeric == int(numeric) else int(numeric)+1
        elif self.rounding_type == "round_down":
            return int(numeric)
        elif self.rounding_type == "round":
            decimal_part = numeric - int(numeric)
            return int(numeric)+1 if decimal_part >= 0.5 else int(numeric)
        else:
            raise ValueError("입력받은 {}은 유효한 라운딩 방법이 아닙니다.".format(rounding_type))
