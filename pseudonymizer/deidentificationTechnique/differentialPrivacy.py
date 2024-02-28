# ./pseudonymizer/pseudonymizer/deidentificationTechnique/differentialPrivacy.py

from pseudonymizer.pseudonymizer.deidentificationTechnique.equivalentClass import EquivalentClass
from typing import *

class DifferentialPrivacy(EquivalentClass):
    """차분 프라이버시 클래스
    Pseudonymizer와는 무관하게 수행되어도 되는지 고민해봐야 함"""
    
    def __init__(self, dataframe):
        super().__init__(dataframe)
        self.ratio_bounded = None 
        # ratio_bounded = epsilon(개인정보(가명정보) 보호 수준 결정)
        self.sensitive_attribute = None
        self.sensitivity = None
    
    def dataGlobalSensitivity(self):
        """
        특정 레코드(식별가능한 개인) 유무에 따른 민감도 산출하는 메서드
        * 전역 민감도란 (DB 테이블 쿼리 결과) - (이웃 DB의 동일한 쿼리 결과)의 차이
        * 민감도 산출 시 gaussianPDF(), laplacePDF() 활용가능
        * 테이블 전체가 아닌 동질집합 단위로 범위 수정하여 적용
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
    
    def gaussianPDF(self, x, mu, sigma):
        """정규분포(가우시안) 확률밀도함수"""
        return (1 / sqrt(2*pi*sigma**2)) * exp(-0.5*((x-mu) / sigma)**2)
    
    def laplacePDF(self, x, mu, scale_param):
        """라플라스분포 확률밀도함수"""
        return (1 / (2*scale_param)) * exp(-abs(x-mu) / scale_param)
