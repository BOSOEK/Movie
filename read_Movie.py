import requests
import json
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django

django.setup()

from MovieApp.models import Movie
# API 지정

apikey = "087a9e847ff25a6c094e1afef9b92bd1"
# 정보를 알고 싶은 영화 리스트 만들기

movie_list = range(15374, 559000)
# string.format_map() 매핑용 클래스 만들기
class Default(dict):
    def __missing__(self, key):
        return key


# 각 영화의 정보 추출하기
for name in movie_list:
    try:
        # API의 URL 구성하기
        # API 지정
        api = "https://api.themoviedb.org/3/movie/{movies}?api_key={key}&language=ko-KR"
        url = api.format_map(Default(movies=name, key=apikey))
        # print(url)  # 데이터 확인
        # API에 요청을 보내 데이터 추출하기
        r = requests.get(url)  # json 형태의 데이터가 나온다.
        # print(type(r))  # <class 'requests.models.Response'>
        # 결과를 JSON 형식으로 변환하기
        data = json.loads(r.text)
        #print(type(data))  # <class 'dict'>
        #print(data)  # 데이터 확인
        MovieTitle = data['title']
        #print("+ 영화제목 = " + MovieTitle + str(type(MovieTitle)))
        MovieGenres = data["genres"][0]["name"]
        #print("| 장르 =" + MovieGenres + str(type(MovieGenres)))
        MovieOverview = data["overview"]
        #print("| 개요 =" + MovieOverview + str(type(MovieOverview)))
        MoviePopularity = data["popularity"]
        #print("| 유명도 =" + str(MoviePopularity) + str(type(MoviePopularity)))
        MovieAdult = data['adult']
        #print("| 성인 = " + str(MovieAdult) + str(type(MovieAdult)))
        MovieProduction = data["production_companies"][0]["name"]
        #print("| 제작사 =" + MovieProduction + str(type(MovieProduction)))
        MovieRuntime = int(data['runtime'])
        #print("상영시간 = " + str(MovieRuntime) + str(type(MovieRuntime)))
        MovieRelease = data['release_date']
        #print('출시일 = ' + str(MovieRelease) + str(type(MovieRelease)))
        MovieDudget = data['budget']
        #print("예산 = " + str(MovieDudget) + str(type(MovieDudget)))
        MovieVoteAver = data['vote_average']
        #print("투표 평균 = " + str(MovieVoteAver) + str(type(MovieVoteAver)))
        MovieVoteCount = data['vote_count']
        #print("투표개수 = " + str(MovieVoteCount) + str(type(MovieVoteCount)))
        MovieTagline = data['tagline']
        #print("태그 라인 = " + MovieTagline + str(type(MovieTagline)))
        MovieStatus = data['status']
        #print("상영 상태 = " + MovieStatus + str(type(MovieStatus)))

        api = "https://api.themoviedb.org/3/movie/{movies}/videos?api_key={key}"
        url = api.format_map(Default(movies=name, key=apikey))
        r = requests.get(url)
        data = json.loads(r.text)
        MovieResults = 'https://www.youtube.com/watch?v=' + data['results'][0]['key']
        #print('video : ' + MovieResults + str(type(MovieResults)))

        api = "https://api.themoviedb.org/3/movie/{movies}/images?api_key={key}"
        url = api.format_map(Default(movies=name, key=apikey))
        r = requests.get(url)
        data = json.loads(r.text)
        MoviePoster = 'https://image.tmdb.org/t/p/w200/' + data['posters'][0]['file_path']
        #print('poster : ' + MoviePoster + str(type(MoviePoster)))

        api = "https://api.themoviedb.org/3/movie/{movies}/images?api_key={key}"
        url = api.format_map(Default(movies=name, key=apikey))
        r = requests.get(url)
        data = json.loads(r.text)
        MovieBackdrop = 'https://image.tmdb.org/t/p/w200/' + data['backdrops'][0]['file_path']
        #print('backdrops : ' + MovieBackdrop + str(type(MovieBackdrop)))

        api = "https://api.themoviedb.org/3/movie/{movies}/credits?api_key={key}"
        url = api.format_map(Default(movies=name, key=apikey))
        r = requests.get(url)
        data = json.loads(r.text)
        MovieCast = ''
        MovieCrew = ''
        for i in data['cast']:
            MovieCast = MovieCast.split()
            MovieCast.insert(len(MovieCast), '_' + i['name'])
            MovieCast = ' '.join(MovieCast)
        #print('배우 : ' + MovieCast + str(type(MovieCast)))

        for i in data['crew']:
            if i['job'] == 'Director':
                MovieCrew = i['name']
                #print('Director : ' + MovieCrew + str(type(MovieCrew)))
                break
        movies = Movie(title=MovieTitle, genres=MovieGenres, overview=MovieOverview, adult=MovieAdult, production=MovieProduction,
                       runtime=MovieRuntime, release=MovieRelease, budget=MovieDudget, voteAver=MovieVoteAver, voteCount=MovieVoteCount, status=MovieStatus, video=MovieResults, poster=MoviePoster, backdrop=MovieBackdrop, cast=MovieCast, director=MovieCrew)
        movies.save()
        print("영화번호 " + str(name) + " 저장 성공")
    except:
       print("영화번호 " + str(name) + " 에 데이터 없음")
