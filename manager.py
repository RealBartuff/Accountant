
class NotEnoughDataException(Exception):
    pass


class NotEnoughMoneyException(Exception):
    pass


class NotEnoughStockException(Exception):
    pass


class NoActionException(Exception):
    pass


class Manager:
    def __init__(self, reader):
        self.reader = reader
        self.history = []
        self.account = 0
        self.stock = {}
        self.actions = {}

    def modify_account(self, value):
        if self.account + value < 0:
            raise NotEnoughMoneyException()
        self.account += value

    def add_history(self, row):
        self.history.append(row)

    def modify_stock(self, item, qty):
        if item not in self.stock:
            self.stock[item] = 0
        if self.stock[item] + qty < 0:
            raise NotEnoughStockException()
        self.stock[item] += qty

    def action(self, name, parameters):
        def action_in(callback):
            self.actions[name] = (parameters, callback)
        return action_in

    def process(self):
        while True:
            action = self.reader.get_line()[0]
            if action == 'stop':
                break
            if action not in self.actions:
                raise NoActionException()
            parameters, callback = self.actions[action]
            rows = self.reader.get_line(parameters)
            self.add_history([action] + rows)
            callback(self, rows)

    def review(self, start, end):
        for x in self.history[int(start):int(end)]:
            for i in x:
                print(i)

    def check_stock(self, items):
        for item in items:
            if item not in self.stock:
                self.stock[item] = 0.0
        print(self.stock)


class Reader:
    def __init__(self, path):
        self.path_file = path
        self.file1 = open(path)

    def get_line(self, count=1):
        countlist = []
        for i in range(count):
            read_line = self.file1.readline()
            if not read_line:
                raise NotEnoughDataException("za malo danych w pliku")
            countlist.append(read_line.strip())
        return countlist


class Writer(Reader):
    def __init__(self, path, path2):
        self.path_file = path
        self.file1 = open(path)
        self.file2 = open(path2, "w")

    def write_line(self, actions):
        content = self.file1.readlines()
        content.insert(-1, (str(actions) + "\n"))
        f = "".join(content)
        self.file2.write(f)
