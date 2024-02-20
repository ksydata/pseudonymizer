from pseudonymizer.encryptionPseudonyms.abstractpreprocessQuery import PreprocessQuery
from typing import *

class PyMySQL(PreprocessQuery):
    def __init__(self, pw):
        self._pw = pw
        self.connection = None
        self.cursor = None
        self.SQL = None
    
    def connectDatabase(self, 
                     serverIP: str, port_num: int, user_name: str, database_name: str, kr_encoder: str):
        """MySQL DBMS 데이터베이스에 접속 메서드
        : 서버IP주소, 사용자명, 계정 암호, 데이터베이스명, 한글 인코딩 방식"""
        try:
            self.connection = pymysql.connect(
                host = serverIP, port = port_num,
                user = user_name, password = self._pw,
                db = database_name, charset = kr_encoder
            )
            self.cursor = self.makeCursor(self.connection)
        except pymysql.Error as e:
            print(f"Error Connecting to MySQL from Python: {e}")
    
    def makeCursor(self, connect):
        """커서 생성 메서드"""
        return connect.cursor()
    
    def dataQueryLanguage(self, sql):
        """SQL쿼리문 작성 메서드"""
        self.SQL = f"{sql}"
    
    def executeQuery(self):
        """SQL쿼리문 실행 및 예외처리 메서드"""
        try:
            self.cursor.execute(self.SQL)
            action_output = self.cursor.fetchall()
            return action_output
        except pymysql.Error as e:
            print(f"Error Executing Query: {e}")
    
    def commitTransaction(self):
        """실행결과를 확정(트랜잭션을 커밋)하는 메서드"""
        self.connection.commit()
    
    def closeConnection(self):
        """연결 및 커서 닫기 메서드"""
        if self.cursor:
            self.cursor.close()
            
        if self.connection:
            self.connection.close()