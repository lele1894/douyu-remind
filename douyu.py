import requests
from datetime import datetime

def check_douyu(room_id):
    url = f"https://open.douyucdn.cn/api/RoomApi/room/{room_id}"
    response = requests.get(url)
    data = response.json()
    
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    if data['data']['room_status'] == '1':
        status = "斗鱼正常"
    else:
        status = "斗鱼关播"
        requests.post("http://miaotixing.com/trigger?id=tzLyHCO", data={"text": f"{status} at {current_time}"})
    
    with open("douyu.txt", "a") as file:
        file.write(f"{status} at {current_time}\n")

    print(f"{status} at {current_time}")

if __name__ == "__main__":
    import sys
    room_id = sys.argv[1] if len(sys.argv) > 1 else "292098"
    check_douyu(room_id)
