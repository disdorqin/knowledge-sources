#!/usr/bin/env python3
"""Dependency-free static metadata integrity checks; no network or user data."""
import json
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
D = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
assert D["schema"] == "knowledge-source-shelf/v1"
topics = {t["id"]:t for t in D["topics"]}
assert len(topics) == len(D["topics"]) == 8
assert len(D["sources"]) <= 30
ids, repos = set(), set()
readme = (ROOT / "README.md").read_text(encoding="utf-8")
for t in topics.values():
    assert (ROOT / t["path"]).is_file(), f"missing topic {t['path']}"
    assert f'({t["path"]})' in readme, f"topic missing from README: {t['id']}"
for item in D["sources"]:
    id_, repo, topic = item["id"],item["repo"],item["topic"]
    assert id_ not in ids and repo not in repos and topic in topics
    ids.add(id_); repos.add(repo)
    assert repo.count("/") == 1 and item["url"] == "https://github.com/" + repo
    assert item["official_source"] and item["copying"] == "link-only"
    assert all(item[k].strip() for k in ("title","role","boundary","kind","checked_at"))
    source_md = (ROOT / topics[topic]["path"]).read_text(encoding="utf-8")
    assert f"https://github.com/{repo}" in source_md, f"{repo} absent in topic"
counts=Counter(s["topic"] for s in D["sources"])
assert max(counts.values()) <= 6
assert min(counts.values()) >= 1
print(f'PASS: {len(D["sources"])} unique remote sources; {len(topics)} topical routes; no third-party bodies')
