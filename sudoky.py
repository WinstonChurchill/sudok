class Sudoky:
    def __init__(self, pole=False):
        if pole == False:
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
                    print(f' | {"." if x == 0 else x}', sep='', end='')
                elif col_x == 9:
                    print(f' {"." if x == 0 else x} | ', sep='', end='')
                else:
                    print(f' {"." if x == 0 else x}', sep='', end='')
            print('\n', end='')

            if col_y % 3 == 0:
                print(' +-------+-------+-------+ ')


    def checking_for_correctness(self, x, y):
        if self.pole[y][x] != 0:
            return 'filled cell'

        vivod = [i for i in range(1, 10)]
        for x_prov in self.pole[y]:
            if x_prov in vivod:
                vivod.remove(x_prov)

        for y_prov in range(9):
            if self.pole[y_prov][x] in vivod:
                vivod.remove(self.pole[y_prov][x])

        if y / 2 <= 1:
            var_v_kvad = self.pole[0:3]
        elif y / 2 >= 1 and y / 2 < 3:
            var_v_kvad = self.pole[3:6]
        else:
            var_v_kvad = self.pole[6:9]

        var_itog = []
        if x / 2 <= 1:
            for i in var_v_kvad:
                var_itog.extend(i[0:3])
        elif x / 2 >= 1 and x / 2 < 3:
            for i in var_v_kvad:
                var_itog.extend(i[3:6])
        else:
            for i in var_v_kvad:
                var_itog.extend(i[6:9])

        for i in var_itog:
            if i in vivod:
                vivod.remove(i)
        
        return vivod


    def proverka_res(self):
        col = 0
        for y in self.pole:
            for x in y:
                if x == 0:
                    col += 1

        if col == 0:
            return 0
        else:
            return 1


    def sudoku_solution_iteration(self):
        col_y = 0
        for y in self.pole:
            col_x = 0
            for x in y:
                col_resh = Sudoky.checking_for_correctness(self, col_x, col_y)
                if len(col_resh) == 1 and col_resh != 'filled cell':
                    self.pole[col_y][col_x] = col_resh[0]
                col_x += 1
            col_y += 1


    def reshenie_sudoky(self):
        while Sudoky.proverka_res(self):
            Sudoky.sudoku_solution_iteration(self)
            maping.beautiful_print_map()



test_map = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]]

test_prav = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
             [6, 7, 2, 1, 9, 5, 3, 4, 8],
             [1, 9, 8, 3, 4, 2, 5, 6, 7],
             [8, 5, 9, 7, 6, 1, 4, 2, 3],
             [4, 2, 6, 8, 5, 3, 7, 9, 1],
             [7, 1, 3, 9, 2, 4, 8, 5, 6],
             [9, 6, 1, 5, 3, 7, 2, 8, 4],
             [2, 8, 7, 4, 1, 9, 6, 3, 5],
             [3, 4, 5, 2, 8, 6, 1, 7, 9]]

maps = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]

maping = Sudoky()
maping.reshenie_sudoky()
