#!/usr/bin/env python
# coding: utf-8

# ### 가명처리 모듈 파이썬 오픈소스 라이브러리 구현 프로젝트
# 
# **가명정보**
# 
# 개인정보 일부를 삭제, 대체하는 등 가명처리함으로써 원래 상태로 복원하기 위한 추가정보의 사용, 결합 없이는 특정 개인을 알아볼 수 없는 정보
# 
# **가명정보 처리**
# 
# 가명처리와 달리 가명정보 처리는 가명정보의 수집, 생성, 연계, 연동, 기록, 저장, 보유, 가공, 편집, 검색, 출력, 정정, 복구, 이용, 제공, 공개, 파기, 그밖에 이와 유사한 행위를 말한다. 

# **신용정보의 이용에 관한 법률 제2조제15호 및 제16호에 의한 가명정보**
# 
# 15. “가명처리”란 추가정보를 사용하지 아니하고는 특정 개인인 신용정보주체를 알아볼 수 없도록 개인신용정보를 처리(그 처리 결과가 다음 각 목의 어느 하나에 해당하는 경우로서 제40조의2제1항 및 제2항에 따라 그 추가정보를 분리하여 보관하는 등 특정 개인인 신용정보주체를 알아볼 수 없도록 개인신용정보를 처리한 경우를 포함한다)하는 것을 말한다.
#     
# 가. 어떤 신용정보주체와 **다른 신용정보주체가 구별**되는 경우
#     
# 나. 하나의 정보집합물(정보를 체계적으로 관리하거나 처리할 목적으로 일정한 규칙에 따라 구성되거나 배열된 둘 이상의 정보들을 말한다. 이하 같다)에서나 서로 다른 둘 이상의 정보집합물 간에서 어떤 신용정보주체에 관한 **둘 이상의 정보가 연계되거나 연동**되는 경우
#     
# 다. 가목 및 나목과 유사한 경우로서 대통령령으로 정하는 경우
#     
# 16. “가명정보”란 가명처리한 개인신용정보를 말한다.
# 
# **개인식별정보와 개인식별가능정보**
# 
# |  | 식별정보 | 식별가능정보 |
# | --- | --- | --- |
# | 정의 | 특정 개인과 직접적으로 연결되는 정보 | 다른 항목과 결합하는 경우 식별가능성이 높아지는 항목 해당 정보를 처리하는 자(이용 또는 제공하는 자)를 기준으로 판단 |
# | 예시 | 성명, 고유식별정보, 의료기록번호, 건강기록번호, (개인)휴대전화번호, (개인)전자우편주소 등 | 성별, 연령, 거주 지역, 국적, 직업, 위치정보 등 |

# https://github.com/ksydata/pseudonymizer/tree/main

# ---

# **가명처리의 5단계 절차**

# 1. 목적 설정 등 사전 준비 단계
#     
#     개인정보를 가명처리하는 목적을 설정한다. 개인정보 처리방침 및 내부관리계획 등 필요한 기본 서류를 작성한다. 정보주체의 동의 없이 가명처리하기 위해서는 1️⃣ 통계 작성, 2️⃣ 과학적 연구(상업 목적 연구 포함), 3️⃣ 공익적 기록 보존이라는 3가지 목적으로 한정된다. 

# 2. **위험성 검토 단계**
#     
#     가명처리 대상 데이터의 식별 위험성을 분석 · 평가한다. 데이터 식별가능성은 1️⃣ 데이터 자체의 식별 위험성(data, context side)과 2️⃣ 처리 환경의 안전성에 따른 식별 위험성으로 구분된다. 
#     
#     데이터 자체의 식별 위험성은 1️⃣ 성명 · 고유식별정보 등 데이터 식별성이 일정 수준 이상인지, 2️⃣ 특이정보(희귀 성씨 등)가 포함되어 있는지, 3️⃣ 식별될 경우 사회적 파장이 클 수 있는 정보(유명인의 정보 등)에 대한 종합 결론을 말한다. 
#     
#     처리 환경의 식별 위험성은 1️⃣ 데이터의 활용 형태(내부 이용 또는 외부 제공), 2️⃣ 처리 장소(다른 정보의 접근이 제한된 장소에서 처리되는지 여부 등),  3️⃣ 처리 방법(가명정보를 다른 정보와 연계하는지 등)을 고려해 판단한다. 
#     
#     위험성 검토 결과는 보고서로 작성되어 적정성 검토 시 활용된다.

# 3. **가명처리 단계**
# 
#     가명처리 기법과 처리 수준을 결정 · 실행한다. 대표적인 가명처리 기술은 대체 · 삭제 ·  범주화다. 1️⃣ 대체는 개인식별정보를 암호화된 일련번호(해시값)으로 대신한다. 2️⃣ 삭제는 개인정보 전부 또는 일부(행, 열, 로컬 등)를 없애는 것이다. 3️⃣ 범주화는 연속형 변수를 일정 단위로 묶는 것이다. 이외에도 4️⃣ 양쪽 끝에 치우친 정보를 삭제 또는 경계치를 입력하는 상하단 코딩 기법과 프라이버시 보호 모델(KLT 모델)이 주로 활용된다.

# 4. 적정성 검토 단계  
#     
#     내부 또는 외부 검토위원들은 가명처리 결과의 적적성을 최종 논의한다. 3명 이상의 검토위원이 도출한 최종 검토 결과를 개인정보 처리자에게 전달한다. 

