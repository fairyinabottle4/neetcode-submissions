class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # to check the row, just check each array to make sure no duplicates
        for row in board:
            row_set = set()
            for elem in row:
                if elem != '.':
                    if elem in row_set:
                        return False
                    else:
                        row_set.add(elem)
        # to check the column, form an array with the same element in each array out of each column. or maybe you could just rotate the entire board. 
        # I want to get board[0][0], board[1][0]
        # followed by board[1][1], board[2][1]
        for i in range(len(board)): # for each row
            col = [0] * 9
            col_set = set()
            for j in range(len(board[i])): # for each elem
                col[j] = board[j][i]
            for elem in col:
                if elem != '.':
                    if elem in col_set:
                        return False
                    else:
                        col_set.add(elem)
        # to check the box, you can hard code the index positions of the array since there are guaranteed to only be 9 boxes
        box = {}
        for i in range(9):
            for j in range(9):
                box_row = i // 3
                box_col = j // 3
                box_id = (box_row, box_col)
                box[box_id] = []
        for i in range(9):
            for j in range(9):
                box_row = i // 3
                box_col = j // 3
                box_id = (box_row, box_col)
                box[box_id].append(board[i][j])
        boxes = list(box.values())
        for b in boxes:
            box_set = set()
            for elem in b:
                if elem != '.':
                    if elem in box_set:
                        return False
                    else:
                        box_set.add(elem)
        return True


        