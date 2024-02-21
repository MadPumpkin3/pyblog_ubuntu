from .settings import *

DEBUG = False

# DEBUG가 False 경우, ALLOWED_HOSTS에 공인 IP를 넣어야 한다.
ALLOWED_HOSTS = ['3.38.115.107'] # 클라우드 web or was IP, 도메인 차후 추가