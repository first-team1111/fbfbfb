# 100 Prisoners Problem
## collaborate practice 🙌

## [프로그램 실행 방법]

## 실행 명령어 :thumbsup:
python fb3.py

## 실행 결과 :thumbsup:
Simulation count: 100000

Random play wins:  0.0% of simulations
Optimal play wins: 31.3% of simulations


# 깃 협업 메모❤

## 시작 방법 :bulb:
1. 팀장은 처음 깃 홈페이지 상단에서 - New organization - Free 로 만듦
2. 팀원들 메일 input box 에 넣고 클릭
3. Git clone 팀레포 주소
4. 해당 클론에서 .gitignore 생성 파일 touch 로 만들고 값 입력
5. Git add .gitignore 
6. Git add 작업파일.py
7. Git commit 
8. Git push origin main
9. 이제 팀원들은 각자 팀레포를 포크해서 포크 레포를 로컬환경에 git clone 
10. 팀원들은 git clone 한 로컬 환경에서 작업 후 포크 레포에 git add - commit - push 
11. 팀장은 팀 레포 pull requests 에 올라온  팀원들의 소스파일들을 검토하고 문제 없으면 Conversion 탭에서 Merge 함

## 궁금한 점 & 작업 메모 :rocket:
1. 팀 레포지토리에서 issue 올라온 글  pull request - Conversation 탭 에서 resolve #1 -> 이렇게 issue 번호로  comment 하면 conversation 에서 머지 했을 때 해당 issue #1 번이 자동 close	 됨
2. Mileston 만들면 해당 pull requests 올라 온 거에 할당해야 함 
	-> 	 pull requests 오른쪽 중간에 milestone 설정
3. 세모 느낌 표를 완료하면 초록색 체크표시 -> 이건 어디서 어떻게? 
4. conflict 테스트를 해봤으면 함
-> 팀원들이 같은 소스파일을 수정할 때 발생할 것으로 보임

## 팀원 각자의 포크 레포에 팀 레포 파일들을 가져와서 동기화하는 방법  :computer:
	git remote add upstream https://github.com/first-team1111/fbfbfb.git
	git remote -v
	git fetch upstream main
	git merge FETCH_HEAD

## Reference :bulb:
## gitignore 사이트 주소
https://www.toptal.com/developers/gitignore/
