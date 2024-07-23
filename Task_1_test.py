import Task_1


def test_sum():
    assert Task_1.sum(1,2) == 3
    assert Task_1.sum(2,3) == 5
    assert Task_1.sum(3,4) == 7


def main():
    test_sum()

if __name__ == "__main__":
    main()