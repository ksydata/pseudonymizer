from pseudonymizer.pseudonymizer import Pseudonymizer

class ResidentNumberMaskingModule(Pseudonymizer):
    """
    주민등록번호 마스킹 클래스
    --------------------
    주민등록번호 뒷자리를 복원할 수 없는 비가역성 기법으로 개인의 식별을 방지하는 구체 클래스
    """        
    def pseudonymizeData(self, resident_number):
        """한국 주민등록번호의 정규표현식을 기준으로 패턴 매칭이 되는 경우 뒷자리 7자리 중 
        성별정보 1자리를 제외한 나머지 출생지정보에 대한 6자리에 대한 마스킹을 수행하는 메서드"""
        pattern_match = re.match(r"^\d{6}-[1-8]\d{6}$", resident_number)
        
        if pattern_match:
            front_part, rear_part = resident_number.split("-")
            return front_part + rear_part[0] + "*"*6
            
        else:
            print("입력받은 { }은 주민등록번호 패턴에 매칭되지 않아 마스킹할 수 없습니다.".format(resident_number))
            