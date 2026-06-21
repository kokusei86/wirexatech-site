# WIREXA TECH V1.0_GITHUB_READY

This checklist defines what should be committed to GitHub for the static website repository.

## Recommended To Commit

- Root HTML pages: `*.html`
- Static assets: `assets/style.css`, `favicon.svg`
- Product and site images: `images/*`, `assets/*` image files
- SEO files: `robots.txt`, `sitemap.xml`
- Project documents: `*.md`
- Video tooling source: `video-builder/build_branded_videos.py`, `video-builder/README.md`
- Video review assets only:
  - `video-ready/*-wirexa-v1-preview.jpg`
  - `video-ready/video_build_report.md`
  - `video-ready/.gitkeep`
- Repository rules: `.gitignore`

## Recommended To Exclude

- All `.mp4` files
- Old branded video outputs
- Old branded video preview screenshots
- Python cache: `__pycache__/`, `*.pyc`
- Temporary files: `*.tmp`, `*.temp`, `*.part`, `*.log`
- Local backup files: `*.bak`, `*.backup`, `*.old`
- Backup archives: `*.zip`, `*.rar`, `*.7z`, `*.tar`, `*.tar.gz`, `*.tgz`
- OS/editor noise: `.DS_Store`, `Thumbs.db`, `desktop.ini`

## Video Policy

Do not commit video binaries to GitHub. Upload the final `*-wirexa-v1.mp4` files to YouTube or external video storage, then embed the YouTube URLs in the website later.

The current GitHub repository should keep only lightweight preview images and the video build report.

## Current Status

- Website version: `V1.0_DEPLOY_READY`
- Video version: `WIREXA TECH V1.0_VIDEO_READY_CHECK`
- GitHub package target: `WIREXA TECH V1.0_GITHUB_READY`
- GitHub upload: not performed
- Cloudflare deployment: not performed
