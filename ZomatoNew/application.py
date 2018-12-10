import logging
from mylibrary.zomato import SuperiorZomatoClient

if __name__ == "__main__":

    # ------- OLD CODE

    # cli = BaseHTTPClient(
    #     "https://developers.zomato.com/api/v2.1",
    #     headers={"user-key": "96de02583dbb02fae87e834846ee7ee5"}
    # )

    # result = cli.get("/categories")
    # print(result)

    # ------- NEW CODE

    # A formatter defines how each log entry should be formatted
    # You need to create a `Formatter` instance with the format
    fmt_string = "%(asctime)s | %(levelname)s | %(module)s | %(message)s"
    fmtr = logging.Formatter(fmt=fmt_string)

    # A stream handler logs to the console.
    # On each logHandler (like StreamHandler), you can set a formatter,
    # log_level, etc. We'll set only a formatter here
    sh = logging.StreamHandler()
    sh.setFormatter(fmtr)

    # getLogger(<module-name>) will fetch the `logger` instance associated
    # with that module. This is a `singleton` which means, in your python
    # process, no matter from which module you do `getLogger(<name>)`, you'll
    # get the logger associated with the supplied <name>

    # Example, in `mylibrary\zomato.py` if I did getLogger("mylibrary"),
    # I'll still get `mylibrary` logger (exact same instance as the one below)

    # 1. Get the logger
    my_lib_logger = logging.getLogger("mylibrary")
    # 2. Attach the stream handler
    my_lib_logger.addHandler(sh)
    # 3. Set the level for the `mylibrary` logger as `DEBUG`. This
    #    automatically applies to submodules as well, unless you explicitly
    #    getLogger("mylibrary.<something>") and setLevel(to-some-other-level)
    my_lib_logger.setLevel("DEBUG")

    zom = SuperiorZomatoClient("96de02583dbb02fae87e834846ee7ee5")
    cat = zom.get_categories()
