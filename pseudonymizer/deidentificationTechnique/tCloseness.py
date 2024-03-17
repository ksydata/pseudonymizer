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
        
    def checkSensitivesDistribution(self, dataseries):
        """개인식별가능정보(준식별자)의 모든 가능한 조합 n개의 관심 대상값
        (sensitive_attribute)의 분포와 전체 집단의 분포의 거리 최댓값이 <= t로 규정할 때
        분포를 계산하는 메서드"""
        sensitive_vector = dataseries
        cumulative_distribution = {}
        cumulative_probability = 0
        
        # 민감속성의 고유한 값과 그 값의 비율 {v: count/len(V)}
        if sensitive_vector.dtype in ["int64", "float"]:
            # 오름차순 정렬 후 중복값을 제거한 SA를 전체 데이터의 길이로 나눈 값을 확률로 하는 누적분포를 계산 
            ordered_vector = np.sort(sensitive_vector)
            unique_value, counts = np.unique(ordered_vector, return_counts = True)
            distribution = np.cumsum(counts) / len(sensitive_vector)
            
            print(unique_value)
            print(cumulative_distribution)
    
        elif sensitive_vector.dtype in ["object", "category"]:
            # cumulative_distribution = {v: count/len(v) for (v, count) in Counter(sensitive_vector).items()}
            for value, count in Counter(sensitive_vector).items():
                probability = count / len(sensitive_vector)
                cumulative_probability += probability
                cumulative_distribution[value] = cumulative_probability
            
            print(cumulative_distribution)
        
        else: 
            raise ValueError("입력받은 {}은 유효한 자료형이 아닙니다.".format(dataseries.dtype))
        
        return cumulative_distribution
        # UnboundLocalError: local variable 'distribution' referenced before assignment
    
    def earthMoversDistance(self, qi_dist, total_dist):
        """scipy.wasserstein_distance(data_sensitivity, data_population)"""
        # 누적 분포가 아닌 개별 값의 분포가 필요
        # eucdistance = np.sqrt((qi_dist - total_dist)**2)
        # emdistance = np.sum(np.abs(qi_dist - total_dist))
        emdvalues: List = []
        
        for key in qi_dist:
            emdvalue = np.sum( np.abs(qi_dist[key] - total_dist[key]) )
            # TypeError: unsupported operand type(s) for -: 'dict' and 'dict'
            emdvalues.append(emdvalue)
        emdistance = np.mean(emdvalues)
        
        return emdistance

    def applyTCloseness(self, quasi_identifiers, tolerance: float, sensitive_attribute: str):
        """tolerance: 허용가능한 확률분포 차이의 범위를 정의하여 T-근접성을 적용하는 메서드"""
        T_data = dict()
        qi_distribution, total_distribution = {}, {}

        if 0 <= tolerance <= 1: 
            # threshold
            vector = np.array(self._dataframe[sensitive_attribute])
            super().categorizeEquivalentClass(quasi_identifiers)

            for group_key, index_value in self.equivalent_class.items():
                # 1. Empirical Cummulative Probability Distribution
                qi_distribution[group_key] = self.checkSensitivesDistribution(vector[index_value])
                total_distribution[group_key] = self.checkSensitivesDistribution(vector)
                    # self._dataframe.loc[index_value, sensitive_attribute]
                    # .value_count(normalize = True) = .value_counts() / sum 
                print(qi_distribution, total_distribution)
                break

                # 2. Earth's Mover Distance
                emd = self.earthMoversDistance(qi_distribution, total_distribution)

                # 3.
                if emd < tolerance:
                    T_data[group_key] = index_value
                else:
                    print(group_key, len(unique_sensitive_values))
            self.T_data = T_data
        else: 
            raise ValueError("입력받은 {}은 허용가능한 동질집합과 전체집단 간 확률분포 차이의 범위로서 유효하지 않습니다.".format(tolerance))