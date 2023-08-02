import pygame
import sys

# Pygame 초기화
pygame.init()

# 창 크기 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("게임 제목")

# 색깔 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 유저 아이디 및 비밀번호 생성 창
def show_login_screen():
    done = False
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)

    input_id = ""
    input_password = ""

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and input_id and input_password:
                    done = True  # Done 버튼을 엔터 키로 대체
                elif event.key == pygame.K_END:
                    pygame.quit()
                    sys.exit()
                else:
                    if len(input_id) < 20 and event.key != pygame.K_RETURN:
                        input_id += event.unicode
                    if len(input_password) < 20 and event.key != pygame.K_RETURN:
                        input_password += event.unicode

        screen.fill(WHITE)
        # 아이디 및 비밀번호 입력 란 그리기
        pygame.draw.rect(screen, BLACK, (screen_width // 2 - 100, 200, 200, 40))
        pygame.draw.rect(screen, BLACK, (screen_width // 2 - 100, 300, 200, 40))

        # 아이디 및 비밀번호 텍스트 그리기
        id_text = font.render("ID: " + input_id, True, BLACK)
        screen.blit(id_text, (screen_width // 2 - 100, 180))

        password_text = font.render("Password: " + "*" * len(input_password), True, BLACK)
        screen.blit(password_text, (screen_width // 2 - 100, 280))

        # Done 버튼 그리기
        pygame.draw.rect(screen, BLACK, (screen_width // 2 - 50, 400, 100, 40))
        done_text = font.render("Done", True, WHITE)
        screen.blit(done_text, (screen_width // 2 - 30, 410))

        # End 버튼 그리기
        pygame.draw.rect(screen, RED, (screen_width // 2 - 50, 460, 100, 40))
        end_text = font.render("End", True, WHITE)
        screen.blit(end_text, (screen_width // 2 - 30, 470))

        pygame.display.flip()
        clock.tick(60)

    show_next_page()

# 다음 페이지
def show_next_page():
    done = False
    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)
        # 다음 페이지의 내용 그리기

        pygame.display.flip()
        clock.tick(60)

# 유저 아이디 및 비밀번호 생성 창을 보여줌
show_login_screen()

# Pygame 종료
pygame.quit()
