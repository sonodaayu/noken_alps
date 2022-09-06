import requests
import sys
LINE_URL = "https://notify-api.line.me/api/notify"
LINE_TOKEN = "lYE3ignkHk8GqcYHfsVdGyMDd9aX9ugGt3OxUjZMvwy"
LINE_HEADERS = {
    "Authorization": "Bearer " + LINE_TOKEN
}
params = {
    'message': "{}の接続に失敗しました".format(sys.argv[1])
}
requests.post(LINE_URL, headers=LINE_HEADERS, params=params)