# 5. 안전한 관리 단계
#     
#     가명정보[개인정보]에 대한 안전성 확보 조치를 이행하고, 처리내역을 기록 ·  보관한다. 특정 개인의 재식별 위험을 모니터링하는 것이 중요하다. 가명정보의 보유기간이 도래하면 지체없이 파기하여야 한다.

# In[1]:


import pymysql
from sqlalchemy import create_engine
# pip install mysqlclient

from abc import ABC, abstractmethod
from typing import *
import re

from prettytable import PrettyTable
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns


# **0.파이썬 스크립트를 통해 MySQL 데이터베이스에 접속하여 테이블을 조회하는 방식**
# 
# * import ⇢ db접속 ⇢ cursor 생성* ⇢ sql문 작성 ⇢ sql문 실행 ⇢ 실행 결과 확정(commit) ⇢ 연결 해제
# * 검색해온 데이터를 key:value 타입으로 가지고 오는 pymysul.cursor.Dictionary
# * insert, update, delete의 경우 자원 닫아주기 전에 commit을 해야 DB에 작업 내용이 저장
# ```
# CURSOR = PseudonymDB.cursor()
# SQL = """SELECT * FROM DATABASE.TABLE"""
# CURSOR.execute(SQL)
# PseudonymDB.commit()
# PseudonymDB.close()
# ```

# In[2]:


class PreprocessQuery:
    """데이터 전처리 목적의 SQL 쿼리 클래스"""
    def __init__(self, pw):
        self._pw = pw
        self.connection = None
        self.Cursor = None
        self.SQL = None
    
    def connectMySQL(self, 
                     serverIP: str, port_num: int, user_name: str, database_name: str, kr_encoder: str):
        """MySQL DBMS 데이터베이스에 접속: 서버IP주소, 사용자명, 계정 암호, 데이터베이스명, 한글 인코딩 방식"""
        try:
            self.connection = pymysql.connect(
                host = serverIP, port = port_num,
                user = user_name, password = self._pw,
                db = database_name, charset = kr_encoder
            )
            self.Cursor = self.makeCursor(self.connection)
        except pymysql.Error as e:
            print(f"Error Connecting to MySQL from Python: {e}")
    
    def makeCursor(self, connect):
        """커서 생성"""
        return connect.cursor()
    
    def dataQueryLanguage(self, sql):
        """SQL 쿼리문 작성"""
        self.SQL = f"{sql}"
    
    def queryExecute(self):
        """SQL 쿼리문 실행 및 예외처리"""
        try:
            self.Cursor.execute(self.SQL)
            actionOutput = self.Cursor.fetchall()
            return actionOutput
        except pymysql.Error as e:
            print(f"Error Executing Query: {e}")
    
    def queryCommit(self):
        """실행 결과 확정"""
        self.Cursor.execute(self.SQL)
        self.Cursor.commit()
    
    def closeConnection(self):
        """연결 및 커서 닫기"""
        if self.Cursor:
            self.Cursor.close()
        if self.connection:
            self.connection.close()


# In[3]:


queryObject = PreprocessQuery(pw = "0123")


# In[4]:


queryObject.connectMySQL( 
    serverIP = "localhost", port_num = 3306, user_name = "root", database_name = "FINANCIALCONSUMER", kr_encoder = "utf8")


# In[5]:


SQL = input("SQL 쿼리문 입력변수 = ")
queryObject.dataQueryLanguage(sql = SQL)
results = queryObject.queryExecute()


# In[6]:


results


# In[7]:


DQL = """SELECT 
    SUBSCRIPTION_MONTH,
    MEMBERSHIP_GRADE,
    SUBSCRIPTION_SALES * 100 / TOTAL_SALES AS PCT_TOTAL_SALES
FROM (
    SELECT 
        T1.SUBSCRIPTION_MONTH,
        T1.MEMBERSHIP_GRADE,
        T1.SUBSCRIPTION_SALES,
        SUM(T2.SUBSCRIPTION_SALES) AS TOTAL_SALES
    FROM (
        SELECT 
            DATE_FORMAT(STR_TO_DATE(SUBSCRIPTION_DATE, '%Y%m%d'), '%Y-%m') AS SUBSCRIPTION_MONTH,
            MEMBERSHIP_GRADE,
            SUM(SUBSCRIPTION_FEE) AS SUBSCRIPTION_SALES
        FROM 
            DATA_MOBILE_COMMUNICATION
        GROUP BY 
            SUBSCRIPTION_MONTH, MEMBERSHIP_GRADE
    ) AS T1
    JOIN (
        SELECT 
            DATE_FORMAT(STR_TO_DATE(SUBSCRIPTION_DATE, '%Y%m%d'), '%Y-%m') AS SUBSCRIPTION_MONTH,
            MEMBERSHIP_GRADE,
            SUM(SUBSCRIPTION_FEE) AS SUBSCRIPTION_SALES
        FROM 
            DATA_MOBILE_COMMUNICATION
        WHERE 
            MEMBERSHIP_GRADE IN ('VIP', 'VVIP')
        GROUP BY 
            SUBSCRIPTION_MONTH, MEMBERSHIP_GRADE
    ) AS T2
    ON T1.SUBSCRIPTION_MONTH = T2.SUBSCRIPTION_MONTH
    WHERE T1.MEMBERSHIP_GRADE IN ('VIP', 'VVIP')
    GROUP BY 1, 2, 3
) T3
ORDER BY 1, 2;
"""


