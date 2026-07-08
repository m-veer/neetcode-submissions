class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        columns = {}
        boxes = {}

        for r_index, r in enumerate(board):
            if r_index not in rows:
                rows[r_index] = set()

            for c_index, c in enumerate(r):
                box_number = (r_index // 3, c_index // 3)
                if box_number not in boxes:
                    boxes[box_number] = set()

                if c.isdigit():
                    if c not in rows.get(r_index):
                        rows.get(r_index).add(c)
                    else:
                        return False

                    if c_index not in columns:
                        columns[c_index] = set()
                    if c not in columns.get(c_index):
                        columns.get(c_index).add(c)
                    else:
                        return False

                    if c not in boxes.get(box_number):
                        boxes.get(box_number).add(c)
                    else:
                        return False
        return True