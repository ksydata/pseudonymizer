# ./pseudonymizer/pseudonymizer/deidentificationTechnique/equivalent_class.py

from typing import *

class EquivalentClass:
    """개인식별가능정보 속성을 기준으로 데이터를 그룹화하는 부모 클래스
    
    준식별자를 이용한 그룹화 기법 의사코드
    --------------------------------------
    data grouping using quasi-identifier
    Input : PI(Personal Information)
    Output : Grouped PI

    grouped_PI = dict()
    for identifier, quasi in PI.items():
        key = quasi[0] + quasi[1] + quasi[2] + quasi[3]
        if key in grouping_PI:
            grouping_PI[key].append(identifier)
        else:
            grouping_PI[key] = []
            grouping_PI[key].append[identifier]

        return grouping_PI
    """
    def __init__(self, dataframe):
        self._dataframe = dataframe
        self.equivalent_class = {}

    def __str__(self):
        """캡슐화된 데이터셋의 속성(컬럼)정보를 반환하는 메서드"""
        return self._dataframe.info()
    
    def categorizeEquivalentClass(self, attributes: List[str]):
        """각 행(레코드)에 대한 개인식별가능정보 속성(컬럼)들 사이에 동질 집합을 확인하는 메서드"""
        groupby_data = self._dataframe.groupby(attributes)
        
        for group, data in groupby_data:
            if len(group) > 1:
                key = tuple(group)
                # 딕셔너리에서 키 값으로 리스트(동적 타입)는 사용할 수 없으므로 튜플로 변환
                self.equivalent_class[key] = data.index.tolist()
                # 동질 집합에 해당하는 행(레코드)의 인덱스 번호를 키 값으로 조회되도록 저장

    def removeDuplicatesInEquivalentClass(self):
        """각 동질집합 내 레코드 간 중복된 행을 제거하는 메서드"""
        for group_key, index_value in self.equivalent_class.items():
            unique_record = self._dataframe.loc[index_value, :].drop_duplicates()
            # set(self._dataframe.loc[index_value, :])
            self.equivalent_class[group_key] = unique_records.index.tolist()