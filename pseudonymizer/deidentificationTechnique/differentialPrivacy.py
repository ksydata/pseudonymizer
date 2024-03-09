# ./pseudonymizer/pseudonymizer/deidentificationTechnique/differentialPrivacy.py

from pseudonymizer.pseudonymizer.deidentificationTechnique.equivalentClass import EquivalentClass
from typing import *
from numpy import exp
from scipy.stats import laplace

from pseudonymizer.pseudonymizer.deidentificationTechnique.equivalentClass import EquivalentClass
from typing import List
import numpy as np
from numpy import exp
from scipy.stats import laplace

class DifferentialPrivacy(EquivalentClass):
    """라플라스 메커니즘 적용 차분 프라이버시 클래스
    차등적 정보보호 기능을 수행"""
    
    def __init__(self, dataframe, ratio_bounded: float):
        super().__init__(dataframe)
        # 동질집합을 키로하고 인덱스 번호를 값으로 하는 신뢰구간 초과하는 값을 
        self.upperoutlier_dictionary = {}
        self.loweroutlier_dictionary = {}
        self.sensitive_attribute = None
        
        # ratio_bounded = epsilon(개인정보(가명정보) 보호 수준 결정)
        self.ratio_bounded = ratio_bounded
    
    def dataDeviatingfromCI(self, boundary: float, attributes: List[str], sensitive_attribute: str):
        """동질집합 내 평균에서 양쪽 3표준편차의 범위 99.7%에 들지 않는 민감정보 행 번호만 별도로 추출하는 메서드
        가설검정 기반에서 노이즈를 입력하는 방식인 GDP(Gaussian Differential Privacy) 방법
        이 방식은 통계 가설 관점에서 주어진 유의수준에서 최소의 제2종 오류를 trade-off function으로 나타냄으로써 차분 정보보호를 적용
        """
        super().categorizeEquivalentClass(attributes)
        self.sensitive_attribute = sensitive_attribute
        for group_key, index_value in self.equivalent_class.items():
            mu = np.nanmean(self._dataframe.loc[index_value, sensitive_attribute])
            sigma = np.nanstd(self._dataframe.loc[index_value, sensitive_attribute])
            
            for i in index_value:
                x = self._dataframe.loc[i, self.sensitive_attribute]
                if mu-boundary*sigma <= x <= mu+boundary*sigma:
                    pass
                elif x > mu+boundary*sigma:
                    self.upperoutlier_dictionary.setdefault(group_key, []).append(i)
                elif x < mu-boundary*sigma:
                    self.loweroutlier_dictionary.setdefault(group_key, []).append(i)
                else:
                    raise ValueError(f"{x}은 유효한 수가 아닙니다.")
    
    def dataGlobalSensitivity(self, outlier):
        """특정 레코드(식별가능한 개인) 유무에 따른 민감도 산출하는 메서드
        특정 결과를 얻기 위한 쿼리 K를 각 데이터에 적용한 결과인 K(D1)와 K(D2)가 동일한 분포 S에 속할
        확률의 비율(두 데이터 분포의 차이)을 일정 수준(epsilon)보다 작도록 함
        """
        if outlier == "upper":
            for group_key, outlier_list in self.upperoutlier_dictionary.items():
                for i in outlier_list:
                    group_data, exception_data = 0, 0
                    group_list = self.equivalent_class[group_key]
                    exception_list = group_list.remove(i)

                    group_data = self._dataframe.loc[group_list, self.sensitive_attribute]
                    exception_data = self._dataframe.loc[exception_list, self.sensitive_attribute]

                    pseudonymize_data = self.laplaceMechanism(
                        group_data, exception_data, self._dataframe.loc[i, self.sensitive_attribute], outlier)
                    self._dataframe.loc[i, self.sensitive_attribute] = pseudonymize_data
        
        elif outlier == "lower":
            for group_key, outlier_list in self.loweroutlier_dictionary.items():
                for i in outlier_list:
                    group_data, exception_data = 0, 0
                    group_list = self.equivalent_class[group_key]
                    exception_list = group_list.remove(i)

                    group_data = self._dataframe.loc[group_list, self.sensitive_attribute]
                    exception_data = self._dataframe.loc[exception_list, self.sensitive_attribute]

                    pseudonymize_data = self.laplaceMechanism(
                        group_data, exception_data, self._dataframe.loc[i, self.sensitive_attribute], outlier)
                    self._dataframe.loc[i, self.sensitive_attribute] = pseudonymize_data

    @staticmethod
    def estimateLaplaceParameters(cls, data):
        """라플라스 분포의 모수 평균(mu)과 스케일(beta)을 추정하는 메서드"""
        mu = np.nanmean(data)
        beta = np.nanmean(np.abs(data - mu))
        return mu, beta

    @staticmethod
    def laplacePDF(cls, x, mu, beta):
        """라플라스 연속확률분포 확률밀도함수
        확률분포(확률변수가 특정한 값을 가질 확률을 나타내는 함수)"""
        return (1 / (2*beta)) * exp(-abs(x-mu) / beta)

    @staticmethod
    def calculateProbabilityRatio(cls, include_data, exclude_data):
        """확률변수 x가 라플라스 분포에 속할 확률과 특정 행의 포함 여부 데이터 간 비율을 계산하는 메서드"""
        # 두 데이터의 평균과 스케일 파라미터를 추정
        mu_include, beta_include = cls.estimateLaplaceParameters(include_data)
        mu_exclude, beta_exclude = cls.estimateLaplaceParameters(exclude_data)
        
        # 두 데이터의 라플라스 분포에 속할 확률 계산
        prob_include = cls.laplacePDF(include_data, mu_include, beta_include)
        prob_exclude = cls.laplacePDF(exclude_data, mu_exclude, beta_exclude)
        prob_ratio = prob_include / prob_exclude
        
        # 두 데이터의 라플라스 분포에 속할 확률의 비율 계산
        return prob_ratio

    @staticmethod
    def laplaceMechanism(cls, include_data, exclude_data, particular_record, outlier):
        """라플라스 메커니즘을 적용하여 특정 데이터 행에 랜덤 노이즈값을 추가하는 메서드"""
        # 전역 민감도 계산
        sensitivity = cls.calculateProbabilityRatio(include_data, exclude_data)
        # 사용자 지정 개인정보 보호 수전 하이퍼파라미터 엡실론을 통해 스케일 파라미터 정의
        beta = sensitivity / cls.ratio_bounded
        # 평균 0, 베타를 분산으로 가지는 라플라스 분포에 속하는 랜덤 난수 추출
        noise = np.random.laplace(0, beta, len(include_data))
        
        # 이상치에 노이즈 추가
        if outlier == "lower":
            return particular_record + noise
        elif outlier == "upper":
            return particular_record - noise
        else:
            raise ValueError(f"{outlier}은 유효한 이상치 유형이 아닙니다.")
