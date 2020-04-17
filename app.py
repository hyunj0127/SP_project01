from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('form.html')





##새로운 일기 DB에 넣어주기
@app.route('/new', methods=['POST'])
def new_post():
    title_receive = int(request.form['title_give'])
    content_receive = request.form['content_give']
    emo_receive = request.form['emo_give']

    db.mymemo.insert_one({'title': title_receive, 'content': content_receive, 'emo' : emo_receive})

    return jsonify({'result':'success'})


## API 역할을 하는 부분.index에서
@app.route('/api/list', methods=['GET'])
def listing():
    memos = list(db.mymemo.find({},{'_id':False}))
    return jsonify({'result': 'success','memos_list':memos})



## 메모 지우는 부분 index.html에서 해야 됨.
@app.route('/api/delete', methods=['POST'])
def memo_delete():
    title_receive = request.form['title_give']
    db.mymemo.delete.one({'title':title_receive})
    return jsonify({'result':'success'})

print(listing)



if __name__ == '__main__':
    app.run('0.0.0.0', port=8000, debug=True)