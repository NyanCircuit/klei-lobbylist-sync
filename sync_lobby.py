import gzip, json, sys, requests
from pathlib import Path

CAP = "https://lobby-v2-cdn.klei.com/regioncapabilities-v2.json"
LIST = "https://lobby-v2-cdn.klei.com/{}-Steam.json.gz"
H = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept": "*/*",
}

def fetch(url):
    r = requests.get(url, headers=H, timeout=120)
    r.raise_for_status()
    raw = r.content
    if raw[:2] == b"\x1f\x8b":
        raw = gzip.decompress(raw)
    return json.loads(raw)

def main():
    out = Path(".")
    regions = [x["Region"] for x in fetch(CAP)["LobbyRegions"]]
    print("regions:", regions)
    failed = []
    for rg in regions:
        try:
            data = fetch(LIST.format(rg))
            (out / f"{rg}-Steam.json").write_text(
                json.dumps(data, ensure_ascii=False), encoding="utf-8"
            )
            print(f"ok  {rg}")
        except Exception as e:
            failed.append(rg)
            print(f"err {rg}: {e!r}", file=sys.stderr)
    if failed:
        print("failed regions:", failed, file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()