# In[8]:


# DQL = input("SQL 쿼리문 입력변수 = ")
queryObject.dataQueryLanguage(sql = DQL)
results = queryObject.queryExecute()


# In[9]:


if results:
    # PrettyTable에 결과를 추가할 때 각 행의 값이 컬럼 수와 일치해야 함
    # ValueError: Row has incorrect number of values, (actual) 5!=1 (expected)
    columns = [ [desc[0] for desc in queryObject.Cursor.description] ]
    table = PrettyTable(*columns)
    
    for row in results:
        row_list = list(row)
        table.add_row(row_list)
    print(table)
    # ???
    # 원인은 DB에 애초에 잘못 저장된 테이블의 가입일자 컬럼에 있었음
    # 해결은 모바일 통신서비스 가입일자가 YYYYMMDD 형식이므로 일단 가변문자 타입인 VARCHAR로 선언한 후
    # DATE_FORMAT(time, timestamp)으로 형식 변환 등 수행


# In[10]:


# 월간 전체 (통신서비스 가입) 매출액 대비 멤버십 회원등급별 매출액 비율 시각화  
plt.figure(figsize = (50, 10))
plt.plot(
    pd.DataFrame(results).loc[pd.DataFrame(results)[1] == "VIP", 0],
    pd.DataFrame(results).loc[pd.DataFrame(results)[1] == "VIP", 2],
    color = "green"
)
# plt.show()
# plt.figure(figsize = (50, 10))
plt.plot(
    pd.DataFrame(results).loc[pd.DataFrame(results)[1] == "VVIP", 0],
    pd.DataFrame(results).loc[pd.DataFrame(results)[1] == "VVIP", 2],
    color = "orange"
)
plt.show()


# ---

# In[11]:


engine = create_engine(
    "mysql://root:0123@localhost/FINANCIALCONSUMER", 
    convert_unicode = True)
conn = engine.connect()


# In[12]:


DATA_FINANCE = pd.read_sql_table("DATA_FINANCE", conn)
DATA_RETAIL = pd.read_sql_table("DATA_RETAIL", conn)
DATA_MOBILE_COMMUNICATION = pd.read_sql_table("DATA_MOBILE_COMMUNICATION", conn)
DATA_JOIN_CARDPAYMENT = pd.read_sql_table("DATA_JOIN_CARDPAYMENT", conn)
DATA_FINANCE = pd.read_sql_table("DATA_FINANCE", conn)


# ---

# 1. 구현의 핵심 목표는 **가명처리 패키지를 구조화하고 필요한 기능을 제공하기 위해 디렉토리 구조와 객체 및 속성을 설계**함에 있다.

# In[13]:


# ./pseudonymizer/

class Pseudonymizer(ABC):
    """가명처리 추상 클래스 및 추상 메서드 선언"""
    @abstractmethod
    def pseudonymizeData(self, value):
        """확장성을 갖춘 가명처리 클래스를 만들어 특정 가명처리 기법으로 구체화하기 위한 추상 메서드"""
        pass


# ---

# 2. **MaskingPseudonymizer | 마스킹 적용(정규표현식을 주로 활용)**
# 
# * 성명: 직접 식별자에 대해 마스킹을 적용하여 식별성을 낮출 수 있음. 단, 이름이 세글자가 아닌 경우에는 어떻게 할지(두글자이거나 네글자 이상일 경우. 한국인이 아닌 외국인일 경우 어떻게 처리할지)
# 
# * 나이 : 간접 식별자에 대해 마스킹을 적용할 수는 있지만 마스킹 방식을 거의 사용하지 않음
# 
# * 질병코드 : 민감 질병에 대해 마스킹을 적용하여 식별성을 낮춘 사례
# 
# * 사업자 등록번호 :
# 
#     (1) 법인의 종류를 알 수 없도록 가운데 마스킹(2자릿수)
#     
#     (2) 법인의 종류만 구분가능하도록 맨 마지막 마스킹(5자릿수)
#     
# * 이메일 주소 : 메일발신기관만 구분가능하도록 마스킹하거나 발신자와 발신기관 모두 구분할 수 없도록 마스킹

# * 특수문자 체크 정규식
#   const regExp = /[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]/g;
# 
# * 모든 공백 체크 정규식
#   const regExp = /\s/g;
# 
# * 숫자만 체크 정규식
#   const regExp = /[0-9]/g;
# 
# * 이메일 체크 정규식
#   const regExp = /^[0-9a-zA-Z]([-_\.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_\.]?[0-9a-zA-Z])*\.[a-zA-Z]{2,3}$/i;
#   
# * 핸드폰번호 정규식
#   const regExp = /^\d{3}-\d{3,4}-\d{4}$/;
# 
# * 일반 전화번호 정규식
#   const regExp = /^\d{2,3}-\d{3,4}-\d{4}$/;
# 
# * 아이디나 비밀번호 정규식
#   const regExp = /^[a-z0-9_]{4,20}$/;
# 
# * 휴대폰번호 체크 정규식
#   const regExp = /^01([0|1|6|7|8|9]?)-?([0-9]{3,4})-?([0-9]{4})$/;

