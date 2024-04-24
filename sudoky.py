class Sudoky:
    def __init__(self, pole=None):
        if pole is None:
            self.pole = test_map
        else:
            self.pole = pole
    
    def beautiful_print_map(self, maps=None):
        if maps is None:
            maps = self.pole

        col_y = 0
        for y in maps:
            col_y += 1

            if col_y == 1:
                print(' +-------+-------+-------+ ')

            col_x = 0
            for x in y:
                col_x += 1
                if col_x == 1 or col_x == 4 or col_x == 7:
                    print(f' | {"." if x == 0 else x}', end='')
                elif col_x == 9:
                    print(f' {"." if x == 0 else x} | ', end='')
                else:
                    print(f' {"." if x == 0 else x}', end='')
            print('\n', end='')

            if col_y % 3 == 0:
                print(' +-------+-------+-------+ ')

    def check_variation(self, x, y):
        if self.pole[y][x] != 0:
            return 'filled cell'

        vivod = [i for i in range(1, 10)]
        for x_prov in self.pole[y]:
            if x_prov in vivod:
                vivod.remove(x_prov)

        for y_prov in range(9):
            if self.pole[y_prov][x] in vivod:
                vivod.remove(self.pole[y_prov][x])

        kvadrat_x = x // 3
        kvadrat_y = y // 3
        var_v_kvad = [self.pole[kvadrat_y * 3 + i][kvadrat_x * 3 + j] for i in range(3) for j in range(3)]
        
        for i in var_v_kvad:
            if i in vivod:
                vivod.remove(i)
        
        return vivod

    def proverka_res(self):
        return not any(0 in row for row in self.pole)

    def sudoku_solution_iteration(self):
        for y in range(9):
            for x in range(9):
                col_resh = self.check_variation(x, y)
                if len(col_resh) == 1 and col_resh != ['filled cell']:
                    self.pole[y][x] = col_resh[0]

    def reshenie_sudoky(self):
        while not self.proverka_res():
            self.sudoku_solution_iteration()
            self.beautiful_print_map()


test_map = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]]

maping = Sudoky()
maping.reshenie_sudoky()
