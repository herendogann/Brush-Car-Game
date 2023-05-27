print("""
        <----RULES---->
        1. BRUSH DOWN
        2. BRUSH UP
        3. VEHICLE ROTATES RIGHT
        4. VEHICLE ROTATES LEFT
        5. MOVE UP TO X (5_X)
        6. JUMP 
        7. REVERSE DIRECTION
        8. VIEW THE MATRIX
        0. EXIT
""")

input_command = input("Please enter the commands with a plus sign (+) between them: ")
command = input_command.split("+")
frame_size = int(command[0])

for a in range(1, len(command)):
    next_command = command[a]

while int(next_command[0]) not in [int(o) for o in range(0, 9)]:
    input_command = input("It contains invalid commands. Please try again: ")
    command = input_command.split("+")
    frame_size = int(command[0])
    for a in range(1, len(command)):
        next_command = command[a]


matrix = [[" " for i in range(frame_size)]
          for j in range(frame_size)]

x = 0
y = 0

position = x, y

brush = 0

direction = 1
# 1:RIGHT 2:UP 3:LEFT 4:DOWN


def turn_left():
    global matrix
    global direction

    direction += 1
    if direction > 4:
        direction = direction % 4


def turn_right():
    global matrix
    global direction

    direction += 3
    if direction > 4:
        direction = direction % 4


def turn_back():
    global matrix
    global direction

    direction += 2
    if direction > 4:
        direction = direction % 4


def move_brush_up(X):
    global matrix
    global position
    global x, y
    global frame_size

    if direction == 1:
        x += X
        y += 0
        if x >= frame_size:
            x = x % frame_size
        position = x, y

    elif direction == 2:
        x += 0
        y -= X
        if y < 0:
            y = y % int(command[0])
        position = x, y

    elif direction == 3:
        x -= X
        y += 0
        if x < 0:
            x = x % frame_size
        position = x, y

    elif direction == 4:
        y += X
        x += 0
        if y >= frame_size:
            y = y % frame_size
        position = x, y


def move_brush_down(X):
    global matrix
    global position
    global x, y
    global frame_size

    if direction == 1:
        for cell in range(x, x+X):
            x += 1
            y += 0
            if x < frame_size:
                matrix[y][x] = matrix[y][x].replace(" ", "*")
                position = x, y
            elif x >= frame_size:
                x = x % frame_size
                matrix[y][x] = matrix[y][x].replace(" ", "*")
                position = x, y

    if direction == 2:
        for cell in range(y-X, y):
            x += 0
            y -= 1
            if y >= 0:
                matrix[y][x] = matrix[y][x].replace(" ", "*")
                position = x, y
            elif y < 0:
                y = y % frame_size
                matrix[y][x] = matrix[y][x].replace(" ", "*")
                position = x, y

    if direction == 3:
        for cell in range(x-X, x):
            x -= 1
            y += 0
            if x >= 0:
                matrix[y][x] = matrix[y][x].replace(" ", "*")
                position = x, y
            elif x < 0:
                x = x % frame_size
                matrix[y][x] = matrix[y][x].replace(" ", "*")
                position = x, y


    if direction == 4:
        for cell in range(y, y+X):
            x += 0
            y += 1
            if y < frame_size:
                matrix[y][x] = matrix[y][x].replace(" ", "*")
                position = x, y
            elif y >= frame_size:
                y = y % frame_size
                matrix[y][x] = matrix[y][x].replace(" ", "*")
                position = x, y


def jump():
    global matrix
    global position
    global x, y
    global brush
    global frame_size

    if direction == 1:
        x += 3
        y += 0
        position = x, y
        if x >= frame_size:
            x = x % frame_size

        if brush == 0:
            brush += 0
        elif brush == 1:
            brush -= 1

    elif direction == 2:
        y -= 3
        x += 0
        position = x, y
        if y < 0:
            y = y % frame_size

        if brush == 0:
            brush += 0
        elif brush == 1:
            brush -= 1

    elif direction == 3:
        x -= 3
        y += 0
        position = x, y
        if x < 0:
            x = x % frame_size

        if brush == 0:
            brush += 0
        elif brush == 1:
            brush -= 1

    elif direction == 4:
        y += 3
        x += 0
        position = x, y
        if y >= frame_size:
            y = y % frame_size
        if brush == 0:
            brush += 0
        elif brush == 1:
            brush -= 1


def brush_up():
    global matrix
    global brush
    if brush == 0:
        brush += 0
    elif brush == 1:
        brush -= 1


def brush_down():
    global matrix
    global brush
    matrix[y][x] = matrix[y][x].replace(" ", "*")
    if brush == 0:
        brush += 1
    elif brush == 1:
        brush += 0


def printing_matrix():
    global matrix
    global frame_size

    for i in range(frame_size):
        aaa = matrix[i]
        print(aaa)


def printing_matrix_with_frame():
    global matrix
    global frame_size
    matrix_with_frame = matrix
    f = -1
    top_and_down_sides_of_frame = ["+" for i in range(int(command[0])+2)]
    top_and_down_sides_of_frame = "".join(str(m) for m in top_and_down_sides_of_frame)
    for i in range(frame_size):
        f += 1
        matrix_with_frame[f].append("+")
        matrix_with_frame[f].reverse()
        matrix_with_frame[f].append("+")
        matrix_with_frame[f].reverse()
        matrix_with_frame[f] = "".join(str(m) for m in matrix_with_frame[f])
    print(top_and_down_sides_of_frame)
    for i in range(frame_size):
        frame = matrix_with_frame[i]
        print(frame)
    print(top_and_down_sides_of_frame)


for a in range(1, len(command)):
    next_command = command[a]

    if next_command == "1":
        brush_down()

    if next_command == "2":
        brush_up()

    if next_command == "3":
        turn_right()

    if next_command == "4":
        turn_left()

    if next_command.startswith("5_"):
        X = int(next_command[2:])
        if brush == 0:
            move_brush_up(X)
        elif brush == 1:
            move_brush_down(X)

    if next_command == "6":
        jump()

    if next_command == "7":
        turn_back()

    if next_command == "8":
        printing_matrix_with_frame()

    if next_command == "0":
        quit()
