from pseudonymizer.cryptocontainers.tableContainer import TableContainer


class InitTables:
    """원본 스키마&테이블, 결합키 스키마&테이블, 결합대상정보 스키마&테이블 모으기"""
    def __init__(self):
        self.original_table = None
        self.key_table = None
        self.target_table = None
        self.serial_col = None
        self.serial_text = None
        self.key_cols = None

    def addOriginalTable(self, original_table: TableContainer):
        """원본 스키마 & 테이블 입력 메서드"""
        self.original_table = original_table

    def addKeyTable(self, key_table: TableContainer):
        """결합키 스키마 & 테이블 입력 메서드"""
        self.key_table = key_table

    def addTargetTable(self, target_table: TableContainer):
        """결합대상정보 스키마 & 테이블 입력 메서드"""
        self.target_table = target_table

    def addSerialColInfo(self, serial_col: str, serial_text: str):
        """일련번호 컬럼명 (serial_col), 일련번호 내용 (serial_text1, serial_text2 형태) 입력 메서드"""
        self.serial_col = serial_col
        self.serial_text = serial_text

    def addKeyColInfo(self, columns: list):
        """결합키 생성 항목 컬럼명 입력 메서드"""
        self.key_cols = columns
