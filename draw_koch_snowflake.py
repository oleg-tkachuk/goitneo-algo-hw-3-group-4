import sys
import turtle


def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order-1, size/3)
            t.left(angle)


def draw_koch_snowflake(order, size):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.color("blue")

    for i in range(3):
        koch_snowflake(t, order, size)
        t.right(120)

    window.mainloop()


def main():
    order = sys.argv[1] if len(sys.argv) > 1 else 3
    size = sys.argv[2] if len(sys.argv) > 2 else 200
    draw_koch_snowflake(int(order), int(size))


if __name__ == "__main__":
    print(f"Homework 3 - Task 2 | Starting...")
    main()
    print(f"Homework 3 - Task 2 | Done")
