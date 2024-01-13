# ./pseudonymizer/privacyPreservingModels.py

from pseudonymizer.pseudonymizer import Pseudonymizer, Pseudonym
    # 가명처리 전후 데이터의 속성을 비교하기 위한 유용성 지표 적용 등에 활용하는 방법 고민
from typing import *
import pandas as pd

class PrivacyPreservingModel:
    """개인식별가능정보 속성을 기준으로 데이터를 그룹화하는 클래스"""
    def __init__(self, dataframe):
        self._dataframe = dataframe
        self.equivalent_class = {}

    def __str__(self):
        """주어진 데이터 셋의 컬럼 정보를 반환하는 메서드"""
        return self._dataframe.info()
    
    def categorizeEquivalentClass(self, attributes: List[str]):
        """각 행(레코드)에 대한 개인식별가능정보 속성(컬럼)들 사이에 동질 집합 확인"""
        # groupby_data = self._dataframe.groupby(attribute)
        # for group, data in groupby_data:
        
        groupby_data = self._dataframe.groupby(attributes)
            # self._dataframe[attributes].groupby( list(range(len(self._dataframe[attributes]))) )
        
        for group, data in groupby_data:
            if len(group) > 1:
                key = tuple(group)
                # 딕셔너리에서 키 값으로 리스트(동적 타입)는 사용할 수 없으므로 튜플로 변환
                self.equivalent_class[key] = data.index.tolist()
                # 동질 집합에 해당하는 행(레코드)의 인덱스 번호를 키 값으로 조회되도록 저장
        
        return self.equivalent_class
        
    # def K_Anonymity(self):
       # """개별 레코드가 최소한 K개 이상의 동일한 속성값을 가지도록 하는 K-익명성 메서드"""
        
    # def L_Diversity(self):
       # """각 동질집합 내 특정 민감 속성의 빈도가 L값 이상의 다양성을 가지도록 하는 L-다양성 메서드"""
    
    # def T_Closeness(self):
       # """민감 정보(SA)의 분포를 전체 데이터 셋의 분포와 유사하도록 하는 T-근접성메서드"""