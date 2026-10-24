"""Steam Pazar Panosu veri hattı.

SteamSpy'dan en popüler oyunları, Steam Web API'den anlık oyuncu sayısını çeker.
Çıktı: data/latest.json (arayüz bunu okur) ve data/history.csv (her çalıştırmada
bir özet satırı: kendi zaman serimiz). Anahtar gerekmez.
Hata olursa mevcut data/latest.json'a dokunulmaz (son başarılı veri korunur).
"""
import csv, datetime, json, os, statistics, sys, time, urllib.error, urllib.request

SPY = "https://steamspy.com/api.php"
PLAYERS = "https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?appid={}"
UA = {"User-Agent": "steam-pazar-panosu/1.0 (ogrenci odevi)"}
OUT = os.path.join(os.path.dirname(__file__), "..", "data")


def get(url, tries=3):
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
                return json.load(r)
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as e:
            print(f"uyarı: {url} -> {e}", file=sys.stderr)
            time.sleep(2 * (i + 1))
    return None


def main():
    top = get(f"{SPY}?request=top100in2weeks")
    if not top:
        sys.exit("SteamSpy yanıt vermedi; mevcut veri korunuyor.")

    games = []
    for appid, g in top.items():
        detail = get(f"{SPY}?request=appdetails&appid={appid}") or {}
        time.sleep(1.1)  # SteamSpy hız sınırı: saniyede ~1 istek
        live = get(PLAYERS.format(appid)) or {}
        time.sleep(0.3)
        players = live.get("response", {}).get("player_count")
        if players is None:
            players = g.get("ccu", 0)
        genre = (detail.get("genre") or "Bilinmiyor").split(",")[0].strip()
        pos, neg = g.get("positive", 0), g.get("negative", 0)
        games.append({
            "appid": int(appid),
            "name": g.get("name", "?"),
            "genre": genre,
            "price": int(g.get("price") or 0) / 100,  # SteamSpy: ABD doları, sent
            "players": int(players),
            "rating": round(100 * pos / (pos + neg), 1) if pos + neg else None,
        })

    if len(games) < 20:
        sys.exit("Çok az oyun alındı; mevcut veri korunuyor.")

    now = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0)
    os.makedirs(OUT, exist_ok=True)
    tmp = os.path.join(OUT, "latest.json.tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump({"updated": now.isoformat(), "source": "SteamSpy + Steam Web API", "games": games},
                  f, ensure_ascii=False)
    os.replace(tmp, os.path.join(OUT, "latest.json"))  # yarım dosya kalmasın

    hist = os.path.join(OUT, "history.csv")
    new = not os.path.exists(hist)
    with open(hist, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if new:
            w.writerow(["timestamp", "games", "total_players", "median_price"])
        w.writerow([now.isoformat(), len(games), sum(x["players"] for x in games),
                    statistics.median(x["price"] for x in games)])
    print(f"{len(games)} oyun yazıldı.")


if __name__ == "__main__":
    main()
