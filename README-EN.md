# Whisper-Speech-to-Text-API 🎙️➡️📜

## This project is still under active development and optimization. The current readme document is outdated. Please wait for the next version update.

[Chinese](README.md) | [English](README-EN.md)

Welcome to the **[Whisper-Speech-to-Text-API](https://github.com/Evil0ctal/Whisper-Speech-to-Text-API)** project! This project provides developers with a fast and reliable API, enabling efficient transcription of various video and audio file formats into text using the [OpenAI Whisper](https://github.com/openai/whisper) model. It’s ideal for speech recognition, subtitle generation, and text analysis needs.

## Project Link 📂

* **GitHub** : [Whisper-Speech-to-Text-API](https://github.com/Evil0ctal/Whisper-Speech-to-Text-API)

## 🌟 Features

* **High-Performance API** : Built with FastAPI to support asynchronous operations, including background task management and storage in an SQLite database for controlled task management.
* **Multi-Format Support** : Supports audio and video files (e.g., MP4) and utilizes `ffmpeg` for broad compatibility.
* **CUDA Acceleration** : For users with GPUs, offers CUDA-accelerated processing, significantly speeding up transcription.
* **Model Optimization** : Fine-tuned Whisper model for higher recognition accuracy, supporting multilingual audio transcription. (Coming soon🔜)
* **Text Analysis** : Enables further processing, such as summarization and content analysis, suitable for extended development needs.
* **Automatic Language Detection** : Whisper model supports automatic language detection, using the first 30 seconds of the media file to auto-set the target language.

## 🚀 Quick Deployment

1. **Python Environment** : Ensure Python version >= 3.8. This project widely uses the `asyncio` library for asynchronous processing.
2. **Install FFmpeg** : Install FFmpeg with the following commands based on your system.

```bash
# Ubuntu or Debian System
sudo apt update && sudo apt install ffmpeg

# Arch Linux System
sudo pacman -S ffmpeg

# MacOS System -> Homebrew
brew install ffmpeg

# Windows System -> Chocolatey(Method one)
choco install ffmpeg

# Windows System -> Scoop(Method two)
scoop install ffmpeg
```

3. **Install CUDA** : To enable GPU acceleration, download and install [CUDA](https://developer.nvidia.com/cuda-12-4-0-download-archive); CPU-only users can skip this step.
4. **Install CUDA-Supported PyTorch** : `python3 -m pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118`
5. **Install Project Dependencies** : `pip install -r requirements.txt`

## ⚗️ Technology Stack

* **[Whisper](https://github.com/openai/whisper)** - Speech recognition model
* **[ffmpeg](https://ffmpeg.org/)** - Audio and video format conversion
* **[torch](https://pytorch.org/)** - Deep learning framework
* **[FastAPI](https://github.com/fastapi/fastapi)** - High-performance API framework
* **[aiofile](https://github.com/Tinche/aiofiles)** - Asynchronous file operations
* **[aiosqlite](https://github.com/omnilib/aiosqlite)** - Asynchronous database operations
* **[moviepy](https://github.com/Zulko/moviepy)** - Video editing
* **[pydub](https://github.com/jiaaro/pydub)** - Audio editing

## 💡 Project Structure

```text
./📂 Whisper-Speech-to-Text-API/
├── 📂 app/                      # Main app directory
│   ├── 📂 api/                  # API routes
│   │   ├── 📄 health_check.py   # Health check endpoint
│   │   └── 📄 transcribe.py     # Transcription endpoint
│   ├── 📂 database/             # Database module
│   │   ├── 📄 database.py       # Database connection and initialization
│   │   └── 📄 models.py         # Database models
│   ├── 📂 models/               # Data models
│   │   └── 📄 APIResponseModel.py # API response model
│   ├── 📂 services/             # Service layer logic
│   │   ├── 📄 whisper_service.py # Whisper model handling logic
│   │   └── 📄 whisper_service_instance.py # Whisper service singleton
│   ├── 📂 utils/                # Utilities
│   │   ├── 📄 file_utils.py     # File handling utilities
│   │   └── 📄 logging_utils.py  # Logging utilities
│   └── 📄 main.py               # Application entry point
├── 📂 config/                   # Configuration files
│   └── 📄 settings.py           # Application settings
├── 📂 scripts/                  # Scripts
│   ├── 📄 run_server.sh         # Server start script
│   └── 📄 setup.sh              # Environment setup script
├── 📁 log_files/                # 📒 Default log folder
├── 📁 temp_files/               # 📂 Default temp folder
├── 📄 requirements.txt          # Dependency list
├── 📄 start.py                  # Start script
└── 📄 tasks.db                  # 📊 Default database file
```

## 🛠️ User Guide

* Switch to the project directory, then start the API service with:
* `python3 start.py`
* You can then visit `http://localhost` to view the API documentation and test the endpoints on the web.

### API Usage Example

* Add a transcription task

```curl
curl -X 'POST' \
  'http://127.0.0.1/transcribe/task/create' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'verbose=false' \
  -F 'priority=normal' \
  -F 'logprob_threshold=-1' \
  -F 'prepend_punctuations="'\''“¿([{-' \
  -F 'no_speech_threshold=0.6' \
  -F 'clip_timestamps=0' \
  -F 'word_timestamps=false' \
  -F 'temperature=0.2' \
  -F 'hallucination_silence_threshold=0' \
  -F 'condition_on_previous_text=true' \
  -F 'file=@Example.mp4;type=video/mp4' \
  -F 'compression_ratio_threshold=2.4' \
  -F 'append_punctuations="'\''.。,，!！?？:：”)]}、' \
  -F 'initial_prompt='
```

- Response

```json
{
  "code": 200,
  "router": "http://127.0.0.1/transcribe/task/create",
  "params": {},
  "data": {
    "id": 1,
    "created_at": "2024-10-27T06:40:55.413738",
    "updated_at": null,
    "status": "queued",
    "file_path": "C:\\Users\\Evil0ctal\\PycharmProjects\\Whisper-Speech-to-Text-API\\temp_files\\02fe0aa4265e43ed91532107b9f6303b.mp4",
    "file_name": "Example.mp4",
    "file_size_bytes": 5273783,
    "duration": 39.612,
    "decode_options": {
      "temperature": [
        0.2
      ],
      "verbose": false,
      "compression_ratio_threshold": 2.4,
      "logprob_threshold": -1,
      "no_speech_threshold": 0.6,
      "condition_on_previous_text": true,
      "initial_prompt": "",
      "word_timestamps": false,
      "prepend_punctuations": "\"'“¿([{-",
      "append_punctuations": "\"'.。,，!！?？:：”)]}、",
      "clip_timestamps": [
        0
      ],
      "hallucination_silence_threshold": 0
    },
    "result": null,
    "error_message": null,
    "attempts": 0,
    "priority": "normal",
    "output_url": null,
    "language": null,
    "progress": 0
  }
}
```

- View task results

```curl
curl -X 'GET' \
  'http://127.0.0.1/transcribe/tasks/result?task_id=1' \
  -H 'accept: application/json'
```

- Response

```json
{
  "id": 1,
  "created_at": "2024-10-27T06:40:55.413738",
  "updated_at": "2024-10-27T06:45:38.557478",
  "status": "completed",
  "file_path": "C:\\Users\\Evil0ctal\\PycharmProjects\\Whisper-Speech-to-Text-API\\temp_files\\02fe0aa4265e43ed91532107b9f6303b.mp4",
  "file_name": "Example.mp4",
  "file_size_bytes": 5273783,
  "duration": 39.612,
  "decode_options": {
    "temperature": [
      0.2
    ],
    "verbose": false,
    "compression_ratio_threshold": 2.4,
    "logprob_threshold": -1,
    "no_speech_threshold": 0.6,
    "condition_on_previous_text": true,
    "initial_prompt": "",
    "word_timestamps": false,
    "prepend_punctuations": "\"'“¿([{-",
    "append_punctuations": "\"'.。,，!！?？:：”)]}、",
    "clip_timestamps": [
      0
    ],
    "hallucination_silence_threshold": 0
  },
  "result": {
    "text": "我们并没有在一起只是聊了很久的天我知道我们并没有感情每天我们就是问问在干嘛我们就是早安晚安拿大游戏发发呆没话讲就发表情报号下去因为相较于情感的挥霍爱的执照总是要显得繁琐些要好像从来都不好气我是怎么样的人我半夜不睡觉的时候在干嘛摩卡就牵是什么意思我的社交圈我的朋友我的爱好你好像通通不在乎我只是你刚好寂寞的时候我撞了上去刚好我心里还挺知道我们有点两万个的话题当然我稍微能入你的眼刚好而已我们都在场口是心非却又希望对方有所察觉但很多时候沉默都比解释热和悲伤来得更容易",
    "segments": [
      {
        "id": 0,
        "seek": 0,
        "start": 0,
        "end": 1.28,
        "text": "我们并没有在一起",
        "tokens": [
          50365,
          15003,
          3509,
          114,
          17944,
          3581,
          29567,
          50429
        ],
        "temperature": 0.2,
        "avg_logprob": -0.21540247599283854,
        "compression_ratio": 1.4733727810650887,
        "no_speech_prob": 3.287499161785945e-10
      },
      {
        "id": 1,
        "seek": 0,
        "start": 1.28,
        "end": 2.64,
        "text": "只是聊了很久的天",
        "tokens": [
          50429,
          36859,
          40096,
          2289,
          4563,
          25320,
          1546,
          6135,
          50497
        ],
        "temperature": 0.2,
        "avg_logprob": -0.21540247599283854,
        "compression_ratio": 1.4733727810650887,
        "no_speech_prob": 3.287499161785945e-10
      },
      {
        "id": 2,
        "seek": 0,
        "start": 2.64,
        "end": 4.2,
        "text": "我知道我们并没有感情",
        "tokens": [
          50497,
          33838,
          15003,
          3509,
          114,
          17944,
          9709,
          10570,
          50575
        ],
        "temperature": 0.2,
        "avg_logprob": -0.21540247599283854,
        "compression_ratio": 1.4733727810650887,
        "no_speech_prob": 3.287499161785945e-10
      },
      {
        "id": 3,
        "seek": 0,
        "start": 4.2,
        "end": 5.84,
        "text": "每天我们就是问问在干嘛",
        "tokens": [
          50575,
          23664,
          6135,
          15003,
          5620,
          22064,
          22064,
          3581,
          26111,
          20722,
          50657
        ],
        "temperature": 0.2,
        "avg_logprob": -0.21540247599283854,
        "compression_ratio": 1.4733727810650887,
        "no_speech_prob": 3.287499161785945e-10
      },
      {
        "id": 4,
        "seek": 0,
        "start": 5.84,
        "end": 7.2,
        "text": "我们就是早安晚安",
        "tokens": [
          50657,
          15003,
          5620,
          21176,
          16206,
          27080,
          16206,
          50725
        ],
        "temperature": 0.2,
        "avg_logprob": -0.21540247599283854,
        "compression_ratio": 1.4733727810650887,
        "no_speech_prob": 3.287499161785945e-10
      },
      {
        "id": 5,
        "seek": 0,
        "start": 7.2,
        "end": 8.52,
        "text": "拿大游戏发发呆",
        "tokens": [
          50725,
          24351,
          3582,
          9592,
          116,
          1486,
          237,
          28926,
          28926,
          3606,
          228,
          50791
        ],
        "temperature": 0.2,
        "avg_logprob": -0.21540247599283854,
        "compression_ratio": 1.4733727810650887,
        "no_speech_prob": 3.287499161785945e-10
      },
      {
        "id": 6,
        "seek": 0,
        "start": 8.52,
        "end": 10.56,
        "text": "没话讲就发表情报号下去",
        "tokens": [
          50791,
          10062,
          21596,
          39255,
          3111,
          28926,
          17571,
          10570,
          49817,
          26987,
          34473,
          50893
        ],
        "temperature": 0.2,
        "avg_logprob": -0.21540247599283854,
        "compression_ratio": 1.4733727810650887,
        "no_speech_prob": 3.287499161785945e-10
      },
      {
        "id": 7,
        "seek": 0,
        "start": 10.56,
        "end": 12.44,
        "text": "因为相较于情感的挥霍",
        "tokens": [
          50893,
          34627,
          15106,
          9830,
          225,
          37732,
          10570,
          9709,
          1546,
          8501,
          98,
          18594,
          235,
          50987
        ],
        "temperature": 0.2,
        "avg_logprob": -0.21540247599283854,
        "compression_ratio": 1.4733727810650887,
        "no_speech_prob": 3.287499161785945e-10
      },
      {
        "id": 8,
        "seek": 0,
        "start": 12.44,
        "end": 14.76,
        "text": "爱的执照总是要显得繁琐些",
        "tokens": [
          50987,
          27324,
          1546,
          3416,
          100,
          32150,
          33440,
          1541,
          4275,
          1431,
          122,
          5916,
          23141,
          223,
          10568,
          238,
          13824,
          51103
        ],
        "temperature": 0.2,
        "avg_logprob": -0.21540247599283854,
        "compression_ratio": 1.4733727810650887,
        "no_speech_prob": 3.287499161785945e-10
      },
      {
        "id": 9,
        "seek": 0,
        "start": 14.76,
        "end": 15.92,
        "text": "要好像从来都不好气",
        "tokens": [
          51103,
          4275,
          33242,
          35630,
          6912,
          7182,
          15769,
          42204,
          51161
        ],
        "temperature": 0.2,
        "avg_logprob": -0.21540247599283854,
        "compression_ratio": 1.4733727810650887,
        "no_speech_prob": 3.287499161785945e-10
      },
      {
        "id": 10,
        "seek": 0,
        "start": 15.92,
        "end": 16.96,
        "text": "我是怎么样的人",
        "tokens": [
          51161,
          15914,
          48200,
          29979,
          51213
        ],
        "temperature": 0.2,
        "avg_logprob": -0.21540247599283854,
        "compression_ratio": 1.4733727810650887,
        "no_speech_prob": 3.287499161785945e-10
      },
      {
        "id": 11,
        "seek": 0,
        "start": 16.96,
        "end": 18.96,
        "text": "我半夜不睡觉的时候在干嘛",
        "tokens": [
          51213,
          1654,
          30018,
          30124,
          1960,
          40490,
          24447,
          49873,
          3581,
          26111,
          20722,
          51313
        ],
        "temperature": 0.2,
        "avg_logprob": -0.21540247599283854,
        "compression_ratio": 1.4733727810650887,
        "no_speech_prob": 3.287499161785945e-10
      },
      {
        "id": 12,
        "seek": 0,
        "start": 18.96,
        "end": 20.400000000000002,
        "text": "摩卡就牵是什么意思",
        "tokens": [
          51313,
          34783,
          102,
          32681,
          3111,
          6935,
          113,
          1541,
          10440,
          16697,
          51385
        ],
        "temperature": 0.2,
        "avg_logprob": -0.21540247599283854,
        "compression_ratio": 1.4733727810650887,
        "no_speech_prob": 3.287499161785945e-10
      },
      {
        "id": 13,
        "seek": 0,
        "start": 20.400000000000002,
        "end": 21.44,
        "text": "我的社交圈",
        "tokens": [
          51385,
          14200,
          27658,
          28455,
          2523,
          230,
          51437
        ],
        "temperature": 0.2,
        "avg_logprob": -0.21540247599283854,
        "compression_ratio": 1.4733727810650887,
        "no_speech_prob": 3.287499161785945e-10
      },
      {
        "id": 14,
        "seek": 0,
        "start": 21.44,
        "end": 22.32,
        "text": "我的朋友",
        "tokens": [
          51437,
          14200,
          19828,
          51481
        ],
        "temperature": 0.2,
        "avg_logprob": -0.21540247599283854,
        "compression_ratio": 1.4733727810650887,
        "no_speech_prob": 3.287499161785945e-10
      },
      {
        "id": 15,
        "seek": 0,
        "start": 22.32,
        "end": 23,
        "text": "我的爱好",
        "tokens": [
          51481,
          14200,
          27324,
          2131,
          51515
        ],
        "temperature": 0.2,
        "avg_logprob": -0.21540247599283854,
        "compression_ratio": 1.4733727810650887,
        "no_speech_prob": 3.287499161785945e-10
      },
      {
        "id": 16,
        "seek": 0,
        "start": 23,
        "end": 24.52,
        "text": "你好像通通不在乎我",
        "tokens": [
          51515,
          26410,
          12760,
          19550,
          19550,
          1960,
          3581,
          2930,
          236,
          1654,
          51591
        ],
        "temperature": 0.2,
        "avg_logprob": -0.21540247599283854,
        "compression_ratio": 1.4733727810650887,
        "no_speech_prob": 3.287499161785945e-10
      },
      {
        "id": 17,
        "seek": 0,
        "start": 24.52,
        "end": 25.84,
        "text": "只是你刚好寂寞的时候",
        "tokens": [
          51591,
          36859,
          2166,
          49160,
          2131,
          4510,
          224,
          4510,
          252,
          49873,
          51657
        ],
        "temperature": 0.2,
        "avg_logprob": -0.21540247599283854,
        "compression_ratio": 1.4733727810650887,
        "no_speech_prob": 3.287499161785945e-10
      },
      {
        "id": 18,
        "seek": 0,
        "start": 25.84,
        "end": 26.96,
        "text": "我撞了上去",
        "tokens": [
          51657,
          1654,
          20559,
          252,
          2289,
          5708,
          6734,
          51713
        ],
        "temperature": 0.2,
        "avg_logprob": -0.21540247599283854,
        "compression_ratio": 1.4733727810650887,
        "no_speech_prob": 3.287499161785945e-10
      },
      {
        "id": 19,
        "seek": 0,
        "start": 26.96,
        "end": 28.240000000000002,
        "text": "刚好我心里还挺",
        "tokens": [
          51713,
          49160,
          2131,
          1654,
          7945,
          15759,
          14852,
          41046,
          51777
        ],
        "temperature": 0.2,
        "avg_logprob": -0.21540247599283854,
        "compression_ratio": 1.4733727810650887,
        "no_speech_prob": 3.287499161785945e-10
      },
      {
        "id": 20,
        "seek": 2824,
        "start": 28.24,
        "end": 30.36,
        "text": "知道我们有点两万个的话题",
        "tokens": [
          50365,
          7758,
          15003,
          2412,
          12579,
          36257,
          23570,
          7549,
          44575,
          30716,
          50471
        ],
        "temperature": 0.2,
        "avg_logprob": -0.2133265408602628,
        "compression_ratio": 1.1271676300578035,
        "no_speech_prob": 0.005595638416707516
      },
      {
        "id": 21,
        "seek": 2824,
        "start": 30.36,
        "end": 31.919999999999998,
        "text": "当然我稍微能入你的眼",
        "tokens": [
          50471,
          40486,
          1654,
          10415,
          235,
          39152,
          8225,
          14028,
          18961,
          25281,
          50549
        ],
        "temperature": 0.2,
        "avg_logprob": -0.2133265408602628,
        "compression_ratio": 1.1271676300578035,
        "no_speech_prob": 0.005595638416707516
      },
      {
        "id": 22,
        "seek": 2824,
        "start": 31.919999999999998,
        "end": 32.839999999999996,
        "text": "刚好而已",
        "tokens": [
          50549,
          49160,
          2131,
          48420,
          50595
        ],
        "temperature": 0.2,
        "avg_logprob": -0.2133265408602628,
        "compression_ratio": 1.1271676300578035,
        "no_speech_prob": 0.005595638416707516
      },
      {
        "id": 23,
        "seek": 2824,
        "start": 32.839999999999996,
        "end": 34.44,
        "text": "我们都在场口是心非",
        "tokens": [
          50595,
          15003,
          7182,
          3581,
          50255,
          18144,
          1541,
          7945,
          12107,
          50675
        ],
        "temperature": 0.2,
        "avg_logprob": -0.2133265408602628,
        "compression_ratio": 1.1271676300578035,
        "no_speech_prob": 0.005595638416707516
      },
      {
        "id": 24,
        "seek": 2824,
        "start": 34.44,
        "end": 36.239999999999995,
        "text": "却又希望对方有所察觉",
        "tokens": [
          50675,
          5322,
          112,
          17047,
          29955,
          8713,
          9249,
          2412,
          5966,
          47550,
          24447,
          50765
        ],
        "temperature": 0.2,
        "avg_logprob": -0.2133265408602628,
        "compression_ratio": 1.1271676300578035,
        "no_speech_prob": 0.005595638416707516
      },
      {
        "id": 25,
        "seek": 2824,
        "start": 36.239999999999995,
        "end": 37.08,
        "text": "但很多时候",
        "tokens": [
          50765,
          8395,
          20778,
          29111,
          50807
        ],
        "temperature": 0.2,
        "avg_logprob": -0.2133265408602628,
        "compression_ratio": 1.1271676300578035,
        "no_speech_prob": 0.005595638416707516
      },
      {
        "id": 26,
        "seek": 2824,
        "start": 37.08,
        "end": 39.599999999999994,
        "text": "沉默都比解释热和悲伤来得更容易",
        "tokens": [
          50807,
          3308,
          231,
          6173,
          246,
          7182,
          11706,
          17278,
          5873,
          232,
          23661,
          255,
          12565,
          14696,
          110,
          7384,
          97,
          6912,
          5916,
          19002,
          49212,
          50933
        ],
        "temperature": 0.2,
        "avg_logprob": -0.2133265408602628,
        "compression_ratio": 1.1271676300578035,
        "no_speech_prob": 0.005595638416707516
      }
    ],
    "language": "zh"
  },
  "error_message": null,
  "attempts": 0,
  "priority": "normal",
  "output_url": null,
  "language": null,
  "progress": 0
}
```

**Include an audio or video file in the request, and the API will return the transcribed text result.**

### Text Analysis and Extended Functionality

**The transcribed text can be used for further processing, such as content summarization and semantic analysis, suitable for secondary analysis or text mining needs.**

## Contribution Guide

**Feedback and suggestions are highly welcome! Reach out through GitHub issues, and if you’d like to contribute, please fork the project and submit a pull request. We look forward to your participation! 💪**
