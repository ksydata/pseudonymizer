# ./pseudonymizer/privacyPreservingModels.py

from pseudonymizer.pseudonymizer import Pseudonymizer, Pseudonym
    # 가명처리 전후 데이터의 속성을 비교하기 위한 유용성 지표 적용 등에 활용하는 방법 고민
from typing import *
import pandas as pd

class PrivacyPreservingModel:
    """
    동질 집합(Equivalent class)
    프라이버시 보호 모델에 따른 PPDM(Privacy Preserving Data Mining)
    ----------------------------------------------------------------
    개인식별가능정보 속성을 기준으로 데이터를 그룹화하여 프라이버시 보호 모델을 적용하는 클래스
    """
    def __init__(self, dataframe):
        self._dataframe = dataframe
        # self.pseudo_dataframe = pseudo_dataframe
        # 가명처리 전이면 pseudo_dataframe = None
        self.equivalent_class = [] # {}
        # 동질 집합을 저장할 딕셔너리 / 리스트를 초기화
        
    def __str__(self):
        """주어진 데이터 셋의 컬럼 정보를 반환하는 메서드"""
        return self._dataframe.info()
    
    def categorizeEquivalentClass(self, attributes: List):
        # -> Dict[str, List[str]]:
        """각 행(레코드)에 대한 개인식별가능정보 속성(컬럼)들 사이에 동질 집합 확인"""
        # groupby_data = self._dataframe.groupby(attribute)
        # for group, data in groupby_data:
        
        groupby_data = self._dataframe[attributes].groupby(list(range(
            len(self._dataframe[attributes]))))
        for _, group in groupby_data:
            if len(group) > 1:
                self.equivalent_class.append(
                    group.index.tolist())
        return self.equivalent_class
    
    def K_Anonymity(self):
        """각 동질 집합 내 개별 레코드가 최소한 K개 이상의 동일한 속성값을 가지도록 하는 K-익명성 메서드"""
        
        
    def L_Diversity(self):
        """각 동질 집합 내 특정 민감 속성의 빈도가 L값 이상의 다양성을 가지도록 하는 L-다양성 메서드"""
        
    
    def T_Closeness(self):
        """민감 정보(SA)의 분포를 전체 데이터 셋의 분포와 유사하도록 하는 T-근접성 메서드"""
        
        