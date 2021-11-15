# Welcome to DOTORI World 🐿

2021년 11월 15일에 개설된 동국대학교 알고리즘 스터디 그룹입니다.

알고리즘 풀이 언어는 **파이썬**입니다.

백준 단계별로 풀기 완료 후, 프로그래머스 문제 풀이로 넘어갑니다.

1일 1커밋(1문제 이상 풀이)을 목표로 하며, 주 1회 코드 리뷰를 진행합니다.

문제 풀기전에 본인 알고리즘 시간복잡도 대략 계산해본 후 코딩을 시작합니다.
👉 [시간복잡도 계산](https://life-with-coding.tistory.com/273)


## ✅ 파일 및 폴더 구조
- 백준 <br>
```/깃허브아이디/플랫폼/카테고리/문제번호.py``` 형식으로 업로드해주세요. <br>
  - 예시 01: /leeez0128/backjoon/DFS와 BFS/1260.py
- 프로그래머스 <br>
```/깃허브아이디/플랫폼/카테고리 or 문제 모음/문제명.py``` 형식으로 업로드해주세요. <br>
  - 예시 01: /leeez0128/programmers/해시/완주하지_못한_선수.py
  - 예시 02: /leeez0128/programmers/2021 KAKAO BLIND RECRUITMENT/신규_아이디_추천.py

<br>

## ✅ 스터디 규칙
### 1. 소통 방법
해당 레파지토리는 Slack과 연동되어 모든 커밋은 Slack 알림으로 뜨게 됩니다.<br>
태그나 피드백이 필요한 경우, Slack의 멘션과 스레드를 이용하여 작성합니다. 

### 2. 주 1회 코드리뷰
대면/비대면 혼용 방식으로 매주 토요일 저녁에 진행합닏.

### 3. 풀이 고민 시간 : 30분~60분
최소 30분 이상 문제 풀이방법에 대해 고민합니다. <br>
한 시간 경과 후에는 솔루션을 찾아 공부하며, 솔루션을 참고하여 풀이한 방식은 코드 리뷰에 필수적으로 포함됩니다.

<br>

## ✅ 알고리즘 규칙

### 1. 명확한 변수명과 로직
코드리뷰의 가독성을 위해, 변수명과 로직을 명확하게 하도록 노력합니다. <br>
현업에서 내가 짠 코드를 <b>나 혹은 다른 사람이 이해할 수 있게 짜는</b> 배려가 중요합니다. <br>
주석을 달지 않아도 이해할 수 있을 정도의 코드를 짜봅시다.


### 2. PEP 8 스타일 준수
   ☝️ pycodestyle 모듈을 설치합니다. (구. pep8 모듈)
   ``` shell
   pip install pycodestyle
   ```
   
   ✌️ python 코드를 작성한 후, 가이드를 준수했는지 확인합니다. <br>
   (--show-source 옵션은 미준수 소스코드도 함께 출력합니다)
   ``` shell
   pycodestyle --show-source mycode.py
   ```
   
   🤟 결과를 확인합니다.  <br>
   👉 2가지 요소가 미준수 상태입니다 <br>
   &nbsp;&nbsp;&nbsp;&nbsp;✔️ 한줄에 한개 모듈을 import 하도록 권장합니다 (E401) <br>
   &nbsp;&nbsp;&nbsp;&nbsp;✔️ 쉼표(,) 뒤에는 공백을 권장합니다. (E231) <br>
   ``` python
   mycode.py:1:11: E401 multiple imports on one line
   import sys, os
             ^
   mycode.py:6:11: E231 missing whitespace after ','
   def plus(x,y):
             ^
   ```
|코드 앞 2자리 정의|E*|W*|
|------|---|---|
||E1: Indentation|W1: Indentation warning|
||E2: Whitespace|W2: Whitespace warning|
||E3: Blank line|W3: Blank line warning|
||E4: Import||
||E5: Line length|W5: Line break warning|
|||W6: Deprecation warning|
||E7: Statement||
||E9: Runtime||