# In[14]:


# ./pseudonymizer/pseudonymizers/nameMasking.py

# from pseudonymizer.pseudonymizer import Pseudonymizer

class NameMaskingModule(Pseudonymizer):
    """
    성명 마스킹 클래스
    ------------------
    성명 식별자에 직접 마스킹을 적용하여 식별성을 낮추는 구체 클래스
    3자릿수가 넘는 이름은 특정인에 대한 식별가능성이 높아지므로 4자릿수로 마스킹
    """
    def pseudonymizeData(self, name):
        name_list = list(name)
        if 2 <= len(name) <= 3:
            return name_list[0] + "*"*(len(name)-1)
        else: 
            # len(name) > 4:
            return name_list[0] + "*"*3


# In[15]:


# ./pseudonymizer/pseudonymizers/emailMasking.py

# from pseudonymizer.pseudonymizer import Pseudonymizer
# import re
# from typing import *

class EmailMaskingModule(Pseudonymizer):
    """
    이메일 마스킹 클래스
    --------------------
    이메일 주소의 메일 발신자 또는 발신기관을 구분할 수 없도록 하는 구체 클래스
    """
    def __init__(self, masking_domain: bool):
        self.masking_domain = masking_domain
        
    def pseudonymizeData(self, email):
        pattern_match = re.match(
            r"^[a-zA-z0-9]([-_\.]?[a-zA-Z0-9])*@[a-zA-Z0-9]+\(.[a-zA-Z]{2,3})", email)
            # .: 정확히 1개 문자 매칭
            # * : 앞 패턴이 0개 이상이어야 함
            # ? : 앞 패턴이 없거나 하나이어야 함
            # + : 1회 이상 반복되는 패턴을 매칭
            # \. : 도메인과 최상위 도메인(TLD)에 대한 구분자 마침표 
            # {,} : 중괄호 안에 표기된 범위만큼 반복되는 패턴을 매칭. {3,5}는 3~5회 매칭을 의미함
            
        if pattern_match:
            local_part = pattern_match.group(0)
            domain_part = pattern_match.group(1)
            tld_part = pattern_math.group(2)
            # local_part, domain_part = email.split("@")
            
            if self.masking_domain:
                masked_local_part = re.sub(r"\S", "*", local_part)
                masked_domain_part = re.sub(r"\S", "*", domain_part)
                return masked_local_part + "@" + masked_domain_part + tld_part
            else:
              # self.masking_domain = False:
                masked_local_part = re.sub(r"\S", "*", local_part)
                return masked_local_part + "@" + domain_part + tld_part

        else:
            print("입력받은 { }은 이메일 패턴에 매칭되지 않아 마스킹할 수 없습니다.".format(email))
    
        # 이메일의 표준은 인터넷 표준 기구(IETF, Internet Engineering Task Force)에서 정의
        # re.sub(pattern, replace, text)


# In[16]:


# ./pseudonymizer/pseudonymizers/residentNumMasking.py

# from pseudonymizer.pseudonymizer import Pseudonymizer

class ResidentNumberMaskingModule(Pseudonymizer):
    """
    주민등록번호 마스킹 클래스
    --------------------
    주민등록번호 뒷자리를 복원할 수 없는 비가역성 기법으로 개인의 식별을 방지하는 구체 클래스
    """        
    def pseudonymizeData(self, resident_number):
        """한국 주민등록번호의 정규표현식을 기준으로 패턴 매칭이 되는 경우 뒷자리 7자리 중 
        성별정보 1자리를 제외한 나머지 출생지정보에 대한 6자리에 대한 마스킹을 수행하는 메서드"""
        pattern_match = re.match(r"^\d{6}-[1-8]\d{6}$", resident_number)
        
        if pattern_match:
            front_part, rear_part = resident_number.split("-")
            return front_part + rear_part[0] + "*"*6
            
        else:
            print("입력받은 { }은 주민등록번호 패턴에 매칭되지 않아 마스킹할 수 없습니다.".format(resident_number))


# In[17]:


# ./pseudonymizer/pseudonymizers/businessMasking.py

# from pseudonymizer.pseudonymizer import Pseudonymizer
# from typing import *

class BusinessNumberMaskingModule(Pseudonymizer):
    """
    사업자등록번호 마스킹 클래스
    --------------------
    사업자등록번호의 일부(2번째 혹은 3번째 자리)를 복원할 수 없는 비가역성 기법으로 개인의 식별을 방지하는 구체 클래스
    """
    def __init__(self, masking_part: str):
        self.masking_part = masking_part
        
    def pseudonymizeData(self, business_number):
        """한국 사업자등록번호의 정규표현식을 기준으로 패턴 매칭이 되는 경우 마스킹을 수행하는 메서드"""
        pattern_match = re.match(r"^\d{3}-\d{2}-\d{5}$", business_number)
        # ex) 124-86-23875
        
        if pattern_match:
            front_part, middle_part, rear_part = business_number.split("-")
            
           # 2번째 자리인 법인의 등록지역을 마스킹할 때
            if self.masking_part == "middle":
                return front_part + "*"*2 + rear_part
           # 3번째 자리인 법인의 일련번호를 마스킹할 때
            elif self.masking_part == "rear":
                return front_part + middle_part + "*"*5
           # 1번째 자리인 법인의 유형만을 남기고 마스킹할 때
            elif self.masking_part == "both":
                return front_part + "*"*2 + "-" + "*"*5
        else:
            print("입력받은 { }은 사업자등록번호 패턴에 매칭되지 않아 마스킹할 수 없습니다.".format(business_number))


