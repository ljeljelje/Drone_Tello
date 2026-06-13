# DJI Tello Drone (2024-2)

## 1. 프로젝트 소개

본 프로젝트는 Python을 이용하여 DJI Tello 드론을 제어하는 실습 프로젝트입니다.

`djitellopy` 라이브러리를 기반으로 Tello 드론과 연결하고, 기본 이동, 카메라 스트리밍, 키보드 조종, 사진 저장, ArUco Marker 인식 실습을 수행합니다.

드론 제어와 영상처리 기초를 함께 학습하는 것을 목표로 합니다.

---

## 2. 주요 기능

- DJI Tello 드론 연결
- 배터리 상태 확인
- 이륙 및 착륙 제어
- 전진, 후진, 좌우 이동
- 상승, 하강 제어
- 시계방향 및 반시계방향 회전
- OpenCV 기반 카메라 스트리밍
- 키보드 입력 기반 드론 조종
- Tello 카메라 이미지 저장
- ArUco Marker 인식 및 추적 실습

---

## 3. 개발 환경

본 프로젝트는 다음 환경을 기준으로 작성되었습니다.

- Python 3.x
- DJI Tello Drone
- Windows 또는 Ubuntu 환경
- OpenCV
- DJITelloPy
- Pygame
- NumPy
- imutils

---

## 4. 설치 방법

필요한 Python 패키지를 설치합니다.

```bash
pip install djitellopy
pip install opencv-python
pip install pygame
pip install numpy
pip install imutils
```

ArUco Marker 예제를 실행하려면 추가 패키지가 필요할 수 있습니다.

```bash
pip install droneblocksutils
```

---

## 5. 파일 구성

```text
Drone_Tello/
├── README.md
├── main.py
├── BasicMove.py
├── TelloCam.py
├── Take_picture.py
├── Record_TelloCam.py
├── Keyboard_opencv.py
├── Keyboard_pygame.py
└── Aruco_Marker/
    ├── 0.png
    ├── 1.png
    ├── 2.png
    ├── 3.png
    ├── 4.png
    ├── 5.png
    ├── 6.png
    ├── 7.png
    ├── 8.png
    ├── 9.png
    ├── aruco-marker-flying.py
    ├── aruco_marker_test.py
    ├── aruco_mouse_tracking.py
    ├── basic_droneblocks_marker_test.py
    ├── tello_script_runner.py
    ├── tello_drone_image.png
    └── test.JPG
```

---

## 6. 파일별 설명

| 파일명 | 설명 |
|---|---|
| `main.py` | Tello 객체 생성 및 드론 연결 기본 예제 |
| `BasicMove.py` | 이륙 후 전진, 좌우 이동, 회전, 착륙을 수행하는 기본 이동 예제 |
| `TelloCam.py` | Tello 카메라 영상을 OpenCV 창에 출력하는 예제 |
| `Take_picture.py` | Tello 카메라 프레임을 이미지 파일로 저장하는 예제 |
| `Record_TelloCam.py` | 카메라 화면을 보면서 키보드로 드론을 조종하는 예제 |
| `Keyboard_opencv.py` | OpenCV 키 입력을 이용한 드론 조종 예제 |
| `Keyboard_pygame.py` | Pygame 화면과 키보드 입력을 이용한 드론 조종 예제 |
| `Aruco_Marker/` | ArUco Marker 이미지 및 마커 인식/추적 실습 코드 |

---

## 7. OpenCV 키보드 조종

`Keyboard_opencv.py`는 OpenCV 창에서 키보드 입력을 받아 Tello를 제어합니다.

조작 키:

| 키 | 동작 |
|---|---|
| `W` | 전진 |
| `S` | 후진 |
| `A` | 왼쪽 이동 |
| `D` | 오른쪽 이동 |
| `E` | 시계방향 회전 |
| `Q` | 반시계방향 회전 |
| `R` | 상승 |
| `F` | 하강 |
| `ESC` | 착륙 후 종료 |

---

## 8. ArUco Marker 예제

`Aruco_Marker` 폴더에는 ArUco Marker 이미지와 마커 인식 실습 코드가 포함되어 있습니다.

주요 파일:

| 파일명 | 설명 |
|---|---|
| `aruco_marker_test.py` | 이미지에서 ArUco Marker를 검출하는 테스트 |
| `aruco_mouse_tracking.py` | 마우스 위치와 ArUco Marker 중심 사이의 거리 시각화 |
| `basic_droneblocks_marker_test.py` | DroneBlocks 유틸 기반 ArUco Marker 검출 예제 |
| `aruco-marker-flying.py` | Tello 영상에서 ArUco Marker를 찾고 위치 오차를 기반으로 이동 명령을 계산하는 예제 |
| `0.png` ~ `9.png` | ArUco Marker 이미지 |
| `test.JPG` | ArUco Marker 테스트용 이미지 |

