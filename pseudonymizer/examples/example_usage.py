# ./pseudonymizer/example/example_usage.py

from pseudonymizer.pseudonymizer import Pseudonym
from pseudonymizer.pseudonymizers.{MODULE.py} import {MODULE}Pseudonymizer


# DB 데이터프레임 생성
Engine = create_engine(
    "mysql://{user_name}:{password}@localhost/{database}".format(root, 0123, FINANCIALCONSUMER), 
    convert_unicode = True)
Connection = Engine.connect()

DATA = pd.read_sql_table("DATA", Connection)


# Pseudonymizer 추상클래스 인스턴스 생성 및 추가
{MODULE}_pseudonymizer = {MODULE}Pseudonymizer
pseudonym_instance = Pseudonym(dataframe = DATA)

# Pseudonymizer의 인스턴스를 입력변수로 설정
pseudonym_instance.addPseudonymizer(pseudonymizer = {MODULE}_pseudonymizer)

# DATA의 특정 컬럼에 가명처리 기법을 적용하기 위한 Dictionary에 입력
pseudonym_instance.addDictionary(column = "PHONE_NUMBER", pseudonymizers = [{MODULE}_pseudonymizer])

# 가명처리 수행
pseudonym_instance.pseudonymizeData()

# 가명처리 데이터프레임 반환
print(pseudonym_instance.getPseudonymizedDataframe())
