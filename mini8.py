def format_table(benchmarks, algorithms, times):
    max_benchmark_len = max(len(benchmark) for benchmark in benchmarks)
    max_algorithm_len = max(len(algorithm) for algorithm in algorithms)

    header = '| ' + "Benchmark".ljust(max_benchmark_len)
    for algorithm in algorithms:
        header += ' | ' + (algorithm).center(max_algorithm_len)
    header += ' |'
    separator = "|" + "-" * (len(header) - 2) + "|"

    print(header)
    print(separator)

    for i, benchmark in enumerate(benchmarks):
        row = "| " + benchmark.ljust(max_benchmark_len)
        for time in times[i]:
            row += " | " + f"{time:.2f}".rjust(max_algorithm_len)
        row += " |"
        print(row)

    print(separator)


# Данные
benchmarks = ["best case", "worst case"]
algorithms = ["quick sort", "merge sort", "bubble sort"]
times = [[1.23, 1.56, 2.0], [3.3, 2.9, 3.9]]

# Вызов функции
format_table(benchmarks, algorithms, times)
