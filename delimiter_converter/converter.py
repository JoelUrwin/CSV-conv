
class Converter():

    def __init__(self, args):
        self.dict = dict()
        self.column_names = list()
        self.list = list()
        self.rowdepth = int()

        #Converting the file from IOWrapper to a String.
        def convert():
            file = args['f'].read()
            ln_file = file.splitlines()
            self.rowdepth = 0

            for line in ln_file:
                line = line.split(",")
                line = [i.strip(' ') for i in line]
                line = [i.strip('.') for i in line]
                if self.rowdepth < len(line):
                    self.rowdepth = len(line)

                self.list.append(line)

            column_create()

        def column_create():
            for x in (range(self.rowdepth)):
                try:
                    i = str(input(f"Input Column Name (Data : {self.list[0][x]}): "))
                    self.column_names.append(i)
                except ValueError:
                    print("Value is not a string!")

        if args['json'] is True:
            parsed_file = convert()
            print("json")
        if args['yml'] is True:
            parsed_file = convert()
            print("yml")
        if args['sql'] is True:
            parsed_file = convert()
            print("sql")
        if args['enum'] is True:
            parsed_file = convert()
            print("enum")