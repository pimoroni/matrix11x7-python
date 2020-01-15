class not_numpy:
        def pad(self, oldarray, padding, mode="constant"):
            if mode != "constant":
                raise NotImplementedError("No mode other than 'constant' has been implemented")
            array = [[i for i in row] for row in oldarray]
            x_pad = padding[0]
            y_pad = padding[1]
            x_pad_before = x_pad[0]
            x_pad_after = x_pad[1]
            y_pad_before = y_pad[0]
            y_pad_after = y_pad[1]
            if x_pad_before > 0:
                for i in range(x_pad_before):
                    array.insert(0, [0] * len(array[0]))

            if x_pad_after > 0:
                for i in range(x_pad_after):
                    array.insert(len(array), [0] * len(array[0]))

            if y_pad_before > 0:
                for x in range(y_pad_before):
                    for i,j in enumerate(array):
                        array[i].insert(0, 0)

            if y_pad_before > 0:
                for x in range(y_pad_after):
                    for i,j in enumerate(array):
                        array[i].insert(len(j), 0)

            return array

        def roll(self, oldarray, shift, axis=0):
            array = [[i for i in row] for row in oldarray]
            if axis == 0:
                if shift > 0:
                    for i in range(shift):
                        array.insert(0, array.pop(len(array) - 1))

                if shift < 0:
                    for i in range(abs(shift)):
                        array.insert(len(array), array.pop(0))

            if axis == 1:
                if shift > 0:
                    for i in range(shift):
                        for j in array:
                            j.insert(0, j.pop(len(j) - 1))

                if shift < 0:
                    for i in range(abs(shift)):
                        for j in array:
                            j.insert(len(j), j.pop(0))

            return array

        def flipud(self, oldarray):
            array = [[i for i in row] for row in oldarray]
            return array.reverse()

        def fliplr(self, oldarray):
            array = [[i for i in row] for row in oldarray]
            for i in array:
                i.reverse()
            return array

        def rot90(self, oldarray, rotations):
            array = [[i for i in row] for row in oldarray]
            for i in range(rotations):
                array = list(reversed(list(zip(*array))))
            return array

        def zeros(self, shape):
            return [[0]*shape[1] for i in range(shape[0])]