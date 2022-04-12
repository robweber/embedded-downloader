#!/usr/bin/env python
"""
Embedded Video Downloader

Download a specific video url (Youtube, etc) or a list of urls from a file

Usage: python3 downloader.py -f https://path/to/video
"""
import argparse
import os.path
import youtube_dl


def download_file(url, dir):
    """download the file to the given directory"""
    path = os.path.join(dir, '%(title)s.%(ext)s')

    ydl_opts = {
        'format': 'best',
        'outtmpl': path,
        'nooverwrites': True,
        'no_warnings': False,
        'ignoreerrors': True,
    }

    print(f"Downloading {url} to {path}")
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return True


def check_exists(p, is_dir=False):
    """check that this path exists and either is or isn't a directory"""
    if(os.path.exists(p) and os.path.isdir(p) == is_dir):
        return p
    else:
        raise argparse.ArgumentTypeError(f"Path '{p}' does not exist")


def check_file_exists(f):
    return check_exists(f)


def check_dir_exists(d):
    return check_exists(d, True)


def main():

    parser = argparse.ArgumentParser(description='Embedded Video Downloader')
    parser.add_argument('-d', '--dir', default='downloads', type=check_dir_exists, help='download directory, default is downloads/')
    # can only use one or the other of these
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-u', '--url', help='video url to download, cannot be used with -f')
    group.add_argument('-f', '--file', type=check_file_exists, help='file containining URLs, cannot be used with -u')
    args = parser.parse_args()

    print("Embedded Video Downloader")
    print(f"Downloads Directory: {args.dir}")

    if(args.url):
        # download this url
        download_file(args.url, args.dir)
    else:
        # read in the file of urls
        urls = []
        with open(args.file) as f:
            urls = f.readlines()
        print(f"Found {len(urls)} urls")

        # download each url in the file
        for u in urls:
            download_file(u, args.dir)


if __name__ == '__main__':
    main()
