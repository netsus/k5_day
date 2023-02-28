## 메인 페이지

<img width="1312" alt="image" src="https://user-images.githubusercontent.com/57648890/221797392-b2fd3ff3-d65c-47b1-ad03-8c2efe9a6f94.png">


## 세부 액티비티

<img width="1312" alt="image" src="https://user-images.githubusercontent.com/57648890/221797960-a24ef20e-ea26-461b-b631-06af6387a4a6.png">


- 좋아요 기능
- 댓글 달기, 수정, 삭제
- 신청하기 기능
- 신청취소 기능

## 초기 

Pycharm을 이용한 Django Project 초기 셋팅

가상환경 설정 및 django 설치
1. python -m venv venv
2. source venv/Scripts/activate
3. python -m pip install django
4. python -m djagno startapp config .
5. python manage.py migrate
6. python manage.py createsuperuser

pycharm 환경설정
1. Settings - Pyton Interpreter - 현재 가상환경 python
2. Settings - Languages & Framework - Enable Djnago
3. .gitignore 생성

black 설치 및 적용
1. python -m pip install black
2. which black -> 경로 복사
3. Settings - File Watchers - Program에 black 경로 붙여넣기. Arguments에는 FilePath, Output path, Working directory는 ProjectFileDir. Advanced Options는 모두 해제

Git 연동
1. git repository 생성
2. git remote add origin <깃 주소>
3. 커밋하고 푸시
