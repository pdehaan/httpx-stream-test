# httpx-stream-test

Download remote MP3s using [httpx](https://www.python-httpx.org/) streaming client.

## OUTPUT

```txt
uv run main.py

File already downloaded: data/who-designed-design.mp3
{
  "_file": "data/who-designed-design.mp3",
  "duration_ms": 404090,
  "size_bytes": 16212718,
  "title": "Who Designed Design?",
  "album": "The Next Big Idea Daily",
  "artist": null,
  "album_artist": null,
  "chapters": []
}

File already downloaded: data/what-cultures-around-the-world-can-teach-you-about-parenting.mp3
{
  "_file": "data/what-cultures-around-the-world-can-teach-you-about-parenting.mp3",
  "duration_ms": 411100,
  "size_bytes": 16497677,
  "title": "What Cultures Around the World Can Teach You About Parenting",
  "album": "The Next Big Idea Daily",
  "artist": null,
  "album_artist": null,
  "chapters": []
}

File already downloaded: data/bears.mp3
{
  "_file": "data/bears.mp3",
  "duration_ms": 404090,
  "size_bytes": 16218914,
  "title": "Bears!",
  "album": "The Next Big Idea Daily",
  "artist": null,
  "album_artist": null,
  "chapters": []
}

File already downloaded: data/dangers-of-automatically-converting-a-rest-api-to-mcp.mp3
{
  "_file": "data/dangers-of-automatically-converting-a-rest-api-to-mcp.mp3",
  "duration_ms": 5076810,
  "size_bytes": 82046885,
  "title": "266: Dangers of Automatically Converting a REST API to MCP",
  "album": "The Real Python Podcast",
  "artist": "The Real Python Podcast",
  "album_artist": null,
  "chapters": [
    {
      "title": "Introduction",
      "subtitle": null,
      "url": "https://realpython.com/podcasts/rpp/266/",
      "time_start": 0,
      "time_end": 161500
    },
    {
      "title": "Updates on career",
      "subtitle": null,
      "url": "https://www.oreilly.com/library/view/ai-agents-with/9798341639546/",
      "time_start": 161500,
      "time_end": 276000
    },
    ...
  ]
}
```
