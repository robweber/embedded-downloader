# Embedded Video Downloader
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)

A simple video downloader application to pull in videos from a url, or list of urls

## Install
```

git clone
cd embedded-downloader
pip3 install .

```

__Note__ You may need to add the `$HOME/.local/bin` directory to your PATH variable to use the console utility. You can get around this by installing the script with `sudo`, then it will be available in `/usr/local/bin` instead.

## Usage

Once installed you can use the command line utility or call the downloader Python script directly.

__CLI Utility__
```
usage: embedded-video-downloader [-h] [-d DIR] (-u URL | -f FILE)

Embedded Video Downloader

optional arguments:
  -h, --help            show this help message and exit
  -d DIR, --dir DIR     download directory, default is downloads/
  -u URL, --url URL     video url to download, cannot be used with -f
  -f FILE, --file FILE  file containining URLs, cannot be used with -u
```

__Calling Directly__
```
python3 src/embedded_downloader/downloader.py -u https://video/urls
python3 src/embedded_downloader/downloader.py -f path/to/file.txt
```

If using the `-f` option you should use a text file with one URL per line.

## License
[MIT](/LICENSE)
