from abc import ABCMeta, abstractmethod


class IConnectionState(object, metaclass=ABCMeta):
    @abstractmethod
    def open(self, conn):
        pass

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass

    @abstractmethod
    def close(self, conn):
        pass


class OpenState(IConnectionState):
    def open(self, conn):
        raise RuntimeError('It\'s already opened!!!')

    def read(self):
        print('Reading...')

    def write(self):
        print('Writing...')

    def close(self, conn):
        print('Closing')
        conn.set_state(CloseState())


class CloseState(IConnectionState):
    def open(self, conn):
        print('Opening...')
        conn.set_state(OpenState())

    def read(self):
        raise RuntimeError('Please open it before you read...')

    def write(self):
        raise RuntimeError('Please open it before you write...')

    def close(self, conn):
        raise RuntimeError('It\'s already closed!!!')


class Connection(object):
    def __init__(self):
        self._state = CloseState()

    def set_state(self, state):
        self._state = state

    def open(self):
        self._state.open(self)

    def read(self):
        self._state.read()

    def write(self):
        self._state.write()

    def close(self):
        self._state.close(self)

if __name__ == '__main__':
    conn = Connection()
    #conn.read()
    conn.open()
    #conn.open()
    conn.write()
    conn.close()

