import random


def main():
    sides_of_triangle = []
    length_of_rod = 1
    for i in range(2):
        piece = random.uniform(0, length_of_rod)
        sides_of_triangle.append(piece)
        length_of_rod -= piece
    sides_of_triangle.append(length_of_rod)

    sides_of_triangle.sort()

    if (sides_of_triangle[0] + sides_of_triangle[1]) > sides_of_triangle[2]:
        return True
    else:
        return False


if __name__ == "__main__":
    count_of_possible_triangles = 0
#    count_of_not_possible_triangles = 0     # Nur zum Überprüfen

    count_of_tries = 1000000
    for i in range(count_of_tries):
        if (main()):
            count_of_possible_triangles += 1
#        else:                                       # Kann eig weggelassen werden
#            count_of_not_possible_triangles += 1    # Kann eig weggelassen werden

    print(count_of_possible_triangles/count_of_tries)