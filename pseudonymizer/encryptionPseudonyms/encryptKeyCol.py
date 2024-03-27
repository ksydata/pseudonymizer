import binascii
import os
from pseudonymizer.cryptocontainers.keyTables import KeyTables
from pseudonymizer.encryptionPseudonyms.pyMySQLQuery import PyMySQLQuery


class EncryptKeyCol(PyMySQLQuery):
    """결합키 암호화 클래스 : KeyTables에 들어있는 모든 key_tables의 key_col에 적용"""
    def __init__(self, pw: str, serverIP: str, port_num: int, user_name: str, database_name: str, kr_encoder: str):
        self.kr_encoder = kr_encoder
        super().__init__(pw = pw)
        super().connectDatabase(serverIP, port_num, user_name, database_name, kr_encoder)
        
        self.key_tables = None
        self.salt_col = None

    def addKeyTables(self, key_tables: KeyTables):
        """원본 테이블, 결합키 테이블, 결합대상정보 테이블 객체 통해 입력"""
        self.key_tables = key_tables

    def addSaltCol(self, salt_col: str):
        """Salt키 컬럼명 입력"""
        self.salt_col = salt_col

    def encryptKeyCol(self, func: str):
        """self.key_tables에 저장된 모든 key_tables를 대상으로 암호화를 실행하는 메서드"""
        for key_table in self.key_tables:
            schema = key_table.getSchema()
            table = key_table.getTable()
            self.createKey(func, schema, table, self.key_tables.key_col, self.salt_col)

    def createKey(self, func: str, schema: str, table: str, key_col: str, salt_col: str):
        """결합키 암호화 방식을 선택하여 실행시키는 메서드"""
        if func == "SHA256":
            self.applySHA256(schema, table, salt_col, key_col)
        elif func == "SHA512":
            self.applySHA512(schema, table, salt_col, key_col)
        else:
            print("SHA256과 SHA512 중 하나를 입력하십시오")

    def createSalt(self, schema: str, table: str, salt_col: str, key_col: str):
        """SALT값을 만들어 테이블 특정 컬럼에 붙이는 메서드"""
        # SALT값 컬럼 만들기
        super().dataQueryLanguage(f"ALTER TABLE {salt_col} VARCHAR(1000)")
        super().executeQuery()

        # SALT값을 만들고 컬럼에 입력하기
        super().dataQueryLanguage(f"SELECT * FROM {schema}.{table}")
        rows = super().useFetchallQuery()

        for row in rows:
            salt = binascii.hexlify(os.urandom(16)).decode(self.kr_encoder)
            sql = f"UPDATE {schema}.{table} SET {salt_col} = {salt} WHERE {key_col} = {row[0]}"
            super().dataQueryLanguage(sql)
            super().executeQuery()

    def applySHA256(self, schema: str, table: str, key_col: str, salt_col: str):
        """SHA256 해시함수를 통해 결합키 컬럼을 암호화하는 메서드"""
        sql = f"UPDATE {schema}.{table} SET {key_col} = SHA2(CONCAT({key_col}, {salt_col}), 256)"
        super().dataQueryLanguage(sql)
        super().executeQuery()

    def applySHA512(self, schema: str, table: str, key_col: str, salt_col: str):
        """SHA512 해시함수를 통해 결합키 컬럼을 암호화하는 메서드"""
        sql = f"UPDATE {schema}.{table} SET {key_col} = SHA2(CONCAT({key_col}, {salt_col}), 512)"
        super().dataQueryLanguage(sql)
        super().executeQuery()