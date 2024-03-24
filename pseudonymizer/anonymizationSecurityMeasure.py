from pseudonymizer.pseudonymizer import Pseudonymizer

class AnonymizationSecurityMeasure(Pseudonym):
    """익명처리 기법이 적용된 정보의 안전성을 측정하는 지표"""
    def __init__(self, dataframe, attributes, anonymizeddata, degreeoffredom):
        super().__init__(dataframe)
        super().categorizeEquivalentClass(attributes)
        self.anonymizeddata = anonymizeddata
        self.degreeoffredom = degreeoffredom 
        # 0 or 1
        
    def measureSecurity(self, parameter, quasi_identifiers, sensitive_attribute):
        """
        staticmethod에서는 부모클래스의 클래스속성 값을 가져오지만, classmethod에서는 cls인자를 활용하여 cls의 클래스속성을 가져오는 것을 알 수 있습니다.
        """
        self.equivalent_class[quasi_identifiers] = index_list
        column_reference = self._datframe.get_column(sensitive_attribute)
        column_forward = self.anonymizeddata.get_column(sensitive_attribute)
        
        if parameter == "var":
            variance_reference = cls.meanDistributionECMetric(self._datframe.iloc[index_list, column_reference])
            variance_forward = cls.meanDistributionECMetric(self.anonymizeddata.iloc[index_list, column_forward])
            return variance_reference, variance_forward
        
        elif parameter == "norm_aver":
            average_reference = cls.normalizedAverageECSizeMetric(self._datframe.iloc[index_list, column_reference])
            average_forward = cls.normalizedAverageECSizeMetric(self.anonymizeddata.iloc[index_list, column_forward])
            return average_reference, average_forward
        
        elif parameter == "entropy":
            entrophy_reference = cls.nonUniformEntropyMetric(self._datframe.iloc[index_list, column_reference])
            entrophy_forward = cls.nonUniformEntropyMetric(self.anonymizeddata.iloc[index_list, column_forward])
            return entrophy_reference, entrophy_forward
        
        else:
            raise ValueError(f"{x}은 유효한 익명정보 안전성 평가지표가 아닙니다.")
            
    @classmethod
    def meanDistributionECMetric(cls, x):
        """동질집합별 속성들에 대한 평균 분포도(분산) 계산 메서드"""
        if self.degreeoffredom == 0:
            # 표본분산
            variance_x = np.mean(abs(x - np.mean(x))**2)
        elif self.degreeoffredom == 1:
            # 불편분산(불편추정량)
            variance_x = sum((x - np.mean(x))**2 for x in x.values()) / (len(x) - 1)
        else:
            raise ValueError(f"{self.degreeoffredom}은 유효한 자유도가 아닙니다.")
        return variance_x

    @classmethod
    def normalizedAverageECSizeMetric(cls, x, y):
        """정규화된 동질집합들의 평균 크기 계산 메서드"""
        pass

    @classmethod
    def nonUniformEntropyMetric(cls, x, y):
        """비균일 엔트로피 방법을 이용한 K익명성 프라이버시 보호 모델에서의 정보 손실 측도"""
        pass