import logging
import requests
from typing import Iterable, Tuple, Optional

from config import FEISHU_CONFIG


def send_feishu_card(title: str, markdown_content: str) -> bool:
    """发送飞书卡片消息"""
    webhook = FEISHU_CONFIG.get('webhook_url') or ''
    if not webhook:
        logging.warning("Feishu webhook is not configured; skip sending notification.")
        return False

    payload = {
        "msg_type": "interactive",
        "card": {
            "header": {
                "title": {
                    "tag": "plain_text",
                    "content": title,
                },
                "template": "blue",
            },
            "elements": [
                {
                    "tag": "div",
                    "text": {
                        "tag": "lark_md",
                        "content": markdown_content,
                    },
                }
            ],
        },
    }

    try:
        resp = requests.post(webhook, json=payload, timeout=10)
        resp.raise_for_status()
        logging.info("Feishu notification sent successfully.")
        return True
    except Exception as e:
        logging.error(f"Failed to send Feishu notification: {e}")
        return False


def format_daily_report_summary(timeframe: str, geo: str, total_keywords: int, success_keywords: int) -> str:
    """格式化飞书日报概要内容（不包含明细表格）"""
    failed = total_keywords - success_keywords
    lines = [
        f"**📊 Daily Trends Report**",
        "",
        f"- 🕒 Time Range: `{timeframe}`",
        f"- 🌍 Region: `{geo or 'Global'}`",
        "",
        "**Summary:**",
        f"- Total keywords: **{total_keywords}**",
        f"- Successful: **{success_keywords}**",
        f"- Failed: **{failed}**",
    ]
    return "\n".join(lines)


def format_rising_trends_markdown(
    timeframe: str,
    geo: str,
    rising_items: Iterable[Tuple[str, str, float]],
    batch_info: Optional[Tuple[int, int]] = None,
) -> str:
    """将高增长趋势列表格式化为飞书 Markdown"""
    lines = [
        "**📈 High Rising Trends Alert**",
        "",
        "**Query Parameters:**",
        f"- 🕒 Time Range: `{timeframe}`",
        f"- 🌍 Region: `{geo or 'Global'}`",
        "",
        "**Significant Growth Trends:**",
    ]

    for base_keyword, related_keyword, value in rising_items:
        lines.append(f"- 🎯 `{base_keyword}` → **{related_keyword}**  ⬆️ **{value}%**")

    if batch_info:
        batch_number, total_batches = batch_info
        lines.append("")
        lines.append(f"_This is batch {batch_number} of {total_batches}._")

    return "\n".join(lines)

