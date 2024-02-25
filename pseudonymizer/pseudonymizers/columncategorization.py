import pandas as pd
from pseudonymizer.pseudonymizer import Pseudonymizer


class CategorizationOfColumn(Pseudonymizer):
    """수치(연속형) 데이터를 임의의 수를 기준으로 범위(범주형)으로 설정하는 가명처리기법 구체클래스 """
    def __init__(self, numeric_type, grouping_standard, right, ascending):
        self.numeric_type = numeric_type
        self.grouping_standard = grouping_standard
        self.right = right
        self.ascending = ascending
    
    def pseudonymizeData(self, df):
        """식별성이 높은 그룹을 하나로 묶는 메서드"""
        if self.numeric_type == "bin":
            return self.pseudonymizeAmountbyBin(df, self.grouping_standard, self.right, self.ascending)
        elif self.numeric_type == "pct":
            return self.pseudonymizeAmountbyPct(df, self.grouping_standard, self.right, self.ascending)        
        else: 
            raise ValueError(f"{self.numeric_type}은 유효한 범주화 기법 적용 유형이 아닙니다.")

    def makeLabels(self, num_type, df, grouping_standard, ascending: bool):
        """범주화 중 필요한 label을 만들어주는 클래스"""
        if num_type == "pct":

            labels = []
            
            for i in range(len(grouping_standard)):
                if i == 0:
                    label = f"{grouping_standard[i]} 미만"
                    labels.append(label)
                elif 0 < i < len(grouping_standard) - 1:
                    label = f"{grouping_standard[i-1]} ~ {grouping_standard[i]}"
                    labels.append(label)
                else:
                    label1 = f"{grouping_standard[i-1]} ~ {grouping_standard[i]}"
                    labels.append(label1)
                    label2 = f"{grouping_standard[i]} 이상"
                    labels.append(label2)

            if ascending == False:
                return labels.reverse()
            elif ascending == True:
                return labels
            else:
                raise ValueError("ascending 파라미터는 True / False 형태로 입력해 주십시오.")


        elif num_type == "bin":

            labels = []
            
            category_values = pd.cut(df, bins = grouping_standard).value_counts(sort=False)

            for category in list(category_values.index):
                start_value = category.left
                end_value = category.right
                labels.append(f"{start_value} ~ {end_value}")

            if ascending == False:
                return labels.reverse()
            elif ascending == True:
                return labels

        else:
            raise ValueError(f"{num_type}은 유효한 범주화 기법 적용 유형이 아닙니다.")

    
    def pseudonymizeAmountbyBin(self, df, grouping_standard, right: bool, ascending: bool):
        """기타 금액 구간별 범주화 메서드
        신용공여금액(예: 한도/건별대출, 담보대출, 리스/카드할부금융서비스 등)의 일정 급간화
        pd.cut 활용하여 범주화하되, 입력값 및 오름차순/내림차순, 급간 선택에 따라 파라미터를 달리함
        """
        if isinstance(grouping_standard, list):
            num = len(grouping_standard)
            df = pd.cut(df, bins = num, labels = grouping_standard, right = right)
            return df

        elif isinstance(grouping_standard, int):
            labels = self.makeLabels("bin", df, grouping_standard, ascending = ascending)                              
            df = pd.cut(df, bins = grouping_standard, labels = labels, right = right)
            return df

        else:
            raise ValueError("grouping_standard는 list 또는 int 타입으로 입력해 주십시오.")
                
        
    def pseudonymizeAmountbyPct(self, df, grouping_standard, right: bool, ascending: bool):
        """기타 금액 백분위에 의한 범주화 메서드
        개인사업자의 추청매출액/평당월임대료를 백분위수에 따라 매출등급화(90~100%, 65~90%, 35~65%, 10~35%, 0~10%)

        - 각 레코드별 등수 구하기 (중복값은 가장 낮은 순위로)
        - 백분위수 = ((등수 - 1) / 컬럼 레코드 갯수) * 100
        - 백분위수별로 pd.cut
        """
        rank_df = df
        rank_df["rank"] = df.rank(method='min')
        
        percentiles = []

        for rank in rank_df["rank"]:
            percentile = ((rank - 1) / len(df['rank'])) * 100
            percentiles.append(percentile)

        rank_df["percentile"] = percentiles
        new_labels = self.makeLabels("pct", df, grouping_standard, ascending)
        bins = [0] + grouping_standard + [100]
        result_df = pd.cut(rank_df["percentile"], bins = bins, labels = new_labels, right = right)
        return result_df