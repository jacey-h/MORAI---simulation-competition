# Automous driving competition - MORAI simulation

MORAI 가상 시뮬레이션 환경에서 주어진 미션을 완수하도록 주행시키기

Sensor
    
![image](https://user-images.githubusercontent.com/81483791/171255354-c441f96b-7129-4e08-b8f5-2b21f3ff0587.png)

- GPS
- Camera
- 2D Lidar

### 1. Object detection using Lidar sensor    


https://user-images.githubusercontent.com/81483791/171255614-2f02cc9f-1714-4de4-a59b-948604291020.mp4


차량 앞에 장애물이 있으면

장애물이 있다 : 0

장애물이 없다 : 1

0 또는 1의 데이터를 보내줌

### 2. Vehicle control with Matlab Simulink

- Pure Pursuit algorithm     
![image](https://user-images.githubusercontent.com/81483791/171255726-11f10691-14e0-447e-9556-f128465315b6.png)


차량이 현재위치에서 목표점까지 이동하기 위한 곡률을 계산해 작동하는 경로추종 알고리즘

차량에서 일정거리 앞에 위치한 경로상의 목표점을 선택함

목표지점(Gx,Gy)를 추종하기 위한 차량의 조향각(세타)을 구할 수 있음

Look-ahead-distance는 차량의 후륜에서 목표지점까지의 직선거리     
![image](https://user-images.githubusercontent.com/81483791/171255764-95c5438d-f939-4a5b-92be-6cba9b93a263.png)


1. LD를 짧게 설정할 경우 : 차량이 경로상으로 빠르게 복귀해야하는 경우
2. LD를 길게 설정할 경우 : 차량이 경로를 부드럽게 주행하기 위해서

게인 값 조정을 통해 차량 제어

- Simulink model
     
![image](https://user-images.githubusercontent.com/81483791/171255806-cf44b1d2-3882-424f-aec0-a3647191eb37.png)


- path making      

![image](https://user-images.githubusercontent.com/81483791/171255845-411f1f51-b70a-4149-a2b8-fc77f2fa0101.png)

Pure pursuit 알고리즘은 차량에서 가장 가까운 경로상의 점을 찾아서 가므로

Path를 3구간으로 나누어 주행하도록 함

- State Flow      
![image](https://user-images.githubusercontent.com/81483791/171256639-2fc56f0d-80af-49a5-a669-920886a28d48.png)      
rpm : 속도 제어     

ld값과 g값을 바꿔가며 차량 제어

### 시범 주행 영상



https://user-images.githubusercontent.com/81483791/171256401-b919ca07-0f8b-457d-a920-5032d7b04ea0.mp4

