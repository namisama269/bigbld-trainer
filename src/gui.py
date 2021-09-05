import pygame
from pygame import gfxdraw
from pygame.locals import *

from config import *
from targets import *
from alg import *

WIDTH = 500
HEIGHT = 720

pygame.init()

# Enter the display font (recommended to not change)
#fontbig = pygame.font.Font('cyberbit.ttf', 40)
font = pygame.font.Font('freesansbold.ttf', 16)
fontbig = pygame.font.Font('freesansbold.ttf', 40)
fontmed = pygame.font.Font('freesansbold.ttf', 24)
fontsmall = pygame.font.Font('freesansbold.ttf', 16)

class Gui:
    """
    GUI to display virtual cube
    """
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.virtualcube = pygame.Surface((500,400))
        self.screen.fill(bg_colour)
        self.virtualcube.fill(bg_colour)
        self.curr_alg = ""
        self.curr_targets = ["", ""]
        self.pce_idx = 0
        self.show_cube = True
        self.show_targets = True
        self.out_txt = ""
        self.buttons = [
            Button(50, 650, 40, 40, button_clr, hover_clr, pce_types[self.pce_idx].upper()),
            Button(110, 650, 100, 40, button_clr, hover_clr, "Show Cube"),
            Button(230, 650, 130, 40, button_clr, hover_clr, "Show Targets"),
        ]
    
    def run(self):
        running = True
        self.draw_cube()
        self.draw_buttons(self.buttons)

        while running:
            #self.update_button_text(buttons)
            #self.draw_buttons(buttons)
            # Display the cube after every event in case cube state was changed
            self.draw_buttons(self.buttons)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.gen_targets()
                        self.display_targets()
                        self.draw_cube()
                    if event.key == pygame.K_SPACE:
                        self.display_alg()

                # process button presses
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.buttons[0].is_hover():
                        self.pce_idx += 1
                        self.pce_idx %= 5
                        self.buttons[0].set_text(pce_types[self.pce_idx].upper())
                    if self.buttons[1].is_hover():
                        self.show_cube = not self.show_cube
                        self.draw_cube()
                    if self.buttons[2].is_hover():
                        self.show_targets = not self.show_targets
                        self.display_targets()
                        
            pygame.display.update()
        
    
    def draw_cube(self):
        self.virtualcube.fill(bg_colour)
        if len(self.curr_targets[0]) == 0:
            return
        if not self.show_cube:
            self.screen.blit(self.virtualcube, (55,130))
            return
        pce_type = pce_types[self.pce_idx]
        t1, t2 = self.curr_targets
        try:
            img = pygame.image.load(f"images/{pce_type}/{buffers[pce_type]} {t1} {t2}.png")
        except FileNotFoundError:
            return
        self.virtualcube.blit(img, (0,0))
        self.screen.blit(self.virtualcube, (55,130))
        return

    def draw_buttons(self, buttons):
        for button in buttons:
            button.draw(self.screen)

    def gen_targets(self):
        pce_type = pce_types[self.pce_idx]
        self.curr_targets = gen_letter_pair(pce_type)
        t1, t2 = self.curr_targets
        self.curr_alg = get_3cycle(pce_type, buffers[pce_type], t1, t2)
        l1 = letter_scheme[t1]
        l2 = letter_scheme[t2]
        out_txt = f"{l1}{l2}"
        print(f"[{buffers[pce_type]} {pce_names[pce_type]}] " + out_txt)
        self.out_txt = out_txt

    def display_targets(self):
        pygame.draw.rect(self.screen, bg_colour, (0, 0, 500, 150), 0)  
        pygame.draw.rect(self.screen, bg_colour, (0, 520, 540, 120), 0)  
        if not self.show_targets:
            return
        text = fontbig.render(self.out_txt, True, (0,0,0))
        text_rect = text.get_rect(center=(WIDTH/2, 80))
        self.screen.blit(text, text_rect)

    def display_alg(self):
        pygame.draw.rect(self.screen, bg_colour, (0, 520, 540, 120), 0)   
        out_txt = self.curr_alg
        text = fontmed.render(out_txt, True, (0,0,0))
        text_rect = text.get_rect(center=(WIDTH/2, 580))
        self.screen.blit(text, text_rect)


class Button:
    def __init__(self, x, y, width, height, button_clr, hover_clr, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.button_clr = button_clr
        self.hover_clr = hover_clr
        self.text = text

    def draw(self, screen):
        display_clr = self.hover_clr if self.is_hover() else self.button_clr
        pygame.draw.rect(screen, display_clr, (self.x,self.y,self.width,self.height), 0)

        if self.text != "":
            text = fontsmall.render(self.text, True, (0,0,0))
            screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def is_hover(self):
        mouse_pos = pygame.mouse.get_pos()
        return (mouse_pos[0] > self.x and mouse_pos[0] < self.x + self.width and 
        mouse_pos[1] > self.y and mouse_pos[1] < self.y + self.height)

    def set_text(self, new_text):
        self.text = new_text
