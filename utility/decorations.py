import logging

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)


def log(method):
    def call(func):
        def give(*args):
            logging.info(f'{method.capitalize()} a escola : {args[1].capitalize()}')
            return func(*args)
        return give
    return call
