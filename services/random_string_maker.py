import random, string

class RandomStringMaker:
    
    def exec(num: int = 30) -> str:
        str_list = [random.choice(string.ascii_letters + string.digits) for i in range(num)]
        str = ''.join(str_list)
        return str