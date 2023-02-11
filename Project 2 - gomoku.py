def is_empty(board):
    for i in range(8):
        for j in range(8):
            if board[i][j] != " ":
                return False
    return True


def is_bounded(board, y_end, x_end, length, d_y, d_x):
    if d_x==1 and d_y==0:
        if x_end<7 and x_end-length>=0:
            if board[y_end][x_end+1]==" " and board[y_end][x_end-length]==" ":
                return "OPEN"
            elif (board[y_end][x_end+1]!=" " and board[y_end][x_end-length]==" ") or (board[y_end][x_end+1]==" " and board[y_end][x_end-length]!=" "):
                return "SEMIOPEN"
            elif board[y_end][x_end+1]!=" " and board[y_end][x_end-length]!=" ":
                return "CLOSED"
        elif x_end==7 and x_end-length>=0:
            if board[y_end][x_end-length]==" ":
                return "SEMIOPEN"
            else:
                return "CLOSED"
        elif x_end<7 and x_end-length+1==0:
            if board[y_end][x_end+1]==" ":
                return "SEMIOPEN"
            else:
                return "CLOSED"
    if d_y==1 and d_x==0:
        if y_end<7 and y_end-length>=0:
            if board[y_end+1][x_end]==" " and board[y_end-length][x_end]==" ":
                return "OPEN"
            elif (board[y_end+1][x_end]!=" " and board[y_end-length][x_end]==" ") or (board[y_end+1][x_end]==" " and board[y_end-length][x_end]!=" "):
                return "SEMIOPEN"
            elif board[y_end+1][x_end]!=" " and board[y_end-length][x_end]!=" ":
                return "CLOSED"
        elif y_end==7 and y_end-length>=0:
            if board[y_end-length][x_end]==" ":
                return "SEMIOPEN"
            else:
                return "CLOSED"
        elif y_end<7 and y_end-length+1==0:
            if board[y_end+1][x_end]==" ":
                return "SEMIOPEN"
            else:
                return "CLOSED"
    if d_y==1 and d_x==1:
        if y_end<7 and y_end-length>=0 and x_end<7 and x_end-length>=0:
            if board[y_end+1][x_end+1]==" " and board[y_end-length][x_end-length]==" ":
                return "OPEN"
            elif (board[y_end+1][x_end+1]!=" " and board[y_end-length][x_end-length]==" ") or (board[y_end+1][x_end+1]==" " and board[y_end-length][x_end-length]!=" "):
                return "SEMIOPEN"
            elif board[y_end+1][x_end+1]!=" " and board[y_end-length][x_end-length]!=" ":
                return "CLOSED"
        elif y_end==7 and y_end-length>=0 and x_end-length>=0:
            if board[y_end-length][x_end-length]==" ":
                return "SEMIOPEN"
            else:
                return "CLOSED"
        elif x_end==7 and x_end-length>=0 and y_end-length>=0:
            if board[y_end-length][x_end-length]==" ":
                return "SEMIOPEN"
            else:
                return "CLOSED"
        elif x_end==7 and y_end==7 and x_end-length>=0 and y_end-length>=0:
            if board[y_end-length][x_end-length]==" ":
                return "SEMIOPEN"
            else:
                return "CLOSED"
        elif x_end-length+1==0 and x_end<7 and y_end<7:
            if board[y_end+1][x_end+1]==" ":
                return "SEMIOPEN"
            else:
                return "CLOSED"
        elif y_end-length+1==0 and y_end<7 and x_end<7:
            if board[y_end+1][x_end+1]==" ":
                return "SEMIOPEN"
            else:
                return "CLOSED"
        if y_end-length+1==0 and x_end-length+1==0 and y_end<7 and x_end<7:
            if board[y_end+1][x_end+1]==" ":
                return "SEMIOPEN"
            else:
                return "CLOSED"
    if d_y==1 and d_x==-1:
        if y_end<7 and y_end-length>=0 and x_end>0 and x_end+length<=7:
            if board[y_end+1][x_end-1]==" " and board[y_end-length][x_end+length]==" ":
                return "OPEN"
            elif (board[y_end+1][x_end-1]!=" " and board[y_end-length][x_end+length]==" ") or (board[y_end+1][x_end-1]==" " and board[y_end-length][x_end+length]!=" "):
                return "SEMIOPEN"
            elif board[y_end+1][x_end-1]!=" " and board[y_end-length][x_end+length]!=" ":
                return "CLOSED"
        elif y_end==7 and y_end-length>=0 and x_end+length<=7:
            if board[y_end-length][x_end+length]==" ":
                return "SEMIOPEN"
            else:
                return "CLOSED"
        elif x_end==0 and x_end+length<=7 and y_end-length>=0:
            if board[y_end-length][x_end+length]==" ":
                return "SEMIOPEN"
            else:
                return "CLOSED"
        elif x_end==0 and y_end==7 and x_end+length<=7 and y_end-length>=0:
            if board[y_end-length][x_end+length]==" ":
                return "SEMIOPEN"
            else:
                return "CLOSED"
        elif x_end+length-1==7 and x_end>0 and y_end<7:
            if board[y_end+1][x_end-1]==" ":
                return "SEMIOPEN"
            else:
                return "CLOSED"
        elif y_end-length+1==0 and y_end<7 and x_end>0:
            if board[y_end+1][x_end-1]==" ":
                return "SEMIOPEN"
            else:
                return "CLOSED"
        elif y_end-length+1==0 and x_end+length-1==7 and y_end<7 and x_end>0:
            if board[y_end+1][x_end-1]==" ":
                return "SEMIOPEN"
            else:
                return "CLOSED"
    return "CLOSED"


