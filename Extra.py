# Extra
def mockery():

    sentence = input('Type something (to exit type exit): ')

    if sentence == 'exit':
        print('Goodbye!')
    else:
        print(f'You typed this: "{sentence}"')
        mockery()
mockery()