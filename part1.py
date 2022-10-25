from solution import sum_metadata

if __name__ == "__main__":
    file_raw_entries = input()
    print(sum_metadata(
        list(map(int, file_raw_entries.split()))
    ))