def detect_row(board, col, y_start, x_start, length, d_y, d_x):

    open_seq_count = 0
    semi_open_seq_count = 0
    run = 0

    if (d_y==1 and d_x==0) or (d_y==0 and d_x==1):
        for i in range(1,8):
            if board[y_start+i*d_y][x_start+i*d_x] != col:
                if board[y_start+(i-1)*d_y][x_start+(i-1)*d_x] == col and run == length:
                    if is_bounded(board,y_start+(i-1)*d_y,x_start+(i-1)*d_x,length,d_y,d_x)=="OPEN":
                        open_seq_count += 1
                    if is_bounded(board,y_start+(i-1)*d_y,x_start+(i-1)*d_x,length,d_y,d_x)=="SEMIOPEN":
                        semi_open_seq_count += 1
                run = 0
            else:
                run += 1
                if i == 7 and run == length:
                    if is_bounded(board,y_start+i*d_y,x_start+i*d_x,length,d_y,d_x)=="OPEN":
                        open_seq_count += 1
                    if is_bounded(board,y_start+i*d_y,x_start+i*d_x,length,d_y,d_x)=="SEMIOPEN":
                        semi_open_seq_count += 1
    if d_y==1 and d_x==1:
        for i in range(1,min(8-y_start,8-x_start)):
            if board[y_start+i*d_y][x_start+i*d_x] != col:
                if board[y_start+(i-1)*d_y][x_start+(i-1)*d_x] == col and run == length:
                    if is_bounded(board,y_start+(i-1)*d_y,x_start+(i-1)*d_x,length,d_y,d_x)=="OPEN":
                        open_seq_count += 1
                    if is_bounded(board,y_start+(i-1)*d_y,x_start+(i-1)*d_x,length,d_y,d_x)=="SEMIOPEN":
                        semi_open_seq_count += 1
                run = 0
            else:
                run += 1
                if i == min(8-y_start,8-x_start)-1 and run == length:
                    if is_bounded(board,y_start+i*d_y,x_start+i*d_x,length,d_y,d_x)=="OPEN":
                        open_seq_count += 1
                    if is_bounded(board,y_start+i*d_y,x_start+i*d_x,length,d_y,d_x)=="SEMIOPEN":
                        semi_open_seq_count += 1
    if d_y==1 and d_x==-1:
        for i in range(1,min(8-y_start,x_start)):
            if board[y_start+i*d_y][x_start+i*d_x] != col:
                if board[y_start+(i-1)*d_y][x_start+(i-1)*d_x] == col and run == length:
                    if is_bounded(board,y_start+(i-1)*d_y,x_start+(i-1)*d_x,length,d_y,d_x)=="OPEN":
                        open_seq_count += 1
                    if is_bounded(board,y_start+(i-1)*d_y,x_start+(i-1)*d_x,length,d_y,d_x)=="SEMIOPEN":
                        semi_open_seq_count += 1
                run = 0
            else:
                run += 1
                if i == min(8-y_start,x_start)-1 and run == length:
                    if is_bounded(board,y_start+i*d_y,x_start+i*d_x,length,d_y,d_x)=="OPEN":
                        open_seq_count += 1
                    if is_bounded(board,y_start+i*d_y,x_start+i*d_x,length,d_y,d_x)=="SEMIOPEN":
                        semi_open_seq_count += 1

    return open_seq_count, semi_open_seq_count


