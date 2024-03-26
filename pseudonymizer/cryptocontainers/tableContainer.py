from pseudonymizer.cryptocontainers.SQLTable import SQLTable


class TableContainer(SQLTable):
    """스키마, 테이블 입출력 클래스"""
    def __init__(self):
        self._schema = None
        self._table = None

    def setSchemaTable(self, schema: str, table: str):
        """스키마, 테이블 입력 클래스"""
        self._schema = schema
        self._table = table

    def getSchema(self):
        return self._schema
    
    def getTable(self):
        return self._table