# In[18]:


# ./pseudonymizer/pseudonymizers/phoneNumMasking.py

# from pseudonymizer.pseudonymizer import Pseudonymizer
# from typing import *

class PhoneNumberMaskingModule(Pseudonymizer):
    """
    연락처(휴대전화번호 혹은 일반전화번호) 마스킹 클래스
    --------------------
    3번째 자리를 복원할 수 없는 비가역성 기법으로 개인의 식별을 방지하는 구체 클래스
    특히 연관된 다른 정보(생년월일, 기념일, 가족 전화번호, 기존 통화내역 등)와 쉽게 결합하여 사용자가 누구인지 식별가능하다는 점에서 개인정보에 해당함
    """   
    def pseudonymizeData(self, phone_number):
        """전화번호의 정규표현식을 기준으로 패턴 매칭이 되는 경우 마스킹을 수행하는 메서드"""
        pattern_match = re.match(r"^\[0-9]-\[0-9]-\d{4}$", phone_number)
        
        if pattern_match:
            front_part, middle_part, rear_part = phone_number.split("-")
            return front_part + middle_part + "*"*4
        # 다만, 전화번호 마지막 4자리는 ****와 같은 기호로 대체하지 않고 전체를 해시값으로 암호화하기도 한다는 점에 유의하여야 함
        # 암호화와 복호화는 알고리즘 및 키 관리 등 복잡한 과정이 필요하므로 높은 보안이 필요한 경우 고려함
        else:
            print("입력받은 { }은 전화번호 패턴에 매칭되지 않아 마스킹할 수 없습니다.".format(phone_number))
            


# In[19]:


# ./pseudonymizer/pseudonymizers/maskingPseudonymizer.py

# from pseudonymizer.pseudonymizers.nameMasking import NameMaskingModule
# from pseudonymizer.pseudonymizers.emailMasking import EmailMaskingModule
# from pseudonymizer.pseudonymizers.residentNumMasking import ResidentNumberMaskingModule
# from pseudonymizer.pseudonymizers.businessNumMasking import BusinessNumberMaskingModule
# from pseudonymizer.pseudonymizers.phoneNumMasking import PhoneNumberMaskingModule

# import re
# from typing import *

    
class MaskingPseudonymizer(Pseudonymizer):
    def __init__(self, data_type: str, masking_domain: bool, masking_part: str):
        """data_type은 향후 pseudonymizer.py에서 Pseudonymn 실행 클래스의 
        self._dataframe[column] 개인식별정보의 유형으로 이름, 이메일, 주민등록번호, 사업자등록번호 중 하나로 선언"""
        self.data_type = datatype,
        self.email_masker = EmailMaskingModule(masking_domain)
        self.name_masker = NameMaskingModule()
        self.resident_num_masker = ResidentNumberMaskingModule()
        self.business_num_masker = BusinessNumberMaskingModule(masking_part)
        self.phone_num_masker = PhoneNumberMaskingModule()

    def pseudonymizeData(self, data):
        if data_type == "name":
            return self.name_masker.pseudonymzieData(data)
        elif data_type == "email":
            return self.email_masker.pseudonymzieData(data)
        elif data_type == "resident_number":
            return self.resident_num_masker.pseudonymizeData(data)
        elif data_type == "business_number":
            return self.business_num_masker.pseudonymizeData(data)
        elif data_type == "phone_number":
            return self.phone_num_masker.pseudonymizeData(data)
        else:
            raise ValueError("유효한 마스킹 대상 개인식별정보 데이터 타입이 아닙니다.")


# ---

# 3. **RoundingPseudonymizer**
# * 일반라운딩은 np.round()함수로 처리가능하므로 구현의 의미 없으므로 제외하며,
# * 제어라운딩은 라운딩 적용 전후의 항목 합계를 일치시키면서 소요되는 높은 연산량으로 실무에서 활용하지 않으므로 제외
# * 랜덤라운딩만 구현할 예정
# * 나이, 신장, 소득, 카드지출금액, 유동인구, 사용자 수 등에 적용

# In[20]:


# ./pseudonymizer/pseudonymizers/randomRoundingPseudonymizer.py

# from pseudonymizer.pseudonymizer import Pseudonymizer
# from typing import *

class RandomRoundingPseudonymizer(Pseudonymizer):
    """
    랜덤라운딩 구체 클래스
    ----------------------
    데이터의 길이가 일정하지 않은 경우 값의 크기에 따라 처리 단위를 다르게 올림, 내림, 반올림하는 가명처리 기법
    """
    def __init__(self, rounding_type):
        self.rounding_type = rounding_type
        
    def pseudonymizeData(self, numeric):
        """수치데이터를 실제 수 기준으로 자릿수 올림 또는 내림하여 일반화(범주화)하는 메서드"""
        if self.rounding_type == "round_up":
            return numeric if numeric == int(numeric) else int(numeric)+1
        elif self.rounding_type == "round_down":
            return int(numeric)
        elif self.rounding_type == "round":
            decimal_part = numeric - int(numeric)
            return int(numeric)+1 if decimal_part >= 0.5 else int(numeric)
        else:
            raise ValueError("입력받은 {}은 유효한 라운딩 방법이 아닙니다.".format(rounding_type))


