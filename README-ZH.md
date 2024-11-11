<div align="center">
<a href="https://github.com/Evil0ctal/Fast-Powerful-Whisper-AI-Services-API" alt="logo" ><img src="https://raw.githubusercontent.com/Evil0ctal/Fast-Powerful-Whisper-AI-Services-API/refs/heads/main/github/logo/logo.jpg" width="150"/></a>
</div>
<h1 align="center">Fast-Powerful-Whisper-AI-Services-API</h1>

<div align="center">

[English](./README.md) | [简体中文](./README-ZH.md)

 <hr>
</div>
    
<div align="left">

🚀「**[Fast-Powerful-Whisper-AI-Services-API](https://github.com/Evil0ctal/Fast-Powerful-Whisper-AI-Services-API)** 」的愿景是打造一个强大且开箱即用的 [Whisper](https://github.com/openai/whisper) 服务 API，专为高性能、高扩展性和分布式处理需求而设计，并且以生产者消费者模式为设计核心打造，理想适用于需要大规模、高效自动语音识别的场景。该项目基于 OpenAI Whisper 模型以及推理速度更快并且准确度近似的 Faster Whisper 模型，支持多语言的高质量语音转录和翻译任务，并且内置的爬虫模块可以轻松实现对抖音和TikTok等社交媒体平台的视频进行处理，只需要输入一个链接接口轻松创建任务。

本系统通过异步模型池方案实现了高效的资源调度与任务管理，并且异步模型池支持使用多个GPU进行并行计算，提供完全本地化、高拓展性，且可靠的解决方案。此外，项目计划实现一套灵活的自定义组件和工作流设计，使用户可以通过 JSON 文件定义复杂的多步骤任务流，或通过 Python 编写自定义组件，扩展功能。内置高性能的异步 HTTP 模块，异步文件IO模块，异步数据库模块，用户可以利用这些模块编写自己的服务或任务处理器来拓展业务，未来计划与ChatGPT等LLM API进行接入，实现自动语音识别到自然语言处理和分析的的完整工作流程。
    
</div>

## 🌟 项目特色

* **异步设计** ：基于Python 3.11的 asyncio 异步特性，所有模块都使用异步特性进行编写，实现请求的高效处理，提升整体系统的稳定性和高并发能力。
* **自带文档UI**：得益于FastAPI自动生成的OpenAPI JSON，本项目自带一个可交互的Swagger UI用于在浏览器中可视化的测试接口，并且接口Swagger UI中带有详细的中文+英文双语说明和默认参数设置，用户可以快速的上手测试。
* **高准确率**：使用最新的`large-v3`模型确保输出的准确率，并且得益于Faster Whisper的加持，在保证准确率的情况下可以极大地缩短推理所需的时间。
* **分布式部署**：本项目可以从同一个数据库中获取任务以及存储任务结果，未来计划与Kafka无缝对接，实现FastAPI与Kafka的完美交响：构建实时更新的智能Web API
* **异步模型池** ：本项目实现了一个高效的异步AI模型池，在线程安全的情况下支持 OpenAI Whisper 和 Faster Whisper 模型的多实例并发处理场景，在支持CUDA加速且拥有多个GPU的场景中，通过智能加载机制可以将多个模型智能的加载在多个GPU上，然后模型实例间自动分配任务，确保任务处理速度和系统负载均衡，但是在单一GPU场景下无法提供并发功能。
* **异步数据库**：本项目支持使用MySQL和SQLite作为数据库，在本机运行时无需安装和配置MySQL，使用SQLite即可快速运行项目，如果使用MySQL则可以更好的配合分布式计算，多个节点使用同一个数据库作为任务源。
* **异步网络爬虫**：本项目内置了多个平台的数据爬虫模块，当前支持`抖音`、`TikTok`，用户只需要输入对应的视频链接即可快速的对媒体进行语音识别，并且未来计划支持更多社交媒体平台。
* **ChatGPT集成**：本项目已经集成了ChatGPT作为LLM部分的支持，可以使用数据库中的数据与ChatGPT进行交互。
* **工作流与组件化设计（待实现）** ：围绕 Whisper 转录任务，项目支持高度自定义的工作流系统。用户可以通过 JSON 文件定义组件、任务依赖和执行顺序，甚至可以使用 Python 编写自定义组件，灵活扩展系统功能，轻松实现复杂的多步骤处理流程。
* **事件驱动的智能工作流（待实现）** ：工作流系统支持事件触发，可以基于时间、手动触发，或由爬虫模块自动触发。相比单一任务，工作流更加智能，支持条件分支、任务依赖、动态参数传递和重试策略，为用户提供更高的自动化和可控性。

## 💫 适用场景

* **媒体数据处理** ：适用于需要大规模语音转文本处理的场景，比如网络或本地的媒体文件转录，分析，翻译，生成字幕等应用。
* **自动化工作流** ：虽然目前项目本身没有实现工作流，但是可以通过API于其他平台的任务流系统进行接入，通过事件驱动的工作流，轻松实现复杂任务的自动化执行，适合需要多步骤处理和条件控制的业务逻辑。
* **动态数据采集** ：结合异步爬虫模块，系统可自动采集和处理来自网络的数据，并且存储处理完成后的数据。
* **利用分布算力**：在多个分布的零散算力下，可以使用网关的形式将分散的算力进行有效利用。


## 🚩 已实现的功能：

- **创建任务：** 支持上传媒体文件（`file_upload`）或指定媒体文件链接（`file_url`）作为任务的数据源，并且设置一系列参数更加细粒的处理任务，见下文。
- **设置任务类型：** 用户可以通过修改（`task_type`）参数设置任务类型，当前支持媒体文件转文本（`transcribe`）或自动翻译（`translate`）
- **设置任务处理优先级：** 用户可以通过 `priority` 参数指定任务优先级，目前支持三种优先级（`high`, `normal`, `low`）
- **任务回调通知：** 用户在创建任务时可以指定 `callback_url` 作为任务完成后的数据接收地址，任务处理完成后会向目标地址发送一个HTTP POST请求将任务的结果数据传递到指定服务器，并且回调状态会被记录在数据库中方便审查。
- **多平台支持：** 用户可以在对应接口中创建抖音任务、TikTok任务，也可以手动使用视频链接并且手动使用`platform`参数标记平台名称。
- **设置Whisper参数：** 用户可以手动设置解码参数来修改模型的推理过程，当前支持多种参数（`language`，`temperature`, `compression_ratio_threshold`, `no_speech_threshold`, `condition_on_previous_text`, `initial_prompt`, `word_timestamps`, `prepend_punctuations`, `append_punctuations`, `clip_timestamps`, `hallucination_silence_threshold`）
- **查询任务**：用户可以根据多种筛选条件查询任务列表，包括任务状态、优先级、创建时间、语言、引擎名称等信息，该接口适用于分页查询，并且通过 limit 和 offset 参数控制每页显示的记录数，支持客户端逐页加载数据。
- **删除任务**： 用户可以根据任务ID删除任务，删除后任务数据将被永久删除。
- **获取任务结果**：用户可以根据任务ID获取指定任务的结果信息。
- **提取视频的音频**：运行用户上传文件来从视频文件中提取音频，支持设置采样率（`sample_rate`），位深度（`bit_depth`），输出格式（`output_format`）。
- **生成字幕文件**：用户可以通过指定的任务ID来生成指定任务的字幕，并且支持指定输出格式（`output_format`），当前支持（`srt`）以及（`vtt`）作为字幕文件格式。
- **创建TikTok任务**：用户可以通过 TikTok 视频链接爬取视频并创建任务。
- **创建抖音任务**：用户可以通过抖音视频链接爬取视频并创建任务。
- **使用ChatGPT总结任务**：用户可以使用任务ID将已经转义好的自然语言交给ChatGPT进行内容总结和其他交互，并且支持在接口选择模型和自定义提示词。

## 📸 项目截图


![2024_02_16_AM.png](https://github.com/Evil0ctal/Fast-Powerful-Whisper-AI-Services-API/blob/main/github/screenshots/2024_02_16_AM.png?raw=true)

## 🚀 快速部署

1. **克隆本项目**： 确保你的电脑上正确安装了`git`，然后打开你电脑上的控制台或终端来执行下方的命令
    - 下载项目文件：
        ```bash
        git clone https://github.com/Evil0ctal/Fast-Powerful-Whisper-AI-Services-API.git
        ```
2. **Python 环境**：推荐使用Python 版本 `3.12` 或确保 Python 版本 >= `3.8`。
3. **安装 FFmpeg**：本项目使用 [FFmpeg](https://www.ffmpeg.org/) 作为音视频编解码工具，你可以根据你的系统类型来执行下方对应的命令来安装。
    - **Ubuntu or Debian 系统**  
        ```bash
        sudo apt update && sudo apt install ffmpeg
        ```
    - **Arch Linux 系统**
        ```bash
        sudo pacman -S ffmpeg
        ```
    - **MacOS 系统 (Homebrew)**
        ```bash
        brew install ffmpeg
        ```
    - **Windows 系统 (Chocolatey - 方法一)**
        ```bash
        choco install ffmpeg
        ```
    - **Windows 系统 (Scoop - 方法二)**
        ```bash
        scoop install ffmpeg
        ```
4. **安装 CUDA**：本项目使用 [CUDA](https://developer.nvidia.com/cuda-toolkit) 利用 GPU 进行推理加速，如果你想仅使用 CPU 来进行推理则可跳过这部分。
    - 请根据你的系统下载并安装对应版本的 Cuda-Toolkit
    - [https://developer.nvidia.com/cuda-downloads](https://developer.nvidia.com/cuda-downloads)
5. **安装支持CUDA的PyTorch**: 确保正确安装了匹配你的GPU的CUDA Toolkit。
    - 使用控制台或终端执行下方的命令：
        ```bash
        pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
        ```
6. **安装项目依赖**: 确保你在项目的目录中，这一步将把所需要的依赖库安装到本地。
    - 使用控制台或终端执行下方的命令：
        ```bash
        pip install -r requirements.txt
        ```
7. **修改项目的默认配置**：本项目的大多数设置都是可以修改的，你可以在下面的链接中查看默认的项目配置，默认的配置是不会自动重载项目的，你也可以在配置中开启自动重载，修改配置文件后建议重启一次服务。
    - 默认配置文件链接：
    - https://github.com/Evil0ctal/Fast-Powerful-Whisper-AI-Services-API/blob/main/config/settings.py
8. **启动项目**：确保你在项目的根目录下。
    - 启动API：
        ```bash
        python3 start.py
        ```
    - 在浏览器上查看接口文档
    - 项目默认运行在 http://127.0.0.1/

## ⚗️ 技术栈

* **[OpenAI Whisper](https://github.com/openai/whisper)** - 语音识别模型
* **[Faster Whisper](https://github.com/SYSTRAN/faster-whisper)** - 更快速的语音识别模型
* **[ffmpeg](https://ffmpeg.org/)** - 音视频格式转换
* **[torch](https://pytorch.org/)** - 深度学习框架
* **[FastAPI](https://github.com/fastapi/fastapi)** - 高性能 API 框架
* **[HTTPX](https://www.python-httpx.org/)** - 异步 HTTP 框架
* **[aiofile](https://github.com/Tinche/aiofiles)** - 异步文件操作
* **[aiosqlite](https://github.com/omnilib/aiosqlite)** - 异步数据库操作
* **[aiosmysql](https://github.com/aio-libs/aiomysql)** - 异步数据库操作
* **[moviepy](https://github.com/Zulko/moviepy)** - 视频编辑
* **[pydub](https://github.com/jiaaro/pydub)** - 音频编辑

## 🗃️ 项目结构
```
📂 Fast-Powerful-Whisper-AI-Services-API/
├── 📁 app/
│   ├── 📁 api/ -> API layer containing models and routes
│   │   ├── 📁 models/
│   │   │   ├── 📄 APIResponseModel.py -> Defines API response models
│   │   │   ├── 📄 ChatGPTTaskRequest.py -> Request model for ChatGPT tasks
│   │   │   ├── 📄 DouyinTaskRequest.py -> Request model for Douyin tasks
│   │   │   ├── 📄 TikTokTaskRequest.py -> Request model for TikTok tasks
│   │   │   ├── 📄 WhisperTaskRequest.py -> Request model for Whisper tasks
│   │   │   └── 📄 WorkFlowModels.py -> Workflow data models
│   │   ├── 📁 routers/
│   │   │   ├── 🔍 health_check.py -> Health check endpoint
│   │   │   ├── 📝 whisper_tasks.py -> Routes for Whisper tasks
│   │   │   ├── 🔄 work_flows.py -> Routes for workflow management
│   │   │   ├── 💬 chatgpt_tasks.py -> Routes for ChatGPT-related tasks
│   │   │   ├── 🌐 douyin_tasks.py -> Routes for Douyin-related tasks
│   │   │   └── 🎥 tiktok_tasks.py -> Routes for TikTok-related tasks
│   │   └── 📄 router.py -> Main router module
│   ├── 🕸️ crawlers/ -> Modules for web crawling
│   │   ├── 📁 platforms/
│   │   │   ├── 📁 douyin/
│   │   │   │   ├── 🐛 abogus.py -> (`・ω・´) Whats This? 
│   │   │   │   ├── 🚀 crawler.py -> Douyin data crawler
│   │   │   │   ├── 📡 endpoints.py -> API endpoints for Douyin crawler
│   │   │   │   ├── 🧩 models.py -> Models for Douyin data
│   │   │   │   ├── 🛠️ utils.py -> Utility functions for Douyin crawler
│   │   │   │   └── 📘 README.md -> Douyin module documentation
│   │   │   └── 📁 tiktok/
│   │   │       ├── 🚀 crawler.py -> TikTok data crawler
│   │   │       ├── 📡 endpoints.py -> API endpoints for TikTok crawler
│   │   │       ├── 🧩 models.py -> Models for TikTok data
│   │   │       └── 📘 README.md -> TikTok module documentation
│   ├── 💾 database/ -> Database models and management
│   │   ├── 📁 models/
│   │   │   ├── 📂 TaskModels.py -> Task-related database models
│   │   │   ├── 📂 WorkFlowModels.py -> Workflow-related database models
│   │   │   ├── 🧠 ChatGPTModels.py -> Models for ChatGPT tasks
│   │   │   └── 🕸️ CrawlerModels.py -> Models for crawlers and platforms
│   │   └── 🗄️ DatabaseManager.py -> Handles database connections
│   ├── 🌐 http_client/ -> HTTP client setup
│   │   ├── ⚙️ AsyncHttpClient.py -> Asynchronous HTTP client
│   │   └── ❗ HttpException.py -> Custom HTTP exceptions
│   ├── 🤖 model_pool/ -> Model pooling and management
│   │   └── 🧠 AsyncModelPool.py -> Asynchronous model pool manager
│   ├── 🔄 processors/ -> Task and workflow processors
│   │   ├── 📋 task_processor.py -> Processes Whisper tasks
│   │   └── 🛠️ workflow_processor.py -> Processes workflows
│   ├── 🛎️ services/ -> Service layer for API functions
│   │   ├── 📲 callback_service.py -> Handles callbacks
│   │   ├── 🔄 workflow_service.py -> Workflow handling services
│   │   └── 🗣️ whisper_service.py -> Whisper model-related services
│   ├── 🧰 utils/ -> Utility functions
│   │   ├── 📂 file_utils.py -> File operations and management
│   │   └── 🔍 logging_utils.py -> Logging utilities
│   ├── ⚙️ workflows/ -> Workflow components
│   │   └── 🧩 components/
│   │       ├── 🛠️ base_component.py -> Base workflow component
│   │       ├── 📄 component_a.py -> Custom workflow component A
│   │       └── 📄 component_b.py -> Custom workflow component B
│   └── 🚀 main.py -> Application entry point
├── ⚙️ config/
│   └── 🛠️ settings.py -> Configuration file
├── 📁 temp_files/ -> Temporary files folder
│   └── 📂 -> Default TEMP Files Folder
├── 📁 log_files/ -> Log files folder
│   └── 📂 -> Default LOG Files Folder
├── 📂 WhisperServiceAPI.db -> Default SQLite DB File
├── 📄 requirements.txt -> Python package requirements
└── 📝 start.py -> Run to start the API
```

## 🛠️ 使用指南

- 切换到项目目录，使用下面的命令启动API服务：
- `python3 start.py`
- 随后你可以访问`http://localhost`来查看接口文档，并且在网页上测试。

## 🧵 目录结构详解

### 前言：

> 如果你有意参与本项目的开发，建议先阅读本部分内容，以便快速了解项目的设计和各模块的职责。我非常推荐诸位通读本项目的代码，项目中的每个方法都包含详细的中英双语注释、内部说明和变量解释，并且广泛应用了 `Typing` 标注类型。虽未必做到完美无瑕，但我也力求代码清晰优雅、易于理解。此外，我也希望大家一起学习异步编程，提出优化建议，共同改进代码，使项目更加高效和健壮，并且共同进步！

#### 📁 `app/api/` - API层

* **技术栈** ：基于 FastAPI 框架构建，为 API 请求提供高性能、可扩展的路由系统。
* **功能实现** ：
  * **APIResponseModel.py** ：通过 Pydantic 定义数据模型，确保 API 响应数据结构的统一性。
  * **routers/** ：各路由文件分别管理不同功能模块的 API 端点：
    * `health_check.py` 💓：快速检查服务健康状态，及时了解系统状态。
    * `whisper_tasks.py` 📝：Whisper 相关任务的路由管理，支持任务的创建、查询、删除等操作。
    * `work_flows.py` 🔄：工作流的管理路由，提供对工作流的 CRUD 功能接口，未来计划实现事件驱动式的自动化工作流。

#### 📁 `app/crawlers/` - 异步爬虫模块

* **技术栈** ：`httpx` 进行异步 HTTP 请求，结合 `pydantic` 模型实现数据规范化。
* **功能实现** ：
  * **platforms/** 包含针对各平台的爬虫模块，支持 Douyin 和 TikTok：
    * **douyin/** 🕸️：提供 Douyin 视频的抓取、数据提取和 API 接口，包含了自定义的模型和实用工具类。
    * **tiktok/** 🕹️：支持 TikTok 数据的抓取和 API 数据展示功能，计划进一步扩展其他社交媒体平台。
* **解决问题** ：提供自动化的数据抓取能力，结合 Whisper 模型实现媒体数据的全流程自动化处理。

#### 📁 `app/database/` - 数据库管理模块

* **技术栈** ：
  * 使用 `SQLAlchemy` 异步支持与 `AsyncSession`，提供了多种数据库操作的 CRUD 功能。
  * 支持 `MySQL` 和 `SQLite` 数据库连接，并实现自动重连、表检查与初始化等基础操作。
  * 集成自定义日志记录和异常处理机制，确保数据库操作的可靠性。
* **功能实现** ：
  * **DatabaseManager** 🗄️：实现了数据库连接管理和任务的增删改查等操作，并支持复杂的查询和批量处理。
    * **数据库连接与自动初始化** ：通过 `_connect` 方法实现数据库连接的自动重试和动态表检查，在首次连接时自动创建所需表格。
    * **任务管理** ：包括 `add_task`、`get_task`、`update_task`、`delete_task` 等方法，以便灵活操作任务数据，支持异步批量操作。
    * **查询与筛选** ：提供 `query_tasks` 方法，根据条件过滤任务，并包含分页和条件构建器 `_build_query_conditions`，实现灵活的查询和筛选。
    * **回调状态更新** ：专门的 `update_task_callback_status` 方法用于更新任务的回调信息，包括状态码、消息和回调时间。
    * **工作流管理** ：支持创建和管理工作流（`Workflow`），包括工作流任务和通知，适合自动化任务流程。
* **解决问题** ：
  * **可靠的数据库连接管理** ：采用自动重试和异步上下文管理器（`get_session`）来确保会话管理的稳定性，解决数据库断开或连接失败等问题。
  * **高效的批量操作支持** ：提供批量更新和删除功能，适合大规模任务处理，减少数据库交互次数，提高效率。
  * **灵活的任务查询** ：支持复杂条件查询并实现分页功能，使得数据库管理器能满足多样化的数据访问需求，便于大型项目的管理和查询优化。

#### 📁 `app/http_client/` - 异步 HTTP 客户端模块

* **技术栈** ：
  * 采用 `httpx` 实现高效的异步 HTTP 客户端，支持代理配置、重试机制、并发限制等功能。
  * 自定义异常处理模块，实现针对不同 HTTP 状态码的精细化错误管理。
  * 实现了包括重试、退避、限流等网络请求优化策略。
* **功能实现** ：
  * **AsyncHttpClient** 🌐：为项目提供了一个健壮的异步 HTTP 客户端工具，集成了以下主要功能：
    * **请求与数据获取** ：支持 `GET`、`POST`、`HEAD` 等常见 HTTP 请求，包含 `fetch_get_json` 和 `fetch_post_json` 方法，返回结构化 JSON 数据。
    * **文件下载支持** ：`download_file` 方法可异步下载文件并支持大文件分块下载，具备完善的下载状态监控和异常处理机制。
    * **自动重试与退避策略** ：针对特定 HTTP 状态码，`fetch_data` 方法提供了指数退避策略，支持自定义重试次数，增强了网络请求的鲁棒性。
    * **错误处理与自定义异常** ：根据 HTTP 响应状态码自定义异常类型，实现自动化的错误类型识别和记录，简化错误的调试和追踪。
    * **代理支持与并发管理** ：支持动态代理配置和并发控制，最大并发请求数可调，确保 HTTP 客户端在高负载下的稳定性和可控性。
* **解决问题** ：
  * **网络请求优化** ：通过自动重试与退避机制处理网络中断或服务不可用等异常情况，提供高可用性网络请求支持。
  * **高并发请求场景** ：在高并发场景下，利用 `asyncio.Semaphore` 控制并发数量，防止请求过载，确保客户端服务的稳定性。
  * **可调配置与灵活使用** ：支持上下文管理器，方便资源释放，动态请求头配置满足不同接口需求，通过自定义代理和超时设置增强了请求的适配性和灵活性。

#### 📁 `app/model_pool/` - 异步模型池模块

* **技术栈** ：
  * 使用 `asyncio` 与 `concurrent.futures` 结合管理 GPU 与 CPU 模型实例。
  * 利用线程安全单例模式确保 `AsyncModelPool` 的唯一实例，避免多线程环境下资源竞争。
  * 设备自动分配和池大小优化逻辑：根据系统硬件资源（如 GPU 数量和 CPU 线程）动态调整池的配置参数。
* **功能实现** ：
  * **AsyncModelPool** 🧠：提供一个线程安全、动态可调的模型池管理系统，实现了以下主要功能：
    * **设备分配和动态创建** ：根据 GPU 和 CPU 配置自动分配设备，支持多 GPU 并发，并限制每个 GPU 上的模型实例数量，确保高效利用硬件资源。
    * **初始化与批量加载** ：支持异步批量加载模型实例，通过 `initialize_pool` 方法按需创建模型，减少并发加载冲突。
    * **模型实例获取与归还** ：提供 `get_model` 和 `return_model` 方法，实现模型的并发获取与归还。支持“现有实例”与“动态创建”两种策略，实现灵活的资源分配。
    * **健康检查与销毁** ：包含 `_is_model_healthy` 和 `_destroy_model` 方法，确保模型实例在使用前的健康状态并在销毁后执行资源清理，避免内存泄漏，由于Whisper属于静态模型，这两个方法目前没有使用的必要，暂时保留。
    * **池大小调整** ：`resize_pool` 方法允许动态调整池大小，增加或移除模型实例以适应当前负载，当前未使用该方法，需要设计一个智能的大小调整逻辑。
* **解决问题** ：
  * **硬件资源优化** ：通过动态调整模型池大小，避免了资源浪费和过度分配，确保模型实例数量与硬件资源的实际配置匹配。
  * **多任务并发支持** ：在多任务请求场景下提供高效的模型实例分配策略，支持每个 GPU 的并发使用，并限制最大实例数以避免资源竞争。
  * **自动故障检测与处理** ：具备模型健康检查和错误处理机制，能够在发现损坏或不可用的模型实例后自动销毁并释放资源，保持池内实例健康稳定。

#### 📁 `app/processors/` - 任务与工作流处理模块

* **技术栈** ：
  * 基于 `asyncio` 实现异步处理，结合线程池和队列机制，支持多任务并发管理。使用 `concurrent.futures` 提供线程池以提高任务处理效率。
  * 支持与数据库和文件操作的协同处理，确保高并发情况下的数据一致性和资源高效利用。
* **功能实现** ：
  * **task_processor.py** 📋：实现了 Whisper 任务的后台处理逻辑，具备多队列设计、事件循环管理、任务优先级调度、并行任务处理、数据库更新和文件操作等功能。通过异步和线程池结合，支持大规模、高性能的语音转文本任务处理。
    * **任务队列和优先级调度** ：包含多个任务队列，分离不同类型任务（如清理、回调等），支持任务优先级从数据库按需拉取，保证重要任务优先处理。
    * **并行任务处理** ：结合线程池并行处理多个任务，通过异步方法 `_process_multiple_tasks` 提高处理吞吐量。
    * **事件循环管理** ：通过 `run_loop` 方法启动后台事件循环，持续监控和处理任务队列，实现任务管理的自动化和实时性。
  * **workflow_processor.py** 🔄：用于管理复杂工作流，支持自定义的任务依赖、条件判断和自动化调度。未来将增加事件触发的自动化工作流，进一步扩展处理逻辑。
* **解决问题** ：
  * **高并发处理** ：通过事件循环和多线程的结合，在大批量任务处理场景下提供高吞吐量和低延迟的任务处理能力。
  * **任务分离和优先级支持** ：多队列和优先级调度机制确保不同类型任务独立处理，重要任务可以优先执行，增强了系统的响应速度和任务管理的灵活性。
  * **资源优化** ：对 GPU、数据库、文件存储的有效管理，通过 `AsyncModelPool` 实现高效模型实例管理，确保大规模任务在资源紧张情况下的平稳处理。

#### 📁 `app/services/` - 服务层模块

* **技术栈** ：
  * 使用 `FastAPI` 与 `asyncio` 提供高效异步服务，支持音频处理、转录、回调管理和工作流控制。
  * 集成 `pydub` 和 `moviepy` 库用于音频和视频转换，使用 `ThreadPoolExecutor` 和 `BackgroundTasks` 实现并发文件处理和后台任务。
  * 回调和工作流服务的设计为未来扩展和自定义任务提供支持。
* **功能实现** ：
  * **WhisperService** 🗣️：负责音频提取、转录任务的创建和字幕生成。
    * **音频提取** ：`extract_audio_from_video` 方法提取视频中的音频（WAV 或 MP3 格式），并自动清理临时文件。
    * **转录任务创建** ：`create_whisper_task` 方法接受文件或 URL，创建转录任务并保存到数据库，生成任务输出链接。
    * **字幕生成** ：`generate_subtitle` 方法将转录结果转换为字幕文件（支持 SRT 和 VTT），并在完成后删除临时文件。
  * **CallbackService** 📞：处理任务的回调通知，将结果传递给预定义的回调 URL，并记录回调状态。
    * **回调通知** ：在任务完成后，通过 `task_callback_notification` 发送请求至回调 URL，通知任务结果并记录响应状态。
    * **重试机制** ：支持失败重试，通过 `base_backoff` 设置指数回退，确保重要通知的可靠性。
  * **WorkflowService** 🔄（待实现）：用于管理复杂的自动化任务工作流。
    * **工作流控制** ：计划通过 `WorkflowService` 管理和执行一系列依赖任务，支持条件判断、任务依赖和回调管理，适用于自动化批量任务处理场景。
    * **任务编排与状态跟踪** ：未来将支持工作流任务的状态跟踪和条件控制，提供灵活的工作流设计。
    * **扩展能力** ：支持自定义的工作流步骤与组件配置，用户可以定义和配置不同的工作流来适应业务需求。
* **解决问题** ：
  * **高效任务处理与回调通知** ：利用 `TaskProcessor` 实现任务并发处理，并通过 `CallbackService` 确保任务完成后的回调通知机制的可靠性。
  * **灵活工作流与扩展支持** ：`WorkflowService` 提供面向未来的工作流处理框架，使用户能更灵活地管理和监控一系列任务的执行顺序和依赖。
  * **资源管理与文件清理** ：通过 `BackgroundTasks` 支持异步文件处理和清理，优化资源管理，确保高效和稳定的文件处理体验。

#### 📁 `app/utils/` - 工具模块

* **技术栈** ：Python 原生文件操作与日志模块，结合 `aiofiles` 实现高效异步文件操作，并使用 `ConcurrentRotatingFileHandler` 实现并发安全的日志轮转。
* **功能实现** ：
  * **file_utils.py** 📂：提供文件下载、保存、删除与清理操作，支持文件大小限制与类型检查，确保文件安全，适用于高并发的文件管理需求。
  * **logging_utils.py** 📊：配置项目日志记录，支持文件和控制台输出，日志级别控制、文件自动轮转（10MB）和备份，便于调试与长期日志存储。
* **解决问题** ：
  * **资源管理** ：通过异步上下文管理器和自动删除机制清理临时文件，防止资源泄漏，确保系统稳定。
  * **文件安全与权限管理** ：严格控制文件大小、类型和权限，防止未经授权的文件访问和资源滥用。
  * **并发优化** ：利用信号量控制文件操作并发性，提升 I/O 性能。
  * **日志轮转与安全** ：通过日志轮转与多进程支持，确保在高并发环境下日志输出的完整性与一致性，提供稳定的日志记录系统。

#### 📁 `app/workflows/` - 工作流组件（待完善）

* **技术栈** ：Python 自定义组件设计，未来可扩展支持基于 JSON 或自定义 Python 的任务流配置。
* **功能实现** ：
  * **components/** ：组件模块，用于扩展工作流的功能。
    * `base_component.py` 🛠️：定义工作流组件的基类，支持通用方法和事件。
    * `component_a.py`、`component_b.py`：自定义的工作流组件示例，支持扩展功能。
* **解决问题** ：提供扩展性极高的组件设计，便于用户根据业务需求定义复杂的任务流程和自定义组件。

#### 📄 `config/settings.py` - 配置文件

* **技术栈** ：`dotenv` 解析环境变量，配置 FastAPI、数据库和模型池等参数。
* **功能实现** ：
  * 统一管理项目配置，方便进行数据库、模型池、服务地址等参数的集中配置。
* **解决问题** ：提高配置灵活性，支持快速切换本地和生产环境配置。

## 🍱 接口使用示例

- 添加一个TikTok任务（CURL格式）

```curl
curl -X 'POST' \
  'http://127.0.0.1/api/tiktok/video_task' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'priority=normal&prepend_punctuations=%22'\''%E2%80%9C%C2%BF(%5B%7B-&no_speech_threshold=0.6&clip_timestamps=0&url=https%3A%2F%2Fwww.tiktok.com%2F%40taylorswift%2Fvideo%2F7359655005701311786&word_timestamps=false&platform=tiktok&temperature=0.8%2C1.0&task_type=transcribe&callback_url=&hallucination_silence_threshold=0&language=&condition_on_previous_text=true&compression_ratio_threshold=1.8&append_punctuations=%22'\''.%E3%80%82%2C%EF%BC%8C!%EF%BC%81%3F%EF%BC%9F%3A%EF%BC%9A%E2%80%9D)%5D%7D%E3%80%81&initial_prompt='
```

- 添加一个TikTok任务（Python代码）

```python
# pip install httpx
import httpx

url = "http://127.0.0.1/api/tiktok/video_task"
tiktok_url = "https://www.tiktok.com/@taylorswift/video/7359655005701311786"

# Define the form data as a dictionary
data = {
    "url": tiktok_url,
    "priority": "normal",
    "prepend_punctuations": '"\'“¿([{-',
    "no_speech_threshold": "0.6",
    "clip_timestamps": "0",
    "word_timestamps": "false",
    "platform": "tiktok",
    "temperature": "0.8,1.0",
    "task_type": "transcribe",
    "callback_url": "",
    "hallucination_silence_threshold": "0",
    "language": "",
    "condition_on_previous_text": "true",
    "compression_ratio_threshold": "1.8",
    "append_punctuations": '"\'.。,!！?？:：”)]}、',
    "initial_prompt": ""
}


async def make_request():
    async with httpx.AsyncClient() as client:
        response = await client.post(url, data=data)
        print(response.json())


if __name__ == "__main__":
    # To run the async function
    import asyncio
    # Run the async function
    asyncio.run(make_request())
```

- 请求响应

<div><details><summary>🔎点击展开请求响应</summary>
<pre><code class="json">
{
   "code":200,
   "router":"http://127.0.0.1/api/tiktok/video_task",
   "params":{
      "language":null,
      "temperature":[
         0.8,
         1
      ],
      "compression_ratio_threshold":1.8,
      "no_speech_threshold":0.6,
      "condition_on_previous_text":true,
      "initial_prompt":"",
      "word_timestamps":false,
      "prepend_punctuations":"\"'“¿([{-",
      "append_punctuations":"\"'.。,，!！?？:：”)]}、",
      "clip_timestamps":"0.0",
      "hallucination_silence_threshold":null,
      "task_type":"transcribe",
      "priority":"normal",
      "callback_url":""
   },
   "data":{
      "id":1,
      "status":"queued",
      "callback_url":"",
      "callback_status_code":null,
      "callback_message":null,
      "callback_time":null,
      "priority":"normal",
      "engine_name":"faster_whisper",
      "task_type":"transcribe",
      "created_at":"2024-11-07T16:43:32.768883",
      "updated_at":"2024-11-07T16:43:32.768883",
      "task_processing_time":null,
      "file_path":null,
      "file_url":"https://api.tiktokv.com/aweme/v1/play/?file_id=3146fc434e4d493c93b78566726b9310&is_play_url=1&item_id=7359655005701311786&line=0&signaturev3=dmlkZW9faWQ7ZmlsZV9pZDtpdGVtX2lkLjA3YTkzYjY0ZTliOWUzMzVmN2VhODgxMTMyMDljYTJk&source=FEED&vidc=useast5&video_id=v12044gd0000cohbuanog65ltpj9jdpg",
      "file_name":null,
      "file_size_bytes":null,
      "file_duration":null,
      "language":null,
      "platform":"tiktok",
      "decode_options":{
         "language":null,
         "temperature":[
            0.8,
            1
         ],
         "compression_ratio_threshold":1.8,
         "no_speech_threshold":0.6,
         "condition_on_previous_text":true,
         "initial_prompt":"",
         "word_timestamps":false,
         "prepend_punctuations":"\"'“¿([{-",
         "append_punctuations":"\"'.。,，!！?？:：”)]}、",
         "clip_timestamps":"0.0",
         "hallucination_silence_threshold":null
      },
      "error_message":null,
      "output_url":"http://127.0.0.1/api/whisper/tasks/result?task_id=1",
      "result":null
   }
}
</code></pre>
</details></div>

**在请求体中包含音频或视频文件，API 将返回转录的文本结果。**

- 获取任务结果（CURL格式）

```curl
curl -X 'GET' \
  'http://127.0.0.1/api/whisper/tasks/result?task_id=1' \
  -H 'accept: application/json'
```

- 获取任务结果（Python代码）

```python
# pip install httpx
import httpx

url = "http://127.0.0.1/api/whisper/tasks/result"
task_id = 1

params = {
    "task_id": task_id
}


async def make_request():
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        print(response.json())


if __name__ == "__main__":
    # To run the async function
    import asyncio
    # Run the async function
    asyncio.run(make_request())
```

- 请求响应

<div><details><summary>🔎点击展开请求响应</summary>
<pre><code class="json">
{
  "code": 200,
  "router": "http://127.0.0.1/api/whisper/tasks/result?task_id=1",
  "params": {
    "task_id": "1"
  },
  "data": {
    "id": 1,
    "status": "completed",
    "callback_url": "",
    "callback_status_code": null,
    "callback_message": null,
    "callback_time": null,
    "priority": "normal",
    "engine_name": "faster_whisper",
    "task_type": "transcribe",
    "created_at": "2024-11-07T16:43:33",
    "updated_at": "2024-11-07T16:43:33",
    "task_processing_time": 6.20258,
    "file_path": "C:\\Users\\Evil0ctal\\PycharmProjects\\Fast-Powerful-Whisper-AI-Services-API\\temp_files\\5accc0958ec7476e81d06f8c3897d768.mp4",
    "file_url": "https://api.tiktokv.com/aweme/v1/play/?file_id=3146fc434e4d493c93b78566726b9310&is_play_url=1&item_id=7359655005701311786&line=0&signaturev3=dmlkZW9faWQ7ZmlsZV9pZDtpdGVtX2lkLjA3YTkzYjY0ZTliOWUzMzVmN2VhODgxMTMyMDljYTJk&source=FEED&vidc=useast5&video_id=v12044gd0000cohbuanog65ltpj9jdpg",
    "file_name": null,
    "file_size_bytes": 2401593,
    "file_duration": 30.071,
    "language": "en",
    "platform": "tiktok",
    "decode_options": {
      "language": null,
      "temperature": [
        0.8,
        1
      ],
      "initial_prompt": "",
      "clip_timestamps": "0.0",
      "word_timestamps": false,
      "append_punctuations": "\"'.。,，!！?？:：”)]}、",
      "no_speech_threshold": 0.6,
      "prepend_punctuations": "\"'“¿([{-",
      "condition_on_previous_text": true,
      "compression_ratio_threshold": 1.8,
      "hallucination_silence_threshold": null
    },
    "error_message": null,
    "output_url": "http://127.0.0.1/api/whisper/tasks/result?task_id=1",
    "result": {
      "info": {
        "duration": 30.07125,
        "language": "en",
        "vad_options": null,
        "all_language_probs": [
          [
            "en",
            0.986328125
          ],
          [
            "es",
            0.0013828277587890625
          ],
          [
            "ja",
            0.00125885009765625
          ],
          [
            "fr",
            0.0012197494506835938
          ],
          [
            "de",
            0.0010852813720703125
          ],
          [
            "la",
            0.0010519027709960938
          ],
          [
            "zh",
            0.00089263916015625
          ],
          [
            "pt",
            0.0008320808410644531
          ],
          [
            "ko",
            0.000751495361328125
          ],
          [
            "cy",
            0.000751495361328125
          ],
          [
            "ru",
            0.00074005126953125
          ],
          [
            "nn",
            0.0005245208740234375
          ],
          [
            "sv",
            0.00036072731018066406
          ],
          [
            "it",
            0.0002853870391845703
          ],
          [
            "vi",
            0.00024580955505371094
          ],
          [
            "tr",
            0.0002310276031494141
          ],
          [
            "nl",
            0.00017440319061279297
          ],
          [
            "pl",
            0.00015997886657714844
          ],
          [
            "jw",
            0.0001480579376220703
          ],
          [
            "hi",
            0.00012755393981933594
          ],
          [
            "ar",
            0.00012362003326416016
          ],
          [
            "km",
            0.00012362003326416016
          ],
          [
            "fi",
            0.0001189112663269043
          ],
          [
            "id",
            0.0001170635223388672
          ],
          [
            "haw",
            0.00009781122207641602
          ],
          [
            "th",
            0.00009119510650634766
          ],
          [
            "hu",
            0.00007158517837524414
          ],
          [
            "tl",
            0.000056624412536621094
          ],
          [
            "el",
            0.00005316734313964844
          ],
          [
            "no",
            0.000051975250244140625
          ],
          [
            "ms",
            0.00003892183303833008
          ],
          [
            "cs",
            0.00003802776336669922
          ],
          [
            "ro",
            0.00003129243850708008
          ],
          [
            "ta",
            0.00002312660217285156
          ],
          [
            "mi",
            0.000023066997528076172
          ],
          [
            "da",
            0.000020802021026611328
          ],
          [
            "br",
            0.000020503997802734375
          ],
          [
            "si",
            0.00001800060272216797
          ],
          [
            "sn",
            0.000017702579498291016
          ],
          [
            "fa",
            0.000015079975128173828
          ],
          [
            "ml",
            0.000014007091522216795
          ],
          [
            "uk",
            0.000012218952178955078
          ],
          [
            "he",
            0.000010371208190917969
          ],
          [
            "ca",
            0.000010371208190917969
          ],
          [
            "ur",
            0.000010251998901367188
          ],
          [
            "sl",
            0.000008881092071533203
          ],
          [
            "sa",
            0.000008821487426757812
          ],
          [
            "bn",
            0.000006258487701416016
          ],
          [
            "te",
            0.0000057220458984375
          ],
          [
            "hr",
            0.000005245208740234375
          ],
          [
            "sw",
            0.000004827976226806641
          ],
          [
            "lt",
            0.000003874301910400391
          ],
          [
            "is",
            0.000003874301910400391
          ],
          [
            "sk",
            0.000003039836883544922
          ],
          [
            "lv",
            0.0000025033950805664062
          ],
          [
            "gl",
            0.000002264976501464844
          ],
          [
            "yo",
            0.00000196695327758789
          ],
          [
            "bg",
            0.0000015497207641601562
          ],
          [
            "eu",
            0.0000015497207641601562
          ],
          [
            "et",
            0.0000015497207641601562
          ],
          [
            "hy",
            0.0000013709068298339844
          ],
          [
            "bs",
            0.0000013709068298339844
          ],
          [
            "ne",
            0.000001132488250732422
          ],
          [
            "az",
            0.000001132488250732422
          ],
          [
            "yue",
            9.5367431640625e-7
          ],
          [
            "ht",
            8.940696716308594e-7
          ],
          [
            "my",
            8.344650268554688e-7
          ],
          [
            "mr",
            5.364418029785156e-7
          ],
          [
            "af",
            4.76837158203125e-7
          ],
          [
            "sq",
            4.76837158203125e-7
          ],
          [
            "sr",
            4.172325134277344e-7
          ],
          [
            "oc",
            4.172325134277344e-7
          ],
          [
            "yi",
            4.172325134277344e-7
          ],
          [
            "mn",
            4.172325134277344e-7
          ],
          [
            "be",
            3.576278686523438e-7
          ],
          [
            "lo",
            3.576278686523438e-7
          ],
          [
            "pa",
            3.576278686523438e-7
          ],
          [
            "kk",
            3.576278686523438e-7
          ],
          [
            "fo",
            2.980232238769531e-7
          ],
          [
            "bo",
            2.980232238769531e-7
          ],
          [
            "sd",
            1.788139343261719e-7
          ],
          [
            "ps",
            1.1920928955078125e-7
          ],
          [
            "kn",
            1.1920928955078125e-7
          ],
          [
            "ka",
            5.960464477539064e-8
          ],
          [
            "gu",
            5.960464477539064e-8
          ],
          [
            "mk",
            5.960464477539064e-8
          ],
          [
            "mt",
            5.960464477539064e-8
          ],
          [
            "as",
            5.960464477539064e-8
          ],
          [
            "tg",
            0
          ],
          [
            "uz",
            0
          ],
          [
            "so",
            0
          ],
          [
            "tk",
            0
          ],
          [
            "lb",
            0
          ],
          [
            "mg",
            0
          ],
          [
            "tt",
            0
          ],
          [
            "ln",
            0
          ],
          [
            "ha",
            0
          ],
          [
            "ba",
            0
          ],
          [
            "su",
            0
          ],
          [
            "am",
            0
          ]
        ],
        "duration_after_vad": 30.07125,
        "language_probability": 0.986328125,
        "transcription_options": {
          "prefix": null,
          "best_of": 5,
          "hotwords": null,
          "patience": 1,
          "beam_size": 5,
          "temperatures": [
            0.8,
            1
          ],
          "initial_prompt": "",
          "length_penalty": 1,
          "max_new_tokens": null,
          "suppress_blank": true,
          "clip_timestamps": "0.0",
          "suppress_tokens": [
            -1
          ],
          "word_timestamps": false,
          "log_prob_threshold": -1,
          "repetition_penalty": 1,
          "without_timestamps": false,
          "append_punctuations": "\"'.。,，!！?？:：”)]}、",
          "no_speech_threshold": 0.6,
          "no_repeat_ngram_size": 0,
          "prepend_punctuations": "\"'“¿([{-",
          "max_initial_timestamp": 1,
          "condition_on_previous_text": true,
          "compression_ratio_threshold": 1.8,
          "prompt_reset_on_temperature": 0.5,
          "hallucination_silence_threshold": null
        }
      },
      "text": " And so I enter into evidence, my tarnished coat of arms,  my muses acquired like bruises, my talismans and charms,  the tick, tick, tick of love bombs, my veins of pitch black ink,  all's fair in love and poetry.  Sincerely, the chairman of the Tortured Poets Department.  The Tortured Poets Department, phantom clear vinyl, only at Target.  Subtitles by the Amara.org community",
      "segments": [
        {
          "id": 1,
          "end": 4.3,
          "seek": 3000,
          "text": " And so I enter into evidence, my tarnished coat of arms,",
          "start": 0,
          "words": null,
          "tokens": [
            50365,
            400,
            370,
            286,
            3242,
            666,
            4467,
            11,
            452,
            256,
            1083,
            4729,
            10690,
            295,
            5812,
            11,
            50580
          ],
          "avg_logprob": -0.2094006643752859,
          "temperature": 0.8,
          "no_speech_prob": 0,
          "compression_ratio": 1.6028708133971292
        },
        {
          "id": 2,
          "end": 10.2,
          "seek": 3000,
          "text": " my muses acquired like bruises, my talismans and charms,",
          "start": 5.12,
          "words": null,
          "tokens": [
            50621,
            452,
            1038,
            279,
            17554,
            411,
            25267,
            3598,
            11,
            452,
            4023,
            1434,
            599,
            293,
            41383,
            11,
            50875
          ],
          "avg_logprob": -0.2094006643752859,
          "temperature": 0.8,
          "no_speech_prob": 0,
          "compression_ratio": 1.6028708133971292
        },
        {
          "id": 3,
          "end": 15.88,
          "seek": 3000,
          "text": " the tick, tick, tick of love bombs, my veins of pitch black ink,",
          "start": 10.54,
          "words": null,
          "tokens": [
            50892,
            264,
            5204,
            11,
            5204,
            11,
            5204,
            295,
            959,
            19043,
            11,
            452,
            29390,
            295,
            7293,
            2211,
            11276,
            11,
            51159
          ],
          "avg_logprob": -0.2094006643752859,
          "temperature": 0.8,
          "no_speech_prob": 0,
          "compression_ratio": 1.6028708133971292
        },
        {
          "id": 4,
          "end": 18.22,
          "seek": 3000,
          "text": " all's fair in love and poetry.",
          "start": 16.76,
          "words": null,
          "tokens": [
            51203,
            439,
            311,
            3143,
            294,
            959,
            293,
            15155,
            13,
            51276
          ],
          "avg_logprob": -0.2094006643752859,
          "temperature": 0.8,
          "no_speech_prob": 0,
          "compression_ratio": 1.6028708133971292
        },
        {
          "id": 5,
          "end": 22.82,
          "seek": 3000,
          "text": " Sincerely, the chairman of the Tortured Poets Department.",
          "start": 19.28,
          "words": null,
          "tokens": [
            51329,
            318,
            4647,
            323,
            356,
            11,
            264,
            22770,
            295,
            264,
            48415,
            3831,
            6165,
            1385,
            5982,
            13,
            51506
          ],
          "avg_logprob": -0.2094006643752859,
          "temperature": 0.8,
          "no_speech_prob": 0,
          "compression_ratio": 1.6028708133971292
        },
        {
          "id": 6,
          "end": 27.04,
          "seek": 3000,
          "text": " The Tortured Poets Department, phantom clear vinyl, only at Target.",
          "start": 23.44,
          "words": null,
          "tokens": [
            51537,
            440,
            48415,
            3831,
            6165,
            1385,
            5982,
            11,
            903,
            25796,
            1850,
            25226,
            11,
            787,
            412,
            24586,
            13,
            51717
          ],
          "avg_logprob": -0.2094006643752859,
          "temperature": 0.8,
          "no_speech_prob": 0,
          "compression_ratio": 1.6028708133971292
        },
        {
          "id": 7,
          "end": 33,
          "seek": 3007,
          "text": " Subtitles by the Amara.org community",
          "start": 30,
          "words": null,
          "tokens": [
            50365,
            8511,
            27689,
            904,
            538,
            264,
            2012,
            2419,
            13,
            4646,
            1768,
            50515
          ],
          "avg_logprob": -0.4202356613599338,
          "temperature": 0.8,
          "no_speech_prob": 0.8740234375,
          "compression_ratio": 0.8181818181818182
        }
      ]
    }
  }
}
</code></pre>
</details></div>

## 🦺 性能测试

- 测试环境与硬件配置
  - CPU: 13th Gen Intel(R) Core(TM) i9-13950HX 24核 32线程 @ 2.20 GHz
  - GPU: NVIDIA GeForce RTX 4060 Laptop GPU
  - 内存: 64GB
  - 系统: Windows 11

> 单列模式测试

- 我们使用 `faster whisper` 模型作为引擎，然后使用 `CUDA` 进行加速。
- 使用`large-v3`作为推理模型。
- 异步模型池的最大并发数`MAX_CONCURRENT_TASKS`设置为 1。
- 使用一个时长39秒的短视频作为测试文件，连续发送5个请求，所有任务全部完成的总耗时为 32 秒。

> 并发模式测试

- 待添加。

## 📝 代办清单

- 完善爬虫模块，计划添加并支持更多平台。
- 完善任务流系统，实现一个由事件或时间驱动的自动化工作流系统。
- 添加LLM的支持，转录完成的文本可以直接用于进一步处理，如内容摘要、语义分析等，适合二次分析或文本挖掘需求。
- 优化数据库结构和数据库设计，计划对Redis进行支持，并且计划添加更多字段，数据库以后可以存放更多数据。
- 添加部署脚本，编写一个一键部署脚本方便用户使用bash快速部署本项目。
- 使用Docker容器化项目，计划添加对容器的支持，以及自动化的容器编译脚本。

## 🔧 默认配置文件

```python
import os
from typing import Optional
from dotenv import load_dotenv

# 加载 .env 文件 | Load .env file
load_dotenv()


class Settings:

    # FastAPI 设置 | FastAPI settings
    class FastAPISettings:
        # 项目名称 | Project name
        title: str = "Fast-Powerful-Whisper-AI-Services-API"
        # 项目描述 | Project description
        description: str = "⚡ A high-performance asynchronous API for Automatic Speech Recognition (ASR) and translation. No need to purchase the Whisper API—perform inference using a locally running Whisper model with support for multi-GPU concurrency and designed for distributed deployment. It also includes built-in crawlers for social media platforms like TikTok and Douyin, enabling seamless media processing from multiple social platforms. This provides a powerful and scalable solution for automated media content data processing."
        # 项目版本 | Project version
        version: str = "1.0.4"
        # Swagger 文档 URL | Swagger docs URL
        docs_url: str = "/"
        # 是否开启 debug 模式 | Whether to enable debug mode
        debug: bool = False
        # 当检测到项目代码变动时是否自动重载项目 | Whether to automatically reload the project when changes to the project code are detected
        reload_on_file_change: bool = os.getenv("RELOAD_ON_FILE_CHANGE", False)
        # FastAPI 服务 IP | FastAPI service IP
        ip: str = "0.0.0.0"
        # FastAPI 服务端口 | FastAPI service port
        port: int = 80

    # 数据库设置 | Database settings
    class DatabaseSettings:
        # 选择数据库类型，支持 "sqlite" 和 "mysql" | Select the database type, support "sqlite" and "mysql"
        # "sqlite"：适合小规模项目单机运行，无需安装数据库，直接使用文件存储数据 | "sqlite": Suitable for small-scale projects running on a single machine, no need to install a database, directly use file storage data
        # "mysql"：适合大规模项目分布式部署，需要安装 MySQL 数据库 | "mysql": Suitable for large-scale projects distributed deployment, need to install MySQL database
        # 如果你选择 "mysql"，请确保安装了 aiomysql | If you choose "mysql", please make sure aiomysql is installed
        # 如果你选择 "sqlite"，请确保安装了 aiosqlite | If you choose "sqlite", please make sure aiosqlite is installed
        db_type: str = os.getenv("DB_TYPE", "sqlite")

        # SQLite 数据库设置 | SQLite database settings
        # 数据库名字 | Database name
        sqlite_db_name: str = os.getenv("sqlite_db_name", "WhisperServiceAPI.db")
        # 数据库 URL | Database URL
        sqlite_url: str = f"sqlite+aiosqlite:///{sqlite_db_name}"

        # MySQL 数据库设置 | MySQL database settings
        # 数据库名字 | Database name
        mysql_db_name: str = os.getenv("MYSQL_DB_NAME", "")
        # 数据库用户名 | Database username
        mysql_username: str = os.getenv("MYSQL_USERNAME", "")
        # 数据库密码 | Database password
        mysql_password: str = os.getenv("MYSQL_PASSWORD", "")
        # 数据库地址 | Database host
        mysql_host: str = os.getenv("MYSQL_HOST", "")
        # 数据库端口 | Database port
        mysql_port: int = 3306
        # 数据库 URL | Database URL
        mysql_url: str = f"mysql+aiomysql://{mysql_username}:{mysql_password}@{mysql_host}:{mysql_port}/{mysql_db_name}"

    # Whisper 服务类设置 | Whisper service class settings
    class WhisperServiceSettings:
        # Whisper 服务的最大并发任务数，设置为 1 时为单任务模式 | The maximum number of concurrent tasks for the Whisper service, set to 1 for single task mode
        # 如果你有多个 GPU，可以设置大于 1，在单一 GPU 上运行多个任务无法缩短任务时间，但可以提高任务并发度 | If you have multiple GPUs, you can set it to more than 1. Running multiple tasks on a single GPU cannot shorten the task time, but can increase the task concurrency
        MAX_CONCURRENT_TASKS: int = 1
        # 检查任务状态的时间间隔（秒），如果设置过小可能会导致数据库查询频繁，设置过大可能会导致任务状态更新不及时。
        # Time interval for checking task status (seconds). If set too small, it may cause frequent database queries.
        TASK_STATUS_CHECK_INTERVAL: int = 3

    # OpenAI Whisper 设置 | OpenAI Whisper settings
    class OpenAIWhisperSettings:
        # 模型名称 | Model name
        openai_whisper_model_name: str = "large-v3"
        # 设备名称，如 "cpu" 或 "cuda", 为 None 时自动选择 | Device name, such as "cpu" or "cuda", automatically selected when None
        openai_whisper_device: Optional[str] = None
        # 模型下载根目录 | Model download root directory
        openai_whisper_download_root: Optional[str] = None
        # 是否在内存中加载模型 | Whether to load the model in memory
        openai_whisper_in_memory: bool = False

    # Faster Whisper 设置 | Faster Whisper settings
    class FasterWhisperSettings:
        # 模型名称 | Model name
        faster_whisper_model_size_or_path: str = "large-v3"
        # 设备名称，如 "cpu" 或 "cuda", 为 'auto' 时自动选择 | Device name, such as "cpu" or "cuda", automatically selected when 'auto'
        faster_whisper_device: str = "auto"
        # 设备ID，当 faster_whisper_device 为 "cuda" 时有效 | Device ID, valid when faster_whisper_device is "cuda"
        faster_whisper_device_index: int = 0
        # 模型推理计算类型 | Model inference calculation type
        faster_whisper_compute_type: str = "float16"
        # 模型使用的CPU线程数，设置为 0 时使用所有可用的CPU线程 | The number of CPU threads used by the model, set to 0 to use all available CPU threads
        faster_whisper_cpu_threads: int = 0
        # 模型worker数 | Model worker count
        faster_whisper_num_workers: int = 1
        # 模型下载根目录 | Model download root directory
        faster_whisper_download_root: Optional[str] = None

    # 异步模型池设置 | Asynchronous model pool settings
    class AsyncModelPoolSettings:
        # 引擎名称 | Engine name
        # 目前只支持 "openai_whisper" 和 "faster_whisper" | Currently only supports "openai_whisper" and "faster_whisper"
        engine: str = "faster_whisper"

        # 最小的模型池大小 | Minimum model pool size
        min_size: int = 1

        # 最大的模型池大小，如果你没有多个 GPU，建议设置为 1 | Maximum model pool size, if you don't have multiple GPUs, it is recommended to set it to 1
        # 如果你有多个 GPU，可以设置大于 1，程序会自动为每个 GPU 创建一个模型实例 | If you have multiple GPUs, you can set it to more than 1, and the program will automatically create a model instance for each GPU
        max_size: int = 1

        # 每个 GPU 最多支持的实例数量，如果你的 GPU 内存足够大，可以设置大于 1 | The maximum number of instances supported by each GPU, if your GPU memory is large enough, you can set it to more than 1
        max_instances_per_gpu: int = 1

        # 是否在模型池初始化时以最大的模型池大小创建模型实例 | Whether to create model instances with the maximum model pool size when the model pool is initialized
        init_with_max_pool_size: bool = True

    # 文件设置 | File settings
    class FileSettings:
        # 是否自动删除临时文件 | Whether to automatically delete temporary files
        auto_delete: bool = True
        # 是否限制上传文件大小 | Whether to limit the size of uploaded files
        limit_file_size: bool = True
        # 最大上传文件大小（字节）| Maximum upload file size (bytes)
        max_file_size: int = 2 * 1024 * 1024 * 1024
        # 临时文件目录 | Temporary file directory
        temp_files_dir: str = "./temp_files"
        # 是否在处理后删除临时文件 | Whether to delete temporary files after processing
        delete_temp_files_after_processing: bool = True
        # 允许保存的文件类型，加强服务器安全性，为空列表时不限制 | Allowed file types, enhance server security, no restrictions when the list is empty
        allowed_file_types: list = [
            # （FFmpeg 支持的媒体文件）| (FFmpeg supported media files)
            '.3g2', '.3gp', '.aac', '.ac3', '.aiff', '.alac', '.amr', '.ape', '.asf', '.avi', '.avs', '.cavs', '.dirac',
            '.dts', '.dv', '.eac3', '.f4v', '.flac', '.flv', '.g722', '.g723_1', '.g726', '.g729', '.gif', '.gsm',
            '.h261', '.h263', '.h264', '.hevc', '.jpeg', '.jpg', '.lpcm', '.m4a', '.m4v', '.mkv', '.mlp', '.mmf',
            '.mov', '.mp2', '.mp3', '.mp4', '.mpc', '.mpeg', '.mpg', '.oga', '.ogg', '.ogv', '.opus', '.png', '.rm',
            '.rmvb', '.rtsp', '.sbc', '.spx', '.svcd', '.swf', '.tak', '.thd', '.tta', '.vc1', '.vcd', '.vid', '.vob',
            '.wav', '.wma', '.wmv', '.wv', '.webm', '.yuv',
            # （字幕文件）| (Subtitle files)
            '.srt', '.vtt',
        ]

    # 日志设置 | Log settings
    class LogSettings:
        # 日志级别 | Log level
        """
        CRITICAL = 50
        FATAL = CRITICAL
        ERROR = 40
        WARNING = 30
        WARN = WARNING
        INFO = 20
        DEBUG = 10
        NOTSET = 0
        """
        level: int = 10
        # 日志文件目录 | Log file directory
        log_dir: str = "./log_files"
        # 日志文件前缀 | Log file prefix
        log_file_prefix: str = "app"
        # 日志文件编码 | Log file encoding
        encoding: str = "utf-8"
        # 日志文件备份数 | Log file backup count
        backup_count: int = 7

    # 抖音 API 设置 | Douyin API settings
    class DouyinAPISettings:
        # Douyin Web Cookie
        web_cookie: str = os.getenv("DOUYIN_WEB_COOKIE", "")
        # Proxy
        proxy: str = os.getenv("DOUYIN_PROXY", None)

    # ChatGPT API 设置 | ChatGPT API settings
    class ChatGPTSettings:
        # OpenAI API Key
        API_Key: str = os.getenv("OPENAI_API_KEY", "")
        # OpenAI ChatGPT Model
        GPT_Model: str = "gpt-3.5-turbo"

    # TikHub.io API 设置 | TikHub.io API settings
    class TikHubAPISettings:
        # TikHub.io API URL
        api_domain: str = "https://api.tikhub.io"
        # TikHub.io API Token
        api_key: str = os.getenv("TIKHUB_API_KEY", "")
```

## 🛡️ 许可协议

本项目基于 [Apache2.0](LICENSE) 开源。

商用以及定制合作，请联系 **Email：evil0ctal1985@gmail.com**

## 📬 联系方式

有任何问题或建议，欢迎通过 [issue](https://github.com/Evil0ctal/Fast-Powerful-Whisper-AI-Services-API/issues) 与我们联系。

## 🧑‍💻 贡献指南

非常欢迎大家提出意见和建议！可以通过 GitHub issue 与我们联系，如果希望贡献代码，请 fork 项目并提交 pull request。我们期待你的加入！💪