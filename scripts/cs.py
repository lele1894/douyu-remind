import speedtest

def test_speed():
    st = speedtest.Speedtest()

    print("Finding best server...")
    st.get_best_server()

    print("Performing download test...")
    download_speed = st.download()
    
    print("Performing upload test...")
    upload_speed = st.upload()
    
    print("Performing ping test...")
    ping_result = st.results.ping
    
    print(f"Download speed: {download_speed / 1_000_000:.2f} Mbps")
    print(f"Upload speed: {upload_speed / 1_000_000:.2f} Mbps")
    print(f"Ping: {ping_result:.2f} ms")

if __name__ == "__main__":
    test_speed()
