from pseudonymizer.pseudonymizer import Pseudonymizer
import pandas as pd

class MicroAggregation(Pseudonymizer):
    """특정 그룹의 속성에서 정확한 통계값을 확인하는 가명처리기법 구체 클래스
       클래스를 통해 도출할 부분 통계값: 평균, 총합, 중간값, 최댓값, 최솟값, 최빈값
    """
    def __init__(self, cal_type, category):
        self.cal_type = cal_type
        self.category = category


    def pseudonymizeData(self, df, column, equivalent_class):
        """Pseudonym 클래스 내에서 클래스 실행하는 메서드"""

        if self.cal_type == "avr":
            return self.microAverage(df, column, self.category, equivalent_class)
        elif self.cal_type == "sum":
            return self.microSum(df, column, self.category, equivalent_class)
        elif self.cal_type == "mdn":
            return self.microMedian(df, column, self.category, equivalent_class)
        elif self.cal_type == "max":
            return self.microMax(df, column, self.category, equivalent_class)
        elif self.cal_type == "min":
            return self.microMin(df, column, self.category, equivalent_class)
        elif self.cal_type == "fqr":
            return self.microFrequency(df, column, self.category, equivalent_class)
        elif self.cal_type == "trd":
            return self.microTrend(df, column, self.category, equivalent_class)
        elif self.cal_type == "ded":
            return self.microDeduction(df, column, self.category, equivalent_class)
        else:
            raise ValueError(f"{self.cal_type}은 유효한 부분총계 기법 적용 유형이 아닙니다.")

    def microAverage(self, df, column, category, equivalent_class):
        """그룹별 평균 구하는 메서드"""
        condition = equivalent_class[category]
        selectedData = df.iloc[condition]
        
        partialAverage = selectedData[column].mean()
        df.loc[condition, column] = partialAverage
        return df[column]
        

    def microSum(self, df, column, category, equivalent_class):
        """그룹별 총합 구하는 메서드"""
        condition = equivalent_class[category]
        selectedData = df.iloc[condition]
        
        partialSum = selectedData[column].sum()
        df.loc[condition, column] = partialSum
        return df[column]

    def microMedian(self, df, column, category, equivalent_class):
        """그룹별 중간값 구하는 메서드"""
        condition = equivalent_class[category]
        selectedData = df.iloc[condition]
        
        partialAverage = selectedData[column].median()
        df.loc[condition, column] = partialAverage
        return df[column]

    def microMax(self, df, column, category, equivalent_class):
        """그룹별 최댓값 구하는 메서드"""
        condition = equivalent_class[category]
        selectedData = df.iloc[condition]
        
        partialMax = selectedData[column].max()
        df.loc[condition, column] = partialMax
        return df[column]

    def microMin(self, df, column, category, equivalent_class):
        """그룹별 최솟값 구하는 메서드"""
        condition = equivalent_class[category]
        selectedData = df.iloc[condition]
        
        partialMin = selectedData[column].min()
        df.loc[condition, column] = partialMin
        return df[column]

    def microFrequency(self, df, column, category, equivalent_class):
        """그룹별 최빈값 구하는 메서드"""
        condition = equivalent_class[category]
        selectedData = df.iloc[condition]
        
        partialFrequency = selectedData[column].mode()
        df.loc[condition, column] = partialFrequency
        return df[column]
        
    