def detect_rows(board, col, length):
    open_seq_count, semi_open_seq_count = 0, 0
    for i in range(8):
        open_seq_count += (detect_row(board,col,i,0,length,0,1)[0] + detect_row(board,col,0,i,length,1,0)[0] + detect_row(board,col,i,0,length,1,1)[0] + detect_row(board,col,0,i,length,1,1)[0] + detect_row(board,col,i,7,length,1,-1)[0] + detect_row(board,col,0,i,length,1,-1)[0])
        semi_open_seq_count += (detect_row(board,col,i,0,length,0,1)[1] + detect_row(board,col,0,i,length,1,0)[1] + detect_row(board,col,i,0,length,1,1)[1] + detect_row(board,col,0,i,length,1,1)[1] + detect_row(board,col,i,7,length,1,-1)[1] + detect_row(board,col,0,i,length,1,-1)[1])

    open_seq_count = open_seq_count - detect_row(board,col,0,0,length,1,1)[0] - detect_row(board,col,0,7,length,1,-1)[0]
    semi_open_seq_count = semi_open_seq_count - detect_row(board,col,0,0,length,1,1)[1] - detect_row(board,col,0,7,length,1,-1)[1]

    return open_seq_count, semi_open_seq_count


def score(board):
    MAX_SCORE = 100000

    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}

    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)


    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE

    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE

    return (-10000 * (open_w[4] + semi_open_w[4])+
            500  * open_b[4]                     +
            50   * semi_open_b[4]                +
            -100  * open_w[3]                    +
            -30   * semi_open_w[3]               +
            50   * open_b[3]                     +
            10   * semi_open_b[3]                +
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])


def search_max(board):
    move_y = 0
    move_x = 0
    max_score = score(board)
    for i in range(8):
        for j in range(8):
            if board[i][j] == " ":
                board[i][j] = "b"
                new_score = score(board)
                if new_score > max_score:
                    max_score = new_score
                    move_y = i
                    move_x = j
                board[i][j] = " "
    return move_y, move_x


