from pseudonymizer.pseudonymizer import Pseudonymizer

class TopandBottomCoding(Pseudonymizer):
    """적은 수의 분포를 가진 양 끝단의 정보를 범주화 등의 기법을 적용하여 식별성을 낮추는 가명처리기법 구체클래스"""
    def __init__(self, outlier_type, bounded_value):
        self.outlier_type = outlier_type
        self.bounded_value = bounded_value
    
    def pseudonymizeData(self, dataseries):
        if self.outlier_type == "IQR":
            return self.pseudonymizeOutlierIQR(dataseries)
        elif self.outlier_type == "Pct":
            return self.pseudonymizeOutlierPct(dataseries)
        else: 
            raise ValueError(f"{self.outlier_type}은 유효한 상하단코딩 적용 유형이 아닙니다.")
    
    def pseudonymizeOutlierIQR(self, dataseries):
        """
        상자도표(boxplot)을 이용한 Q3 + 1.5IQR(상위 경계) 이상이거나 Q1 - 1.5IQR(하위 경계) 이하인 관측값
        다만, 다변량 설정이나 고차원 데이터에는 유용성이 떨어진다는 한계
        """
        Q1, Q2, Q3 = self.calculateQuartiles(dataseries)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5*IQR
        upper_bound = Q3 + 1.5*IQR
        
        datatopcoding = dataseries.apply(
          lambda x: x if x <= upper_bound
          else upper_bound)
        databottomcoding = datatopcoding.apply(
          lambda x: x if x >= lower_bound
          else lower_bound)
        return databottomcoding

    def pseudonymizeOutlierPct(self, dataseries):
        """
        백분율을 기준으로 상하단 경계값을 설정
        """
        # 데이터 오름차순 퀵정렬
        datasorted = self.quickSorting(dataseries)
        # 백분율을 기준으로 상하단 경계값의 인덱스 추출
        n = len(datasorted)
        if self.bounded_value < 0.5:
            lower_bound = self.bounded_value
            lower_index = int(n*lower_bound/2)
            upper_index = int(n*(1-lower_bound)/2)
        else:
            upper_bound = self.bounded_value
            upper_index = int(n*upper_bound/2)
            lower_index = int(n*(1-upper_bound)/2)
        # 인덱스 번호를 통해 상하단 코딩 경계값 탐색
        lower_value = datasorted[lower_index]
        upper_value = datasorted[upper_index]
        datareturn = dataseries.apply(
            lambda x: x if lower_value <= x <= upper_value 
            else lower_value if x < lower_value 
            else upper_value)
        return datareturn

    def calculateMedian(self, dataseries):
        """중간값(백분위50%) 계산하는 메서드
        정적 메서드를 선언함으로써
        클래스의 네임스페이스 내 속하는 유틸리티 함수를 제공하며 해당 클래스의 인스턴스를 생성하지 않고(의존성 없이) 필요한 기능 수행"""
        data = dataseries.to_list()
        n = len(data)
        # 전체 길이가 홀수일 때(2로 나눈 나머지가 0일 때, 2로 나눈 몫의 위치에 해당하는 중간값)
        if n % 2 != 0:
            return data[n//2]
        # 전체 길이가 짝수일 때
        else:
            return (data[n//2-1] + data[n//2])/2
        
    def quickSorting(self, dataseries):
        """퀵 정렬 알고리즘 메서드
        그 다음 작은 값과 큰 값을 담고 있는 배열을 대상으로 다시 퀵정렬 재귀호출"""
        # 배열의 길이에 따라 정렬 여부 결정
        data = dataseries.to_list()
        if len(data) <= 1:
            return data
        # 중간 위치의 값을 피봇으로 설정(임의의 값으로 설정할 수 있지만 상용코드임을 고려하여 결정)
        else:
            pivot = data[len(data) // 2]
            # 피봇으로 나누어지는 작은 값 배열과 큰 값 배열
            lower_data, upper_data = [], []
            # 동일한 값일 경우도 고려한 배열
            equal_data = []

            for num in data:
                # 배열 내 값이 피봇보다 작을 때
                if num < pivot:
                    lower_data.append(num)
                # 배열 내 값이 피봇보다 클 때
                elif num > pivot:
                    upper_data.append(num)
                else:
                    equal_data.append(num)
            return self.quickSorting(lower_data) + equal_data + self.quickSorting(upper_data)
            
    def calculateQuartiles(self, dataseries):
        """백분위25%(Q1)과 백분위75%(Q3)를 중간값을 이용하여 구하는 메서드"""
        data = dataseries.to_list()
        # 빠른 quick정렬 알고리즘(heap, merge으로도 대체 가능)
        datasorted = self.quickSorting(data)
        
        # 백분위 25%(가장 작은 수부터 중간값까지 수의 중간값), 백분위 75%(중간값부터 가장 큰 수까지 수의 중간값)
        Quartile2 = self.calculateMedian(datasorted)
        Quartile1 = self.calculateMedian(datasorted[:len(datasorted)//2])
        Quartile3 = self.calculateMedian(datasorted[len(datasorted)//2:])
        return Quartile1, Quartile2, Quartile3