from functions import *
from checker import check

def main():

    # assigns best guess for word length to word_len with chosen sample/batch sizes
    word_len = len_cracker(True, 60, 30)

    # initialises stem with appropriate length
    stem = 'a' * word_len

    # allows code to terminate after 60 passes if password isn't found 
    count = 0
    term_num = 60

    while not check(stem):
        count += 1
        pass_print(count)

        # points at each letter in word and attempts to crack that letter
        for pointer in range(word_len):

            # assigns best guess for password to stem with chosen sample/batch sizes
            stem, is_cracked = letter_cracker(stem, pointer, 70, 20)

            # terminates program if password is cracked
            if is_cracked:
                print(stem)
                break
        
        # terminates code after term_num passes
        if count >= term_num:
            error_print(term_num)
            return

    close_print(stem)

if __name__ == '__main__':
    main()