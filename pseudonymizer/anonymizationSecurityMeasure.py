from pseudonymizer.pseudonymizer import Pseudonymizer

class AnonymizationSecurityMeasure(Pseudonym):
    """익명처리 기법이 적용된 정보의 안전성을 측정하는 지표"""
    def __init__(self, dataframe, attributes, anonymizeddata):
        super().__init__(dataframe)
        super().categorizeEquivalentClass(attributes)
        self.anonymizeddata = anonymizeddata

    def MeanDistributionECMetric(self):
        """동질집합별 속성들에 대한 평균 분포도(분산) 계산 메서드"""
        pass
    
    def NormalizedAverageECSizeMetric(self):
        """정규화된 동질집합들의 평균 크기 계산 메서드"""
        pass

    def nonUniformEntropyMetric(self):
        """비균일 엔트로피 방법을 이용한 K익명성 프라이버시 보호 모델에서의 정보 손실 측도"""
        pass
    
    def AnonymizationRatio(self):
        """원본 데이터셋 대비 익명처리된 데이터셋의 정보량"""
        pass