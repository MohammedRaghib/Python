# Extra
def mockery():

    sentence = input('Type something (to exit type exit): ')

    if sentence == 'exit':
        print('Goodbye!')
    else:
        print(f'You typed this: "{sentence}"')
        mockery()
mockery()


def bettermock():
    while True:
        sentence = input('Type: ')

        if sentence == 'exit':
            print('Good day to you!')
            break
        else:
            print(f'You said: {sentence}')
bettermock()