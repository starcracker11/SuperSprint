import CarGame, pygame


# Set Variables
import User

gamestate = "start_screen"
running = True
pygame.init()
ScreenH = 720
ScreenW = 1280
GameSpeed = 60
wDown = False
aDown = False
sDown = False
dDown = False
click = False


def RenderGame():
    print("rendering")




# Create start screen here
def screen_loop():
    while running:
        screen = pygame.display.set_mode((ScreenW, ScreenH))  # , pygame.FULLSCREEN)
        pygame.display.set_caption("SuperSprint")
        screen.fill((255, 255, 255))
        CarGame.handleInput()

        MouseX, MouseY = pygame.mouse.get_pos()

        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
        if button_1.collidepoint((MouseX, MouseY)):
            if click:
                print("Game")

                # run game here or run main_loop??
        if button_2.collidepoint((MouseX, MouseY)):
            if click:
                print("Options")
                # configure options such as ???
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)

        pygame.display.update()




def start():
    if gamestate == "start_screen":
        screen_loop()