def is_win(board): # 5 in a row = win
    # d_y = 1 ; d_x = 0
    count = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == "b":
                cur_yb = i
                cur_xb = j
                cur_yb += 1
                count += 1
                while 0<=cur_yb<=len(board)-1 and 0<=cur_xb<=len(board)-1:
                    if board[cur_yb][cur_xb] == "b":
                        count += 1
                        if count == 5:
                            return "Black won"
                    else:
                        count = 0
                    cur_yb += 1
            if board[i][j] == "w":
                cur_yw = i
                cur_xw = j
                cur_yw += 1
                count += 1
                while 0<=cur_yw<=len(board)-1 and 0<=cur_xw<=len(board)-1:
                    if board[cur_yw][cur_xw] == "w":
                        count += 1
                        if count == 5:
                            return "White won"
                    else:
                        count = 0
                    cur_yw += 1
    # d_y = 0 ; d_x = 1
    coun = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == "b":
                cur_yb = i
                cur_xb = j
                cur_xb += 1
                coun += 1
                while 0<=cur_yb<=len(board)-1 and 0<=cur_xb<=len(board)-1:
                    if board[cur_yb][cur_xb] == "b":
                        coun += 1
                        if coun == 5:
                            return "Black won"
                    else:
                        coun = 0
                    cur_xb += 1
            if board[i][j] == "w":
                cur_yw = i
                cur_xw = j
                cur_xw += 1
                coun += 1
                while 0<=cur_yw<=len(board)-1 and 0<=cur_xw<=len(board)-1:
                    if board[cur_yw][cur_xw] == "w":
                        coun += 1
                        if coun == 5:
                            return "White won"
                    else:
                        coun = 0
                    cur_xw += 1
    # d_y = 1 ; d_x = 1
    cou = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == "b":
                cur_yb = i
                cur_xb = j
                cur_yb += 1
                cur_xb += 1
                cou += 1
                while 0<=cur_yb<=len(board)-1 and 0<=cur_xb<=len(board)-1:
                    if board[cur_yb][cur_xb] == "b":
                        cou += 1
                        if cou == 5:
                            return "Black won"
                    else:
                        cou = 0
                    cur_yb += 1
                    cur_xb += 1
            if board[i][j] == "w":
                cur_yw = i
                cur_xw = j
                cur_yw += 1
                cur_xw += 1
                cou += 1
                while 0<=cur_yw<=len(board)-1 and 0<=cur_xw<=len(board)-1:
                    if board[cur_yw][cur_xw] == "w":
                        cou += 1
                        if cou == 5:
                            return "White won"
                    else:
                        cou = 0
                    cur_yw += 1
                    cur_xw += 1
    # d_y = 1 ; d_x = -1
    co = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == "b":
                cur_yb = i
                cur_xb = j
                cur_yb += 1
                cur_xb += -1
                co += 1
                while 0<=cur_yb<=len(board)-1 and 0<=cur_xb<=len(board)-1:
                    if board[cur_yb][cur_xb] == "b":
                        co += 1
                        if co == 5:
                            return "Black won"
                    else:
                        co = 0
                    cur_yb += 1
                    cur_xb += -1
            if board[i][j] == "w":
                cur_yw = i
                cur_xw = j
                cur_yw += 1
                cur_xw += -1
                co += 1
                while 0<=cur_yw<=len(board)-1 and 0<=cur_xw<=len(board)-1:
                    if board[cur_yw][cur_xw] == "w":
                        co += 1
                        if co == 5:
                            return "White won"
                    else:
                        co = 0
                    cur_yw += 1
                    cur_xw += -1

    empty = False
    for i in range(8):
        for j in range(8):
            if board[i][j] == " ":
                empty = True
    if empty == False:
        return "Draw"

    return "Continue Playing"

def print_board(board):

    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"

    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1])

        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"

    print(s)


def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board


def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))


def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])

    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)

        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res

        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res


def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col
        y += d_y
        x += d_x


def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")


def test_is_bounded():
    board = make_empty_board(8)
    x = 3; y = 4; d_x = -1; d_y = 1; length = 4
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)

    y_end = 7
    x_end = 0

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'SEMIOPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")


def test_detect_row():
    board = make_empty_board(8)
    x = 3; y = 4; d_x = -1; d_y = 1; length = 4
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0,x,length,d_y,d_x) == (0,1):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")


def test_detect_rows():
    board = make_empty_board(8)
    x = 1; y = 4; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (0,1):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")


def test_search_max():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")


def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()


def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)

    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0

    y = 3; x = 5; d_x = -1; d_y = 1; length = 2

    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)

    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #

    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    analysis(board);

    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #
    #
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0




if __name__ == '__main__':
    # board = [[' ', ' ', 'w', 'w', 'w', ' ', ' ', 'w'],
    #          [' ', ' ', 'b', ' ', 'b', 'w', 'w', 'b'],
    #          ['b', ' ', 'b', 'b', 'w', ' ', 'w', 'b'],
    #          ['b', ' ', ' ', 'w', 'w', ' ', 'b', 'w'],
    #          ['b', ' ', ' ', 'w', 'b', 'b', 'b', 'w'],
    #          ['w', 'b', 'b', 'w', 'b', 'w', 'w', ' '],
    #          ['b', 'b', 'b', 'b', 'b', 'w', ' ', ' '],
    #          ['b', ' ', 'b', 'w', 'w', 'w', 'w', ' ']]
    # print(detect_rows(board,"b",2))
    # print(detect_row(board,"b",0,2,3,1,0))
    # some_tests()
    print(play_gomoku(8))