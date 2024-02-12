from pseudonymizer.pseudonymizer import Pseudonymizer
from datetime import datetime

class CategorizationOfNumeric(Pseudonymizer):
    """수치(연속형) 데이터를 임의의 수를 기준으로 범위(범주형)으로 설정하는 가명처리기법 구체클래스 """
    def __init__(self, numeric_type):
        self.numeric_type = numeric_type
    
    def pseudonymizeData(self, input_numeric: float, grouping_standard):
        """식별성이 높은 그룹을 하나로 묶는 메서드"""
        if self.numeric_type == "age":
            return self.pseudonymizeAge(input_numeric, grouping_standard)
        elif self.numeric_type == "income":
            return self.pseudonymizeIncome(input_numeric, grouping_standard)
        elif self.numeric_type == "amount":
            return self.pseudonymizeAmount(input_numeric, grouping_standard)
        elif self.numeric_type == "user_definition":
            return self.pseudonymizeDefinition(input_numeric, grouping_standard)
        else: 
            pass
    
    def pseudonymizeAge(self, birthdate, grouping_standard):
        """연령 범주화 메서드
        일반적으로 나이 + 주소 + 성별 조합(동질 집합)이 재식별 가능성 있으므로
        5세, 10세 단위 또는 초중후반으로 나이 범주화"""
        pass
        
    def pseudonymizeIncome(self, income, grouping_standard):
        """소득금액 범주화 메서드
        소득을 전체 대상자를 20분위(보험료 분위)로 균등 분할"""
        pass
    
    def pseudonymizeAmount(self, amount, grouping_standard):
        """기타 금액 범주화 메서드
        신용공여금액(예: 한도/건별대출, 담보대출, 리스/카드할부금융서비스 등)의 일정 급간화
        개인사업자의 추청매출액/평당월임대료를 백분위수에 따라 매출등급화(90~100%, 65~90%, 35~65%, 10~35%, 0~10%)
        """
        pass
        
    def pseudonymizeDefinition(self, numeric_tobeclassified. category_mapping: dict):
        pass