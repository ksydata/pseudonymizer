from abc import ABC, abstractmethod


class SQLTable(ABC):
    """스키마와 테이블로 이루어진 SQL 테이블명 구조를 저장하고 꺼내쓰는 목적의 추상 클래스"""
    @abstractmethod
    def setSchemaTable(self):
        """스키마명, 테이블명 저장 메서드"""
        pass

    @abstractmethod
    def getSchema(self):
        """스키마명 꺼내는 메서드"""
        pass

    @abstractmethod
    def getTable(self):
        """테이블명 꺼내는 메서드"""
        pass