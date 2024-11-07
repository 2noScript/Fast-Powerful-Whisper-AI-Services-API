from enum import Enum
from typing import Optional

from fastapi import Form
from pydantic import BaseModel


class TaskPriority(str, Enum):
    HIGH = "high"
    NORMAL = "normal"
    LOW = "low"


class TaskType(str, Enum):
    transcribe: str = "transcribe"
    translate: str = "translate"


class WhisperTaskRequest(BaseModel):
    task_type: TaskType = Form(
        TaskType.transcribe,
        description="任务类型，默认为 'transcribe'，具体取值请参考文档 / Task type, default is 'transcribe', refer to the documentation for specific values"
    )
    callback_url: Optional[str] = Form(
        '',
        description="回调URL，任务完成时通知客户端 / Callback URL to notify the client when the task is completed"
    )
    priority: TaskPriority = Form(
        TaskPriority.NORMAL,
        description="任务优先级 / Task priority"
    )
    language: str = Form(
        "",
        description="指定输出语言，例如 'en' 或 'zh'，留空则自动检测 / Specify the output language, e.g., 'en' or 'zh', leave empty for auto-detection"
    )
    temperature: str = Form(
        "0.8,1.0",
        description="采样温度，控制输出文本的多样性，可以是单个值或使用逗号分隔的多个值 / Sampling temperature, control the diversity of the output text, can be a single value or multiple values separated by commas"
    )
    compression_ratio_threshold: float = Form(
        1.8,
        description="压缩比阈值 / Compression ratio threshold"
    )
    no_speech_threshold: float = Form(
        0.6,
        description="无声部分的概率阈值 / No-speech probability threshold"
    )
    condition_on_previous_text: bool = Form(
        True,
        description="在连续语音中更准确地理解上下文 / Condition on previous text"
    )
    initial_prompt: str = Form(
        "",
        description="初始提示文本 / Initial prompt text"
    )
    word_timestamps: bool = Form(
        False,
        description="是否提取每个词的时间戳信息 / Whether to extract word-level timestamp information"
    )
    prepend_punctuations: str = Form(
        "\"'“¿([{-",
        description="前置标点符号集合 / Prepend punctuation characters"
    )
    append_punctuations: str = Form(
        "\"'.。,，!！?？:：”)]}、",
        description="后置标点符号集合 / Append punctuation characters"
    )
    clip_timestamps: str = Form(
        "0.0",
        description="裁剪时间戳，避免超出范围问题，默认为 '0'，可以是单个值或使用逗号分隔的多个值。 / Clip timestamps to avoid out-of-range issues, default is '0', can be a single value or multiple values separated by commas"
    )
    hallucination_silence_threshold: Optional[float] = Form(
        None,
        description="幻听静音阈值 / Hallucination silence threshold"
    )

    class Config:
        schema_extra = {
            "description": """
            Request model for creating a Whisper transcription task.

            **Usage Notes:**
            - Upload media file or specify URL, and set task type, priority, and callback options as needed.
            - Task processing is asynchronous, with results accessible through `/api/whisper/tasks/result`.
            - See API documentation for callback examples and task type details.

            **Common Parameters:**
            - `file` or `file_url`: Specify a media file directly or provide its URL.
            - `task_type`: Choose transcription or translation as supported by the engine.
            - `priority`, `language`, and other parameters control task behavior and output formatting.
            """
        }


class WhisperTaskFileOption(WhisperTaskRequest):
    file_url: Optional[str] = Form(
        '',
        description="媒体文件的 URL 地址 / URL address of the media file"
    )