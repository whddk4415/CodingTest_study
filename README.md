# :pencil2:코딩테스트 알고리즘 스터디
> 코딩테스트 대비 알고리즘 스터디를 위한 저장소입니다.

## :wrench:Using Programming Language
* Python, JavaScript

## 알고리즘 사이트
* **baekjoon**: https://www.acmicpc.net/
* **programmers**: https://programmers.co.kr/learn/challenges
* **hackerrank**: https://www.hackerrank.com/
* **leetcode**: https://leetcode.com/
* **codeground**: https://www.codeground.org/about
* **synap**: http://euler.synap.co.kr/
* **topcoder**: https://www.topcoder.com/
* **algospot**: https://algospot.com/judge/problem/list/
* **swexpertacademy**: https://www.swexpertacademy.com/main/main.do
* **geeksforgeeks**: https://www.geeksforgeeks.org/
* **codeforces**: http://codeforces.com

## :open_file_folder: Directory Structure
* 폴더 구조는 다음과 같다.
    * 주차별 폴더 - 문제 폴더 - 문제, 소스코드 및 풀이방법 파일
        * 예) ```1st_week ```폴더 -> ```1000``` 폴더 -> ```README.md```,```이종아.py``` , ```이종아.풀이방법.md```
    * 문제 폴더: 숫자를 우선적으로 작성, 숫자가 없다면 영어로 작성한다.
        * ```1000```, ```1234```
    * 소스코드: 자신의 ```이름``` 뒤에 ```.확장자명```으로 작성한다.
        * ```이종아.py```, ```권현빈.js```
    * 풀이방법: 자신의 ```이름``` 뒤에 ```.풀이방법.md``` 로 작성한다.
        * ```이종아.풀이방법.md```


## :memo:Commit Rule
* Commit Rule은 다음을 참고한다
    * 브랜치 생성: ```해당 주차_이름_문제 사이트_문제```
        * 예) ```1주차_이종아_백준_2060```를 브랜치 이름으로 한다.
    * ```commit message```는 자유롭게 한다.

## :page_facing_up:문제별``` README.md``` Rule
* 문제를 선정한 사람이 해당 문제 폴더에 README.md파일을 작성한다.
* 각 문제별 ```README.md``` Rule은 다음을 참고한다.
    * [README Sample](/README.sample.md)
    * 알고리즘 분류는 모든 사람이 다 해결 후 적는다.

## :triangular_ruler:문제별 ```풀이방법.md``` Rule
* 각 문제별 ```풀이방법.md``` Rule은  다음을 참고한다
    * **문제 주소**, **문제 접근 방법** 를 작성한다.
    * **문제 접근 방법** 은 되도록이면 구체적으로 작성한다.
    * [Sample](/1st_week/2606/이종아.풀이방법.md)

## :heavy_plus_sign:PullRequest(PR) Rule
* PR rule은 다음을 참고한다
    * 최소 2명 이상 리뷰가 달릴 경우에 ```PR Merge```가 가능하다.
    * ```Pull request``` 제목 및 내용은 자유롭게 한다.
    * ```Merge``` 버튼은 2명 이상이 리뷰 comment를 남겼을 때, 마지막 리뷰어가 누르는 것으로 한다. 단, 질문을 남겼을 경우 질문에 대한 답을 받고 ```Merge``` 해야한다.
    * ```Merge```는 ```Squash and Merge```를 사용하여 ```Merge```를 하고 하위 commit message를 병합한다.
    * commit message를 병합한 후 해당 commit의 제목은 다음과 같이 한다. ```해당 주차 이름 문제 사이트 문제 해결```
    	* 예) 1주차 이종아 백준 2606 

