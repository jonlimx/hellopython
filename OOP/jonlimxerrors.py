# a simple exception demo
class WrongWayError(Exception):
    def __init__(self, message):
        Exception.__init__(self)
        self.message = message

    def getErrorMessage(self):
        return self.message


if __name__ == '__main__':
    direction = 'Right'
    try:
        if direction != 'Left':
            raise WrongWayError('You Choose a wrong way!')
    except WrongWayError as ex:
        print(ex.getErrorMessage())
    finally:
        print('Hope you choose a right way.')
