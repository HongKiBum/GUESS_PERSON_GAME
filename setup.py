from setuptools import setup, find_packages

setup(
    name="guess_person_game",  # 패키지 이름
    version="0.1.0",  # 패키지 버전
    author="HONGKIBUM",  # 작성자 이름
    author_email="hgb9720@hanyang.ac.kr",  # 작성자 이메일
    description="A fun guessing game to match people with their images.",  # 간단한 설명
    long_description=open("README.md", "r", encoding="utf-8").read(),  # 상세 설명
    long_description_content_type="text/markdown",  # README 형식
    url="https://github.com/YourUserName/GUESS_PERSON_GAME",  # GitHub URL
    packages=find_packages(),  # 자동으로 패키지 탐색
    include_package_data=True,  # 리소스 파일 포함
    install_requires=["kivy"],  # 의존성 패키지
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",  # 지원하는 Python 버전
)
