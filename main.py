from television import *  # import statement needed to gain access to Television class


def main():
    application = QApplication([])
    window = Television()
    window.show()
    application.exec()


if __name__ == '__main__':
    main()

