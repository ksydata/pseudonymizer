from pseudonymizer.cryptocontainers.bundleTables import BundleTables
from pseudonymizer.cryptocontainers.initTables import InitTables


class TargetTables(BundleTables):
    """결합대상정보 생성 테이블 저장 클래스"""
    def __init__(self):
        init_tables = []
        target_tables = []
        columns = None
        serial_cols = []

    @classmethod
    def addInitTables(cls, tables: InitTables):
        """원본테이블, 결합키 생성 테이블, 결합대상정보 테이블로 이루어진 InitTables 클래스 받기"""
        cls.init_tables.append(tables)

    @classmethod
    def addColumns(cls, columns: list):
        """결합키 생성 항목 컬럼명 입력 메서드"""
        cls.columns = columns


    @classmethod
    def selectTables(cls):
        """InitTables에서 target_table만 골라내어 저장하기"""
        for table in cls.init_tables:
            cls.target_tables.append(table.target_table)
            cls.serial_cols.append(table.serial_col)


    @classmethod
    def getTables(cls):
        """결합대상정보 생성 테이블 출력"""
        return cls.target_tables