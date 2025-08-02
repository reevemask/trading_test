from waitress import serve
from app import app
import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    print(f"Waitress 서버 시작... 포트: {port}")
    serve(app, host='0.0.0.0', port=port)
