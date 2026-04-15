import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Music Player")
done = False
clock = pygame.time.Clock()
volume = 0.5
pygame.mixer.music.set_volume(volume)
pygame.mixer.init()

tracks = [
    {"music": "music/Justin_Bieber_Drake_-_Right_Here_48263111.mp3", "image": "image/trek_1(justin).jpg", "name": "Justin Bieber - Right Here"},
    {"music": "music/Darkhan_Juzz_-_de_63779451.mp3", "image": "image/trek_2(juzz).jpg", "name": "Darkhan Juzz - De"},
    {"music": "music/Ne-Yo_-_One_In_A_Million_47998956.mp3", "image": "image/trek_3(ne yo).jpg", "name": "Ne-Yo - One In A Million"},
]

current_track = 0

current_image = pygame.image.load(tracks[current_track]["image"])
current_image = pygame.transform.scale(current_image, (400,300))

MUSIC_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(MUSIC_END)

pygame.mixer.music.load(tracks[current_track]["music"])
pygame.mixer.music.play()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                if not pygame.mixer.music.get_busy():
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.unpause()
                    
            if event.key == pygame.K_s:
                pygame.mixer.music.stop()
                
            if event.key == pygame.K_n:
                current_track = (current_track + 1) % len(tracks)
                pygame.mixer.music.load(tracks[current_track]["music"])
                current_image = pygame.image.load(tracks[current_track]["image"])
                current_image = pygame.transform.scale(current_image, (400,300))
                pygame.mixer.music.play()
                
            if event.key == pygame.K_b:
                current_track = (current_track - 1) % len(tracks)
                pygame.mixer.music.load(tracks[current_track]["music"])
                current_image = pygame.image.load(tracks[current_track]["image"])
                current_image = pygame.transform.scale(current_image, (400,300))
                pygame.mixer.music.play()

            if event.key == pygame.K_UP:
                volume = min(1.0, volume + 0.1)
                pygame.mixer.music.set_volume(volume)

            if event.key == pygame.K_DOWN:
                volume = max(0.0, volume - 0.1)
                pygame.mixer.music.set_volume(volume)

            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
        
        if event.type == MUSIC_END:
            current_track = (current_track + 1) % len(tracks)
            pygame.mixer.music.load(tracks[current_track]["music"])
            current_image = pygame.image.load(tracks[current_track]["image"])
            current_image = pygame.transform.scale(current_image, (400,300))
            pygame.mixer.music.play()

    screen.fill((255,255,255))
    rect = current_image.get_rect(center=(800//2, 600//2))
    screen.blit(current_image, rect)

    font = pygame.font.Font(None, 30)
    text = font.render(tracks[current_track]["name"], True, (100, 100, 100))
    screen.blit(text, (400 - text.get_width()//2, 520))
    
    vol_text = font.render(f"Volume: {int(volume * 100)}%", True, (100, 100, 100))
    screen.blit(vol_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)