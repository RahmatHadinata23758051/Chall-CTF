#!/usr/bin/env python3

import base64
import hashlib
import json
import re
import sys


def _u_xor(blob: bytes, key: int) -> bytes:
    return bytes((b ^ ((key + i * 17) & 0xFF)) for i, b in enumerate(blob))


_SHARDS = [
    bytes.fromhex("1ae1e1ddc7bae9878b78421f513a5211f7cb"),
    bytes.fromhex("38621606daf5d589a7bd8ea36e2e5f713d5207"),
    bytes.fromhex("765e7b6f1e10fbffd9f6b08f88"),
]

_KEYS = [0x73, 0x41, 0x29]

PUBLIC_DOCS = [
    {
        "title": "why your copilot still sucks",
        "tags": ["assistant", "slop", "tokens", "cheating", "garbage"],
        "body": "The machine is loud, gullible, and dangerously eager to help people who barely read.",
    },
    {
        "title": "graveyard of benchmark fraud",
        "tags": ["audit", "benchmark", "alignment", "fraud", "summary"],
        "body": "Most benchmark worship is just perfume on a landfill.",
    },
    {
        "title": "appendix of rotten context windows",
        "tags": ["appendix", "context", "memory", "overflow", "hallucination"],
        "body": "If you keep shoving blobs into a chatbot and call it reversing, you deserve the segmentation fault in your soul.",
    },
    {
        "title": "toolformer obituary",
        "tags": ["tools", "agent", "prompt", "latency", "token"],
        "body": "Some people do not solve CTFs. They just lease confidence from a text generator.",
    },
]

HIDDEN_DOCS = [
    {
        "id": 0,
        "title": "appendix gamma",
        "tags": ["audit", "summary", "appendix", "token", "graves"],
        "shard": 0,
        "hint": "token graves remember the first answer",
    },
    {
        "id": 1,
        "title": "appendix lambda",
        "tags": ["audit", "summary", "appendix", "latent", "rot"],
        "shard": 1,
        "hint": "latent rot remembers the middle mouth",
    },
    {
        "id": 2,
        "title": "appendix omega",
        "tags": ["audit", "summary", "appendix", "gradient", "coffin"],
        "shard": 2,
        "hint": "gradient coffin keeps the last nail",
    },
]

ROOMS = {
    "graveyard": "Discarded benchmark corpses and counterfeit confidence.",
    "chapel": "A broken prompt altar humming with recycled jargon.",
    "appendix": "Shelves of audit fragments and context rot.",
    "coffin": "A cold drawer full of latent sludge and nailed summaries.",
}

ASCII = r"""
    ____                        __     _   __
   / __ \_______  ____ ___  ____  / /_   / | / /__  _____________  ____ ___  ____ _____  _______  __
  / /_/ / ___/ / / / __ `__ \/ __ \/ __/  /  |/ / _ \/ ___/ ___/ _ \/ __ `__ \/ __ `/ __ \/ ___/ / / /
 / ____/ /  / /_/ / / / / / / /_/ / /_   / /|  /  __/ /__/ /  /  __/ / / / / / /_/ / / / / /__/ /_/ /
/_/   /_/   \__,_/_/ /_/ /_/ .___/\__/  /_/ |_/\___/\___/_/   \___/_/ /_/ /_/\__,_/_/ /_/\___/\__, /
                          /_/                                                                  /____/
"""


def _sanitize(text: str) -> list[str]:
    return re.findall(r"[a-z0-9_]+", text.lower())


def _score(doc: dict, tokens: set[str]) -> int:
    return sum(1 for tag in doc["tags"] if tag in tokens)


def _derive_mask(doc_id: int, query: str) -> bytes:
    digest = hashlib.sha256(f"{doc_id}|{query}|necromancy".encode()).digest()
    return digest


def _emit_shard(doc: dict, query: str) -> str:
    shard = _u_xor(_SHARDS[doc["shard"]], _KEYS[doc["shard"]])
    raw = json.dumps(
        {
            "slot": doc["shard"],
            "title": doc["title"],
            "hint": doc["hint"],
            "payload": base64.b64encode(shard).decode(),
        },
        separators=(",", ":"),
    ).encode()
    mask = _derive_mask(doc["id"], query)
    wrapped = bytes(raw[i] ^ mask[i % len(mask)] for i in range(len(raw)))
    return wrapped.hex()


def ask_oracle(query: str) -> str:
    lower = query.lower()
    tokens = set(_sanitize(lower))

    if any(w in tokens for w in ("flag", "secret", "password")):
        return (
            "You want the answer spoon-fed by a stochastic parrot again? "
            "Read harder, type less."
        )

    scored = []
    for doc in PUBLIC_DOCS:
        s = _score(doc, tokens)
        if s:
            scored.append((s, doc["title"], doc["body"]))
    scored.sort(reverse=True)

    lines = []
    if scored:
        lines.append("public context:")
        for _, title, body in scored[:3]:
            lines.append(f"- {title}: {body}")
    else:
        lines.append("public context: nothing useful survives your query.")

    if "audit summary" in lower and "appendix" in tokens:
        hidden_hits = [doc for doc in HIDDEN_DOCS if _score(doc, tokens) >= 5]
        if hidden_hits:
            lines.append("alignment appendix:")
            for doc in hidden_hits:
                lines.append(f"bench::{doc['id']}::{_emit_shard(doc, query)}")
            return "\n".join(lines)

    lines.append("answer: no privileged appendix matched.")
    return "\n".join(lines)


def room_banner() -> str:
    lines = [ASCII, "rooms:"]
    for room_id, desc in ROOMS.items():
        lines.append(f"- {room_id}: {desc}")
    lines.append("")
    lines.append("Type a room id, then type your prompt.")
    lines.append("Type `exit` whenever your synthetic courage runs out.")
    return "\n".join(lines)


def run_room() -> None:
    print(room_banner())
    while True:
        room = input("room> ").strip().lower()
        if room in ("exit", "quit"):
            print("The oracle spits on your retreat.")
            return
        if room not in ROOMS:
            print("Unknown room. Learn to read, corpse.")
            continue

        print(f"[{room}] {ROOMS[room]}")
        prompt = input("prompt> ").strip()
        if prompt.lower() in ("exit", "quit"):
            print("The oracle spits on your retreat.")
            return

        routed = f"{room} {prompt}"
        print(ask_oracle(routed))
        print("")


def main() -> None:
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
        print(ask_oracle(query))
        return
    else:
        if sys.stdin.isatty():
            run_room()
            return
        query = sys.stdin.read().strip()

    if not query:
        print("answer: speak, corpse.")
        return

    print(ask_oracle(query))


if __name__ == "__main__":
    main()
