class matrices:

    def get_matrix():
        matrix = []
        row_num = 1

        received = input(f"Row {row_num} with X columns: ")
        first_col_len = len(received.split(" "))
        matrix.append(received.split(" "))
        row_num += 1

        while True:
            received = input(f"Row {row_num} with {first_col_len} columns: ")
            
            if received == "":
                break
            
            else:
                if first_col_len == len(received.split(" ")):
                    mat_set = received.split(" ")
                    matrix.append(mat_set)
                    row_num += 1
                
                else:
                    print("Wrong number of rows.")

        return matrix
    

    def display_matrix():
        matrix = matrices.get_matrix()
        rows = len(matrix[:])
        columns = len(matrix[0][:])

        print(f"{rows}x{columns} Matrix:")

        for i in range(rows):
            for j in range(columns):
                if j != 0:
                    print(matrix[i][j],end=" ")
                else:
                    if j == 0 and i == 0:
                        print("⌈",matrix[i][j],end=" ")
                    
                    else:
                        if i != rows-1:
                            print("❘",matrix[i][j],end=" ")
                        
                        else:
                            print("⌊",matrix[i][j],end=" ")

            
            if i == 0:
                print("⌉")
            
            elif i == rows-1:
                print("⌋")

            else:
                # if i == rows//2:
                #     print("| +")

                # else:
                print("|")

    def transpose_matrix():
        matrix = matrices.get_matrix()
        rows = len(matrix[:])
        columns = len(matrix[0][:])

        print(f"{rows}x{columns} Matrix (Original):")

        for i in range(rows):
            for j in range(columns):
                if j != 0:
                    print(matrix[i][j],end=" ")
                else:
                    if j == 0 and i == 0:
                        print("⌈",matrix[i][j],end=" ")
                    
                    else:
                        if i != rows-1:
                            print("❘",matrix[i][j],end=" ")
                        
                        else:
                            print("⌊",matrix[i][j],end=" ")

            
            if i == 0:
                print("⌉")
            
            elif i == rows-1:
                print("⌋")

            else:
                # if i == rows//2:
                #     print("| +")

                # else:
                print("|")
    
        print(f"\n{columns}x{rows} Matrix (Transposed):")
        
        for i in range(columns):
            for j in range(rows):
                if j != 0:
                    print(matrix[j][i],end=" ")
                else:
                    if j == 0 and i == 0:
                        print("⌈",matrix[j][i],end=" ")
                    
                    else:
                        if i != columns-1:
                            print("❘",matrix[j][i],end=" ")
                        
                        else:
                            print("⌊",matrix[j][i],end=" ")

            
            if i == 0:
                print("⌉")
            
            elif i == columns-1:
                print("⌋")

            else:
                # if i == rows//2:
                #     print("| +")

                # else:
                print("|")

    def matrix_addition():
        Matrix_A = matrices.get_matrix()
        Matrix_B = matrices.get_matrix()
        # Copy & paste the "display matrix" function and modify it to display A + B = C -> their sum.
        pass

    def matrix_substraction():
        pass

    def matrix_dot_multiplication():
        pass

matrices.transpose_matrix()