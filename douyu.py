import requests

def check_douyu(room_id):
    url = f"https://open.douyucdn.cn/api/RoomApi/room/{room_id}"
    response = requests.get(url)
    data = response.json()
    
    if data['data']['room_status'] == '1':
        print("斗鱼正常")
    else:
        print("斗鱼关播")
        requests.post("http://miaotixing.com/trigger?id=tzLyHCO", data={"text": "斗鱼关播"})

if __name__ == "__main__":
    import sys
    room_id = sys.argv[1] if len(sys.argv) > 1 else "292098"
    check_douyu(room_id)
