import asyncio
from pathlib import Path
import os

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
]


def main():
    # Only process the first 2 list items...
    download_episodes(files[:2])


def download_episodes(files: list[tuple[str, str]]):
    for file_url, title in files:
        filename = f"{slugify(title)}.mp3"
        destination_path = MP3_DIR / filename

        if not os.path.isfile(destination_path):
            asyncio.run(download_file_streamed(file_url, destination_path))
            print(f"File downloaded successfully to: {destination_path}")
        else:
            print(f"File already downloaded: {destination_path}")
        print(f"bytes = {get_file_size(destination_path)}")
        # TODO: Get id3 information to extract chapters and other metadata?
        # See https://github.com/pdehaan/eyeD3-test


def get_file_size(output_path: str | Path) -> int:
    return os.path.getsize(filename=output_path)


async def download_file_streamed(url: str, output_path: str | Path) -> None:
    async with httpx.AsyncClient(follow_redirects=True) as client:
        async with client.stream("GET", url) as response:
            response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
            with open(output_path, "wb") as f:
                async for chunk in response.aiter_bytes():
                    f.write(chunk)


if __name__ == "__main__":
    main()
