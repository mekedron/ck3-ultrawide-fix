# Steam Workshop publishing kit

Everything needed for the Workshop listing. Nothing here ships with the mod
itself — the mod is `descriptor.mod` plus `gui/` in the repository root.

| File | Where it goes |
| --- | --- |
| `description-en.txt` | Workshop item description (BBCode) |
| `description-ru.txt` | Russian version of the same description |
| `short-description-en.txt` | Launcher / Paradox Mods short description, 191 chars |
| `short-description-ru.txt` | Russian short description, 186 chars |
| `preview.jpg` | Workshop preview image |

## Listing metadata

* **Title:** Ultrawide Pause Menu Fix
* **Tags:** Fixes, Graphics, Utilities — same as `descriptor.mod`
* **Version:** 1.0.0, `supported_version="1.19.*"`
* **Visibility:** public

Short descriptions are kept under the launcher's 200 character limit; both
BBCode descriptions are well under Steam's 8000 character limit.

## preview.jpg

1280x1280, 281 KB, under the Workshop's 1 MB preview limit. Stripped of all
metadata: no EXIF, no GPS, no ICC profile, no XMP — only the mandatory JFIF
header and the image data remain. Verify with:

    python3 -c "from PIL import Image; im=Image.open('preview.jpg'); print(len(im.getexif()), im.info)"

Re-run that check on any replacement image before committing it, since photos
straight from a phone normally carry GPS coordinates and a device serial.
