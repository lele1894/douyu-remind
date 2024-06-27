import requests
from datetime import datetime
import pytz

def check_douyu(room_id):
    url = f"https://open.douyucdn.cn/api/RoomApi/room/{room_id}"
    response = requests.get(url)
    data = response.json()
    
    # 获取当前+8时区时间
    target_timezone = pytz.timezone('Asia/Shanghai')
    current_time = datetime.now(target_timezone).strftime('%Y-%m-%d %H:%M:%S')
    
    if data['data']['room_status'] == '1':
        status = "斗鱼直播间运行正常"
    else:
        status = "斗鱼直播间停播，请检查"
        requests.post("http://miaotixing.com/trigger?id=tzLyHCO", data={"text": f"{status} 时间: {current_time}"})
    
    with open("douyu.txt", "a") as file:
        file.write(f"{status} 时间: {current_time}\n")

    print(f"{status} 时间: {current_time}")

if __name__ == "__main__":
    import sys
    room_id = sys.argv[1] if len(sys.argv) > 1 else "292098"
    check_douyu(room_id)
