from abc import ABC, abstractmethod


class BundleTables(ABC):
    """결합키 테이블 저장, 결합대상정보 테이블 저장 클래스를 위한 추상화 클래스"""
    @abstractmethod
    def addInitTables(self):
        """원본테이블, 결합키 생성 테이블, 결합대상정보 테이블로 이루어진 InitTables 클래스 받는 추상 메서드"""
        pass

    @abstractmethod
    def selectTables(self):
        """InitTables에서 해당 클래스의 성격에 맞는 테이블만 골라내어 저장하기"""
        pass

    @abstractmethod
    def getTables(self):
        """클래스 성격에 맞는 테이블을 출력"""
        pass