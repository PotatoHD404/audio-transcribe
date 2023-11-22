import json


def convert_to_subtitle_time(timestamp):
    """Converts a float timestamp to a subtitle time format."""
    hours = int(timestamp // 3600)
    minutes = int((timestamp % 3600) // 60)
    seconds = int(timestamp % 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"


def process_subtitles(json_file, output_file):
    with open(json_file, 'r', encoding='utf-8') as file:  # Specify UTF-8 encoding
        data = json.load(file)

    subtitles = []
    for chunk in data['chunks']:
        start_time = convert_to_subtitle_time(chunk['timestamp'][0])
        end_time = convert_to_subtitle_time(chunk['timestamp'][1])
        text = chunk['text']
        subtitles.append(f"[{start_time} - {end_time}]{text}\n")

    with open(output_file, 'w', encoding='utf-8') as file:  # Also use UTF-8 here for writing
        file.writelines(subtitles)


def main():
    # Example usage
    process_subtitles('output1.json', 'subtitles.txt')


if __name__ == "__main__":
    main()

# flash-attn?
