def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('{}함수가 실행되었습니다.'.format(original_function.__name__))
        for arg in args:
            print(arg)
        return original_function(*args, **kwargs)
    return wrapper_function



@decorator_function
def display():
    pass

#display()

@decorator_function
def display():
    print('web programming 에서 많이 사용합니다.')

#display()

@decorator_function
def display_info(name, age):
    print('web programming(flask, django)에서 많이 사용합니다.')

display_info('lee',30)
