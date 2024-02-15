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
        elif self.numeric_type == "user_definition":
            return self.pseudonymizeDefinition(input_numeric, grouping_standard)
        else: 
            raise ValueError(f"{self.numeric_type}은 유효한 범주화 기법 적용 유형이 아닙니다.")
    
    def pseudonymizeAge(self, birthday, grouping_standard):
        """연령 범주화 메서드
        일반적으로 나이 + 주소 + 성별 조합(동질 집합)이 재식별 가능성 있으므로
        5세, 10세 단위 또는 초중후반으로 만 나이 범주화"""
        currentdate = datetime.now().date()
        if (currentdate.month, currentdate.day) < (birthday.month, birthday.day):
        # 아직 현재 날짜가 생일 전인 경우 만 나이 계산 시 한 살 제외
            age = currentdate.year - birthday.year - 1
        else:
            age = currentdate.year - birthday.year
        
        if grouping_standard in ["3bin", "5bin", "10bin"]:
            if grouping_standard == "3bin":
            # 0,1,2(초반) / 3,4,5,6(중반) / 7,8,9(후반)
                sort = (age % 10) // 3
                range = (age // 10) * 10
                if sort == 0:
                    return f"{range}대 초반"
                elif sort == 1:
                    return f"{range}대 중반"
                elif sort == 2:
                    return f"{range}대 후반"
                else: 
                    return
            elif grouping_standard == "5bin":
            # 0,1,2,3,4(초반) / 5,6,7,8,9(후반)
                return f"{(age // 10) * 10}대 초반" if (age % 10) < 5 else f"{(age // 10) * 10}대 후반"
            elif grouping_standard == "10bin":
            # 10대~100대
                return f"{(age // 10) * 10}대"
            else:
                raise ValueError("입력받은 {}은 연령 범주화 기준으로 유효하지 않습니다.".format(grouping_standard))
        
    def pseudonymizeIncome(self, income, grouping_standard):
        """소득금액 범주화 메서드
        소득을 전체 대상자를 9분위(2024년 건강보험료 1인 기준 소득분위)로 균등 분할"""
        if grouping_standard is None:
            threshold_list= [1841500, 2025500, 2675000, 2897000, 3120000, 3343000, 3566000, 3789000, 4012000]
            for index, threshold in enumerate(threshold_list, start = 1):
                if income <= threshold:
                    return f"{index}분위"
        else:
        # While grouping_standard True:
            grouping_standard.sort()
            # 오름차순 정렬 시 일반적으로 사용하는 버블 정렬은 O(N**2)이므로 
            # 시간복잡도 낮추려면 병합 정렬 O(NlogN) 활용 -> 추후 merge_sort() 메서드 적용하여 리팩토링
            for index, grouping_standard in enumerate(grouping_standard, start = 1):
                if income <= grouping_standard:
                    return f"{index}분위"
            
    def pseudonymizeDefinition(self, numeric_tobeclassified, category_mapping: dict):
        """사용자가 직접 구간을 설정하도록 하는 범주화 메서드
        intervals: [(0, 1000), (1000, 5000), (5000, 10000)]
        """
        for category, interval in category_mapping.items():
            if not isinstance(interval, tuple) or len(interval) != 2:
                return f"유효하지 않은 구간 {interval}입니다."
            
            lower, upper = interval # tuple(lower, upper)
            if lower <= numeric_tobeclassified <= upper:
                return category
        return "other types"