#!/usr/bin/env python3
"""Create/check a reader's own record. Structural checks do not prove reading."""
import argparse
import collections
import json
from pathlib import Path


def corpus():
    return json.loads((Path(__file__).resolve().parents[1] / "references/reading-ledger.json").read_text())["articles"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=["init", "check"])
    parser.add_argument("record", type=Path)
    args = parser.parse_args()
    articles = corpus()
    expected = {str(a.get("doi") or a["title"]): a for a in articles}
    if len(expected) != 150:
        raise SystemExit("Corpus must contain 150 unique articles")
    if args.action == "init":
        rows = [{"id": key, "journal_group": a["journal_group"], "title": a["title"],
                 "status": "unread", "opened_source": "", "source_access_reference": "",
                 "actual_version": "", "full_main_text_read": False,
                 "sections": [], "observations": [], "blocked_reason": ""}
                for key, a in expected.items()]
        args.record.parent.mkdir(parents=True, exist_ok=True)
        with args.record.open("x") as stream:
            json.dump({"scope": "Reader-created source records; all entries start unread", "articles": rows}, stream, indent=2)
            stream.write("\n")
        print("Initialized 150 unread articles; no inherited completion flags.")
        return
    rows = json.loads(args.record.read_text())["articles"]
    ids = [r.get("id") for r in rows]
    if len(ids) != 150 or set(ids) != set(expected) or len(set(ids)) != len(ids):
        raise SystemExit("Record must cover each of the 150 source articles exactly once")
    complete = collections.Counter()
    blocked = 0
    incomplete = []
    for row in rows:
        if row.get("status") == "blocked":
            blocked += 1
            if not row.get("blocked_reason", "").strip():
                incomplete.append((row["title"], "blocked without a reason"))
            continue
        fields = ["opened_source", "source_access_reference", "actual_version"]
        sections = row.get("sections", [])
        observations = row.get("observations", [])
        valid = (row.get("status") == "read" and row.get("full_main_text_read") is True
                 and all(isinstance(row.get(k), str) and row[k].strip() for k in fields)
                 and len(sections) >= 3 and all(isinstance(s, dict) and s.get("section") and s.get("location") for s in sections)
                 and len(observations) >= 3 and all(isinstance(o, dict) and all(isinstance(o.get(k), str) and len(o[k].split()) >= (1 if k == "location" else 5) for k in ["location", "choice", "why_it_works", "transfer"]) for o in observations))
        if valid:
            complete[expected[row["id"]]["journal_group"]] += 1
        else:
            incomplete.append((row["title"], "unread or incomplete source record"))
    total = sum(complete.values())
    print(json.dumps({"complete_records": total, "blocked": blocked,
                      "incomplete": len(incomplete), "by_journal": dict(complete),
                      "note": "Records are structural evidence; the checker cannot establish comprehension."}, indent=2))
    if total != 150:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
