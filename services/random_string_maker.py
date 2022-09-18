import random, string

class RandomStringMaker:
    
    def exec(num: int = 10) -> str:
        str = [random.choice(string.ascii_letters + string.digits) for i in range(num)]
        return ''.join(str)