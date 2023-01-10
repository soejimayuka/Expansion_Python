"""
    G's ACADEMY TOKYO からメンター画像を取得するサンプル.
"""
import os
from urllib.request import urlopen
from pprint import pprint
from bs4 import BeautifulSoup

# メンター一覧ページのHTMLを取得します.
with urlopen("http://gsacademy.jp/mentor-lecturer/") as res:
    html = res.read().decode("utf-8")

# BeautifulSoupインスタンスを生成します.
soup = BeautifulSoup(html, "html.parser")

# 画像のURL一覧を作成します.
img_urls = [e["src"] for e in soup.select(".mentor__list-item img")]
# img_urls = []
# for e in soup.select(".heading.c2 img"):
#     img_urls.append(e["src"])

# 「http://〜」の形式に変換します.
img_urls = [u if u.find("http") == 0 else "http://gsacademy.jp" + u for u in img_urls]
# img_urls2 = []
# for u in img_urls:
#     if u.find("http") == 0:
#         img_urls2.append(u)
#     else:
#         img_urls2.append("http://gsacademy.tokyo" + u)
# img_urls = img_urls2

# 保存先のディレクトリを作成します.
if not os.path.exists("img"):
    os.mkdir("img")

# 画像を読み込んで、ディレクトリに保存します.
for i, url in enumerate(img_urls):
    print(i, url)
    with urlopen(url) as res:
        img = res.read()
        with open("img/%d.png" % (i+1), "wb") as f:
            f.write(img)
