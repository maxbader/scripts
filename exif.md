- Dateinamen in kleinbuchstaben
  ```
  find -name '*.JPG' -exec rename 's/(.*)\/([^\/]*)/$1\/\L$2/' {} \;
  ```
- Set exif date from filename such as signal-2021-03-27-07-18-45-006.jp
  ```
  exiftool "-alldates<filename" ./
  ```
- Set filename based on Exif info
  ```
  exiftool 2*.jpg '-FileName<CreateDate'       -ext jpg -d "%Y-%m-%d--%H-%M-%S-%%-.c-markus.%%e"
  exiftool 2*.mp4 "-FileName<CreateDate"       -ext mp4 -d "%Y-%m-%d--%H-%M-%S-%%-.c-markus.%%e"
  ```
- Python programm to change/check year only
  ```
  find . -iname "*.JPG" -type f -exec ./exif-check-year-only.py {} 2010 2>cp.err \;
  find . -iname "*.JPG" -type f -exec ./exif-set-year-only.py {} 1980 2>cp.err \;
  ```
  
