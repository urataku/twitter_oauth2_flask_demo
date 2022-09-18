from services.random_string_maker import RandomStringMaker

class TokenCodeManager:
    
    def create_code(session) -> None:
        random_str = RandomStringMaker.exec()
        session['token_code'] = random_str
        
    def fetch_code(session) -> str:
        return session.get('token_code')
