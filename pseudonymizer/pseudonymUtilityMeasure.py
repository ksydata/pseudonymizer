from pseudonymizer.pseudonymizer import Pseudonymizer
from numpy import dot
from numpy.linalg import norm

class PseudonymUtilityMeasure(Pseudonym):
    """가명처리 기법이 적용된 개인정보(가명정보)의 유용성을 측정하는 지표"""
    def __init__(self, dataframe, attributes, pseudonymizeddata):
        super().__init__(dataframe)
        super().categorizeEquivalentClass(attributes)
        # self.equivalent_class 상속
        self.pseudonymizeddata = pseudonymizeddata
        
    def measureUtility(self, sensitive_attribute):
        """
        staticmethod에서는 부모클래스의 클래스속성 값을 가져오지만, classmethod에서는 cls인자를 활용하여 cls의 클래스속성을 가져오는 것을 알 수 있습니다.
        """
        if parameter == "cs":
            cls.cosineSimilarity(self.datframe[sensitive_attribute], self.pseudonymizeddata[sensitive_attribute])
        elif parameter == "mc":
            cls.meanCorrelation(self.datframe[sensitive_attribute], self.pseudonymizeddata[sensitive_attribute])
        elif parameter == "mgd":
            cls.meanGeneralizedDifference(self.datframe[sensitive_attribute], self.pseudonymizeddata[sensitive_attribute])
        elif parameter == "scd_sse":
            cls.standardizedEuclidianDistanceSSE(self.datframe[sensitive_attribute], self.pseudonymizeddata[sensitive_attribute])
        elif parameter == "pr":
            cls.pseudonymRatio(self.datframe[sensitive_attribute], self.pseudonymizeddata[sensitive_attribute])
            
    @classmethod
    def cosineSimilarity(cls, x, y):
        """코사인 유사도로 원본과 비식별 동일 속성집합 간 벡터의 스칼라곱과 크기 계산 메서드
        벡터 간의 코사인 각도를 이용해 서로 간에 얼마나 유사한지 산정"""
        # metric 만드는 로직 구현 必
        return np.dot(x, y) / (norm(x)*norm(y))
    
    @classmethod
    def meanCorrelation(cls, x, y):
        """지정된 2개 이상의 특정 속성쌍들에 대한 피어슨 상관계수에 대한 차이(평균절대오차) 계산 메서드"""
        return np.dot( (x-np.mean(x)), ((y-np.mean(y)) ) / (
            np.linalg.norm(x - np.mean(x)) * np.linalg.norm(y-np.mean(y)) )
        
    @classmethod
    def meanGeneralizedDifference(cls, x, y):
        """카테고리형 트리 구조를 갖는 문자 속성집합들 간의 평균 차이 계산 메서드
        원본과 비식별 동일 문자 속성집합 간 일반화된 차이"""
        pass
    
    @classmethod
    def standardizedEuclidianDistanceSSE(cls, x, y):
        """표준화된 유클리디안 거리를 이용한 제곱합오차 계산 메서드"""
        pass
                      
    @classmethod    
    def pseudonymRatio(cls, x, y):
        """원본 데이터셋 대비 가명처리된 데이터셋의 정보량"""
        pass