# ---

# 4. **PrivacyPreservingModel | 동질 집합(Equivalent class) 찾기와 프라이버시 보호 모델에 따른 PPDM(Privacy Preserving Data Mining)**
# 
# * 데이터 비식별화 : 식별방지(식별자 제거) 및 추론방지(프라이버시 모델 준수)
# * 범주화: 연속형 변수를 일정 단위로 묶는 것
# * 프라이버시 보호 모델(KLT 모델)을 주로 활용하여 개인식별가능정보의 동질성 집합(QI)에 대한 비식별조치를 수행하는 것(K-익명성, L-다양성, T-근접성)
# * 출처: 박준범 외 2인, 관계형 데이터베이스에서 데이터 그룹화를 이용한 익명화 처리 기법, 한국전자통신연구원 25권 3호, 2015.6.
    def k_anonymity_check(self, k: int) -> bool:
        """k-익명성 체크"""
        group_sizes = self.pseudonymizer.getPseudonymizedDataframe().groupby(list(self.pseudonymizer._pseudonymDictionary.keys())).size()
        return all(group_size >= k for group_size in group_sizes)

    def l_diversity_check(self, attribute: str, l: int) -> bool:
        """l-다양성 체크"""
        grouped_data = self.pseudonymizer.getPseudonymizedDataframe().groupby(list(self.pseudonymizer._pseudonymDictionary.keys()))

        for group, data in grouped_data:
            unique_sensitive_values = data[attribute].nunique()
            if unique_sensitive_values < l:
                return False

        return True

    def t_closeness_check(self, sensitive_attribute: str, target_distribution: Dict[str, float], threshold: float) -> bool:
        """t-근접성 체크"""
        sensitive_distribution = self.pseudonymizer.getPseudonymizedDataframe()[sensitive_attribute].value_counts(normalize=True).to_dict()

        for value, target_prob in target_distribution.items():
            if value in sensitive_distribution:
                diff = abs(target_prob - sensitive_distribution[value])
                if diff > threshold:
                    return False
            else:
                return False

        return True
# In[24]:


# ./pseudonymizer/pseudonymizer/deidentificationTechnique/equivalent_class.py

class EquivalentClass:
    """개인식별가능정보 속성을 기준으로 데이터를 그룹화하는 부모 클래스
    
    준식별자를 이용한 그룹화 기법 의사코드
    --------------------------------------
    data grouping using quasi-identifier
    Input : PI(Personal Information)
    Output : Grouped PI

    grouped_PI = dict()
    for identifier, quasi in PI.items():
        key = quasi[0] + quasi[1] + quasi[2] + quasi[3]
        if key in grouping_PI:
            grouping_PI[key].append(identifier)
        else:
            grouping_PI[key] = []
            grouping_PI[key].append[identifier]

        return grouping_PI
    """
    def __init__(self, dataframe):
        self._dataframe = dataframe
        self.equivalent_class = {}

    def __str__(self):
        """캡슐화된 데이터셋의 속성(컬럼)정보를 반환하는 메서드"""
        return self._dataframe.info()
    
    def categorizeEquivalentClass(self, attributes: List[str]):
        """각 행(레코드)에 대한 개인식별가능정보 속성(컬럼)들 사이에 동질 집합을 확인하는 메서드"""
        groupby_data = self._dataframe.groupby(attributes)
        
        for group, data in groupby_data:
            if len(group) > 1:
                key = tuple(group)
                # 딕셔너리에서 키 값으로 리스트(동적 타입)는 사용할 수 없으므로 튜플로 변환
                self.equivalent_class[key] = data.index.tolist()
                # 동질 집합에 해당하는 행(레코드)의 인덱스 번호를 키 값으로 조회되도록 저장

    def removeDuplicatesInEquivalentClass(self):
        """각 동질집합 내 레코드 간 중복된 행을 제거하는 메서드"""
        for group_key, index_value in self.equivalent_class.items():
            unique_record = self._dataframe.loc[index_value, :].drop_duplicates()
            # set(self._dataframe.loc[index_value, :])
            self.equivalent_class[group_key] = unique_records.index.tolist()


# In[25]:


# ./pseudonymizer/pseudonymizer/deidentificationTechnique/kAnonimity.py

# from pseudonymizer.pseudonymizer.deidentificationTechnique.equivalent_class import EquivalentClass
# from typing import *

class K_Anonymity(EquivalentClass):
    """개별 레코드가 최소한 K개 이상 동일한 속성값을 가지도록 하는 K-익명성 클래스
    
    데이터 그룹화가 적용된 k-익명성 알고리즘 의사코드
    -------------------------------------------------
    basic k-anonymity algorithm
    Input : grouped_PI, limited_k
    Output : k_data
    
    k_data = dict()
    for key, identifiers in grouped_PI.items():
        k_anonymity = len(identifiers)
        if k_anonymity >= limited_k:
            k_data[k] = identifiers
    return k_data
    """
    def __init__(self, dataframe):
        super().__init__(dataframe)
        self.K_data = None
        
    def applyKAnonymity(self, K: int, attributes: List[str]) -> Dict:
        K_data = dict()
        # EquivalentClass 클래스의 categorizeEquivalentClass 메서드 호출
        super().categorizeEquivalentClass(attributes)

        for group_key, index_value in self.equivalent_class.items():
            K_anonymity = len(index_value)
            # index_value = identifiers
            if K_anonymity >= K:
                K_data[group_key] = index_value
        self.K_data = K_data


