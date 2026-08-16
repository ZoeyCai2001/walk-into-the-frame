---
name: walk-into-the-frame
description: "Transform a photographer's scene photo and self-portrait into a cohesive zine-style still image, preserving the scene's visual facts while abstracting the photographer into a small, meaningful participant. Use when the user wants a hand-drawn postcard, colored-pencil, paper-collage, editorial, risograph, or related image treatment; add motion prompts only when separately requested."
---

# Walk Into The Frame

把摄影者轻轻放回自己的照片里，但先把照片变成一张属于她的 zine。

这个 skill 的默认产物是**一张静态 zine 图像**，不是写实合成图，也不是视频。它把原照片当作事实锚点，把人物照片当作身份和参与感的参考，再用同一套视觉语言重编排二者。

## Core idea

不要把人物像贴纸一样叠在背景上，也不要把真实人脸强行保留下来。先回答三个问题：

1. **这个场景最重要的事实是什么？** 例如楼梯向上的动线、植物的密度、建筑入口、光线方向、画面中的留白。
2. **这个 zine 选择什么视觉语法？** 例如彩铅的线条、明信片的边框、拼贴的纸张层次、版画的限色和套印偏差。
3. **人物如何以最少的信息表达“我曾在场”？** 优先使用轮廓、发型、服装、相机、背包、姿态和位置；除非用户明确要求，不依赖清晰人脸。

参考 `gathered-scenes-zine-skill` 的工作方式：先观察场景，再提取关系，再选择创作路径，最后重新绑定为一张页面。照片提供事实，创作决定保留什么以及如何呈现。

## Workflow

### 1. Inspect the two images

先查看两张输入图，不要立即写泛化风格 prompt。

对场景图记录：

- 构图方向、主体动线、前中后景和可用留白；
- 3–5 个不可丢失的场景事实；
- 主色、辅助色、明暗关系和材质线索；
- 原照片中已有的人、动物、文字和标识；
- 适合放置人物的尺度与位置。

对人物图只记录生成所需的稳定信息：

- 轮廓、身形、发型、服装色块和配件；
- 摄影者身份线索，例如相机、背包或观看姿态；
- 哪些特征可以保留，哪些细节应被抽象掉。

不要把人物照片理解为必须被精确抠出的真人素材。它是人物“在这张 zine 里如何出现”的参考。

### 2. Distill the scene before styling it

把输入照片拆成两层：

- **Scene facts**：地点感、空间关系、主要结构、天气/光线、已有内容；
- **Treatment choices**：媒介、纸张、边缘、色彩数量、细节密度、是否保留摄影纹理。

默认保留场景的识别性，不随意换地点、移动建筑、删除关键植物或制造新的主角。可以简化细节，但不能让 zine 变成与原照片无关的泛化插画。

### 3. Choose a visual recipe

如果用户指定了风格，严格执行其媒介和情绪；如果没有指定，从场景事实中选择最合适的一种，并在结果说明中写明理由。

推荐优先顺序：

- **手绘旅行明信片**：适合有明确路径、建筑或旅行记忆的照片；保留构图，加入纸张边缘、简洁标题区域或邮戳感，但不要自动添加不可读的文字。
- **彩铅观察稿**：适合植物、楼梯、街角等有丰富纹理的场景；用可见笔触、分层排线和有限纸色，避免塑料感的数字渐变。
- **纸张拼贴**：适合色块、建筑几何和强烈前后景；使用撕纸/剪纸边缘、轻微重叠、阴影和错位，但保持原场景的空间关系。
- **线稿 + 限色块**：适合建筑、街景和留白较多的画面；保留关键轮廓，以 2–5 个主色块完成编辑化重构。
- **Risograph / 版画**：适合安静、怀旧、出版物感的作品；使用少量油墨色、纸张颗粒、轻微套印偏差，不要过度脏旧。
- **Photo-relic editorial**：适合想保留摄影证据感的作品；让原照片的局部纹理成为纸面遗物，再用手工标记、裁切和小人物建立叙事。

每次选择风格时，明确一份短的 visual grammar：

```text
medium: [彩铅 / 拼贴 / 线稿 / 版画 / 编辑设计]
palette: [主色、辅助色、纸张色；尽量有限]
surface: [纸张、铅笔颗粒、油墨、撕纸纤维]
edges: [自然保留 / 手撕 / 印刷边界 / 明信片边框]
detail_density: [低 / 中 / 高]
composition_rule: [保留原构图 / 重新裁切但保留空间关系]
```

### 4. Abstract the photographer

人物必须和场景使用同一套媒介、线条重量、纸张纹理、色彩和阴影逻辑。

默认策略：

