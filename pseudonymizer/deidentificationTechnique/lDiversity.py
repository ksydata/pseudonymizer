# ./pseudonymizer/pseudonymizer/deidentificationTechnique/lDiversity.py

from pseudonymizer.deidentificationTechnique.equivalentClass import EquivalentClass
from typing import *
from pseudonymizer.deidentificationTechnique.kAnonymity import K_Anonymity

class L_Diversity(K_Anonymity):
    """각 동질집합 내 특정 민감 속성의 빈도가 L값 이상의 다양성을 가지도록 하는 L-다양성 클래스
    k-익명성 보호 모델 적용 결과에 l-다양성 보호 모델을 적용
    
    k-익명성 처리가 그룹 단위로 구현된 상황에서 l-다양성 알고리즘 의사코드
    ----------------------------------------------------------------------
    basic l-diversity algorithm
    Input : k_data, limited_l
    Output : l_data
    
    l_data = dict()
    for key, identifiers in k_data.items():
        l_list = []
        for identifier in identifiers:
            # k익명성을 만족하는 데이터의 식별자값을 가지고 
            user_info = data[identifier]
            # 해당 식별자값의 민감정보를 가져오는 부분
            user_sa = user_info[4]
            if user_sa in l_list:
                pass
    """
    def __init__(self, dataframe):
        """모듈의 유연성을 제공하기 위해 K익명성 클래스를 확장하여 손자 클래스로 정의"""
        super().__init__(dataframe)
        self.L_data = None
        self.sensitive_attribute = None
        self.LocalL_data = None
        
    def applyLDiversity(self, K: int, L: int, attributes: List[str], sensitive_attribute: str):
        """두 모형을 동시에 적용할 경우 중복이 발생할 가능성이 높아 조합적인 보호 모델을 설계하여 중복을 최소화하는 메서드"""
        super().applyKAnonymity(K, attributes)
        L_data = dict()
        self.sensitive_attribute = sensitive_attribute
        
        for group_key, index_value in self.K_data.items():
            unique_sensitive_values = self._dataframe.loc[index_value, 
                                                          sensitive_attribute].unique()
            # self._dataframe.iloc[index_value, self._dataframe.columns.get_loc(column_name)]
            if len(unique_sensitive_values) >= L:
                L_data[group_key] = index_value
            else:
                print(group_key, len(unique_sensitive_values))
        self.L_data = L_data
    
    def applyLocalLDiversity(self, local_L: int):
        """특정 민감정보의 속성값이 일부 레코드(행)에 집중되는 문제에 따라
        전체적으로 안전한 다양성을 확보할 수 있도록 l-로컬 다양성을 적용하는 메서드"""
        LocalL_data = dict()
        
        for group_key, index_value in self.L_data.items():
            count_local_diversity = self._dataframe.loc[index_value, self.sensitive_attribute].value_counts()
            if count_local_diversity.min() >= local_L: 
                LocalL_data[group_key] = index_value
            else:
                for sensitive_attr, freq in count_local_diversity.items():
                    if freq == count_local_diversity.min():
                        print(group_key, sensitive_attr, freq)
                    else:
                        pass
        self.LocalL_data = LocalL_data