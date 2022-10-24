class Converter():

    def __init__(self, args):

        #Converting the file from IOWrapper to a String.
        def convert():
            file = args['f'].read()
            ln_file = file.splitlines()
            for line in ln_file:
                return line

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