import pygame

def main():
    sair = False
    cor_branca = (255, 255, 255)
    cor_azul = (108, 194, 236)
    cor_verde = (152, 231, 114)
    cor_vermelha = (213, 19, 19)
    
    pygame.init()
    tela = pygame.display.set_mode([300, 300])
    pygame.display.set_caption("Aprendendo Pygame")
    relogio = pygame.time.Clock()
    cor_tela = cor_branca
    
    sup = pygame.Surface((200, 200))
    sup.fill(cor_azul)

    sup2 = pygame.Surface((100, 100))
    sup2.fill(cor_verde)

    ret = pygame.Rect(10, 10, 45, 45)

    #Evento para sair da página
    while sair != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                ret = ret.move(10, 10)
        
        #Frame do jogo
        relogio.tick(27)
        tela.fill(cor_tela)
        tela.blit(sup, [50, 50])
        tela.blit(sup2, [100, 100])

        pygame.draw.rect(sup, cor_vermelha, ret)

        pygame.display.update()
    
    pygame.QUIT

main()