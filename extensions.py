COMPRESSED_FORMATS = [
    '.zip', '.rar', '.7z', '.tar', '.gz',
    '.bz2', '.xz', '.iso', '.cab', '.dmg', '.z'
]

VIDEO_FORMATS = [
    '.mp4', '.mov', '.avi', '.mkv', '.flv',
    '.wmv', '.webm', '.mpeg', '.mpg', '.3gp',
    '.m4v', '.ogv', '.ts'
]

MUSIC_FORMATS = [
    '.mp3', '.wav', '.flac', '.aac', '.ogg',
    '.wma', '.m4a', '.aiff', '.alac', '.opus'
]

DOCUMENT_FORMATS = [
    '.pdf', '.doc', '.docx', '.txt', '.rtf',
    '.odt', '.tex', '.md', '.ppt', '.pptx',
    '.xls', '.xlsx', '.csv', '.epub', '.odp', '.ods'
]

def extf(file: str):
    
    pos = file.find('.')
    return file[pos:].lower()
