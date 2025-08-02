from flask import Flask, jsonify
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    """서버 상태 확인"""
    return jsonify({
        'status': 'success',
        'message': '🎉 서버가 정상 작동중입니다!',
        'time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'server': 'Railway Flask Server'
    })

@app.route('/test', methods=['GET'])
def test():
    """간단한 테스트"""
    return jsonify({
        'status': 'success',
        'message': '✅ /test 경로 정상 작동!',
        'time': datetime.now().strftime("%H:%M:%S")
    })

@app.route('/hello', methods=['GET'])
def hello():
    """추가 테스트"""
    return "Hello World! 서버가 살아있어요! 🚀"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    print(f"서버 시작 중... 포트: {port}")
    print(f"사용 가능한 라우트: {[rule.rule for rule in app.url_map.iter_rules()]}")
    app.run(host='0.0.0.0', port=port, debug=False)
