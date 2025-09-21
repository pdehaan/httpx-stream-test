import asyncio
import json
import os
from pathlib import Path
from typing import Any

import eyed3
from eyed3.id3.frames import ChapterFrame
import httpx
from slugify import slugify

MP3_DIR = Path("data")

files = [
    # Fetch a few short podcasts from Next Big Idea Club Daily...
    (
        "https://traffic.megaphone.fm/LI1822509615.mp3?updated=1752096385",
        "Who Designed Design?",
    ),
    (
        "https://traffic.megaphone.fm/LI9350708647.mp3?updated=1747925465",
        "What Cultures Around the World Can Teach You About Parenting",
    ),
    ("https://traffic.megaphone.fm/LI4466753945.mp3?updated=1746118282", "Bears!"),
    (
        "https://dts.podtrac.com/redirect.mp3/files.realpython.com/podcasts/RPP_E266_03_Kyle.9d97c7238336.mp3",
        "Dangers of Automatically Converting a REST API to MCP",
    ),
]


def main(max_items: int = 5):
    # Only process the first `n` list items...
    download_episodes(files[:max_items])


# TODO: Convert tuple to dict to match podcast structure?
def download_episodes(files: list[tuple[str, str]]) -> None:
    for file_url, title in files:
        filename = f"{slugify(title)}.mp3"
        destination_path = MP3_DIR / filename

        if not os.path.isfile(destination_path):
            asyncio.run(download_file_streamed(file_url, destination_path))
            print(f"File downloaded successfully: {destination_path}")
        else:
            print(f"File already downloaded: {destination_path}")

        print(json.dumps(get_info(destination_path), indent=2))


def parse_chapter(chapter: ChapterFrame) -> dict[str, str | None]:
    time_start, time_end = chapter.times
    return {
        "title": chapter.title,
        "subtitle": chapter.subtitle,
        "url": chapter.user_url,
        "time_start": time_start,
        "time_end": time_end,
    }


def get_info(file: str | Path) -> dict[str, str | Any]:
    audiofile: eyed3.AudioFile | None = eyed3.load(file)

    if not audiofile:
        return {"_file": str(file)}

    tag = audiofile.tag
    info = audiofile.info

    return {
        "_file": str(file),
        "duration_ms": int(info.time_secs * 1000),
        "size_bytes": info.size_bytes,
        "title": tag.title,
        "album": tag.album,
        "artist": tag.artist,
        "album_artist": tag.album_artist,
        "chapters": [parse_chapter(chap) for chap in tag.chapters],  # pyright: ignore[reportAttributeAccessIssue]
    }


# def get_file_size(output_path: str | Path) -> int:
#     return os.path.getsize(filename=output_path)


async def download_file_streamed(url: str, output_path: str | Path) -> None:
    async with httpx.AsyncClient(follow_redirects=True) as client:
        async with client.stream("GET", url) as response:
            response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
            with open(output_path, "wb") as f:
                async for chunk in response.aiter_bytes():
                    f.write(chunk)


if __name__ == "__main__":
    main()
