import os
import re

def generate_chapter_list():
    """
    Scans the current directory for folders named 'Chapter X',
    counts the number of image files within them, and generates
    a chapters.js file.
    """
    # Get all entries in the current directory
    try:
        all_dirs = [name for name in os.listdir('.') if os.path.isdir(name)]
    except FileNotFoundError:
        print("Error: Could not find the current directory.")
        return

    chapter_folders = []
    # Use regex to find folders named "Chapter " followed by a number
    chapter_pattern = re.compile(r'^Chapter\s+(\d+)$', re.IGNORECASE)

    for folder_name in all_dirs:
        match = chapter_pattern.match(folder_name)
        if match:
            chapter_number = int(match.group(1))
            chapter_folders.append((chapter_number, folder_name))
    
    # Sort chapters numerically
    chapter_folders.sort()

    chapters_data = []
    print("Scanning folders...")

    for chapter_number, folder_name in chapter_folders:
        try:
            files = os.listdir(folder_name)
            # Supported image extensions
            image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.webp']
            
            # Count image files and determine the primary extension
            image_files = [f for f in files if os.path.splitext(f)[1].lower() in image_extensions]
            
            if not image_files:
                print(f"- Skipping '{folder_name}': No images found.")
                continue

            # Determine the most common extension in the folder
            extensions = [os.path.splitext(f)[1].lower().replace('.', '') for f in image_files]
            primary_extension = max(set(extensions), key=extensions.count)

            # We assume pages are named numerically (1.jpg, 2.jpg, etc.)
            page_count = len(image_files)

            chapters_data.append({
                "folder": folder_name,
                "pages": page_count,
                "extension": primary_extension
            })
            print(f"- Found '{folder_name}' with {page_count} pages (.{primary_extension})")

        except FileNotFoundError:
            print(f"Warning: Could not access folder '{folder_name}'. Skipping.")
            continue

    # Write the data to chapters.js
    with open('chapters.js', 'w') as f:
        f.write('const chapters = [\n')
        for i, chapter in enumerate(chapters_data):
            f.write(f'    {{ folder: "{chapter["folder"]}", pages: {chapter["pages"]}, extension: \'{chapter["extension"]}\' }}')
            if i < len(chapters_data) - 1:
                f.write(',\n')
            else:
                f.write('\n')
        f.write('];\n')

    print("\nSuccess! 'chapters.js' has been created/updated.")
    print(f"Found a total of {len(chapters_data)} chapters.")

if __name__ == '__main__':
    generate_chapter_list()
