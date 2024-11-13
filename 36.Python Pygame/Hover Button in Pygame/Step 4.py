def update(self, events):
    pos = pygame.mouse.get_pos()
    hit = self.rect.collidepoint(pos)

    self.image = self.hov if hit else self.org
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN and hit:
            self.callback(self)
