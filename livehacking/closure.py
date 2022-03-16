def print_it(msg):
    def print_it_halt_endlich():
        print(msg)
    return print_it_halt_endlich

hansi = print_it('hansi')
satan = print_it(666)

hansi()
satan()
