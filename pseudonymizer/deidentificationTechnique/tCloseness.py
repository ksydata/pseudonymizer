# ./pseudonymizer/pseudonymizer/deidentificationTechnique/tCloseness.py

from pseudonymizer.pseudonymizer.deidentificationTechnique.equivalent_class import EquivalentClass
from typing import *
from scipy.stats import wasserstein_distance

class T_Closeness(EquivalentClass):
    """민감 정보(SA)의 분포를 전체 데이터 셋의 분포와 유사하도록 하는 T-근접성 클래스
    
    l-다양성과 달리 민감정보를 원본 그대로 배열에 저장한 후 
    데이터를 내림차순 정렬하여 (확률분포의 차이)
    데이터의 분포도를 측정하는 t-근접성 알고리즘 의사코드
    -----------------------------------------------------
    basic Earth Mover's Distance algorithms
    Input : t_list
    Output : EMD
    
    total_range = []
    for n in range(100):
        total_range.append(n)
        # 설정된 배열에 정수가 순서대로 추가
        total_length = len(total_info)
        
        static_part = total_length / len(t_list)
        # EMD(데이터의 분산 정도)를 계산하기 위해 나눗셈
        extra_part = float(static_part) % float(len(t_list))
        extra_part = extra_part.split(".")[0]
        # 나누어 떨어지지 않는 여분으로 연산해주어야 할 때 계산

        balance_value = len(t_list) - (extra_part)
        # 데이터의 분산도 측정
        # 여분의 연산으로 하는 부분(나누어 떨어지지 않는 수)에 대하여
        # 배열의 마지막 부분에서 처리
    """
    def __init__(self, dataframe):
        super().__init__(dataframe)
        self.T_data = None
        self.sensitive_attribute = None
        self.tolerance = None
        
    def checkSensitivesDistribution(self, data_set, sensitive_attribute: str):
        """개인식별가능정보(준식별자)의 모든 가능한 조합 n개의 관심 대상값
        (sensitive_attribute)의 분포와 전체 집단의 분포의 거리 최댓값이 <= t로 규정할 때
        분포를 계산하는 메서드"""
        sensitive_vector = data_set[sensitive_attribute]
        
        # 민감속성의 고유한 값과 그 값의 비율 {v: count/len(V)}
        if sensitive_vector.dtype == "int" or "float":
            ordered_vector = np.sort(sensitive_vector)
            distribution = {v: n/len(ordered_vector)  for (v, n)
                            in zip(ordered_vector, list(range(len(ordered_vector))))}
        elif sensitive_vector.dtype == "object":
            distribution = {v: count/len(v) for (v, count) 
                            in Counter(sensitive_vector).items()}
        elif sensitive_vector.dtype == "category":
            distribution = {v: count/len(v) for (v, count) 
                            in Counter(sensitive_vector).items()}
        else: ValueError("입력받은 {}은 유효한 자료형이 아닙니다.".format(
            self._datafrmae[self.sensitive_attribute].dtype))
        return distribution
    
    def earthMoversDistance(self, qi_dist, total_dist):
        """scipy.wasserstein_distance(data_sensitivity, data_population)"""
        # eucdistance = np.sqrt((qi_dist - total_dist)**2)
        emdistance = np.sum(np.abs(qi_dist - total_dist))
        return emdistance

    def applyTCloseness(self, quasi_identifiers: List[str], tolerance: float, sensitive_attribute: str):
        """tolerance: 허용가능한 확률분포 차이의 범위를 정의하여 T-근접성을 적용하는 메서드"""
        T_data, qi_distribution = dict()

        if 0 <= tolerance <= 1: 
            # threshold
            vector = np.array(self._dataframe[sensitive_attribute])
            super().categorizeEquivalentClass(quasi_identifiers)

            for group_key, index_value in self.equivalent_class.items():
                # 1. Empirical Cummulative Probability Distribution
                qi_distribution[group_key] = self.checkSensitivesDistribution(vector[index_value], sensitive_attribute)
                total_distribution[group_key] = self.checkSensitivesDistribution(vector, sensitive_attribute)
                    # self._dataframe.loc[index_value, sensitive_attribute]
                    # .value_count(normalize = True) = .value_counts() / sum 

                # 2. Earth's Mover Distance
                emd = self.earthMoversDistance(qi_distribution, total_distribution)

                # 3.
                if emd < tolerance:
                    T_data[group_key] = index_value
            self.T_data = T_data
        else: 
            ValueError("입력받은 {}은 허용가능한 동질집합과 전체집단 간 확률분포 차이의 범위로서 유효하지 않습니다.".format(tolerance))