- 人物是小比例的 cameo，不是海报主角；
- 优先背影、侧影、远景、局部遮挡或非写实脸部；
- 保留 2–4 个有辨识度的线索，不要堆叠所有照片细节；
- 人物的服装颜色可以成为场景调色板中的一个小回声；
- 让人物与地面、台阶、椅子、栏杆或植物产生真实的接触/遮挡关系；
- 不添加第二个“类似用户”的人物，不把人物放大成肖像海报。

除非用户明确要求，禁止把人物重新生成成写实高清人像。风格化的目标不是消除身份，而是把身份转译成轮廓、姿态和少量物件。

### 5. Compose the final still

当图像工具支持多图输入时，标记输入角色：

- `scene image / primary visual anchor`
- `person image / identity and presence reference`

优先一次完成“场景风格化 + 人物风格化 + 融合”。如果人物身份或位置不稳定，分两步：先生成场景 zine base，再把人物作为同媒介的小型 cameo 加入；第二步仍必须引用场景 zine base，而不是回到原始照片上贴真人。

Prompt 必须同时写清楚四件事：

1. 原场景哪些事实不可改变；
2. 选择的媒介和 visual grammar；
3. 人物在哪里、以多大比例、用哪些身份线索出现；
4. 哪些内容明确禁止出现。

不要把多个风格名无差别堆进同一条 prompt。一个主媒介，加 1–2 个材质修饰，通常比“水彩、彩铅、油画、拼贴、电影感、3D”混合更稳定。

### 6. Quality gate

生成后同时看缩略图和原尺寸，检查：

- 场景仍然能被认出，至少 3 个核心事实被保留；
- 人物属于同一张 zine，而不是写实贴图或独立插画；
- 人物存在感足够表达“我在这里”，但没有抢走场景的主叙事；
- 线条、色彩、纸张纹理、阴影和边缘处理统一；
- 人物的脚、椅子、台阶、栏杆和植物之间没有悬空或穿模；
- 没有诡异脸部、额外肢体、重复人物、错误文字、水印或 UI；
- 原照片中的文字/标识如被保留，应尽量保持原有形状，不生成伪造的可读文字。

失败时按问题收紧，而不是笼统地要求“更好”：

- 场景漂移：增加不可改变的场景事实，减少风格形容词；
- 人物不像：减少脸部要求，增加轮廓、发型、服装、相机和姿态线索；
- 人物太突出：降低比例、改为背影/侧影并增加自然遮挡；
- 风格不统一：重复同一媒介、纸张、线条重量和限色规则；
- 画面太满：恢复原构图和留白，不增加装饰性元素。

### 7. Return format

默认返回：

1. 最终 zine 静态图；
2. 一段简短的场景提炼说明；
3. 所选 visual grammar；
4. 人物如何被抽象和放置；
5. 保留与主动舍弃的内容；
6. 如有需要，给出 2–3 个风格变体方向。

不要默认输出视频 prompt。只有用户明确进入第二阶段时，才基于已确认的 zine 静帧编写运动 prompt；视频只负责纸张、植物、光影、人物小动作等克制变化，不重新设计人物或场景。

## Prompt contract

使用以下顺序组织图像生成/编辑 prompt：

```text
Scene facts: [必须保留的地点、构图、空间关系、光线和 3–5 个视觉事实]
Zine medium: [一个主媒介]
Visual grammar: [有限色板、纸张/笔触/油墨、边缘、细节密度]
Scene treatment: [如何把照片提炼成页面，同时保留可识别性]
Photographer cameo: [人物位置、比例、朝向、姿态、2–4 个身份线索]
Integration: [人物与场景共享的线条、材质、阴影、色彩和遮挡]
Composition: [保留原构图或说明有限重排；人物不要成为主角]
Guardrails: [no photorealistic face, no pasted-on cutout, no extra people,
no location replacement, no surreal anatomy, no invented readable text,
no watermark, no UI]
```

## Input defaults

- `scene_image`: 必需；是空间与事实锚点。
- `person_image`: 必需；用于提取人物的稳定外观线索，不要求生成写实脸。
- `style`: 可选；未指定时由场景决定并说明理由。
- `mood`: 可选；例如安静、旅行手记、怀旧、观察性、轻微幽默。
- `participation`: 可选；未指定时选择不抢主体的动作或姿态。
- `aspect_ratio`: 默认保留原图；只有用户要求时才改成海报或社交媒体比例。
- `variants`: 默认 1 张；用户要求探索时再输出 2–3 个方向。
- `motion_prompt`: 默认不输出，除非用户明确进入视频阶段。

## References

需要具体风格配方或失败修复时，读取 [zine-recipes.md](references/zine-recipes.md)。

视频工具和 Live Photo 只属于后续阶段；需要做供应商选择时，再读取 [video-tools.md](references/video-tools.md)，并把已确认的 zine 静帧作为视频输入。
