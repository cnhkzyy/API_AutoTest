import os
import re
from conf.conf_dir import logs_dir, htmlreports_dir


def clean(dir_path):
    for file in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, file)) and re.search(r".html|.log", file):
            os.remove(os.path.join(dir_path, file))

clean(htmlreports_dir)
clean(logs_dir)