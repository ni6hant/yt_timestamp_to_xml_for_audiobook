def time_stamp_to_seconds(time_string:str):
    time_seconds = 0
    parts = time_string.split(":")

    try:
        time_seconds += int(parts[-1])
    except (IndexError,ValueError):
        pass

    try:
        time_seconds += int(parts[-2])*60
    except (IndexError,ValueError):
        pass

    try:
        time_seconds += int(parts[-3])*60*60
    except (IndexError,ValueError):
        pass
    return time_seconds

def read_timestamp_file_and_store_in_list(timestamp_file:str):
    timestamps = []
    with open(timestamp_file) as new_file:
        for line in new_file:
            parts = line.replace("\n","").replace(" - ","-").replace("&","and").strip().split("-")
            
            time_string = parts[0]
            details = parts[1]

            time_seconds = time_stamp_to_seconds(time_string)

            timestamps.append((time_seconds,details))
    return timestamps

if __name__=="__main__":
    timestamps = read_timestamp_file_and_store_in_list("timestamps.txt")
    fileName = "EFAP #400 - The Eighth Anniversary of Pausing Every Frame - Covering Everything with Everyone - 1 [wGqqvWph1BA].opus"

    open('bookmarks.sabp.xml', 'w').close()

    with open('bookmarks.sabp.xml', 'w') as my_file:
        my_file.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?><root>\n")
        for timestamp in timestamps:
            my_file.write("\t<bookmark>\n")
            my_file.write(f"\t\t<title>{timestamp[1]} </title>\n")
            my_file.write(f"\t\t<description/>\n")
            my_file.write(f"\t\t<fileName>{fileName}</fileName>\n")
            my_file.write(f"\t\t<filePosition>{timestamp[0]}</filePosition>\n")
            my_file.write("\t</bookmark>\n")
        my_file.write("</root>")