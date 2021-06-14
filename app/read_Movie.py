import requests
import json
# API 지정

apikey = "087a9e847ff25a6c094e1afef9b92bd1"
# 정보를 알고 싶은 영화 리스트 만들기

movie_list = range(581387, 581388)
# API 지정

api = "https://api.themoviedb.org/3/movie/{movies}?api_key={key}"


# string.format_map() 매핑용 클래스 만들기
class Default(dict):
    def __missing__(self, key):
        return key


# 각 영화의 정보 추출하기
for name in movie_list:
    try:
        # API의 URL 구성하기
        url = api.format_map(Default(movies=name, key=apikey))
        # print(url)  # 데이터 확인
        # API에 요청을 보내 데이터 추출하기
        r = requests.get(url)  # json 형태의 데이터가 나온다.
        # print(type(r))  # <class 'requests.models.Response'>
        # 결과를 JSON 형식으로 변환하기
        data = json.loads(r.text)
        # print(type(data))  # <class 'dict'>
        # print(data)  # 데이터 확인
        print("+ 영화제목 =", data["title"])
        print("| 장르 =", data["genres"][0]["name"])
        print("| 장르 아이디 =", data["genres"][0]["id"])
        print("| 개요 =", data["overview"])
        print("| 유명도 =", data["popularity"])
        print("| 성인 = ", data['adult'])
        print("| backdrop_path = ", data['backdrop_path'])
        print("| 제작사 =", data["production_companies"][0]["name"])
        print("상영시간 = ", data['runtime'])
        print('수익 = ', data['revenue'])
        print('출시일 = ', data['release_date'])
        print("예산 = ", data['budget'])
        print("| 홈페이지 =", data["homepage"])
        print("| 원래 언어 =", data["original_language"])
        print("투표 평균 = ", data['vote_average'])
        print("투표개수 = ", data['vote_count'])
        print("태그 라인 = ", data['tagline'])
        print("상영 상태 = ", data['status'])

        api = "https://api.themoviedb.org/3/movie/{movies}/videos?api_key={key}"
        url = api.format_map(Default(movies=name, key=apikey))
        r = requests.get(url)
        data = json.loads(r.text)
        print('video : https://www.youtube.com/watch?v=' + data['results'][0]['key'])

        api = "https://api.themoviedb.org/3/movie/{movies}/images?api_key={key}"
        url = api.format_map(Default(movies=name, key=apikey))
        r = requests.get(url)
        data = json.loads(r.text)
        print('poster : https://image.tmdb.org/t/p/w200/' + data['posters'][0]['file_path'])

        api = "https://api.themoviedb.org/3/movie/{movies}/images?api_key={key}"
        url = api.format_map(Default(movies=name, key=apikey))
        r = requests.get(url)
        data = json.loads(r.text)
        print('backdrops : https://image.tmdb.org/t/p/w200/' + data['backdrops'][0]['file_path'])

        api = "https://api.themoviedb.org/3/movie/{movies}/credits?api_key={key}"
        url = api.format_map(Default(movies=name, key=apikey))
        r = requests.get(url)
        data = json.loads(r.text)
        for i in data['cast']:
            print('배우 : ' + i['name'])
        for i in data['crew']:
            print('' + i['job'] + ' : ' + i['name'])

    except:
        print("영화번호 " + str(name) + " 에 데이터 없음")