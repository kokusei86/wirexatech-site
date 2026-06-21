#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build branded machine demo videos with FFmpeg.

This tool only reads the five approved source videos and writes branded copies
to ../video-ready. Original videos are never modified, moved, or overwritten.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = Path(r"F:\新款视频1\新款视频1")
OUTPUT_DIR = PROJECT_ROOT / "video-ready"
LOCAL_FFMPEG_BIN = Path(r"F:\GithubProjects\ffmpeg-8.1.1-essentials_build\bin")

BRAND_LINE_1 = "WIREXA TECH"
BRAND_LINE_2 = "Wire Processing Solutions"
CTA_LINE_1 = "Need Wire Processing Solutions?"
CTA_LINE_2 = "WhatsApp: +86 180 6628 2233"
CTA_LINE_3 = "Website: wirexatech.com"


@dataclass(frozen=True)
class VideoJob:
    source_name: str
    output_stem: str
    model: str
    feature: str


VIDEO_JOBS: tuple[VideoJob, ...] = (
    VideoJob(
        source_name="808单线.mp4",
        output_stem="808-single-wire-wirexa-v1",
        model="FY-808 Automatic Wire Stripping Machine",
        feature="Single Wire Cutting & Stripping Demo",
    ),
    VideoJob(
        source_name="806CN.mp4",
        output_stem="806cn-wirexa-v1",
        model="806CN Wire Stripping & Twisting Machine",
        feature="Automatic Wire Processing Demo",
    ),
    VideoJob(
        source_name="880A.mp4",
        output_stem="880a-wirexa-v1",
        model="FY-880A Heavy Wire Stripping Machine",
        feature="Large Wire Cutting & Stripping Demo",
    ),
    VideoJob(
        source_name="880C2.mp4",
        output_stem="880c2-wirexa-v1",
        model="FY-880C Multi-Core Cable Stripping Machine",
        feature="Outer Jacket & Core Stripping Demo",
    ),
    VideoJob(
        source_name="880D.mp4",
        output_stem="880d-wirexa-v1",
        model="FY-880D Heavy Wire Stripping Machine",
        feature="Heavy-Duty Wire Processing Demo",
    ),
)


def fail(message: str, code: int = 1) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(code)


def find_binary(name: str) -> str | None:
    from_path = shutil.which(name)
    if from_path:
        return from_path

    local_binary = LOCAL_FFMPEG_BIN / f"{name}.exe"
    if local_binary.exists():
        return str(local_binary)

    return None


