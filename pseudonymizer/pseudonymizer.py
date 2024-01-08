# ./pseudonymizer/pseudonymizer.py

from abc import ABC, ABCMeta, abstractmethod
import pandas as pd


class Pseudonymizer(ABC):
    """가명처리 추상 클래스 및 추상 메서드 선언"""
    @abstractmethod
    def pseudonymizeData(self, value):
        """확장성을 갖춘 가명처리 클래스를 만들어 특정 가명처리 기법으로 구체화하기 위한 추상 메서드"""
        pass

    
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
    