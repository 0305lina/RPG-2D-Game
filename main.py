import pygame

def character_selection():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Character Selection")

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

    # 선택된 캐릭터 초기화
    selected_character = None

    done_button_rect = pygame.Rect(300, 500, 200, 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if done_button_rect.collidepoint(pygame.mouse.get_pos()):
                    if selected_character:
                        pygame.quit()
                        return
                # 캐릭터 이미지 버튼 클릭 시 선택된 캐릭터 변경 또는 선택 취소
                elif rabbit_button.collidepoint(pygame.mouse.get_pos()):
                    if selected_character == rabbit_img:
                        selected_character = None  # 선택 취소
                    else:
                        selected_character = rabbit_img
                elif bear_button.collidepoint(pygame.mouse.get_pos()):
                    if selected_character == bear_img:
                        selected_character = None  # 선택 취소
                    else:
                        selected_character = bear_img
                elif dog_button.collidepoint(pygame.mouse.get_pos()):
                    if selected_character == dog_img:
                        selected_character = None  # 선택 취소
                    else:
                        selected_character = dog_img

        # 배경 화면 그리기
        screen.fill((255, 255, 255))

        # 캐릭터 이미지 버튼 그리기 (선택된 캐릭터는 크기가 커짐)
        screen.blit(pygame.transform.scale(rabbit_img, selected_size if selected_character == rabbit_img else default_size), rabbit_button.topleft)
        screen.blit(pygame.transform.scale(bear_img, selected_size if selected_character == bear_img else default_size), bear_button.topleft)
        screen.blit(pygame.transform.scale(dog_img, selected_size if selected_character == dog_img else default_size), dog_button.topleft)

        # Done 버튼 그리기
        pygame.draw.rect(screen, (0, 255, 0), done_button_rect)
        font = pygame.font.SysFont(None, 40)
        done_text = font.render("Done", True, (0, 0, 0))
        screen.blit(done_text, (340, 510))

        pygame.display.update()

def main():
    character_selection()

if __name__ == "__main__":
    main()