# In[26]:


K_DATA_FINANCE = K_Anonymity(dataframe = DATA_FINANCE)


# In[27]:


K_DATA = K_DATA_FINANCE.applyKAnonymity(K = 5, attributes = ["AGE", "TF_PENSION"])


# In[29]:


# DATA_FINANCE.iloc[K_DATA.get((80, 'Y')), :].head(3)
# DATA_FINANCE.iloc[K_DATA.get((80, 'Y')), DATA_FINANCE.columns.get_loc("TF_LOAN")]


# In[114]:


# ./pseudonymizer/pseudonymizer/deidentificationTechnique/lDiversity.py

# from pseudonymizer.pseudonymizer.deidentificationTechnique.equivalent_class import EquivalentClass
# from typing import *

class L_Diversity(K_Anonymity):
    """각 동질집합 내 특정 민감 속성의 빈도가 L값 이상의 다양성을 가지도록 하는 L-다양성 클래스
    k-익명성 보호 모델 적용 결과에 l-다양성 보호 모델을 적용
    
    k-익명성 처리가 그룹 단위로 구현된 상황에서 l-다양성 알고리즘 의사코드
    ----------------------------------------------------------------------
    basic l-diversity algorithm
    Input : k_data, limited_l
    Output : l_data
    
    l_data = dict()
    for key, identifiers in k_data.items():
        l_list = []
        for identifier in identifiers:
            # k익명성을 만족하는 데이터의 식별자값을 가지고 
            user_info = data[identifier]
            # 해당 식별자값의 민감정보를 가져오는 부분
            user_sa = user_info[4]
            if user_sa in l_list:
                pass
    """
    def __init__(self, dataframe):
        """모듈의 유연성을 제공하기 위해 K익명성 클래스를 확장하여 손자 클래스로 정의"""
        super().__init__(dataframe)
        self.L_data = None
        sensitive_attribute = None
        self.LocalL_data = None
        
    def applyLDiversity(self, K: int, L: int, attributes: List[str], sensitive_attribute: str):
        """두 모형을 동시에 적용할 경우 중복이 발생할 가능성이 높아 조합적인 보호 모델을 설계하여 중복을 최소화하는 메서드"""
        super().applyKAnonymity(K, attributes)
        L_data = dict()
        self.sensitive_attribute = sensitive_attribute
        
        for group_key, index_value in self.K_data.items():
            unique_sensitive_values = self._dataframe.loc[index_value, 
                                                          sensitive_attribute].unique()
            # self._dataframe.iloc[index_value, self._dataframe.columns.get_loc(column_name)]
            if len(unique_sensitive_values) >= L:
                L_data[group_key] = index_value
        self.L_data = L_data
        # return L_data
    
    def applyLocalLDiversity(self, local_L: int):
        """특정 민감정보의 속성값이 일부 레코드(행)에 집중되는 문제에 따라
        전체적으로 안전한 다양성을 확보할 수 있도록 l-로컬 다양성을 적용하는 메서드"""
        LocalL_data = dict()
        
        for group_key, index_value in self.L_data.items():
            count_local_diversity = self._dataframe.loc[index_value, self.sensitive_attribute].value_counts()
            if count_local_diversity.min() >= local_L: 
                LocalL_data[group_key] = index_value
        self.LocalL_data = LocalL_data
        # return LocalL_data


# In[115]:


L_DATA_FINANCE = L_Diversity(dataframe = DATA_FINANCE)


# In[116]:


L_DATA_FINANCE.applyLDiversity(K = 5, L = 8, 
                               attributes = ["AGE", "TF_PENSION", "TF_LOAN"], sensitive_attribute = "HOME_TYPE")


# In[117]:


L_DATA_FINANCE.applyLocalLDiversity(local_L = 5)


# In[82]:


Counter(DATA_FINANCE.loc[L_DATA.get((23, 'N', 'N')), "HOME_TYPE"])


# In[65]:


# DATA_FINANCE.loc[L_DATA.get((50, 'Y', 'Y')), "HOME_TYPE"]
# ValueError: Location based indexing can only have [integer, integer slice (START point is INCLUDED, END point is EXCLUDED), listlike of integers, boolean array] types


# In[ ]:


# ./pseudonymizer/pseudonymizer/deidentificationTechnique/tCloseness.py

# from pseudonymizer.pseudonymizer.deidentificationTechnique.equivalent_class import EquivalentClass
# from typing import *

