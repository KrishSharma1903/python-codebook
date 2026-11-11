##Generators for memory efficiency
#generators allow you to produce items one at a time, using memory efficiently by only keeping one item in the memory at a time.

def generate_numbers(n):
    for i in range(n):
        yield i

##using generator
for num in generate_numbers(100000):
    print(num)
    if num>10:
        break

##Profiling memory usage with tracemalloc

import tracemalloc

def create_list():
    return [i for i in range(1000)]

def main():
    tracemalloc.start()

    create_list()

    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')  # Get statistics by line number

    print("[Top 10]")
    for stats in top_stats[:10]:
        print(stats)

main()