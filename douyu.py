import requests
from datetime import datetime

def check_douyu(room_id):
    url = f"https://open.douyucdn.cn/api/RoomApi/room/{room_id}"
    response = requests.get(url)
    data = response.json()
    
    if data['data']['room_status'] == '1':
        print("斗鱼正常")
    else:
        print("斗鱼关播")
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        message = f"斗鱼关播 at {current_time}"
        requests.post("http://miaotixing.com/trigger?id=tzLyHCO", data={"text": message})

if __name__ == "__main__":
    import sys
    room_id = sys.argv[1] if len(sys.argv) > 1 else "292098"
    check_douyu(room_id)
