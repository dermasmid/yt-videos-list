# Automate creation of videos lists for YouTube channels
**TABLE OF CONTENTS**
<br>[Quick Start](./README.md#Quick-Start)
<br>[Running the package from the python interpreter](./README.md#Running-the-package-from-the-python-interpreter)
<br>[Understanding the API](./README.md#Understanding-the-API)
<br>[For more control](./README.md#For-more-control)
<br>[General Overview](./README.md#General-Overview)
<br>[Future Features](./README.md#Future-Features)
<br>[Technical Specifications](./README.md#Technical-Specifications)

## Quick Start
This package uses [f-strings](https://cito.github.io/blog/f-strings/) (more [here](https://realpython.com/python-f-strings/)) and as such requires Python 3.6+. If you have an older version of Python, you can download the Python 3.8.2 [macOS 64-bit installer](https://www.python.org/ftp/python/3.8.2/python-3.8.2-macosx10.9.pkg), [Windows x86-64 executable installer](https://www.python.org/ftp/python/3.8.2/python-3.8.2-amd64.exe), [Windows x86 executable installer](https://www.python.org/ftp/python/3.8.2/python-3.8.2.exe), or the [Gzipped source tarball](https://www.python.org/ftp/python/3.8.2/Python-3.8.2.tgz) (most useful for Linux) and follow the instructions to set up Python for your machine.

It's recommend to install the latest version if you don't have existing projects that are dependent on a specific older version of Python, but if you want to install a different version, visit the [Python Downloads page](https://www.python.org/downloads/) and select the version you want. Once you do that, enter the following in your command line:
```
# if something isn't working properly, try rerunning this
# the problem may have been fixed with a newer version

pip3 install -U yt-videos-list
```

**NOTE**: You do need to have the Selenium driver installed to run this package, but you do ***not*** need to download all Selenium drivers for your OS if you only want to run this program on a specific driver. If you want a specific driver, just copy and paste the corresponding command for the relevant driver from below. Otherwise, download the selenium dependencies for all the drivers that are supported on your OS to play around with them and see how they differ :)
### Copy paste the code block that's relevant for the OS of your machine for the Selenium driver(s) you want from **[here](https://github.com/Shail-Shouryya/yt_videos_list/blob/master/extra/README.md)**
**NOTE** that you also need the corresponding browser installed to properly run the selenium driver.
- To download the most recent version of the browser, go to the page for:
  - [Firefox](https://www.mozilla.org/en-US/firefox/new/)
  - [Opera](https://www.opera.com/)
  - [Chrome](https://www.google.com/chrome/)

## Running the package from the python interpreter
```
python3
```
```python
from yt_videos_list import ListGenerator
LG = ListGenerator()

# "user" channelType (example uses Corey Schafer):
LG.generate_list(channel='schafer5', channelType='user')

# "channel" channelType (example uses freeCodeCamp) along with the optional fileName argument:
LG.generate_list(channel='UC8butISFwT-Wl7EV0hUK0BQ', channelType='channel', fileName='freeCodeCamp_orgVideosList')

# see the new files that were just created:
import os
# MacOS and Linux users:
os.system('ls -lt | head')
# Windows users:
os.system('dir /O-D | find "VideosList"')

# for more information on using the module:
help(LG)
```

### Understanding the API
There are two types of YouTube channels: one type is a `user` channel and the other is a `channel` channel.
* The url for a `user` channel consists of `youtube.com` followed by `user` followed by the name. For example:
  * Disney: https://www.youtube.com/user/disneysshows
  * sentdex: https://www.youtube.com/user/sentdex
  * Marvel: https://www.youtube.com/user/MARVEL
  * Apple: https://www.youtube.com/user/Apple
* The url for a `channel` channel consists of `youtube.com` followed by `channel` followed by a string of rather unpredictable characters. For example:
  * Tasty: https://www.youtube.com/channel/UCJFp8uSYCjXOMnkUyb3CQ3Q
  * Billie Eilish: https://www.youtube.com/channel/UCiGm_E4ZwYSHV3bcW1pnSeQ
  * Gordon Ramsay: https://www.youtube.com/channel/UCIEv3lZ_tNXHzL3ox-_uUGQ
  * PBS Space Time: https://www.youtube.com/channel/UC7_gcs09iThXybpVgjHZ_7g

To scrape the video titles along with the link to the video, you need to run the `generate_list(channel, channelType)` method on the ListGenerator object you just created, substituting the name of the channel for the `channel` argument and the type of channel for `channelType` argument. By default, the name of the file produced will be `channel`VideosList.ext where the `.ext` will be `.csv` or `.txt ` depending on the type of file(s) that you specified.

### For more control
---
**NOTE** that you can also access all the information below in the `python3` interpreter by entering
<br>`from yt_videos_list import ListGenerator`
<br>`help(ListGenerator)`

---
```python
ListGenerator(csv=True, csvWriteFormat='x', txt=True, txtWriteFormat='x',
              chronological=False,
              headless=False, scrollPauseTime=0.8, driver='Firefox')
```
There are a number of optional arguments you can specify during the instantiation of the ListGenerator object. The preceding arguments are run by default, but in case you want more flexibility, you can specify:

* Options for the `driver` argument are
  - `Firefox` (default)
  - `Chrome`
  - `Opera`
  - `Safari`
    - -> driver='firefox'
    - -> driver='chrome'
    - -> driver='opera'
    - -> driver='safari'
* Options for the file type arguments (`csv`, `txt`) are
  - `True` (default) - create a file for the specified type
  - `False` - do not create a file for the specified type.
    * `txt=True`  (default) OR `txt=False`
    * `csv=True`  (default) OR `csv=False`
* Options for the write format arguments (`csvWriteFormat`, `txtWriteFormat`) are
  - `'x'` (default) - does not overwrite an existing file with the same name
  - `'w'` - if an existing file with the same name exists, it will be overwritten
  * NOTE: if you specify the file type argument to be False, you don't need to touch this - the program will automatically skip this step.
    * `txtWriteFormat='x'`  (default) OR `txtWriteFormat='w'`
    * `csvWriteFormat='x'`  (default) OR `csvWriteFormat='w'`
* Options for the `chronological` argument are
  - `False` (default) - write the files in order from most recent video to the oldest video
  - `True` - write the files in order from oldest video to the most recent video
    * `chronological=False` (default) OR `chronological=True`
* Options for the `headless` argument are
  - `False` (default) - run the driver with an open Selenium instance for viewing
  - `True` - run the driver in "invisible" mode.
    * `headless=False` (default) OR `headless=True`
* Options for the `scrollPauseTime` argument are any float values greater than `0` (default `0.8`). The value you provide will be how long the program waits before trying to scroll the videos list page down for the channel you want to scrape. For fast internet connections, you may want to reduce the value, and for slow connections you may want to increase the value.
  * `scrollPauseTime=0.8` (default)
  * CAUTION: reducing this value too much will result in the programming not capturing all the videos, so be careful! Experiment :)

## Running the package from the CLI as a script using -m (coming in `0.3.x`!)
```
python3 -m yt_videos_list
```

## General Overview
This repo is intended to provide a quick, simple way to create a list of all videos posted to any YouTube channel by providing just the URL to that user's channel videos. The general format for this is
`https://www.youtube.com/user/TheChannelYouWantToScrape/videos`
OR
`https://www.youtube.com/channel/TheChannelYouWantToScrape/videos`.

### [Future Features](https://github.com/Shail-Shouryya/yt_videos_list/blob/master/extra/futureFeatures.md)

## Technical Specifications
Please see [/extra/technicalSpecifications.md](https://github.com/Shail-Shouryya/yt_videos_list/blob/master/extra/technicalSpecifications.md)
