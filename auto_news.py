# 导入需要的模块
import feedparser  # 用于解析RSS feed
import subprocess  # 用于运行新的应用程序或命令
import time #用于全屏等待
import pyautogui #用于全屏按键


from datetime import date, timedelta  # 用于获取和处理日期

def play_video(video_url):
    # 在默认的网络浏览器中打开视频
    subprocess.run(['start', video_url], check=True, shell=True)

    #等待20秒打开网页
    time.sleep(5) 

    #按下全屏按键F
    pyautogui.press('f')


def parse_rss_feed(rss_feed_url, video_title):
    # 解析RSS feed
    feed = feedparser.parse(rss_feed_url)

    # 尝试找到具有所需标题的视频
    for entry in feed.entries:
        if entry['title'] == video_title:
            return entry['link']  # 返回找到的视频的URL

    return None  # 如果没找到，返回None

# 获取昨天的日期
yesterday = date.today() - timedelta(days=1)

# 生成昨天新闻的标题
video_title = f"香港無綫｜7:30一小時新聞｜2023年{yesterday.month}月{yesterday.day}日｜"

# 定义RSS feed的URL
tvb_news_url = "https://www.youtube.com/feeds/videos.xml?channel_id=UC_ifDTtFAcsj-wJ5JfM27CQ"
tvb_anywhere_url = "https://www.youtube.com/feeds/videos.xml?channel_id=UCvdc-bj7Onv5XhEC5z8_JUg"

# 解析RSS feed，获取视频的URL
video_url = parse_rss_feed(tvb_news_url, video_title)

# 如果在TVB新闻频道中没找到昨天的新闻
if not video_url:
    # 从TVB Anywhere频道的RSS feed获取最新的视频
    feed = feedparser.parse(tvb_anywhere_url)
    video_url = feed.entries[0]['link']

# 播放视频
play_video(video_url)



#TVB新闻channel_id为UC_ifDTtFAcsj-wJ5JfM27CQ
#TVB_anywhere_channel_id为UCvdc-bj7Onv5XhEC5z8_JUg