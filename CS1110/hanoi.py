def solve_hanoi(source, target, other, n_disks):
    if n_disks == 1:
        print("move from " + source + " to " + target)
    else:
        solve_hanoi(source, other, target, n_disks-1)
        print("move from " + source + " to " + target)
        solve_hanoi(other, target, source, n_disks-1)