## :warning:스터디 Rule
> 주 마다 6 문제를 해결하여 각자 commit을 한다.
* 개인이 할 일
    * 문제 정하기
    	* 주차가 시작하는 첫째 날, 늦어도 둘째 날에 반드시 문제를 추가한다.
        * 자신이 원하는 사이트에서 적절한 난이도의 문제를 선택한다.
        * 해당 주차에 문제 이름을 폴더로 만들고 README.md를 작성한다.
        * 아래 [일정표](#-일정표-0315--매주-6문제)에 해당 문제를 추가한다.
	* 문제 추가 commit은 다음과 같이 한다. `주차 이름 문제 사이트 문제 추가`
		* 예) `1주차 이종아 백준 17836 추가`

    * 문제 풀이
        * 알고리즘 문제를 해결한다.
        * 각자의 풀이 방식을 ```파일이름.md``` Rule에 맞게 작성한다.
    * 공유 및 피드백
        1. 각자가 푼 문제에 대한 코드를 **브랜치**를 따서 github에 push한 후 pull request를 날린다.
        2. 상대방의 코드를 확인한 후 **리뷰나 피드백**을 작성하면 된다.
        3. 만약 리뷰나 피드백할 의견이 없을 경우 **approve** 기능을 사용해 승인해주면 된다.
        3. 2명 이상의 리뷰어가 **approve** 혹은 **리뷰나 피드백**을 작성하였을 경우, 해당하는 **브랜치**를 ```Squash and Merge```한다.
* 정기 리뷰 시간
    * 평일 목 22:00pm

## **📅 일정표 (03.15 ~ 매주 6문제)**
| |1|2|3|4|5|6|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1주차(03.15~03.21)|[트리의 지름](/1st_week/1167)|[바이러스](/1st_week/2606)|[RGB거리](/1st_week/1149)|[공주님을 구해라!](/1st_week/17836)|[봄버맨](/1st_week/16918)|[미로 탐색](/1st_week/2178)|
|2주차(03.22~03.28)|[A → B](/2nd_week/16953)|[뱀](/2nd_week/3190)|[토마토](/2nd_week/7576)|[리모컨](/2nd_week/1107)|[연속합](/2nd_week/1912)|[LCS](/2nd_week/9251)|

## **💻 문제 목록**

<details markdown="1">
<summary><strong>📄 삼성 SW 역량 테스트 기출 문제</strong></summary>

| 문제 번호 |           제목           |                  URL                  | 풀이 여부|
| :-------: | :----------------------: | :-----------------------------------: | :---:|
|   13460   |       구슬 탈출 2        | https://www.acmicpc.net/problem/13460 | &cross; |
|   12100   |        2048(Easy)        | https://www.acmicpc.net/problem/12100 |&cross;|
|   3190    |            뱀            | https://www.acmicpc.net/problem/3190  |&cross;|
|   13458   |        시험 감독         | https://www.acmicpc.net/problem/13458 |&cross;|
|   14499   |      주사위 굴리기       | https://www.acmicpc.net/problem/14499 |&cross;|
|   14500   |        테트로미노        | https://www.acmicpc.net/problem/14500 |&cross;|
|   14501   |           퇴사           | https://www.acmicpc.net/problem/14501 |&cross;|
|   14502   |          연구소          | https://www.acmicpc.net/problem/14502 |&cross;|
|   14503   |       로봇 청소기        | https://www.acmicpc.net/problem/14503 |&cross;|
|   14888   |     연산자 끼워넣기      | https://www.acmicpc.net/problem/14888 |&cross;|
|   14889   |      스타트와 링크       | https://www.acmicpc.net/problem/14889 |&cross;|
|   14890   |          경사로          | https://www.acmicpc.net/problem/14890 |&cross;|
|   14891   |         톱니바퀴         | https://www.acmicpc.net/problem/14891 |&cross;|
|   15683   |           감시           | https://www.acmicpc.net/problem/15683 |&cross;|
|   15684   |       사다리 조작        | https://www.acmicpc.net/problem/15684 |&cross;|
|   15685   |       드래곤 커브        | https://www.acmicpc.net/problem/15685 |&cross;|
|   15686   |        치킨 배달         | https://www.acmicpc.net/problem/15686 |&cross;|
|   5373    |           큐빙           | https://www.acmicpc.net/problem/5373  |&cross;|
|   16234   |        인구 이동         | https://www.acmicpc.net/problem/16234 |&cross;|
|   16235   |       나무 재테크        | https://www.acmicpc.net/problem/16235 |&cross;|
|   16236   |        아기 상어         | https://www.acmicpc.net/problem/16236 |&cross;|
|   17144   |      미세먼지 안녕!      | https://www.acmicpc.net/problem/17144 |&cross;|
|   17143   |          낚시왕          | https://www.acmicpc.net/problem/17143 |&cross;|
|   17140   |    이차원 배열과 연산    | https://www.acmicpc.net/problem/17140 |&cross;|
|   17142   |         연구소 3         | https://www.acmicpc.net/problem/17142 |&cross;|
|   17779   |       게리맨더링 2       | https://www.acmicpc.net/problem/17779 |&cross;|
|   17837   |      새로운 게임 2       | https://www.acmicpc.net/problem/17837 |&cross;|
|   17822   |       원판 돌리기        | https://www.acmicpc.net/problem/17822 |&cross;|
|   17825   |      주사위 윷놀이       | https://www.acmicpc.net/problem/17825 |&cross;|
|   19235   |      모노미노도미노      | https://www.acmicpc.net/problem/19235 |&cross;|
|   20061   |     모노미노도미노 2     | https://www.acmicpc.net/problem/20061 |&cross;|
|   19236   |       청소년 상어        | https://www.acmicpc.net/problem/19236 |&cross;|
|   19237   |        어른 상어         | https://www.acmicpc.net/problem/19237 |&cross;|
|   19238   |       스타트 택시        | https://www.acmicpc.net/problem/19238 |&cross;|
|   20055   | 컨베이어 벨트 위의 로봇  | https://www.acmicpc.net/problem/20055 |&cross;|
|   20056   |  마법사 상어와 파이어볼  | https://www.acmicpc.net/problem/20056 |&cross;|
|   20057   |  마법사 상어와 토네이도  | https://www.acmicpc.net/problem/20057 |&cross;|
|   20058   | 마법사 상어와 파이어스톰 | https://www.acmicpc.net/problem/20058 |&cross;|
------
</details>

