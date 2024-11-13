sprites = pygame.sprite.Group()
sprites.add(Button(pygame.Color('green'),
				pygame.Color('red'), # on hover color
				# four parameters are postion of rec (left,up,right,down)
				# right and down cannot be zero
				pygame.Rect(20, 100, 200, 200),
				# //right these accor to display dimensions
				# f1=pygame.font.SysFont('elephant',20)
				lambda b: print(f"Button '{b.text}' was clicked"),
				'Hover',
				pygame.Color('black'),

				))

sprites.add(Button(pygame.Color('yellow'),
				pygame.Color('red'),
				pygame.Rect(300, 100, 200, 200),
				lambda b: print(f"Click me again!"),
				'Another')) # anoter button
