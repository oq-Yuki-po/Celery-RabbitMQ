from app.task import add


def main():
    result = add.delay(4, 4)
    print(result.get(timeout=1))


if __name__ == "__main__":
    main()
