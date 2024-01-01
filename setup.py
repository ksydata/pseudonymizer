import setuptools
from glob import glob
from os.path import basename, splitext
from setuptools import find_packages, setup

with open("README.md", "r", encoding = "utf-8") as fh:
          long_description = fh.read()
# 모듈에서 사용가능한 함수의 목록
        
setuptools.setup(
    name = "pseudonymizer,
    version = "0.1.1",
    author "SY",
    author_email = "ksydata01@gmail.com",
    description = "pseudonymizer-for-protect-privatedata",
    long_description = open("README.md").read()
    long_description_content_type = "text/markdown",
    url = "https://github.com/ksydata/",
    # 모듈 의존성 관리
    install_requires = [
        "pandas==1.4.4",
        "PyMySQL==1.1.0",
        "numpy==1.21.5",
        "scipy==1.9.1", S
        "matplotlib==3.5.2", 
        "seaborn==0.11.2", 
        "setuptools==63.4.1"
    ],
    # extras_require={"":[]},
    # 필요한 dependencies를 설치하기 위해 requirements.txt를 만드는 것
    # package_data = {"":["LICENSE.txt", "requirements.txt"]},
    include_package_data = True,
    packages = setuptools.find_packages(),
    python_requires = ">3.6"
)