def run_command(command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def require_ffmpeg() -> tuple[str, str]:
    ffmpeg = find_binary("ffmpeg")
    ffprobe = find_binary("ffprobe")
    if not ffmpeg or not ffprobe:
        lines = [
            "FFmpeg was not found in PATH.",
            "Install FFmpeg and make sure both ffmpeg and ffprobe are available from PowerShell.",
            "No videos were processed.",
        ]
        fail("\n".join(lines), code=2)
    return ffmpeg, ffprobe


def font_path(candidates: Iterable[str]) -> Path:
    for item in candidates:
        path = Path(item)
        if path.exists():
            return path
    fail("No suitable Windows font found for FFmpeg drawtext.", code=2)


def ffmpeg_path(path: Path) -> str:
    return path.as_posix().replace(":", r"\:")


def escape_filter_text(text: str) -> str:
    return (
        text.replace("\\", r"\\")
        .replace(":", r"\:")
        .replace("'", r"\'")
        .replace("%", r"\%")
    )


def probe_video(ffprobe: str, source: Path) -> dict:
    command = [
        ffprobe,
        "-v",
        "error",
        "-print_format",
        "json",
        "-show_streams",
        "-show_format",
        str(source),
    ]
    result = run_command(command)
    if result.returncode != 0:
        fail(f"ffprobe failed for {source.name}:\n{result.stderr.strip()}")

    data = json.loads(result.stdout)
    video_stream = next(
        (stream for stream in data.get("streams", []) if stream.get("codec_type") == "video"),
        None,
    )
    if not video_stream:
        fail(f"No video stream found in {source.name}")

    duration = float(
        video_stream.get("duration")
        or data.get("format", {}).get("duration")
        or 0
    )
    return {
        "width": int(video_stream["width"]),
        "height": int(video_stream["height"]),
        "duration": duration,
        "frame_rate": video_stream.get("avg_frame_rate")
        or video_stream.get("r_frame_rate")
        or "30/1",
    }


def seconds_to_stamp(seconds: float) -> str:
    total = max(0, int(round(seconds)))
    minutes, sec = divmod(total, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{hours:02d}:{minutes:02d}:{sec:02d}"


def make_filter(job: VideoJob, width: int, height: int, bold_font: Path, regular_font: Path) -> str:
    brand_size = max(20, min(30, width // 28, height // 38))
    brand_sub_size = max(12, int(brand_size * 0.58))
    watermark_x = max(18, width // 34)
    watermark_y = max(18, height // 48)

    title_h = max(86, min(130, int(height * 0.095)))
    title_bottom_margin = max(34, int(height * 0.04))
    title_y = height - title_h - title_bottom_margin
    title_x = max(24, width // 28)
    title_model_size = max(22, min(38, width // 22, height // 35))
    title_feature_size = max(14, int(title_model_size * 0.58))

    cta_main_size = max(28, min(56, int(width * 0.060), int(height * 0.040)))
    cta_mid_size = max(22, int(cta_main_size * 0.72))
    cta_brand_size = max(24, int(cta_main_size * 0.76))
    cta_sub_size = max(16, int(cta_main_size * 0.48))
    center_y = height // 2

    bold = ffmpeg_path(bold_font)
    regular = ffmpeg_path(regular_font)

    vf_parts = [
        "[0:v]format=rgba",
        (
            f"drawtext=fontfile='{bold}':text='{escape_filter_text(BRAND_LINE_1)}':"
            f"x={watermark_x}:y={watermark_y}:fontsize={brand_size}:"
            "fontcolor=white@0.68:shadowcolor=black@0.32:shadowx=1:shadowy=1"
        ),
        (
            f"drawtext=fontfile='{regular}':text='{escape_filter_text(BRAND_LINE_2)}':"
            f"x={watermark_x}:y={watermark_y + brand_size + 6}:fontsize={brand_sub_size}:"
            "fontcolor=white@0.58:shadowcolor=black@0.28:shadowx=1:shadowy=1"
        ),
        (
            f"drawbox=x=0:y={title_y}:w=iw:h={title_h}:"
            "color=black@0.52:t=fill:enable='lte(t,3)'"
        ),
        (
            f"drawbox=x=0:y={title_y}:w=10:h={title_h}:"
            "color=0xff6600@0.95:t=fill:enable='lte(t,3)'"
        ),
        (
            f"drawtext=fontfile='{bold}':text='{escape_filter_text(job.model)}':"
            f"x={title_x}:y={title_y + 16}:fontsize={title_model_size}:"
            "fontcolor=white@0.95:enable='lte(t,3)'"
        ),
        (
            f"drawtext=fontfile='{regular}':text='{escape_filter_text(job.feature)}':"
            f"x={title_x}:y={title_y + 22 + title_model_size}:fontsize={title_feature_size}:"
            "fontcolor=0xffcc99@0.95:enable='lte(t,3)'"
        ),
        "format=yuv420p[branded]",
    ]

    cta_parts = [
        "[1:v]format=rgba",
        "drawbox=x=0:y=0:w=iw:h=ih:color=0x1a1a1a@1:t=fill",
        "drawbox=x=0:y=0:w=iw:h=12:color=0xff6600@1:t=fill",
        (
            f"drawtext=fontfile='{bold}':text='{escape_filter_text(CTA_LINE_1)}':"
            f"x=(w-text_w)/2:y={center_y - int(cta_main_size * 2.05)}:"
            f"fontsize={cta_main_size}:fontcolor=white@0.98"
        ),
        (
            f"drawtext=fontfile='{regular}':text='{escape_filter_text(CTA_LINE_2)}':"
            f"x=(w-text_w)/2:y={center_y - int(cta_mid_size * 0.55)}:"
            f"fontsize={cta_mid_size}:fontcolor=0xffcc99@0.98"
        ),
        (
            f"drawtext=fontfile='{regular}':text='{escape_filter_text(CTA_LINE_3)}':"
            f"x=(w-text_w)/2:y={center_y + int(cta_mid_size * 0.55)}:"
            f"fontsize={cta_mid_size}:fontcolor=white@0.86"
        ),
        (
            f"drawtext=fontfile='{bold}':text='{escape_filter_text(BRAND_LINE_1)}':"
            f"x=(w-text_w)/2:y={center_y + int(cta_brand_size * 1.65)}:"
            f"fontsize={cta_brand_size}:fontcolor=0xff6600@0.98"
        ),
        (
            f"drawtext=fontfile='{regular}':text='{escape_filter_text(BRAND_LINE_2)}':"
            f"x=(w-text_w)/2:y={center_y + int(cta_brand_size * 2.85)}:"
            f"fontsize={cta_sub_size}:fontcolor=white@0.78"
        ),
        "format=yuv420p[cta]",
    ]

    return ";".join([",".join(vf_parts), ",".join(cta_parts), "[branded][cta]concat=n=2:v=1:a=0[outv]"])


def build_video(
    ffmpeg: str,
    ffprobe: str,
    job: VideoJob,
    bold_font: Path,
    regular_font: Path,
    overwrite: bool,
) -> dict:
    source = SOURCE_DIR / job.source_name
    output = OUTPUT_DIR / f"{job.output_stem}.mp4"
    preview = OUTPUT_DIR / f"{job.output_stem}-preview.jpg"
    if not source.exists():
        fail(f"Required source video missing: {source}")
    if output.exists() and not overwrite:
        fail(f"Output already exists: {output}\nUse --overwrite to rebuild it.")

    meta = probe_video(ffprobe, source)
    width = int(meta["width"])
    height = int(meta["height"])
    frame_rate = str(meta["frame_rate"])
    filter_complex = make_filter(job, width, height, bold_font, regular_font)

    command = [
        ffmpeg,
        "-y" if overwrite else "-n",
        "-i",
        str(source),
        "-f",
        "lavfi",
        "-i",
        f"color=c=#1a1a1a:s={width}x{height}:r={frame_rate}:d=3",
        "-filter_complex",
        filter_complex,
        "-map",
        "[outv]",
        "-c:v",
        "libx264",
        "-preset",
        "medium",
        "-crf",
        "20",
        "-pix_fmt",
        "yuv420p",
        "-movflags",
        "+faststart",
        "-an",
        str(output),
    ]

    print(f"Building {output.name} ...")
    result = run_command(command)
    if result.returncode != 0:
        fail(f"ffmpeg failed for {job.source_name}:\n{result.stderr.strip()}")

    preview_time = min(2.0, max(0.1, meta["duration"] * 0.25))
    preview_command = [
        ffmpeg,
        "-y",
        "-ss",
        str(preview_time),
        "-i",
        str(output),
        "-frames:v",
        "1",
        "-q:v",
        "2",
        str(preview),
    ]
    preview_result = run_command(preview_command)
    if preview_result.returncode != 0:
        fail(f"Preview export failed for {output.name}:\n{preview_result.stderr.strip()}")

    output_meta = probe_video(ffprobe, output)
    return {
        "source": str(source),
        "output": str(output),
        "preview": str(preview),
        "source_duration": seconds_to_stamp(meta["duration"]),
        "output_duration": seconds_to_stamp(output_meta["duration"]),
        "resolution": f"{width}x{height}",
    }


def write_report(records: list[dict]) -> Path:
    report = OUTPUT_DIR / "video_build_report.md"
    lines = [
        "# Video Build Report",
        "",
        f"Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "Brand watermark:",
        f"- {BRAND_LINE_1}",
        f"- {BRAND_LINE_2}",
        "",
        "CTA screen:",
        f"- {CTA_LINE_1}",
        f"- {CTA_LINE_2}",
        f"- {CTA_LINE_3}",
        f"- {BRAND_LINE_1}",
        f"- {BRAND_LINE_2}",
        "",
        "| Original File | Output File | Duration | Resolution | Screenshot |",
        "|---|---|---:|---|---|",
    ]
    for record in records:
        lines.append(
            "| {source} | {output} | {duration} | {resolution} | {preview} |".format(
                source=Path(record["source"]).name,
                output=Path(record["output"]).name,
                duration=record["output_duration"],
                resolution=record["resolution"],
                preview=Path(record["preview"]).name,
            )
        )
    lines.append("")
    lines.append("Original source videos were not modified, moved, or overwritten.")
    report.write_text("\n".join(lines), encoding="utf-8-sig")
    return report


def check_environment(ffmpeg: str | None, ffprobe: str | None) -> int:
    print("Video builder environment check")
    print(f"Project root: {PROJECT_ROOT}")
    print(f"Source dir: {SOURCE_DIR}")
    print(f"Output dir: {OUTPUT_DIR}")
    print(f"Local FFmpeg bin: {LOCAL_FFMPEG_BIN}")
    print(f"ffmpeg: {ffmpeg or 'NOT FOUND'}")
    print(f"ffprobe: {ffprobe or 'NOT FOUND'}")
    missing_sources = [job.source_name for job in VIDEO_JOBS if not (SOURCE_DIR / job.source_name).exists()]
    if missing_sources:
        print("Missing source videos:")
        for name in missing_sources:
            print(f"- {name}")
    else:
        print("All required source videos found.")
    if not ffmpeg or not ffprobe:
        print("\nERROR: FFmpeg is not available. Install FFmpeg before building videos.")
        return 2
    if missing_sources:
        return 1
    return 0


def dry_run() -> None:
    print("Dry run: approved video jobs")
    for job in VIDEO_JOBS:
        print(f"- {job.source_name} -> {job.output_stem}.mp4")
        print(f"  Title: {job.model}")
        print(f"  Feature: {job.feature}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Build branded WireHarness demo videos.")
    parser.add_argument("--check", action="store_true", help="Check environment only; do not build.")
    parser.add_argument("--dry-run", action="store_true", help="List planned jobs only; do not build.")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing generated outputs.")
    args = parser.parse_args()

    ffmpeg = find_binary("ffmpeg")
    ffprobe = find_binary("ffprobe")

    if args.check:
        return check_environment(ffmpeg, ffprobe)
    if args.dry_run:
        dry_run()
        return 0

    ffmpeg, ffprobe = require_ffmpeg()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    bold_font = font_path(
        [
            r"C:\Windows\Fonts\arialbd.ttf",
            r"C:\Windows\Fonts\segoeuib.ttf",
            r"C:\Windows\Fonts\msyhbd.ttc",
        ]
    )
    regular_font = font_path(
        [
            r"C:\Windows\Fonts\arial.ttf",
            r"C:\Windows\Fonts\segoeui.ttf",
            r"C:\Windows\Fonts\msyh.ttc",
        ]
    )

    records = [
        build_video(ffmpeg, ffprobe, job, bold_font, regular_font, args.overwrite)
        for job in VIDEO_JOBS
    ]
    report = write_report(records)
    print(f"Done. Report: {report}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
