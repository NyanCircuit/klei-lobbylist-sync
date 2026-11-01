### klei-lobbylist-sync

每小时同步 Klei Steam 版《饥荒联机版》全地区大厅列表，并提交到仓库根目录。

Syncs the full-region Klei lobby list for Steam Don't Starve Together every hour, committed to the repository root.

### 说明

本仓库通过 GitHub Actions **每小时**拉取 Klei 公开大厅 CDN 的 Steam 版服务器列表，保存为 JSON 文件并自动提交。数据仅供查询与分析，不保证实时性。

### 文件

| 文件 | 说明 |
| --- | --- |
| `us-east-1-Steam.json` | 美东区域 |
| `eu-central-1-Steam.json` | 欧洲中部区域 |
| `ap-southeast-1-Steam.json` | 亚太东南区域 |
| `ap-east-1-Steam.json` | 亚太东部区域 |
| `sync_lobby.py` | 同步脚本 |
| `.github/workflows/sync-lobby.yml` | 定时任务配置 |

### 数据来源

`https://lobby-v2-cdn.klei.com/{region}-Steam.json.gz`

可用区域由 `https://lobby-v2-cdn.klei.com/regioncapabilities-v2.json` 提供。

### 手动运行

```bash
pip install requests
python sync_lobby.py
```

### 注意

- 由 GitHub Actions 定时执行，实际触发时间可能有延迟。
- 任一区域拉取失败则整体退出、不提交，避免残缺数据覆盖旧快照。

---

### About

This repository uses GitHub Actions to fetch the Steam lobby list for Don't Starve Together from Klei's public CDN **every hour**, saves it as JSON, and commits automatically. Data is for lookup and analysis only; freshness is not guaranteed.

### Files

| File | Description |
| --- | --- |
| `us-east-1-Steam.json` | US East |
| `eu-central-1-Steam.json` | EU Central |
| `ap-southeast-1-Steam.json` | AP Southeast |
| `ap-east-1-Steam.json` | AP East |
| `sync_lobby.py` | Sync script |
| `.github/workflows/sync-lobby.yml` | Workflow config |

### Source

`https://lobby-v2-cdn.klei.com/{region}-Steam.json.gz`

Available regions are listed in `https://lobby-v2-cdn.klei.com/regioncapabilities-v2.json`.

### Run Locally

```bash
pip install requests
python sync_lobby.py
```

### Notes

- Scheduled by GitHub Actions; actual trigger time may be delayed.
- If any region fails, the run exits without committing, so a broken snapshot never overwrites the previous one.
