### Features

저녁에 폰을 끄면, 다시 아침에 일어난(수면시간) 시간 측정
연령별로 적절한 수면시간 기준. User의 수면시간과 비교
알맞게 자면 소정의 기프티콘
RNN or LSTM  사용시 좋음 -> 이는 시계열 데이터 필요
(한 사람의 수면시간과 성적데이터를 몇달어치를 싹 분석하는느낌)

-> 여러 사람의 데이터를 수집하여 분석은 XGBoost/MLP 회귀 모델이 좋음
목표 수면시간 + 공부시간 산출 : Grid Search or Scipy optimizer

### Target
고딩

### Thinking
<수면시간>
영향 : 카페인, 학년, 지역 등

Data(이게 제일 찾기 빡세긴함)

OECD(경제협력개발기구) : 청소년(13세 ~ 18세)에게 8~10h의 수면시간 권장
2024년 평균 청소년 남 : 6.1h,  여 : 5.6h 수면(평균값만 나와잇음)  [자료](https://data.seoul.go.kr/dataList/10961/S/2/datasetView.do)
Student Study Performance [Keggle]( https://www.kaggle.com/datasets/nabilajahan/student-study-performance/data
) (기준 : CPGA)
CGPA를 등급으로 환산필요. ([정확도](https://www.cgpa2percentage.com/#google_vignette) : 모르겟노 ?)


사는 위치, 나이, 성별 등등 종합해서 하나의 데이터 라인을 알려줌 평균값을

그럼 평균은 알겟는데, 데이터 양이 많아야 ai model에 돌릴텐데

그거 없잖슴

그래서 ai 모델에 사용은 안됨 걍 아 코렇구나 정도의 데이터임


### Blueprint

Python을 이용해 XGBoost 모델 정의 및 학습
User에게 내일 공부할 시간, 수면시간 등 데이터를 받아 모델에 넣으면 예상 성적 산출 가능
목표의 성적을 위한 최적의 수면시간 찾기
app에서 수면시간 받아오기
Server or 수동으로 모델에 입력하여 최적의 시간 계산.

추천 Tool
이정도 기능이면… 휴대폰 어플보다는 개인 노트북에 프로그램 만들어서 간단히 수면시간 넣어서 확인하는 것이 나을지도 ?
휴대폰 어플로 하면 99%이상 서버 필요. 모델의 계산값을 휴대폰에 받아와야 하기 때문
