import CarGame as carGameLib
import GameRenderer as gameRenderer
import pygame
import time

class GameFrontend:

    def __init__(self):
        # Set Variables - Most of these need removing
        self.game_state = "start_screen"
        self.running = False
        pygame.init()
        self.ScreenH = 720
        self.ScreenW = 1280
        self.GameSpeed = 60
        self.wDown = False
        self.aDown = False
        self.sDown = False
        self.dDown = False
        self.click = False
        self.screen = object
        # Actual properties we need
        # CarGame object currently requires nothing as it builds its own Track object,
        # but we will need to provide it with Users eventually
        # so for in the simple case of 1 player and 2 player game, we would provide it with
        # 1 or 2 users accordingly
        self.car_game = carGameLib.CarGame()
        self.screen = pygame.display.set_mode((self.ScreenW, self.ScreenH))  # , pygame.FULLSCREEN)
        self.game_renderer = gameRenderer.GameRenderer(self.car_game, self.screen)

    def start(self):

        self.screen.fill((255, 255, 255))

        self.running = True
        # just start screen update loop
        if self.game_state == "start_screen":
            self.screen_loop()

    # Create start screen here
    def screen_loop(self):
        target_fps = 60
        prev_time = 0
        title = 'car game'
        while self.running:

            self.handle_input()

            # this can be scrapped:
            self.handle_mouse_input()

            # this is doing all the drawing
            self.game_renderer.render_game()

            pygame.display.update()

            # Timing code at the END!
            curr_time = time.time()  # so now we have time after processing
            diff = curr_time - prev_time  # frame took this much time to process and render
            delay = max(1.0 / target_fps - diff,
                        0)  # if we finished early, wait the remaining time to desired fps, else wait 0 ms!
            time.sleep(delay)
            fps = 1.0 / (delay + diff)  # fps is based on total time ("processing" diff time + "wasted" delay time)
            prev_time = curr_time
            pygame.display.set_caption("{0}: {1:.2f}".format(title, fps))

    def handle_mouse_input(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
        if button_1.collidepoint((mouse_x, mouse_y)):
            if self.click:
                print("Game")

        # run game here or run main_loop??
        if button_2.collidepoint((mouse_x, mouse_y)):
            if self.click:
                print("Options")
                # configure options such as ???
        # pygame.draw.rect(self.screen, (255, 0, 0), button_1)
        # pygame.draw.rect(self.screen, (255, 0, 0), button_2)

    # CarGame does not care about specifics of inputs
    # only that up/dow/left/right/accelerate has been pressed
    # these events will come from each user object
    def handle_input(self):
        # global running, aDown, dDown, wDown, sDown, click
        # GET AND REACT TO INPUT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.click = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    print("a was pressed")
                    self.aDown = True
                elif event.key == pygame.K_d:
                    print("d was pressed")
                    self.dDown = True
                elif event.key == pygame.K_w:
                    print("w was pressed")
                    self.wDown = True

                elif event.key == pygame.K_s:
                    print("s was pressed")
                    self.sDown = True
                elif event.key == pygame.K_ESCAPE:
                    self.running = False
                    # SHOUDL NOT BE QUITTING HERE!
                    # THIS SHOULD BE HANDLED IN FRONTEND!!!
                    pygame.quit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    # print("a was pressed")
                    self.aDown = False
                elif event.key == pygame.K_d:
                    # print("d was pressed")
                    self.dDown = False
                # elif event.key == pygame.K_g:
                # gDown = True
                # print("g was pressed")
                else:
                    print("Nothing To Change")
        # GET AND REACT TO INPUT ENDS HERE
