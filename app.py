from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/form')
def form():
    return render_template('form.html')


## 폼에서 데이터 받아가기.
@app.route('/memos', methods=['POST'])
def new_post():
    title_receive = request.form['title_give']
    content_receive = request.form['content_give']
    emo_receive = request.form['emo_give']

    memo = {
        'title': title_receive,
        'content': content_receive,
        'emo': emo_receive
    }
    db.memos.insert_one(memo)
    return jsonify({'result':'success','msg':'입력이 완료되었습니다.'})


## 폼에서 받은 데이 터 뿌려주기.
@app.route('/memos', methods=['GET'])
def listing():
    memos = list(db.memos.find({},{'_id':0}))
    return jsonify({'result' : 'success','memos' : memos})



## 무드보드에 뿌려주기.
@app.route('/moodboard', methods=['GET'])
def moods():
    mood = list(db.memos.find({},))





if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)