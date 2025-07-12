import thinker as tk
import xgboost as xgb
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

# 1. 데이터셋 불러오기
df = pd.read_csv("Student_Study_data.csv")

# 2. 불필요한 컬럼 제거 (예: 이름, 날짜 등)
df = df.drop(columns=["Name", "Date"])

# 3. 범주형 변수 One-hot 인코딩
df = pd.get_dummies(df, columns=["Day", "weekend", "Marital Status", "Your gender?"], drop_first=True)

# 4. 특징 변수(X), 타겟 변수(y) 설정
X = df.drop(columns=["what is your cgpa"])
y = df["what is your cgpa"]

# 5. XGBoost 회귀 모델 학습
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = xgb.XGBRegressor()
model.fit(X_train, y_train)

# 6. 최적 조합 찾는 함수 정의
def predict_best_combination(goal_cgpa):
    study_range = np.arange(10, 80, 1)       # 예: 주당 10~80시간 공부
    sleep_range = np.arange(20, 80, 1)       # 예: 주당 20~80시간 수면
    min_error = float("inf")
    best_combination = None

    for study in study_range:
        for sleep in sleep_range:
            # 기본 입력 샘플에서 복사
            sample = X.iloc[0].copy()
            sample["study hour"] = study
            sample["your sleep hour?"] = sleep

            pred = model.predict(pd.DataFrame([sample]))[0]
            error = abs(pred - goal_cgpa)

            if error < min_error:
                min_error = error
                best_combination = (study, sleep, pred)

    return best_combination

# 7. GUI 생성
app = tk.App("목표 CGPA 예측기")

cgpa_label = tk.Label(app, text="목표 CGPA를 입력하세요 (예: 3.5)")
cgpa_label.pack()

cgpa_input = tk.Entry(app)
cgpa_input.pack()

result_label = tk.Label(app, text="", wraplength=400)
result_label.pack()

def on_predict_click():
    try:
        goal_cgpa = float(cgpa_input.get())
        study, sleep, predicted = predict_best_combination(goal_cgpa)

        result = f"""🎯 목표 CGPA: {goal_cgpa}
📚 최적 공부 시간: {study} 시간/주
😴 최적 수면 시간: {sleep} 시간/주
📈 예측된 CGPA: {predicted:.2f}"""
        result_label.config(text=result)
    except Exception as e:
        result_label.config(text=f"오류 발생: {e}")

predict_button = tk.Button(app, text="최적 시간 예측하기", command=on_predict_click)
predict_button.pack()

# 실행
app.run()
