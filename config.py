import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# Feishu Configuration（从环境变量读取，适配 GitHub Actions Secrets）
FEISHU_CONFIG = {
    # GitHub Actions 中建议用 Secrets.FEISHU_WEBHOOK 注入为环境变量 FEISHU_WEBHOOK
    'webhook_url': os.getenv('FEISHU_WEBHOOK', ''),
}
# https://swmedbueei.feishu.cn/sheets/UZpGshLvKhq7MdtQOFycstuUn4e
# Keywords to monitor（来自截图配置）
KEYWORDS = [
    # 一类：功能词
    "Generator", "Calculator", "Extractor",
    "Guide", "Editor", "Creator", "Maker", "Checker",

    # 一类：图像 / 聊天
    "ai image", "ai picture", "ai photo", "ai", 
    "image", "picture", "photo",

    # 一类：音频 / 视频
    "ai audio", "ai music", "ai song", "ai voice", "ai video",
    "audio", "music", "song", "voice", "video",
    "face","style","anime","avatar","logo","icon"

    # 一类：品牌 / 项目名
    "seedream", "nano banana", "hailuo", "seedance",
    "describer",
    #
    "test","copy and paste","merge","letter","recognize","brainrot","template","sample",
    "designer","downloader","converter","enhancer","detector","humanizer",
    "Group Buy",#合租
    "answer","summarizer"
]


# Trends Query Configuration
TRENDS_CONFIG = {
    #     'timeframe': 'last-3-d',  # 可选值: now 1-d, now 7-d, now 30-d, now 90-d, today 12-m, 
    #                         # last-2-d, last-3-d 或者 "2024-01-01 2024-01-31"
    # 'geo': '',  # 地区代码，例如: 'US' 表示美国, 'CN' 表示中国, '' 表示全球

    # 默认使用最近 3 天，可以通过环境变量 TRENDS_TIMEFRAME 覆盖，例如 "now 1-d"
    'timeframe': os.getenv('TRENDS_TIMEFRAME', 'last-3-d'),
    # 地区代码，例如: 'US' 表示美国, 'CN' 表示中国, '' 表示全球；亦可用 TRENDS_GEO 覆盖
    'geo': os.getenv('TRENDS_GEO', ''),  # 默认全球
}

# Rate Limiting Configuration
RATE_LIMIT_CONFIG = {
    'max_retries': 3,
    'min_delay_between_queries': 10,  # 最小延迟10秒
    'max_delay_between_queries': 20,  # 最大延迟20秒
    'batch_size': 5,  # 每批处理的关键词数量
    'batch_interval': 300,  # 批次间隔时间（秒）
}

# Schedule Configuration
SCHEDULE_CONFIG = {
    'hour': 23,                    # 计划执行的小时（0-23）
    'minute': 5,                 # 计划执行的分钟（0-59）
    'random_delay_minutes': 15   # 随机延迟的最大分钟数（可选）
}

# Monitoring Configuration
MONITOR_CONFIG = {
    'rising_threshold': 500,  # 高增长趋势阈值
}

# Logging Configuration
LOGGING_CONFIG = {
    'log_file': 'trends_monitor.log',
    'level': 'INFO',
    'format': '%(asctime)s - %(levelname)s - %(message)s'
}

# Data Storage Configuration
STORAGE_CONFIG = {
    'data_dir_prefix': 'data_',  # 数据目录前缀
    'report_filename_prefix': 'daily_report_',  # 报告文件名前缀
    'json_filename_prefix': 'related_queries_'  # JSON文件名前缀
} 