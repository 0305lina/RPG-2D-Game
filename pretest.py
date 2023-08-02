import pygame
import sqlite3

# 데이터베이스 연결
conn = sqlite3.connect('character.db')
cursor = conn.cursor()

# 데이터베이스 테이블 생성
cursor.execute('''
    CREATE TABLE IF NOT EXISTS character (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        eye_color TEXT,
        size INTEGER
    )
''')
conn.commit()

# 캐릭터 정보 조회 예시
cursor.execute('SELECT * FROM character')
result = cursor.fetchall()
for row in result:
    print(row)

# pygame 초기화
pygame.init()

# 창 크기 설정
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Character Customization")

# 캐릭터 이미지 로드
character_image = pygame.image.load("character.png")  # 이미지 파일 경로에 맞게 수정해주세요.

# 눈 색깔 리스트
eye_colors = ['blue', 'green', 'brown']

# 현재 눈 색깔 인덱스
current_eye_color_index = 0

# 캐릭터 정보 업데이트 함수
def update_character():
    # 데이터베이스 업데이트
    cursor.execute('UPDATE character SET eye_color = ? WHERE id = ?', (eye_colors[current_eye_color_index], 1))
    conn.commit()

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # 눈 색깔 변경
            if event.key == pygame.K_SPACE:
                current_eye_color_index = (current_eye_color_index + 1) % len(eye_colors)
                update_character()

    # 화면 그리기
    screen.fill((255, 255, 255))  # 배경색

    # 캐릭터 이미지 그리기
    screen.blit(character_image, (width // 2 - character_image.get_width() // 2, height // 2 - character_image.get_height() // 2))

    # 눈 색깔 변경
    eye_color = eye_colors[current_eye_color_index]
    pygame.draw.circle(screen, eye_color, (width // 2 + 50, height // 2 - 50), 10)  # 캐릭터의 눈

    pygame.display.flip()

# 게임 종료
pygame.quit()
conn.close()
