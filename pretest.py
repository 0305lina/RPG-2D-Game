import pygame
#import sqlite3

# 데이터베이스 연결
#connection = sqlite3.connect('characters.db')
#cursor = connection.cursor()

# 캐릭터 선택 페이지 초기화
def character_selection():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Character Selection")

    # 캐릭터 이미지 로드
    rabbit_img = pygame.image.load('spaceship1.png')
    bear_img = pygame.image.load('spaceship1.png')
    dog_img = pygame.image.load('spaceship1.png')

    # 기본 이미지 크기와 선택된 이미지 크기 설정
    default_size = (200, 200)
    selected_size = (200, 200)

    # 캐릭터 이미지 버튼 생성 (위치와 크기를 이미지와 동일하게)
    rabbit_button = pygame.Rect(100, 200, rabbit_img.get_width(), rabbit_img.get_height())
    bear_button = pygame.Rect(300, 200, bear_img.get_width(), bear_img.get_height())
    dog_button = pygame.Rect(500, 200, dog_img.get_width(), dog_img.get_height())

    # 캐릭터 선택 상태 변수
    selected_character = None

    done_button_rect = pygame.Rect(300, 500, 200, 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if done_button_rect.collidepoint(pygame.mouse.get_pos()):
                    #if selected_character:
                        # 선택한 캐릭터를 데이터베이스에 저장
                        #cursor.execute("INSERT INTO characters (character_name) VALUES (?)", (selected_character,))
                        #connection.commit()
                        p#ygame.quit()
                        #return
                # 캐릭터 이미지 버튼 클릭 시 선택된 캐릭터 변경 및 이미지 크기 조정
                elif rabbit_img.get_rect(topleft=(100, 200)).collidepoint(pygame.mouse.get_pos()):
                    selected_character = "rabbit.png"
                    rabbit_img = pygame.transform.scale(rabbit_img, selected_size)
                elif bear_img.get_rect(topleft=(300, 200)).collidepoint(pygame.mouse.get_pos()):
                    selected_character = "bear.png"
                    bear_img = pygame.transform.scale(bear_img, selected_size)
                elif dog_img.get_rect(topleft=(500, 200)).collidepoint(pygame.mouse.get_pos()):
                    selected_character = "dog.png"
                    dog_img = pygame.transform.scale(dog_img, selected_size)

        # 배경 화면 그리기
        screen.fill((255, 255, 255))

        # 캐릭터 이미지 버튼 그리기
        screen.blit(rabbit_img, (100, 200))
        screen.blit(bear_img, (300, 200))
        screen.blit(dog_img, (500, 200))

        # Done 버튼 그리기
        pygame.draw.rect(screen, (0, 255, 0), done_button_rect)
        font = pygame.font.SysFont(None, 40)
        done_text = font.render("Done", True, (0, 0, 0))
        screen.blit(done_text, (340, 510))

        pygame.display.update()

# 데이터베이스 테이블 생성
#def create_table():
#    cursor.execute("CREATE TABLE IF NOT EXISTS characters (id INTEGER PRIMARY KEY, character_name TEXT)")

# 메인 함수
#def main():
#    create_table()
#    character_selection()
#    connection.close()

#if __name__ == "__main__":
#    main()
