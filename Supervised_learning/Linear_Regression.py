import numpy as np

def prediction(theta_0, theta_1, x):  # 가설함수
    return theta_0 + theta_1 * x

def prediction_difference(theta_0, theta_1, x, y): # error 리턴
    return prediction(theta_0, theta_1, x) - y

def gradient_descent(theta_0, theta_1, x, y, iterations, alpha): # 경사하강법
   for _ in range(iterations):
        error = prediction_difference(theta_0, theta_1, x, y)  # 예측값들과 입력 변수들의 오차를 계산
        theta_0 = theta_0 - alpha * error.mean()
        theta_1 = theta_1 - alpha * (error * x).mean()
   return theta_0, theta_1


# 입력 변수
house_size = np.array([0.8, 1.4, 2, 2.1, 2.6, 3.3, 3.35, 3.9, 4.4, 4.7, 5.2, 5.75, 6.7, 6.9])

# 목표 변수
house_price = np.array([0.3, 0.75, 0.45, 1.1, 1.45, 0.9, 1.8, 0.9, 1.5, 2.2, 1.75, 2.3, 2.49, 2.6])

# theta 값들 초기화 (아무 값이나 시작함)
theta_0 = 2.5
theta_1 = 0

# 학습률 0.1로 200번 경사 하강
theta_0, theta_1 = gradient_descent(theta_0, theta_1, house_size, house_price, 200, 0.1)

print(theta_0, theta_1)
