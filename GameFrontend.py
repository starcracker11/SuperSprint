import CarGame as carGameLib
import GameRenderer as gameRenderer
import pygame
import time
import TextRenderer as textLib
import TitleScreenRenderer as titlesLib

class GameFrontend:

    def __init__(self):
        # Set Variables - Most of these need removing
        self.game_state = "start_screen"
        self.game_paused = False
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
        self.title_screen_renderer = titlesLib.TitleScreenRenderer(self.screen)
        self.text_renderer = textLib.TextRenderer(self.screen)
        self.mode = 'title_screen'

    def start(self):
        self.car_game.reset()
        self.running = True
        # just start screen update loop
        if self.game_state == "start_screen":
            self.main_loop()

    # Create start screen here
    def main_loop(self):
        target_fps = 60
        prev_time = 0
        title = 'car game'
        while self.running:
            # self.car_game.users[0].car.angle = rotateTest2

            self.handle_input()

            # this can be scrapped:
            self.handle_mouse_input()

            # clear screen:
            self.screen.fill((255, 255, 255))

            if self.mode == 'running_game':
                self.update_game()
            elif self.mode == 'title_screen':
                self.update_title_screen()
            elif self.mode == 'options_screen':
                self.update_options_screen()
            elif self.mode == 'game_over_screen':
                self.update_game_over_screen()

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

        print('Left main loop in GameFrontend')
        pygame.quit()

    def update_title_screen(self):
        self.title_screen_renderer.update()
        self.title_screen_renderer.render()
        if self.wDown:
            self.mode = 'running_game'

    def update_options_screen(self):
        print("updating options screen")

    def update_game_over_screen(self):
        # display game over message
        self.text_renderer.y_line_offset = 100
        # TODO: make it show the correct player who won
        self.text_renderer.render_text("PLAYER ONE", 10)
        self.text_renderer.y_line_offset += 150
        self.text_renderer.render_text("  WON")
        # TODO: make 'space' or accelerate button leave game over screen

    def update_game(self):
        if not self.game_paused:
            self.update_game_inputs()
            # update the state of the game
            self.car_game.update()
        if self.car_game.is_game_over():
            self.mode = 'game_over_screen'
        # this is doing all the drawing
        self.game_renderer.render()

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

    def update_game_inputs(self):
        # handle user input for player 1
        user_0 = self.car_game.users[0]
        if self.aDown:
            user_0.car.increase_turn_angle()
        elif self.dDown:
            user_0.car.decrease_turn_angle()
        if self.wDown:
            user_0.car.increase_acceleration()
        else:
            user_0.car.stop_acceleration()

        # maybe implement a CPU_User class to control player 2

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
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    self.aDown = True
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.dDown = True
                elif event.key == pygame.K_w or event.key == pygame.K_UP or event.key == pygame.K_SPACE \
                        or event.key == pygame.K_LCTRL:
                    self.wDown = True
                elif event.key == pygame.K_r:
                    self.car_game.reset()
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    self.sDown = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    self.aDown = False
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.dDown = False
                elif event.key == pygame.K_w or event.key == pygame.K_UP or event.key == pygame.K_SPACE \
                        or event.key == pygame.K_LCTRL:
                    self.wDown = False
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    self.sDown = False
                elif event.key == pygame.K_p:
                    self.game_paused = not self.game_paused
                elif event.key == pygame.K_ESCAPE:
                    # SHOUDL NOT BE QUITTING HERE!
                    # TODO: This needs to go back to a different screen or present the user with option to exit game
                    # TODO: so it can safely exit pygame (end loops etc)
                    # TODO: REMOVE STRINGS AND REPLACE WITH CONTANTS
                    if self.mode == 'game_over_screen':
                        self.mode = 'title_screen'
                    elif self.mode == 'title_screen':
                        self.running = False
                    elif self.mode == 'running_game':
                        self.mode = 'game_over_screen'

        # GET AND REACT TO INPUT ENDS HERE
