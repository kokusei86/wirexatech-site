# WIREXA TECH Branded Video Builder

This tool builds branded copies of selected machine demo videos for YouTube or website use.

It does not modify, move, overwrite, or rename the original source videos.

## Source Videos

The tool only reads these five videos:

```text
F:\新款视频1\新款视频1\808单线.mp4
F:\新款视频1\新款视频1\806CN.mp4
F:\新款视频1\新款视频1\880A.mp4
F:\新款视频1\新款视频1\880C2.mp4
F:\新款视频1\新款视频1\880D.mp4
```

## Output Folder

Generated files are written to:

```text
WireHarness_Global_V1\video-ready\
```

Expected outputs:

```text
808-single-wire-wirexa-v1.mp4
808-single-wire-wirexa-v1-preview.jpg
806cn-wirexa-v1.mp4
806cn-wirexa-v1-preview.jpg
880a-wirexa-v1.mp4
880a-wirexa-v1-preview.jpg
880c2-wirexa-v1.mp4
880c2-wirexa-v1-preview.jpg
880d-wirexa-v1.mp4
880d-wirexa-v1-preview.jpg
video_build_report.md
```

## Branding

Top-left watermark:

```text
WIREXA TECH
Wire Processing Solutions
```

End CTA screen:

```text
Need Wire Processing Solutions?
WhatsApp: +86 180 6628 2233
Website: wirexatech.com
WIREXA TECH
Wire Processing Solutions
```

## Requirements

Python 3 and FFmpeg are required.

Both commands must be available from PowerShell:

```powershell
ffmpeg -version
ffprobe -version
```

This project is also configured to automatically use this local FFmpeg folder if it exists:

```text
F:\GithubProjects\ffmpeg-8.1.1-essentials_build\bin
```

If FFmpeg is missing, the script stops with a clear error message and no videos are processed.

## Usage

Check environment only:

```powershell
python .\video-builder\build_branded_videos.py --check
```

Preview planned jobs only:

```powershell
python .\video-builder\build_branded_videos.py --dry-run
```

Build all branded videos:

```powershell
python .\video-builder\build_branded_videos.py
```

Rebuild and overwrite previously generated outputs:

```powershell
python .\video-builder\build_branded_videos.py --overwrite
```

## Notes

- Original aspect ratio and resolution are preserved.
- Vertical videos remain vertical.
- The script exports one preview screenshot per finished video.
- The finished report is written to `video-ready\video_build_report.md`.
