from checker import check
from time import perf_counter as time

# Reads letters in alphabet.txt into list called alphabet
alphabet_file = open('alphabet.txt', 'r')
data = alphabet_file.read()
alphabet = data.split('\n')
alphabet_file.close()

def len_cracker(verbose = True, sample_size = 20, batch_size = 1000):
    """
    -------------------------------------------------------------------------------
    Returns the expected length of the password based on a timing attack.
    -------------------------------------------------------------------------------
        Parameters:
            verbose (bool, optional)
            sample_size (int, optional): number of elements in time_list
            batch_size (int, optional): number of times check() is called per sample
        
        Returns:
            max_len (int): best guess at password length by timing attack
    """

    print('-' * 80)
    print('Cracking length:')
    print('')

    max_time = 0

    # checking password lengths up to 20
    for num in range(20):  
        time_list = []

        # loop allows timing to checked accurately even with random time spikes
        for i in range(sample_size):
            start_time = time()
            for j in range(batch_size):
                check('a' * num)
            end_time = time()
            time_list.append(end_time - start_time)

        # chooses minimum time to check password in case of time spikes
        delta_time = min(time_list)

        # keeps track of highest time to check password and corresponding password length
        if delta_time > max_time:
            max_time = delta_time
            max_len = num
        
        if verbose:
            print(f'Time to check {num} digits:')
            print(round(1000000 * delta_time, 2))
    print('')
    print(f'The password is {max_len} digits long')

    return max_len

def letter_cracker(stem, pointer, sample_size = 100, batch_size = 100):
    """
    -------------------------------------------------------------------------------
    Returns the best guess for password modified at pointer location, given a stem
    -------------------------------------------------------------------------------
      Parameters:
            stem (str): original word on which function bases best guess
            pointer (int): points at letter which is varied to find best guess for password
            sample_size (int, optional): number of elements in time_list
            batch_size (int, optional): number of times check() is called per sample
        
        Returns:
            cracked_word (str): new best guess for password
            (bool): is the password cracked or not
    """

    max_time = 0

    # checking pointed letter in alphabet
    for letter in alphabet:
        time_list = []

        # modifies stem character in pointer position to letter and assigns to word
        word = stem[: pointer] + letter + stem[pointer + 1: ]

        # breaks if password is correct
        if check(word):
            return word, True

        # loop allows timing to checked accurately even with random time spikes
        for i in range(sample_size):
            start_time = time()
            for j in range(batch_size):
                check(word)
            end_time = time()
            time_list.append(end_time - start_time)

        # chooses minimum time to check password in case of time spikes
        delta_time = min(time_list)

        # keeps track of highest time to check password and corresponding password content
        if delta_time > max_time:
            max_time = delta_time
            cracked_letter = letter

    cracked_word = stem[: pointer] + cracked_letter + stem[pointer + 1: ]
    print(cracked_word)

    # unless check(word) returns True earlier, the password has not been cracked, hence returns False
    return cracked_word, False

# quality of life print functions:
def pass_print(pass_num):
    print('-' * 80)
    print(f'Cracking letters: pass {pass_num}')
    print('')

def close_print(password):
    print('-' * 80)
    print(f'The password is: {password}')
    print('-' * 80)

def error_print(term_num):
    print('-' * 80)
    print(f'Program terminated after {term_num} passes.')
    print('-' * 80)