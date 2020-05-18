def name():
    a = 'amar'
    def sir_name():
        # nonlocal a
        a = 'radha'
        print('sir_name',a)
    sir_name()
    print('inner',a)
name()

