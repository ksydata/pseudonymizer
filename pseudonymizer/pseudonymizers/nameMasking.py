# ./pseudonymizer/pseudonymizers/
from pseudonymizer.pseudonymizer import Pseudonymizer

class NameMaskingModule(Pseudonymizer):
    """
    성명 마스킹 클래스
    ------------------
    성명 식별자에 직접 마스킹을 적용하여 식별성을 낮추는 구체 클래스
    3자릿수가 넘는 이름은 특정인에 대한 식별가능성이 높아지므로 4자릿수로 마스킹
    """
    def pseudonymizeData(self, name):
        name_list = list(name)
        if 2 <= len(name) <= 3:
            return name_list[0] + "*"*(len(name)-1)
        else: 
            # len(name) > 4:
            return name_list[0] + "*"*3