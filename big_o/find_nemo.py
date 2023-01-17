import time

sample_list_1 = ["nemo"]
sample_list_2 = ["bryan", "cory", "adam", "wright", "leslie", "gavin", "betty", "nemo"]
sample_list_3 = ["nemo"] * 1000
# sample_list_4 = ["nemo" for item in range(10000)]


def find_nemo(array_list):
    start_time = time.perf_counter()

    for item in array_list:
        if item == "nemo":
            print("Found Nemo!!")

    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print(f"function execution time -> {execution_time}")


find_nemo(sample_list_1)
find_nemo(sample_list_2)
find_nemo(sample_list_3)
# find_nemo(sample_list_4)