<details markdown="1">
<summary><strong>📄 카카오 코드 페스티벌 2018 예선</strong></summary>

| 문제 번호 |   제목    |               URL                | 풀이 여부 |
| :-------: | :-------: | :------------------------------: | :-------: |
|   15953   | 상금 헌터 | http://acmicpc.net/problem/15953 | &cross;   |
|   15954   |  인형들   | http://acmicpc.net/problem/15954 | &cross;   |

------
</details>

<details markdown="1">
<summary><strong>📄 카카오 코드 페스티벌 2018</strong></summary>

| 문제 번호 |    제목    |               URL                | 풀이 여부 |
| :-------: | :--------: | :------------------------------: | :----: |
|   15997   | 승부 예측  | http://acmicpc.net/problem/15997 |&cross;|
|   15998   | 카카오머니 | http://acmicpc.net/problem/15998 |&cross;|

------
</details>

<details markdown="1">
<summary><strong>📄 SW Expert Academy 모의 SW 역량테스트 </strong></summary>

| 문제 번호 |         제목         |                             URL                              |
| :-------: | :------------------: | :----------------------------------------------------------: |
|   1949    |     등산로 조성      | [클릭](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PoOKKAPIDFAUq) |
|   1953    |     탈주범 검거      | [클릭](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpLlKAQ4DFAUq) |
|   2105    |     디저트 카페      | [클릭](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5VwAr6APYDFAWu) |
|   2112    |      보호 필름       | [클릭](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5V1SYKAaUDFAWu) |
|   2117    |    홈 방범 서비스    | [클릭](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5V61LqAf8DFAWu) |
|   2382    |     미생물 격리      | [클릭](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV597vbqAH0DFAVl) |
|   2383    |    점심 식사시간     | [클릭](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5-BEE6AK0DFAVl) |
|   4013    |     특이한 자석      | [클릭](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeV9sKkcoDFAVH) |
|   4014    |     활주로 건설      | [클릭](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeW7FakkUDFAVH) |
|   5644    |      무선 충전       | [클릭](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRDL1aeugDFAUo) |
|   5648    | 원자 소멸 시뮬레이션 | [클릭](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRFInKex8DFAUo) |
|   5650    |      핀볼 게임       | [클릭](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRF8s6ezEDFAUo) |
|   5653    |     줄기세포배양     | [클릭](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRJ8EKe48DFAUo) |
|   5656    |      벽돌 깨기       | [클릭](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRQm6qfL0DFAUo) |
|   5658    |  보물상자 비밀번호   | [클릭](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRUN9KfZ8DFAUo) |

