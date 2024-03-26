from pseudonymizer.cryptocontainers.initTables import InitTables
from pseudonymizer.encryptionPseudonyms.pyMySQLQuery import PyMySQLQuery


class DivideOriginalTable(PyMySQLQuery):
    """원본 테이블을 결합키와 결합대상정보로 분할하기"""
    def __init__(self, pw: str, serverIP: str, port_num: int, user_name: str, database_name: str, kr_encoder: str):
        super().__init__(pw = pw)
        super().connectDatabase(serverIP, port_num, user_name, database_name, kr_encoder)
        self.init_tables = None
        self.original_table = None
        self.serial_col = None
        self.serial_text = None
        self.key_cols = None
        

    def addInitTables(self, init_tables: InitTables):
        """원본 테이블, 결합키 테이블, 결합대상정보 테이블 객체 통해 입력"""
        self.init_tables = init_tables

        self.original_table = self.init_tables.original_table
        self.serial_col = self.init_tables.serial_col
        self.serial_text = self.init_tables.serial_text

        self.key_cols = self.init_tables.key_cols

    def addSerialNum(self):
        """일련번호 컬럼 추가 메서드"""
        schema = self.original_table.getSchema()
        table = self.original_table.getTable()

        # 컬럼명 중복시 해당 컬럼 삭제
        super().dataQueryLanguage(f"ALTER TABLE {schema}.{table} DROP COLUMN {self.serial_col}")
        super().executeQuery()

        # 컬럼 만들기
        make_column = f"ALTER TABLE {schema}.{table} ADD COLUMN {self.serial_col} VARCHAR(1000)"
        super().dataQueryLanguage(make_column)
        super().executeQuery()

        # 값 할당
        super().dataQueryLanguage("SET @counter = 0;")
        super().executeQuery()
        
        super().dataQueryLanguage(f"UPDATE {schema}.{table} SET {self.serial_col} = CONCAT('{self.serial_text}', @counter := @counter + 1);")
        super().executeQuery()

    def insertKey(self):
        """결합키 테이블 DB 입력 메서드"""
        key_table = self.init_tables.key_table
        key_schema = key_table.getSchema()
        key_result = key_table.getTable()

        join_columns = ', '.join(self.key_cols)

        super().dataQueryLanguage(f"DROP TABLE IF EXISTS {key_schema}.{key_result}")
        super().executeQuery()
        
        sql = f"CREATE TABLE {key_schema}.{key_result} AS SELECT {self.serial_col}, {join_columns} FROM {self.original_table}"
        super().dataQueryLanguage(sql)
        super().executeQuery()

        # 결합키 컬럼 만들기
        super().dataQueryLanguage(f"ALTER TABLE {key_schema}.{key_result} ADD COLUMN {self.key_cols} VARCHAR(1000)")
        super().executeQuery()

        super().dataQueryLanguage(f"UPDATE {key_schema}.{key_result} SET {self.key_cols} = CONCAT({join_columns})")
        super().executeQuery()
        
    def insertTarget(self):
        """결합대상정보 테이블 DB 입력 메서드
           : 원래 테이블을 복사한 뒤, 결합키 생성항목 columns를 제거하여 생성
        """
        target_table = self.init_tables.target_table
        target_schema = target_table.getSchema()
        target_result = target_table.getTable()

        super().dataQueryLanguage(f"DROP TABLE IF EXISTS {target_schema}.{target_result}")
        super().executeQuery()

        create_sql = f"CREATE TABLE {target_schema}.{target_result} AS SELECT * FROM {self.original_table}"
        super().dataQueryLanguage(create_sql)
        super().executeQuery()

        for column in self.key_cols:
            drop_sql = f"ALTER TABLE {target_schema}.{target_table} drop {column}"
            super().dataQueryLanguage(drop_sql)
            super().executeQuery()