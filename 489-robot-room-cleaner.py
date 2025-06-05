def solution(robot: "Robot"):
    visited = set()

    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def go_back():
        robot.turnRight()
        robot.turnRight()
        robot.move()
        robot.turnRight()
        robot.turnRight()

    def dfs(pos, heading):
        robot.clean()
        visited.add(pos)

        for i in range(4):
            next_heading = (heading + i) % 4
            next_pos = (pos[0] + dirs[next_heading][0], pos[1] + dirs[next_heading][1])

            if (not next_pos in visited) and robot.move():
                dfs(next_pos, next_heading)
                go_back()

            robot.turnRight()

    dfs((0, 0), 0)
