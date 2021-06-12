import requests

class URLMaker() :
    # base_url 설정 - 클래스 변수 : 클래스 사용 내내 고정된 값 - 모든 클래스에서 공유 가능
    base_url = 'https://developers.themoviedb.org/3'

    # 생성자 - api_key를 인스턴스 변수로 초기화 하여 생성
    def __init__(self, key):
        self.key = key

    # 인스턴스 메서드, url 반환
    def get_url(self, category, feature, **kwargs):  # param으로 가변 인자로 받아온다 - query string 방식 이요을 위해
        # -class 속성인 base_url에 접근
        # - category, feature는 인스턴스에 할당되어 있는 변수가 아닌
        # 함수의 인자 argument로 들어온 값이기 때문에 self.변수명 형태가 아니라
        # 인자값(아규먼트값)을 바로 사용한다.
        url = f'{URLMaker.base_url}/{category}/{feature}'

        # 인스턴스 생성시, 인스턴스 변수로 저장된 api_key 값을 받아온다
        url += f'?api_key={self.key}'

        # 가변인자로 받아온 값을 쿼리스트링 방식으로 url에 이어준다.
        for key, value in kwargs.items() :
            url += f'&{key}={value}'

        return url

    # 인스턴스 메서드
    # 영화 제목을 입력받아 영화 아이디를 반환
    # - 요청으로 받을 응답에 영화정보 데이터가 있을 것이고, 그 id를 반환해 줄 것이다.
    def movie_id(self, title):
        # 인서턴스 메서드인 get_url() 호출 (self/move는 영화제목을 받아 영화정보를 반환)
        # - title을 입력하면 해당 영화제목에 맞는 영화 정보 url을 반환
        url = self.get_url('search', 'movie', region='KR', language='ko', query=title)

        # 만들어진 url을 통해 서버에 요청해, 응답을 받아온다.
        response = requests.get(url)

        # 받아온 데이터를 json -> dict으로 변환
        movie_dict = response.json()

        # 만약 영화 제목에 해당하는 값이 있다면
        if movie_dict.get('results') :
            # movie_dict에서 movie_id를 추출한다
            result = movie_dict.get('result')[0].get('id')
            # 영화 제목에 해당하는 id 반환
            return result
        # 해당하는 값이 없다면, -result가 비어있다면
        else :
            return None  # None 출력

maker = URLMaker('[api_key]')

print(maker.get_url('movie', 'popular', region='KR', language='ko'))