# ./pseudonymizer/pseudonymizer/deidentificationTechnique/lDiversity.py

from pseudonymizer.pseudonymizer.deidentificationTechnique.equivalent_class import EquivalentClass
from typing import *

class L_Diversity(EquivalentClass):
    """각 동질집합 내 특정 민감 속성의 빈도가 L값 이상의 다양성을 가지도록 하는 L-다양성 클래스
    
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
    pass