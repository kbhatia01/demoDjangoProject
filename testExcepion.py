
def handle_exception():
    try:
        print("A")
        val = 10/0

        print(val)
        print("B")

    except Exception as e:
        raise ZeroDivisionError("You can't divide by zero!")
        print("C")

    except ZeroDivisionError:
        print("D")


    finally:
        print("M")

if __name__ == "__main__":
    handle_exception()
