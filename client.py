import httpx

def main():
    url = "http://127.0.0.1:8000"
    with httpx.Client(base_url=url) as client:
        resp = client.get(
            "/recommendations/content-based/Hey, Soul Sister",
            params={"limit": 5}
        )
        print("Status:", resp.status_code)
        print("JSON response:\n", resp.json())

if __name__ == "__main__":
    main()