------
</details>

<details markdown="1">
<summary><strong>📄 프로그래머스</strong></summary>

|     제목      |                           URL                            | 풀이 여부 |
| :-----------: | :------------------------------------------------------: | :----: |
|  가장 큰 수   | https://programmers.co.kr/learn/courses/30/lessons/42746 |&cross;|
|     카펫      | https://programmers.co.kr/learn/courses/30/lessons/42842 |&cross;|
|   조이스틱    | https://programmers.co.kr/learn/courses/30/lessons/42860 |&cross;|
|   숫자야구    | https://programmers.co.kr/learn/courses/30/lessons/42841 |&cross;|
|   타겟 넘버   | https://programmers.co.kr/learn/courses/30/lessons/43165 |&cross;|
|  N으로 표현   | https://programmers.co.kr/learn/courses/30/lessons/42895 |&cross;|
|  타일 장식물  | https://programmers.co.kr/learn/courses/30/lessons/43104 |&cross;|
| 전화번호 목록 | https://programmers.co.kr/learn/courses/30/lessons/42577 |&cross;|
|   네트워크    | https://programmers.co.kr/learn/courses/30/lessons/43162 |&cross;|
|     위장      | https://programmers.co.kr/learn/courses/30/lessons/42578 |&cross;|
|   단어변환    | https://programmers.co.kr/learn/courses/30/lessons/43163 |&cross;|
|      탑       | https://programmers.co.kr/learn/courses/30/lessons/42588 |&cross;|
|    H-Index    | https://programmers.co.kr/learn/courses/30/lessons/42747 |&cross;|
|   입국 심사   | https://programmers.co.kr/learn/courses/30/lessons/43238 |&cross;|
|     예산      | https://programmers.co.kr/learn/courses/30/lessons/43237 |&cross;|

------
</details>


<details markdown="1">
<summary><strong>📄 2020 카카오 인턴십 (프로그래머스)</strong></summary>

|     문제      | 레벨 |                           URL                            | 풀이 여부 |
| :-----------: | :--: | :------------------------------------------------------: | :---: |
| 키패드 누르기 |  1   | https://programmers.co.kr/learn/courses/30/lessons/67256 |&cross;|
|  수식 최대화  |  2   | https://programmers.co.kr/learn/courses/30/lessons/67257 |&cross;|
|   보석 쇼핑   |  3   | https://programmers.co.kr/learn/courses/30/lessons/67258 |&cross;|
|  경주로 건설  |  3   | https://programmers.co.kr/learn/courses/30/lessons/67259 |&cross;|
|   동굴 탐험   |  4   | https://programmers.co.kr/learn/courses/30/lessons/67260 |&cross;|

------
</details>

<details markdown="1">
<summary><strong>📄 2019 카카오 개발자 겨울 인턴십 문제 (프로그래머스)</strong></summary>

|         문제         | 레벨 |                           URL                            | 풀이 여부 |
| :------------------: | :--: | :------------------------------------------------------: | :---: |
| 크레인 인형뽑기 게임 |  1   | https://programmers.co.kr/learn/courses/30/lessons/64061 |&cross;|
|         튜플         |  2   | https://programmers.co.kr/learn/courses/30/lessons/64065 |&cross;|
|     불량 사용자      |  3   | https://programmers.co.kr/learn/courses/30/lessons/64064 |&cross;|
|     호텔 방 배정     |  3   | https://programmers.co.kr/learn/courses/30/lessons/64063 |&cross;|
|   징검다리 건너기    |  4   | https://programmers.co.kr/learn/courses/30/lessons/64062 |&cross;|

------
</details>


<details markdown="1">
<summary><strong>📄 2020 KAKAO BLIND RECRUITMENT (프로그래머스)</summary></strong>

