# 벽돌부수기 게임

## 개요
이 프로젝트는 Python과 `pygame` 라이브러리를 이용하여 개발한 벽돌부수기 게임입니다. 
플레이어는 패들을 움직여 공을 튕겨 벽돌을 부수는 것을 목표로 합니다.

## 주요 기능
- 클래식 벽돌부수기 게임 플레이
- 키보드 입력을 통한 패들 제어
- 공과 벽돌의 충돌 감지 및 처리
- 다양한 아이템 기능

## 파일 설명
### ball.py
공 객체를 정의하는 파일로, 공의 속성 및 동작을 관리합니다.
- `Ball` 클래스: 공의 초기 위치, 속도, 방향 등을 설정하고, 이동 및 충돌 로직을 포함합니다.

### button.py
게임 내 버튼을 정의하는 파일로, 다양한 버튼의 위치 및 텍스트를 관리합니다.

### game_state.py
게임의 상태를 관리하는 파일로, 게임의 주요 요소들을 초기화하고 업데이트합니다.
- `GameState` 클래스: 패들, 공, 벽돌, 아이템 등 게임 요소를 초기화하고, 게임의 시작, 일시정지, 종료 등의 상태를 관리합니다.

### main.py
게임의 메인 루프를 실행하는 파일로, 게임 실행의 핵심 로직이 포함되어 있습니다. 게임의 초기화, 이벤트 처리, 화면 업데이트 등을 담당합니다.

### maps.py
게임의 각 스테이지에 따른 벽돌 배치를 설정하는 파일입니다.
- `get_stage_1_bricks()`, `get_stage_2_bricks()`, `get_stage_3_bricks()`, `get_stage_4_bricks()` 함수: 각 스테이지의 벽돌 배치를 정의합니다.

### paddle.py
패들 객체를 정의하는 파일로, 패들의 속성 및 동작을 관리합니다.
- `Paddle` 클래스: 패들의 초기 위치, 크기, 속도 등을 설정하고, 이동 로직을 포함합니다.

### setting.py
게임의 설정을 관리하는 파일로, 화면 크기, 색상, 폰트, 이미지 로드 등을 포함합니다.

## 지원 운영 체제  (Window 이외에는 테스트해보지 못했습니다. 오류가 발생 시 윈도우로 실행 부탁드립니다.)
| OS      | 지원 여부 |
|---------|-----------|
| Windows | :o:       |
| Linux   | :o:       |
| MacOS   | :o:       |


## 설치 방법
### Windows
1. Python 3.12 설치
2. 필수 라이브러리 설치
    ```bash
    pip install pygame
    ```

3. 게임 실행
    ```bash
    python main.py
    ```

### MacOS
1. Homebrew 설치 (이미 설치되어 있다면 생략 가능):
    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```

2. Python 설치:
    ```bash
    brew install python
    ```

3. 필수 라이브러리 설치:
    ```bash
    pip install pygame
    ```

4. 게임 실행:
    ```bash
    python main.py
    ```

### Linux
1. Python 및 필수 패키지 설치:
    ```bash
    sudo apt update
    sudo apt install python3 python3-pip
    ```

2. pygame 설치:
    ```bash
    pip3 install pygame
    ```

3. 게임 실행:
    ```bash
    python3 main.py
    ```

## 게임 실행 예시
#추가예정

## 추가 기능 구현 예정
- 점수 계산 기능 추가
- 패들 이동 속도 조절 기능 추가
- 아이템 추가 (공 추가 아이템, 공 속도 증가 감소 아이템 등)
- 게임 시작, 종료, 재시작, 메뉴 버튼 추가
- 온라인 랭킹 시스템 추가

## 레퍼런스
- [Pygame 공식 문서](https://www.pygame.org/docs/)
