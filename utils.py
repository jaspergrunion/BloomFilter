def read_words(words_file):
    """ Create a list object of the lines read from a file """
    return [word for line in open(words_file, 'r') for word in line.split()]

def time_it(func):
    """ Decorator function to calculate elapsed time """
    import time
    def wrapper(*args, **kwargs):
        print("Timing:", str(func.__doc__))
        print("---------------")
        start_time = time.perf_counter()
        func(*args, **kwargs)
        elapsed_time = time.perf_counter() - start_time
        print("---------------")
        print("Elaspsed time:", str(elapsed_time), "seconds")
    return wrapper