|      문제      | 레벨 |                           URL                            | 풀이 여부 |
| :------------: | :--: | :------------------------------------------------------: | :----: |
|  문자열 압축   |  2   | https://programmers.co.kr/learn/courses/30/lessons/60057 |&cross;|
|   괄호 변환    |  2   | https://programmers.co.kr/learn/courses/30/lessons/60058 |&cross;|
| 자물쇠와 열쇠  |  3   | https://programmers.co.kr/learn/courses/30/lessons/60059 |&cross;|
| 기둥과 보 설치 |  3   | https://programmers.co.kr/learn/courses/30/lessons/60061 |&cross;|
|   외벽 점검    |  3   | https://programmers.co.kr/learn/courses/30/lessons/60062 |&cross;|
| 블록 이동하기  |  3   | https://programmers.co.kr/learn/courses/30/lessons/60063 |&cross;|
|   가사 검색    |  4   | https://programmers.co.kr/learn/courses/30/lessons/60060 |&cross;|

------
</details>

<details markdown="1">
<summary><strong>📄 2019 KAKAO BLIND RECRUITMENT (프로그래머스)</summary></strong>

|        문제        | 레벨 |                           URL                            | 풀이 여부 |
| :----------------: | :--: | :------------------------------------------------------: | :----: |
|       실패율       |  1   | https://programmers.co.kr/learn/courses/30/lessons/42889 |&cross;|
|     오픈채팅방     |  2   | https://programmers.co.kr/learn/courses/30/lessons/42888 |&cross;|
|       후보키       |  2   | https://programmers.co.kr/learn/courses/30/lessons/42890 |&cross;|
|    길 찾기 게임    |  3   | https://programmers.co.kr/learn/courses/30/lessons/42892 |&cross;|
|     매칭 점수      |  3   | https://programmers.co.kr/learn/courses/30/lessons/42893 |&cross;|
| 무지의 먹방 라이브 |  4   | https://programmers.co.kr/learn/courses/30/lessons/42891 |&cross;|
|     블록 게임      |  4   | https://programmers.co.kr/learn/courses/30/lessons/42894 |&cross;|

------
</details>

<details markdown="1">
<summary><strong>📄 2018 KAKAO BLIND RECRUITMENT (프로그래머스)</summary></strong>

|         문제          | 레벨 |                           URL                            | 풀이 여부 |
| :-------------------: | :--: | :------------------------------------------------------: | :----: |
|    [1차] 비밀지도     |  1   | https://programmers.co.kr/learn/courses/30/lessons/17681 |&cross;|
|    [1차] 다트 게임    |  1   | https://programmers.co.kr/learn/courses/30/lessons/17682 |&cross;|
| [1차] 뉴스 클러스터링 |  2   | https://programmers.co.kr/learn/courses/30/lessons/17677 |&cross;|
|   [1차] 프렌즈4블록   |  2   | https://programmers.co.kr/learn/courses/30/lessons/17679 |&cross;|
|      [1차] 캐시       |  2   | https://programmers.co.kr/learn/courses/30/lessons/17680 |&cross;|
|    [3차] 방금그곡     |  2   | https://programmers.co.kr/learn/courses/30/lessons/17683 |&cross;|
|      [3차] 압축       |  2   | https://programmers.co.kr/learn/courses/30/lessons/17684 |&cross;|
|   [3차] 파일명 정렬   |  2   | https://programmers.co.kr/learn/courses/30/lessons/17686 |&cross;|
|   [3차] n진수 게임    |  2   | https://programmers.co.kr/learn/courses/30/lessons/17687 |&cross;|
|   [1차] 추석 트래픽   |  3   | https://programmers.co.kr/learn/courses/30/lessons/17676 |&cross;|
|    [1차] 셔틀버스     |  3   | https://programmers.co.kr/learn/courses/30/lessons/17678 |&cross;|
|    [3차] 자동완성     |  4   | https://programmers.co.kr/learn/courses/30/lessons/17685 |&cross;|

------
</details>

------

## 참고사이트

* https://github.com/epicarts/algorithm-study
* https://github.com/CodeTest-StudyGroup/Code-Test-Study
