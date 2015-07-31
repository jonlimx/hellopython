__author__ = 'jonathanlim'

import string

'''Use this function to check if a ID is valid or not
Rules: 1. at least contains 2 characters 2. should only contains alphas or digits'''


def checkid(id):
    alphas = string.ascii_letters + '_'
    digits = string.digits
    validCharacters = alphas + '_' + digits
    idlen = len(id)
    if idlen <= 1:
        print 'ID is too short!'
        return

    if id[0] not in alphas:
        print 'ID should begin with alphas'
        return

    for index in range(1, idlen-1):
        if id[index] not in validCharacters:
            print 'Invalid characters found in your ID'
            return

    print 'congratulation! Your ID just passed validation!'


if __name__ == '__main__':
    checkid('!@dggh22')
    checkid('dg#$gh22')
    checkid('helloworld880719')
    checkid('3')
