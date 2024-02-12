from pseudonymizer.pseudonymizer import Pseudonymizer
from datetime import datetime

class CategorizationOfCharacter(Pseudonymizer):
    """문자형으로 저장된 정보에 대하여 상위의 개념으로 범주화하는 가명처리기법 구체클래스"""    
    def __init__(self, category_type: str):
        self.category_type = category_type
    
    def pseudonymizeData(self, input_string: str, category_mapping: dict):
        """식별성이 높은 그룹을 하나로 묶는 메서드
        일반적으로 나이 + 주소 + 성별 조합(동질 집합)이 재식별 가능성 있음
        주소 | 시군구만 남기고 읍면동 단위 삭제
        
        입력값
        ------
        실행 클래스 Pseudonym 자체에서 열 벡터 자체가 아닌 **특정 열의 개별 레코드 형태**로 
        입력받아 가명처리 기법을 적용하므로 별도로 자료형으로 제약 요건을 두지 아니함
        입력값을 특정 범주로 분류하기 위한 전제 조건
        : 실행 클래스에 범주 파악을 위한 Counter함수 적용하는 메서드 정의해야 함
        
        출력값
        ------
        조건에서 정의한 특정속성의 개별레코드별 그룹값 할당
        """
        if self.category_type == "date":
            return self.pseudonymizeDate(input_string)
        elif self.category_type == "user_definition":
            return self.pseudonymizeDefinition(input_string, category_mapping)
        else:
            raise ValueError(f"{self.category_type}은 유효한 범주화 기법 적용 유형이 아닙니다.")
    
    def pseudonymizeDate(self, date_time):
        """개인과 관련된 날짜 정보(자격 취득일짜, 합격일 등)는 연 단위로 처리"""
        if isinstance(date_time, datetime):
            # datetime.datetime객체일 경우 날짜 문자열로 반환
            date_time = date_time.strftime("%Y-%m-%d")
        try:
            date = datetime.strptime(date_time, "%Y-%m")
            # 연월만 남기고 일시 삭제
            return date.strftime("%Y-%m")
        except ValueError:
            return f"{datetime}은 유효한 날짜 형식이 아닙니다."
    
    def pseudonymizeDefinition(self, string_tobeclassified, category_mapping: dict):
        """직접 특정 범주에 속하는 문자열 리스트를 딕셔너리 키, 값으로 입력
        서울특별시 141,704개의 고유필지 → 2023년 기준 서울특별시 1,650개의 골목상권코드으로 그룹핑할 수 있도록 유형화
        코스피 상장주식회사 종목 810개 → 24개 업종 분류로 범주화"""
        for category, string_list in self.category_mapping.items():
            # key는 범주이면서 value는 문자열 리스트일 때
            if string_tobeclassified in string_list: 
                # 입력받은 문자열이 for루프에 걸린 문자열 리스트의 원소인 경우 해당 범주형 반환
                # 접근 연산 시간복잡도를 줄이기 위한 시도는?
                # 현재의 배열과 같이 링크드 리스트의 경우 원하는 노드에 접근하는 시간은 몇 번째 인덱스인지에 비례
                return category
            return "other types"
            # 없으면 기타