class T_Closeness(EquivalentClass):
    """민감 정보(SA)의 분포를 전체 데이터 셋의 분포와 유사하도록 하는 T-근접성 클래스
    
    l-다양성과 달리 민감정보를 원본 그대로 배열에 저장한 후 
    데이터를 내림차순 정렬하여 
    데이터의 분포도를 측정하는 t-근접성 알고리즘 의사코드
    -----------------------------------------------------
    basic Earth Mover's Distance algorithms
    Input : t_list
    Output : EMD
    
    total_range = []
    for n in range(100):
        total_range.append(n)
        # 설정된 배열에 정수가 순서대로 추가
        total_length = len(total_info)
        
        static_part = total_length / len(t_list)
        # EMD(데이터의 분산 정도)를 계산하기 위해 나눗셈
        extra_part = float(static_part) % float(len(t_list))
        extra_part = extra_part.split(".")[0]
        # 나누어 떨어지지 않는 여분으로 연산해주어야 할 때 계산

        balance_value = len(t_list) - (extra_part)
        active_loop = True
        
        count_t = 0, hap = 0
        for a in t_list:
        # 데이터의 분산도 측정
            count_t += 1
            for i in range(static_part):
                gap = int(a) - (total_info[count_m])
                if gap < 0:
                    gap *= -1
                    hap += gap
            
            if count_t >= balance_value and active_loop == True:
            # 여분의 연산으로 하는 부분(나누어 떨어지지 않는 수)에 대하여
            # 배열의 마지막 부분에서 처리
                active_loop = False
                static_part += 1
            
            hap = float(hap) / float(total_length)
            return hap
    """
    pass


# In[ ]:


def K_Anonymity(self, K: int): # sensitive_attributes):
    """개별 레코드가 최소한 K개 이상의 동일한 속성값을 가지도록 하는 K-익명성 메서드"""
    for group_key, index_value in self.equivalent_class.items():
        if len(set(self._dataframe.loc[index_value, :])) <= K:
        # print( Counter(self._dataframe.loc[index_value, sensitive_attributes]) )
            print( group_key, 
                  len(set(self._dataframe.loc[index_value, :])),"\n", 
                  self._dataframe.loc[index_value, :],"\n")
        else:
            break


# In[ ]:


PPDM = PrivacyPreservingModel(dataframe = DATA_FINANCE)


# In[ ]:


DATA_FINANCE.value_counts


# In[ ]:


PPDM = PrivacyPreservingModel(dataframe = DATA_FINANCE)


# In[ ]:


# TypeError: __str__ returned non-string (type NoneType)
# print(PPDM)


# In[ ]:


# AttributeError: 'PrivacyPreservingModel' object has no attribute 'equivalent_class'
PPDM.categorizeEquivalentClass(attributes = ["AGE", "TF_LOAN", "TF_PENSION"])


# In[ ]:


PPDM.K_Anonymity(K = 20)
# PPDM.K_Anonymity(K = 3, sensitive_attributes = "HOME_TYPE")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ---

# 5. **가명처리 결합**
# 
# 결합키(이름, 생년월일, 연락처 등을 활용하여 생성한 암호화된 해시값), 결합키연계정보(결합키가 동일한 정보를 결합할 수 있도록 서로 다른 결합신청자의 결합키를 연계한 정보)

# ---

# 6. **가명처리 실행 클래스**

# In[ ]:


# ./pseudonymizer/pseudonymizer.py

# from abc import ABC, ABCMeta, abstractmethod
# import pandas as pd
    
class Pseudonym:
    def __init__(self, dataframe):
        """원본정보(재현데이터)와 가명처리 구체 클래스를 인스턴스 변수로 선언하는(초기화) 생성자"""
        self._dataframe = dataframe
        self._pseudonymizers = []
        self._pseudonymDictionary = {}
        
    def addPseudonymizer(self, pseudonymizer):
        """가명처리 추상 클래스에 대한 자식 클래스를 입력받는 pseudonymizer파라미터를 가지는 메서드"""
        if isinstance(pseudonymizer, Pseudonymizer):
            self._pseudonymizers.append(pseudonymizer)
        else:
            print("입력받은 {} 기술은 가명처리 기법에 추가할 수 없습니다.".format(pseudonymizer))
    
    def addDictionary(self, column, pseudonymizers):
        """가명처리를 수행할 데이터 컬럼명과 해당 열에 적용할 여러 가명처리 기법 리스트를 입력받아 다양한 비식별 조치를 수행할 수 있도록 지정하는 메서드"""
        self._pseudonymDictionary[column] = pseudonymizers
        
    def pseudonymizeData(self):
        """가명처리 기법을 해당 컬럼에 적용하는 메서드(apply함수를 활용하여 데이터프레임 모든 행, 특정 열에 비식별조치를 취하는 접근방식) """
        for column, pseudonymizers in self._pseudonymDictionary.items():
            for pseudonymizer in pseudonymizers:
                self._dataframe[column] = self._dataframe[column].apply(pseudonymizer.pseudonymizeData)

    def getPseudonymizedDataframe(self):
        """가명처리 데이터 반환"""
        return self._dataframe
    
    # def getAge(self): 
        # """getattr method: 숨겨놓은 변수 __age의 값을 전달하는 메서드"""
        # return self.__age
        
    # def setAge(self, value):
        # """setattr method: 숨겨놓은 변수 __age의 값을 설정(변경)하는 메서드"""
        # if value < 0:
           # print("나이는 0보다 작을 수 없습니다.")
           # self.__age = 0
        # else: 
           # self.__age = value


# In[ ]:


# PseudonymizeFinanceData = Pseudonym(dataframe = DATA_FINANCE)


# ---

# 7. **가명처리 모듈 활용 예제 스크립트**
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
# In[ ]:




