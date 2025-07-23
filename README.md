# spa-comicbook-reader
Single Page Application Comic Book Reader

This is a basic and lightweight, single page application used to render comic books from a collection of common image formats (jpg, png).  

## Setup
#### Directory structure
This assumes a directory structure where the index.html is at the root of the application, and there exists one chapter folder for each chapter, containing a series of images in alpha-numeric order.

For example
```shell
.                               # Root Folder
├── /Chapter 1/                 # First Chapter Folder
│   ├── 1.jpg                   # First image
│   ├── 2.jpg                   # Second image
│   ├── 3.jpg                   # Third image
├── /Chapter 2/                 # Second Chapter Folder
│   ├── A.jpg                   # First image
│   ├── B.jpg                   # Second image 
│   ├── C.jpg                   # Third image
├── generate_chapter_config.py  # Scans directories and generates a static config to be used by index.html for navigation and page loading
├── index.html                  # Main HTML file
├── chapters.js                 # Generated from generate_chapter_config.py (run one or at time of update)
└── README.md                   # This file
```

#### Run once
Run the `generate_chapter_config.py` script once, or at any time of update to update the `chapters.js` file.

