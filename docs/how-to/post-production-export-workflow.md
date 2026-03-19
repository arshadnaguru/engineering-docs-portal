# Post-Production Export Workflow

> **Author:** Arshad Naguru · **Last Updated:** March 2026 · **Category:** How-To

Standard workflow for exporting final assets from post-production for delivery.

## Pre-Export Checklist

- [ ] Timeline is locked (no further editorial changes)
- [ ] All VFX shots are final
- [ ] Color grading is approved
- [ ] Audio mix is complete
- [ ] Subtitles/captions are reviewed

## Export Specifications

### Web Delivery (YouTube, Vimeo)

| Setting | Value |
|---------|-------|
| Codec | H.264 |
| Container | .mp4 |
| Resolution | 1920×1080 or 3840×2160 |
| Frame Rate | 24/30 fps (match source) |
| Bitrate | 10-20 Mbps (1080p) / 35-60 Mbps (4K) |
| Audio | AAC, 320 kbps, 48 kHz |

### Archival Master

| Setting | Value |
|---------|-------|
| Codec | ProRes 422 HQ or DNxHR |
| Container | .mov |
| Resolution | Match project resolution |
| Frame Rate | Match project frame rate |
| Audio | PCM uncompressed, 48 kHz, 24-bit |

### DCP (Digital Cinema Package)

| Setting | Value |
|---------|-------|
| Codec | JPEG2000 |
| Resolution | 2048×1080 (2K) or 4096×2160 (4K) |
| Frame Rate | 24 fps |
| Audio | PCM, 48 kHz, 24-bit |

## Export Using FFmpeg

```bash
# Web delivery (H.264)
ffmpeg -i master.mov -c:v libx264 -preset slow -crf 18 \
  -c:a aac -b:a 320k -movflags +faststart output_web.mp4

# ProRes archival
ffmpeg -i master.mov -c:v prores_ks -profile:v 3 \
  -c:a pcm_s24le output_archive.mov

# Extract audio only
ffmpeg -i master.mov -vn -c:a pcm_s24le audio_master.wav
```

## File Naming Convention

```
ProjectName_Version_Resolution_Codec_Date.ext
```

Example: `ShortFilm_v3_4K_ProRes422HQ_20260319.mov`

## Verify the Export

```bash
# Check file properties
ffprobe -v quiet -print_format json -show_format -show_streams output.mp4
```

Verify: resolution, frame rate, codec, duration, and audio tracks all match specifications.

---

*Last updated: March 2026 · Author: Arshad Naguru*
