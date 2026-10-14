"""Библиотека утилит project-b-utils."""
from .date_utils import (get_current_date, format_date, days_between,
                         add_working_days, is_weekend, start_of_month)
from .string_utils import (reverse_string, capitalize_words, slugify, truncate,
                           count_words, is_palindrome)

__version__ = "1.0.0"
__all__ = [
    "get_current_date", "format_date", "days_between", "add_working_days",
    "is_weekend", "start_of_month",
    "reverse_string", "capitalize_words", "slugify", "truncate",
    "count_words", "is_palindrome",
]
