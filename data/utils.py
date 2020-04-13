import csv
import json

import requests


def get_raw_data(url):
    with requests.Session() as s:
        download = s.get(url)
        decoded_content = download.content.decode("utf-8")
        data = list(csv.reader(decoded_content.splitlines(), delimiter=","))
        return data


def write_data(total_data, save_dir, crawler_name, var_name):
    with open(save_dir, "w", encoding="utf-8") as make_file:
        json.dump(total_data, make_file, ensure_ascii=False, indent=4)

    data = ""
    with open(save_dir, "r", encoding="UTF-8-sig") as f:
        while True:
            line = f.readline()
            if not line:
                break
            data += line

    final_data = f"//Auto-generated by {crawler_name}\nvar {var_name} = {data};"

    with open(save_dir, "w", encoding="UTF-8-sig") as f_write:
        f_write.write(final_data)