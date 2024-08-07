import pygame

# Keys class used for taking input
class Keys():
    pressed:list = []           # list of curently pressed keys
    just_pressed:list = []      # list of just pressed keys
    just_released:list = []     # list of just released keys

    # func for updating keys
    def update(self) -> None:
        events = pygame.event.get()

        # clearing all vars
        self.pressed, self.just_pressed, self.just_released = [], [], []

        # going thru all events
        for event in events:
            if event.type == pygame.QUIT:
                self.just_pressed.append(pygame.QUIT)

            elif event.type == pygame.KEYDOWN:    # if just pressed
                self.just_pressed.append(event.key)

            elif event.type == pygame.KEYUP:    # if just released
                self.just_released.append(event.key)

            # same but for mouse buttons
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.just_pressed.append(event.button)
            
            elif event.type == pygame.MOUSEBUTTONUP:
                self.just_released.append(event.button)

        # getting all pressed keys
        self.pressed = pygame.key.get_pressed()