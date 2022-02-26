import pygame, Track, GameMob, User


def handleInput():
    global running, aDown, dDown, wDown, sDown, click
    # GET AND REACT TO INPUT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print("a was pressed")
                aDown = True
            elif event.key == pygame.K_d:
                print("d was pressed")
                dDown = True
            elif event.key == pygame.K_w:
                print("w was pressed")
                wDown = True

            elif event.key == pygame.K_s:
                print("s was pressed")
                sDown = True
            elif event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                # print("a was pressed")
                aDown = False
            elif event.key == pygame.K_d:
                # print("d was pressed")
                dDown = False
            # elif event.key == pygame.K_g:
                # gDown = True
                # print("g was pressed")
            else:
                print("Nothing To Change")
    # GET AND REACT TO INPUT ENDS HERE



# Create track here ~~ and draw?



