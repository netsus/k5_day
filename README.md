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