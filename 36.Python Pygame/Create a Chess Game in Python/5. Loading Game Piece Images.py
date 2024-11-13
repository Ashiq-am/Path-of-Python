# load in game piece images (queen, king, rook, bishop, knight, pawn) x 2
black_queen = pygame.image.load(
    BytesIO(rembg.remove(requests.get(image_urls[0]).content)))
black_queen = pygame.transform.scale(black_queen, (80, 80))
black_queen_small = pygame.transform.scale(black_queen, (45, 45))
black_king = pygame.image.load(
    BytesIO(rembg.remove(requests.get(image_urls[1]).content)))
black_king = pygame.transform.scale(black_king, (80, 80))
black_king_small = pygame.transform.scale(black_king, (45, 45))
black_rook = pygame.image.load(
    BytesIO(rembg.remove(requests.get(image_urls[2]).content)))
black_rook = pygame.transform.scale(black_rook, (80, 80))
black_rook_small = pygame.transform.scale(black_rook, (45, 45))
black_bishop = pygame.image.load(
    BytesIO(rembg.remove(requests.get(image_urls[3]).content)))
black_bishop = pygame.transform.scale(black_bishop, (80, 80))
black_bishop_small = pygame.transform.scale(black_bishop, (45, 45))
black_knight = pygame.image.load(
    BytesIO(rembg.remove(requests.get(image_urls[4]).content)))
black_knight = pygame.transform.scale(black_knight, (80, 80))
black_knight_small = pygame.transform.scale(black_knight, (45, 45))
black_pawn = pygame.image.load(
    BytesIO(rembg.remove(requests.get(image_urls[5]).content)))
black_pawn = pygame.transform.scale(black_pawn, (65, 65))
black_pawn_small = pygame.transform.scale(black_pawn, (45, 45))
white_queen = pygame.image.load(
    BytesIO(rembg.remove(requests.get(image_urls[6]).content)))
white_queen = pygame.transform.scale(white_queen, (80, 80))
white_queen_small = pygame.transform.scale(white_queen, (45, 45))
white_king = pygame.image.load(
    BytesIO(rembg.remove(requests.get(image_urls[7]).content)))
white_king = pygame.transform.scale(white_king, (80, 80))
white_king_small = pygame.transform.scale(white_king, (45, 45))
white_rook = pygame.image.load(
    BytesIO(rembg.remove(requests.get(image_urls[8]).content)))
white_rook = pygame.transform.scale(white_rook, (80, 80))
white_rook_small = pygame.transform.scale(white_rook, (45, 45))
white_bishop = pygame.image.load(
    BytesIO(rembg.remove(requests.get(image_urls[9]).content)))
white_bishop = pygame.transform.scale(white_bishop, (80, 80))
white_bishop_small = pygame.transform.scale(white_bishop, (45, 45))
white_knight = pygame.image.load(
    BytesIO(rembg.remove(requests.get(image_urls[10]).content)))
white_knight = pygame.transform.scale(white_knight, (80, 80))
white_knight_small = pygame.transform.scale(white_knight, (45, 45))
white_pawn = pygame.image.load(
    BytesIO(rembg.remove(requests.get(image_urls[11]).content)))
white_pawn = pygame.transform.scale(white_pawn, (65, 65))
white_pawn_small = pygame.transform.scale(white_pawn, (45, 45))
