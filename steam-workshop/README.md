# Steam Workshop publishing kit

Everything needed for the Steam Workshop and Paradox Mods listings. Nothing here ships with the mod
itself — the mod is `descriptor.mod` plus `gui/` in the repository root.

| File | Where it goes |
| --- | --- |
| `description-en.txt` | Workshop item description (BBCode) |
| `description-ru.txt` | Russian version of the same description |
| `description-paradoxmods-en.txt` | same text without BBCode, for the Paradox Mods site |
| `description-paradoxmods-ru.txt` | Russian version without BBCode |
| `short-description-en.txt` | Launcher / Paradox Mods short description, 191 chars |
| `short-description-ru.txt` | Russian short description, 186 chars |

## Listing metadata

* **Title:** Ultrawide Pause Menu Fix
* **Tags:** Fixes, Graphics, Utilities — same as `descriptor.mod`
* **Version:** 1.0.0, `supported_version="1.19.*"`
* **Visibility:** public

Short descriptions are kept under the launcher's 200 character limit; both
BBCode descriptions are well under Steam's 8000 character limit.

## Preview image on Steam

The Workshop preview is **not** set from the uploader form — the launcher picks up
`thumbnail.png` from the mod root (next to `descriptor.mod`), which is also what
`picture="thumbnail.png"` in the descriptor points at. Without that file the item
shows Steam's default placeholder, and images added to the item's gallery on the
website do not replace it.

`thumbnail.png` in the repo root is 1280x720, 646 KB, under Steam's 1 MB limit.
After changing it, re-run `install.sh` and upload the mod again from the launcher —
it updates the existing Workshop item rather than creating a new one.

The uploader form's own image field applies to Paradox Mods, not to Steam.

## Image metadata

`thumbnail.png` in the repo root is cropped from a phone photo, re-encoded from
raw pixels and stripped of everything else: no EXIF, no GPS, no ICC profile, no
XMP. The uncropped original is deliberately not kept in this repository. Verify
any replacement image before committing it, since photos straight from a phone
normally carry GPS coordinates and a device serial:

    python3 -c "from PIL import Image; im=Image.open('thumbnail.png'); print(len(im.getexif()), im.info)"
