from pseudonymizer.pseudonymizer import Pseudonymizer
from datetime import datetime

class CategorizationOfColumn(Pseudonymizer):
    """수치(연속형) 데이터를 임의의 수를 기준으로 범위(범주형)으로 설정하는 가명처리기법 구체클래스 """
    def __init__(self, numeric_type):
        self.numeric_type = numeric_type
    
    def pseudonymizeData(self, input_numeric: float, grouping_standard):
        """식별성이 높은 그룹을 하나로 묶는 메서드"""
        if self.numeric_type == "bin":
            return self.pseudonymizeAmountbyBin(input_numeric, grouping_standard)
        elif self.numeric_type == "pct":
            return self.pseudonymizeAmountbyPct(input_numeric, grouping_standard)        
        else: 
            raise ValueError(f"{self.numeric_type}은 유효한 범주화 기법 적용 유형이 아닙니다.")
    
    def pseudonymizeAmountbyBin(self, amount, grouping_standard):
        """기타 금액 구간별 범주화 메서드
        신용공여금액(예: 한도/건별대출, 담보대출, 리스/카드할부금융서비스 등)의 일정 급간화
        다만, pd.cut과의 차별점 없으며, pandas 내장 함수를 활용하여 범주화하는 것이 훨씬 효율적
        """
        pass
        
    def pseudonymizeAmountbyPct(self, amount, grouping_standard):
        """기타 금액 백분위에 의한 범주화 메서드
        개인사업자의 추청매출액/평당월임대료를 백분위수에 따라 매출등급화(90~100%, 65~90%, 35~65%, 10~35%, 0~10%)
        개별 행을 바라보고 가명처리기법을 적용하는 객체에 적합한 메서드인지 의문
        """
        pass
        
    def pseudonymizeDefinition(self, numeric_tobeclassified, category_mapping: dict):
        for category, interval in category_mapping.items():
            if not isinstance(interval, tuple) or len(interval) != 2:
                return f"유효하지 않은 구간 {interval}입니다."
            
            lower, upper = interval # tuple(lower, upper)
            if lower <= numeric_tobeclassified <= upper:
                return category
        return "other types"