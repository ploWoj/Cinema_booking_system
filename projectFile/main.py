from menu import Menu
import logging

FORMATER = ('%(asctime)s:%(name)s:%(message)s')

def main():
    logging.basicConfig(filename='example.log', filemode='w',  level=logging.DEBUG, format= FORMATER)
    start = Menu()
    start.runMenu()

if __name__ == "__main__":
    main()
