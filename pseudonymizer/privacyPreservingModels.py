from pseudonymizer.pseudonymizer.deidentificationTechnique.equivalent_class import EquivalentClass
from pseudonymizer.pseudonymizer.deidentificationTechnique.kAnonimity import K_Anonymity
from pseudonymizer.pseudonymizer.deidentificationTechnique.lDiversity import L_Diversity
from pseudonymizer.pseudonymizer.deidentificationTechnique.tCloseness import T_Closeness

from typing import *

class PrivacyPreservingModel:
    """개인식별가능정보 속성을 기준으로 그룹화된 데이터로 프라이버시 보호 모델을 적용하여 정량적인 위험성을 규정하는 실행 클래스"""
    def __init__(self, dataframe):
        self._dataframe = dataframe
        self.equivalnt_class = EquivalentClass(self._dataframe)
        self.Kanonymity = K_Anonymity(self._dataframe)
        self.Ldiversity = L_Diversity(self._dataframe)
        self.Tcloseness = T_Closeness(self._dataframe)
        
    def applyKAnonymityOrLDiversity(self, method: str, **kwargs):
        """K-익명성과 L-다양성 모델을 선택적으로 적용하는 메서드
        input
        -----
        method: 프라이버시 보호 모델 메서드를 받고, 
        keyword arguments에 딕셔너리 형식으로 각 기법에 필요한 파라미터를 받아옴"""
        if method == "K":
            self.Kanonymity.applyKAnonymity(**kwargs)
            return self.Kanonymity.K_data
        elif method == "L":
            self.Ldiversity.applyLDiversity(**kwargs)
            return self.Ldiversity.L_data
        elif method == "LL":            
            self.Ldiversity.applyLocalLDiversity(**kwargs)
            return self.Ldiversity.LocalL_data

    def applyTCloseness(self, aquasi_identifiers: List[str], sensitive_attribute: str, tolerance: float):
        self.Tcloseness.applyTCloseness(quasi_identifiers, tolerance, sensitive_attribute)
        return self.Tcloseness.T_data
    
    def __str__(self):
        """동질집합에 대한 정보를 문자열로 반환하는 메서드"""
        return str(self.equivalent_class)
    
# if __name__ == "__main__":