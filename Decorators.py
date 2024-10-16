def decr(func):
    def wrapper(*args, **kwargs):
        print("hello")
        func(*args, **kwargs)
        print("bye")

    return wrapper


def is_admin(func):
    def wrapper(is_admin_var, *args, **kwargs):
        if not is_admin_var:
            print("not admin")
            return False
        return func(*args, **kwargs)

    return wrapper


@decr
def print_name(name):
    print(name)


@decr
def print_name2(name):
    print(f"Hello : {name}")


@is_admin
def print_name3(name):
    print(name)


@is_admin
def print_name4(name):
    print(name)


if __name__ == '__main__':
    # print_name("John")
    # print_name2("John")
    print_name3(name="John 3", is_admin_var=True)
