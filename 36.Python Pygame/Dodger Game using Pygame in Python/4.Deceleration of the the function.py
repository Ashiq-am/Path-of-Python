def check_for_colision(gamer_movement, enemy_pos):
    p_x, p_y = gamer_movement
    e_x, e_y = enemy_pos
    if (e_x < p_x < e_x + to_dodge_detail or e_x < p_x + gamer_detail < e_x + to_dodge_detail) and \
            (e_y < p_y < e_y + to_dodge_detail or e_y < p_y + gamer_detail < e_y + to_dodge_detail):
        return True
    return False
