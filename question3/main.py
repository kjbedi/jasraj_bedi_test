from LruUtil import LruCache


def main():
    """
    This is the first function called by the main program
    """
    cache = LruCache(10, 20)
    print("here")
    cache.add("e4", 655)
    cache.add("e444", 655)
    cache.add("e3", 655)
    cache.add("e1", 55)
    cache.add("e2", 55)
    cache.add("e0", 55)
    cache.add("e8", 55)
    cache.access("e444")


if __name__ == "__main__":
    main()


