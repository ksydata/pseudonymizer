# ./pseudonymizer/pseudonymizer/deidentificationTechnique/differentialPrivacy.py

from pseudonymizer.pseudonymizer.deidentificationTechnique.equivalentClass import EquivalentClass
from typing import *

# ./pseudonymizer/pseudonymizer/deidentificationTechnique/differentialPrivacy.py

# from pseudonymizer.pseudonymizer.deidentificationTechnique.equivalentClass import EquivalentClass
# from typing import *

# ./pseudonymizer/pseudonymizer/deidentificationTechnique/differentialPrivacy.py

# from pseudonymizer.pseudonymizer.deidentificationTechnique.equivalentClass import EquivalentClass
# from typing import *

class DifferentialPrivacy(EquivalentClass):
    """차분 프라이버시 클래스
    차등적 정보보호 기능을 수행"""
    
    def __init__(self, dataframe):
        super().__init__(dataframe)
        # 동질집합을 키로하고 인덱스 번호를 값으로 하는 신뢰구간 초과하는 값을 
        self.upperoutlier_dictionary = {}
        self.loweroutlier_dictionary = {}
        self.sensitive_attribute = None
        
        # ratio_bounded = epsilon(개인정보(가명정보) 보호 수준 결정)
        self.ratio_bounded = None
        self.sensitivity = None
    
    def dataDeviatingfromCI(self, boundary: float, attributes: List[str], sensitive_attribute: str):
        """동질집합 내 평균에서 양쪽 3표준편차의 범위 99.7%에 들지 않는 민감정보 행 번호만 별도로 추출하는 메서드"""
        super().categorizeEquivalentClass(attributes)
        for group_key, index_value in self.equivalent_class.items():
            mu = np.nanmean(self._dataframe.loc[index_value, sensitive_attribute])
            sigma = np.nanstd(self._dataframe.loc[index_value, sensitive_attribute])
            
            for i in index_value:
                x = self._dataframe.loc[i, sensitive_attribute]
                if mu-boundary*sigma <= x <= mu+boundary*sigma:
                    pass
                elif x > mu+boundary*sigma:
                    self.upperoutlier_dictionary.setdefault(group_key, []).append(i)
                elif x < mu-boundary*sigma:
                    self.loweroutlier_dictionary.setdefault(group_key, []).append(i)
                else:
                    raise ValueError(f"{x}은 유효한 수가 아닙니다.")
    
    def dataGlobalSensitivity(self):
        """특정 레코드(식별가능한 개인) 유무에 따른 민감도 산출하는 메서드
        특정 결과를 얻기 위한 쿼리 K를 각 데이터에 적용한 결과인 K(D1)와 K(D2)가 동일한 분포 S에 속할
        확률의 비율(두 데이터 분포의 차이)을 일정 수준(epsilon)보다 작도록 함
        """
        pass
    
    def gaussianMechanism(self, ratio_bounded: float):
        """가우스 메커니즘을 적용하여 특정 데이터 행에 랜덤 노이즈값을 추가하는 메서드"""
        sigma = self.sensitivity / ratio_bounded
        noise = np.random.normal(0, sigma, len(data))
        return data + noise

    def laplaceMechanism(self, ratio_bounded: float):
        """라플라스 메커니즘을 적용하여 특정 데이터 행에 랜덤 노이즈값을 추가하는 메서드"""
        beta = self.sensitivity / ratio_bounded
        noise = np.random.laplace(0, beta, len(data))
        return data + noise
    
    @staticmethod
    def gaussianPDF(self, x, mu, sigma):
        """정규분포(가우시안) 확률밀도함수"""
        return (1 / sqrt(2*pi*sigma**2)) * exp(-0.5*((x-mu) / sigma)**2)

    @staticmethod
    def laplacePDF(self, x, mu, scale_param):
        """라플라스분포 확률밀도함수"""
        return (1 / (2*scale_param)) * exp(-abs(x-mu) / scale_param)
