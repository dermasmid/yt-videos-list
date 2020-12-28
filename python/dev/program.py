import os
import datetime

from .              import file
from .notifications import Common


COMMON_MESSAGE = Common()
NOW            = datetime.datetime.now


def determine_action(url, driver, scroll_pause_time, reverse_chronological, file_name, txt, csv, markdown, logging_output_location):
    txt_exists = os.path.isfile(f'{file_name}.txt')
    csv_exists = os.path.isfile(f'{file_name}.csv')
    md_exists  = os.path.isfile(f'{file_name}.md')
    txt_videos = None
    csv_videos = None
    md_videos  = None
    if txt_exists and csv_exists and md_exists: videos_list, txt_videos, csv_videos, md_videos = file.update_file.scroll_to_old_videos(url, driver, scroll_pause_time, file_name, logging_output_location)
    else:                                       videos_list                                    = file.create_file.scroll_to_bottom    (url, driver, scroll_pause_time, logging_output_location)
    if len(videos_list) == 0:
        logging_output_location.writelines(COMMON_MESSAGE.no_videos_found)
        return
    if txt:
        if txt_exists: file.update_file.write_to_txt(videos_list, file_name, reverse_chronological, logging_output_location, timestamp=NOW().isoformat().replace(':', '-').replace('.', '_'), stored_in_txt=txt_videos)
        else:          file.create_file.write_to_txt(videos_list, file_name, reverse_chronological, logging_output_location, timestamp=NOW().isoformat().replace(':', '-').replace('.', '_'))
    if csv:
        if csv_exists: file.update_file.write_to_csv(videos_list, file_name, reverse_chronological, logging_output_location, timestamp=NOW().isoformat().replace(':', '-').replace('.', '_'), stored_in_csv=csv_videos)
        else:          file.create_file.write_to_csv(videos_list, file_name, reverse_chronological, logging_output_location, timestamp=NOW().isoformat().replace(':', '-').replace('.', '_'))
    if markdown:
        if md_exists:  file.update_file.write_to_md (videos_list, file_name, reverse_chronological, logging_output_location, timestamp=NOW().isoformat().replace(':', '-').replace('.', '_'), stored_in_md=md_videos)
        else:          file.create_file.write_to_md (videos_list, file_name, reverse_chronological, logging_output_location, timestamp=NOW().isoformat().replace(':', '-').replace('.', '_'))
