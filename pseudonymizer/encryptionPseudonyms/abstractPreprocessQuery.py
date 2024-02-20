import pymysql
from abc import ABC, abstractmethod

class PreprocessQuery(ABC):
    """가명처리를 위한 개인정보 추출 목적의 SQL쿼리 추상클래스"""
    @abstractmethod
    def connectDatabase(self):
        """데이터베이스에 연결하기 위해 접속하는 메서드"""
        pass
    
    @abstractmethod
    def executeQuery(self, SQL):
        """SQL쿼리를 실행하는 메서드"""
        pass
    
    @abstractmethod
    def closeConnection(self):
        """데이터베이스와의 연결을 종료하는 메서드"""
        pass