from flask import Flask

# API 서버 구축하기 위한 기본 구조
app = Flask(__name__)

# API가 있어야 한다.
# API는 함수로 처리한다.
@app.route('/', methods = ['GET'])
def hello_world() :
    return 'Hello world'

if __name__ == '__main__' :
    app.run()