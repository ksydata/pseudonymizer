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
        Q1, _, Q3 = self.calculateQuartiles(dataseries)
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
        if self.bounded_value < 0.5:
            lower_bound = self.bounded_value
            upper_bound = 1 - lower_bound
        else:
            upper_bound = self.bounded_value
            lower_bound = 1 - upper_bound

    def calculateMedian(self, data):
        """중간값(백분위50%) 계산하는 메서드"""
        n = len(data)
        # 전체 길이가 홀수일 때(2로 나눈 나머지가 0일 때, 2로 나눈 몫의 위치에 해당하는 중간값)
        if n % 2 != 0:
            return data[n//2]
        # 전체 길이가 짝수일 때
        else:
            return (data[n//2-1] + data[n//2])/2
    
    def sort(self, data):
        pass

    def calculateQuartiles(self, dataseries):
        """백분위25%(Q1)과 백분위75%(Q3)를 중간값을 이용하여 구하는 메서드"""
        data = dataseries.to_list()
        # 빠른 quick정렬 알고리즘(heap, merge으로도 대체 가능)
        data
        
        # 백분위 25%(가장 작은 수부터 중간값까지 수의 중간값), 백분위 75%(중간값부터 가장 큰 수까지 수의 중간값)
        Quartile2 = self.calculateMedian(data)
        Quartile1 = self.calculateMedian(data[:Q2])
        Quartile3 = self.calculateMedian(data[Q2:])
        return Quartile1, Quartile2, Quartile3