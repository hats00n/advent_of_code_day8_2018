from solution import get_value

if __name__ == "__main__":
    file_raw_entries = input()
    print(get_value(
        list(map(int, file_raw_entries.split()))
    ))
