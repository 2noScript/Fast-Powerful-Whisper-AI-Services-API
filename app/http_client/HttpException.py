# ==============================================================================
# Copyright (C) 2021 Evil0ctal
#
# This file is part of the Douyin_TikTok_Download_API project.
#
# This project is licensed under the Apache License 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at:
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
# 　　　　 　　  ＿＿
# 　　　 　　 ／＞　　フ
# 　　　 　　| 　_　 _ l
# 　 　　 　／` ミ＿xノ
# 　　 　 /　　　 　 |       Feed me Stars ⭐ ️
# 　　　 /　 ヽ　　 ﾉ
# 　 　 │　　|　|　|
# 　／￣|　　 |　|　|
# 　| (￣ヽ＿_ヽ_)__)
# 　＼二つ
# ==============================================================================

class APIError(Exception):
    """
    基本 API 异常类，其他 API 异常类都继承自此类 (Base API exception class for all API-related errors)
    """

    def __init__(self, message: str = "An API error occurred.", status_code: int = None):
        self.message = message
        self.status_code = status_code

    def __str__(self):
        """
        返回格式化的错误信息 (Return formatted error message)

        :return: 错误信息字符串 | Error message string
        """
        return f"{self.message}" + (f" Status Code: {self.status_code}." if self.status_code else "")


class APIConnectionError(APIError):
    """当与 API 的连接出现问题时抛出 (Raised when there is a connection issue with the API)"""

    def __init__(self, message: str = "Failed to connect to the API.", status_code: int = None):
        super().__init__(message, status_code)


class APIUnavailableError(APIError):
    """当 API 服务不可用时抛出，例如维护或超时 (Raised when the API service is unavailable, e.g., maintenance or timeout)"""

    def __init__(self, message: str = "The API service is currently unavailable.", status_code: int = 503):
        super().__init__(message, status_code)


class APINotFoundError(APIError):
    """当 API 端点不存在时抛出 (Raised when the API endpoint does not exist)"""

    def __init__(self, message: str = "The requested API endpoint was not found.", status_code: int = 404):
        super().__init__(message, status_code)


class APIResponseError(APIError):
    """当 API 返回的响应与预期不符时抛出 (Raised when the API response is not as expected)"""

    def __init__(self, message: str = "Unexpected API response.", status_code: int = None):
        super().__init__(message, status_code)


class APIRateLimitError(APIError):
    """当达到 API 的请求速率限制时抛出 (Raised when the API rate limit has been reached)"""

    def __init__(self, message: str = "API rate limit exceeded.", status_code: int = 429):
        super().__init__(message, status_code)


class APITimeoutError(APIError):
    """当 API 请求超时时抛出 (Raised when the API request times out)"""

    def __init__(self, message: str = "The API request timed out.", status_code: int = 408):
        super().__init__(message, status_code)


class APIUnauthorizedError(APIError):
    """当 API 请求由于授权失败而被拒绝时抛出 (Raised when the API request is unauthorized)"""

    def __init__(self, message: str = "Unauthorized API request.", status_code: int = 401):
        super().__init__(message, status_code)


class APIRetryExhaustedError(APIError):
    """当 API 请求重试次数用尽时抛出 (Raised when the API retry attempts are exhausted)"""

    def __init__(self, message: str = "API retry limit exhausted.", status_code: int = None):
        super().__init__(message, status_code)


class APIFileDownloadError(APIError):
    """当下载文件时出现问题时抛出 (Raised when there is an issue downloading a file)"""

    def __init__(self, message: str = "Failed to download the file.", status_code: int = None):
        super().__init__(message, status_code)