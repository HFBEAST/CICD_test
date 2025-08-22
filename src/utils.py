import re
from typing import Optional

def validate_email(email: str) -> bool:
    """验证邮箱格式"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def sanitize_string(text: str) -> str:
    """清理字符串，移除特殊字符"""
    return re.sub(r'[^a-zA-Z0-9\s]', '', text).strip()

def calculate_percentage(value: float, total: float) -> Optional[float]:
    """计算百分比"""
    if total == 0:
        return None
    return round((value / total) * 100, 2)