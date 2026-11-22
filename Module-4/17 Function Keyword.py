def data(**user_data):
    for key,value in user_data.items():
        print(f"{key}:{value}")

data(name='Mithun',age=24,gender='Male')


def variable(*position, **keyword):
    for i in position:
        print(i)

    for  key, value in keyword.items():
        print(f"{key}:{value}")

variable(1,2,4,5,name='Mithun',age=25,qualification="Bteck")