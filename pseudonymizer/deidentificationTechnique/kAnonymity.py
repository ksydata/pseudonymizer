# ./pseudonymizer/pseudonymizer/deidentificationTechnique/kAnonimity.py

from pseudonymizer.pseudonymizer.deidentificationTechnique.equivalent_class import EquivalentClass
from typing import *

# ./pseudonymizer/pseudonymizer/deidentificationTechnique/kAnonimity.py

# from pseudonymizer.pseudonymizer.deidentificationTechnique.equivalent_class import EquivalentClass
# from typing import *

class K_Anonimyity(EquivalentClass):
    """개별 레코드가 최소한 K개 이상 동일한 속성값을 가지도록 하는 K-익명성 클래스
    
    데이터 그룹화가 적용된 k-익명성 알고리즘 의사코드
    -------------------------------------------------
    basic k-anonymity algorithm
    Input : grouped_PI, limited_k
    Output : k_data
    
    k_data = dict()
    for key, identifiers in grouped_PI.items():
        k_anonymity = len(identifiers)
        if k_anonymity >= limited_k:
            k_data[k] = identifiers
    return k_data
    """
    def __init__(self, dataframe):
        super().__init__(dataframe)
        
    def applyKAnonymity(self, K: int, attributes: List[str]) -> Dict:
        K_data = dict()
        # EquivalentClass 클래스의 categorizeEquivalentClass 메서드 호출
        super().categorizeEquivalentClass(attributes)

        for group_key, index_value in self.equivalent_class.items():
            K_anonymity = len(index_value)
            # index_value = identifiers
            if K_anonymity >= K:
                K_data[group_key] = index_value
                
        return K_data
