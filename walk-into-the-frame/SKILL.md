---
name: walk-into-the-frame
description: "Turn a photographer's scene photo and self-portrait into an original, sparse editorial zine poster. Distil the photos into a semantic nucleus, emotional proposition, visual metaphor, paper collage, abstract photographer cameo, generous negative space, and deliberate color accent; do not preserve photographic pixels or the full original composition. Use for scene-distillation, minimal zine, hand-made collage, paper poster, risograph, cut-paper, or authored editorial reinterpretations."
---

# Walk Into The Frame

把摄影者放回自己的记忆里，但不把照片原样搬进 zine。

这个 skill 的默认产物是一张**独立成立的、稀疏的编辑性 zine 海报**。场景照片提供语义和情绪证据，人物照片提供当天的穿搭、轮廓和参与线索；最终图像重新组织这些信息，不保留原照片像素，不照搬完整构图，也不做“照片加滤镜”。

## Core contract

每次生成都必须从以下链条开始：

```text
source facts → emotional residue → artistic proposition → central tension
→ visual metaphor → paper-based composition → photographer cameo
```

先决定作品要让观众感受到什么，再决定如何画。不要堆叠“彩铅、拼贴、版画、电影感、复古”等风格名；选择一个主视觉语法，最多加一个辅助语法。

## Request routing

选择满足请求所需的最小模式：

- **Generate**：主题/照片/一句话 → 视觉命题 → prompt → 生成海报 → 检查。
- **Photo Input**：用户照片会影响结果 → 为每张图指定角色和保留等级 → 使用真实输入生成 → 检查来源关系。
- **Reference Analysis**：用户只要求学习参考图 → 输出固定规则、可变规则、样本残留和可复用 prompt，不生成图。
- **Prompt-only**：用户明确只要 prompt 时才使用，不要暗示已经生成图。
- **Analyze + Generate**：用户说“参考这些风格并做一张”时，先做参考分析，再生成一张全新的构图。

如果用户已经明确说“做一张”，不要因为风格仍有选择空间而停下来；自行选择最符合场景的方案，并在结果中说明。

## 1. Assign image roles

先查看所有图片，再决定角色。对于本项目的两张照片，默认这样处理：

| 输入 | 角色 | 默认保留 |
| --- | --- | --- |
| 风景/人文照片 | semantic scene reference | 中：默认保留主要场景结构和 3–5 个锚点；只有明确要求极简时才大幅拆散构图 |
| 摄影者照片 | supporting person reference | 中：保留当天穿搭、帽子、发型、体态、相机/肩带等线索；脸部默认抽象 |

只有用户明确要求“保留原照片内容或原人物身份”时，才提高保留等级。人物不是必须被精确抠出的真人素材，而是一个将“我曾经在这里”变成视觉事件的 cameo。

## 2. Build a distillation card

不要在没有分析的情况下直接写风格 prompt。先内部整理：

- **Semantic nucleus**：照片最核心的主体、关系或事件；
- **Core subject**：最多一个主要主体，必要时加一个不可分开的对象；
- **Supporting elements**：1–3 个建立地点、季节、动作或气氛的元素；
- **Dominant gesture**：最强的方向、路径、重复、凝视、倾斜或汇聚；
- **Spatial cue**：只保留一个重要的近远、上下、包围、重叠或朝向关系；
- **Native palette**：主色温度、明暗范围和有意义的次要颜色；
- **Material/weather**：木头、石头、水、雾、植物、布料、阳光、风等；
- **Emotional residue**：去掉事实描述后仍然留下的感觉；
- **Discard list**：应消失的杂物、重复细节、写实信息和无关背景；
- **Transformation opportunity**：哪些形状可以放大、合并、切碎、重复、偏移或变成留白。

平衡场景拼贴默认保留 3–5 个 source anchors，以及建筑、台阶、路径或主体之间的主要关系；不要把有识别力的场景压缩成一个无关的抽象符号。只有选择“稀疏蒸馏”模式时，才只保留 2–4 个 anchors 并大幅重排空间。

## 3. Choose one artistic proposition

写一句具体的内部命题，让视觉选择围绕它服务。命题应来自照片中的关系，而不是泛泛的“治愈、梦幻、怀旧”。例如：

- 一个很小的人，面对一座无法一次看完的建筑；
- 入口既像邀请，也像一道暂时的边界；
- 穿过风景的人只留下服装的颜色和一条行进方向；
- 被阳光照亮的日常建筑，像一段尚未关闭的记忆。

再选择一个主要张力：`smallness / vastness`、`movement / stillness`、`visibility / concealment`、`warmth / distance`、`order / growth` 等。不要叠加多个互不相关的主题。

## 4. Turn the scene into an authored collage

将原照片变成**原创纸面构成**，而不是完整的插画化风景。允许：

- 改变比例、裁切、间隔、方向和元素位置；
- 删除大部分写实背景，只保留暗示地点的形状；
- 将台阶、门、树、光、影、水或路径变成色块、线条、纸片或节奏场；
- 让元素穿过撕纸边界、断裂、漂移或互相遮挡；
- 使用一个源自照片的视觉隐喻，而不是添加通用装饰符号。

每个新增元素都必须完成至少一个任务：延伸情绪、说明关系、建立节奏、平衡重量、引导视线或强化隐喻。不要为了“看起来像设计”而自动加入邮票、坐标、胶带、十字、网格、随机圆点或装饰性英文。

## 5. Compose with proportion and negative space

默认使用 **Balanced Scene Collage｜平衡场景拼贴**，因为本项目需要让摄影者和原地点都可读。只有用户明确说“极简、稀疏、大片留白、单色块海报”时，才使用 **Sparse Distillation｜稀疏蒸馏**。

两种模式的比例规则：

| 模式 | 主体/active mass | 安静纸面 | 场景保留 |
| --- | --- | --- | --- |
| 平衡场景拼贴（默认） | 约 `45–65%` 画面 | 约 `30–45%` | 主要结构相对完整，保留 3–5 个锚点 |
| 稀疏蒸馏（显式选择） | 约 `12–32%` 画面 | 约 `68–85%` | 只保留 2–4 个锚点，允许大幅重排 |

两种模式都默认保留原照片方向：横向约 `5:3`，纵向约 `3:5`。平衡模式可以保留建筑门面、台阶、植物或路径的整体关系，但必须将摄影纹理转译为纸张、印刷、线稿或拼贴；它不是满版照片，也不是简单滤镜。

构图仍可使用不对称岛、撕纸窗口、方向漂移、错落碎片或辅助星群，但要先满足主体与人物的比例关系。视线要有入口、主要相遇、运动方向和出口，不要习惯性居中。

## 6. Translate the photographer into a cameo

人物不是海报主角，而是一个**可读但不喧宾夺主**的视觉线索。平衡场景拼贴中，人物不能小到只剩装饰点；默认使用画面高度的 `12–16%`，并根据前后景和台阶/建筑尺度调整。只有用户明确要求“若隐若现”时，才降到 `6–10%`。优先使用以下语法之一：

- **cut-paper mass**：由草帽、外套、裤子和肩带组成的几块不规则纸片；
- **dry-print silhouette**：只保留背影、姿态和服装色块；
- **broken contour**：用断裂线条表达行走、观看或持相机的方向；
- **fragment stack**：人物只以两三块重叠纸片出现在路径或门前；
- **rhythm field**：人物被拆成小轮廓，与台阶、门格或植物节奏呼应。

从人物照片提取当天的视觉线索：帽子、发型、米色外套、黑色内搭、浅色裤子、相机或肩带等。默认不生成写实脸，不追求脸部像素级相似；如果用户要求本人辨识度，优先强化服装、轮廓、姿态和物件，而不是恢复写实人脸。

人物的面积应小于主要场景 mass，但必须能在缩略图中被识别为一个人在场；应与场景共享同样的纸张、线条、印刷颗粒、色板和边缘。不能像贴纸、独立卡通或摄影抠图。

## 7. Select one visual grammar and one color decision

主视觉语法从以下方向中选择一个，最多加一个辅助方向：

- cut-paper collage；
- dry-print / risograph silhouette；
- broken ink contour；
- colored-pencil fragment；
- photo-relic editorial，但最终仍不能保留写实照片像素。

默认使用 **Standard Accent Mode**：纸张和大部分图形保持低饱和，选择一个具有明确功能的高饱和色，作为 focal pin、counterweight、bridge、directional cue 或 rhythmic beat。高饱和区域约占整张海报 `0.8–3%`，不要变成多色装饰。

如果用户明确写出 `单色块模式`，切换为 **Solid Color-Block Mode**：

1. 自然纸色；
2. 统一的炭黑/石墨/暖灰印刷系统；
3. 一个连续、饱和、不可拆分的色块。

除此之外不使用其他彩色区域。

## 8. Typography and surface

文字不是默认必需品。没有用户提供的准确文字时，优先不生成可读文字；如果文字能强化命题，可以使用极短的标题、碎片或作者性标记，但必须说明它在画面中的视觉作用。不要生成长段落、品牌、日期、坐标、伪造地点或不可控的中文正文。

纸张、撕边、干墨、铅笔颗粒、丝网印刷偏差和扫描痕迹必须承担构图或情绪功能，不能全部同时出现。避免 glossy、3D、电影灯光、卡通、动漫、儿童绘本、商业广告和密集 scrapbook。

## 9. Prompt contract

图像生成 prompt 按五段编写，只写最终图像中会成为可见像素的内容：

```text
Expression: [艺术命题、主要张力、视觉隐喻、留下的解释空间]
Canvas: [3:5 or 5:3, composition mode, paper tone, quiet-space share, active mass size and eye path]
Distillation: [semantic nucleus, 2–4 preserved anchors, what disappears, transformation]
Cameo and color: [photographer's clothing/objects translated into an abstract cameo;
figure height as a percentage of frame; one visual grammar; one accent hue or solid color-block rule]
Reproduction and avoids: [paper/print material and explicit no-photo constraints]
```

必须包含：

```text
Use the supplied photos only as semantic and visual references.
Do not reproduce, embed, crop, collage, trace, or retain photographic pixels.
Do not preserve the full original composition or create photorealistic regions.
The final image must be an original paper-based editorial artwork.
```

## 10. Generate and inspect

使用实际输入图片生成，不要只根据文字描述猜测照片内容。若所有输入都有本地路径，使用多图 reference 输入，并明确标记每张图的角色。

生成后在缩略图和原尺寸检查：

- 图像是否像一张独立的 zine 海报，而不是照片滤镜；
- 所选模式的主体 mass、留白和场景结构是否成立；
- 人物是否在约 12–16% 的默认比例内清楚可读，但没有成为主体；
- 人物的穿搭线索是否保留，但是否已经被同一媒介抽象；
- 是否只有一个主要色彩重点；
- 是否出现原照片像素、写实脸、贴纸边缘、随机装饰、伪造文字、水印或 UI；
- 是否出现与照片无关的通用图标、船锚、邮戳、坐标、网格等元素。

如果失败，最多针对一个问题再生成一次：

- 太像完整照片：减少摄影纹理，转译为纸片/干墨/线稿，但不要继续缩小主体；
- 主体太碎：切换到平衡场景拼贴，恢复 3–5 个 source anchors 和主要结构；
- 留白过多：将安静纸面收回到 30–45%，把主体 mass 提高到 45–65%；
- 太像滤镜照片：加入“no photographic pixels”，要求 paper-based original illustration；
- 人物太小：明确 `12–16% of frame height`，放到有尺度参照的台阶、门前或路径上；
- 人物太写实：改为 cut-paper mass 或 dry-print silhouette，降低 face preservation；
- 人物太大：降低到 10–12%，改为背影或自然遮挡；
- 人物消失：增加帽子、外套、肩带、姿态和一个小的高饱和 accent；
- 画面太装饰：删除随机符号和第二个视觉隐喻；
- 颜色失控：明确唯一 accent hue 或触发 `单色块模式`。

## Return format

生成请求默认返回：

1. 生成的 raster zine poster；
2. 最终 image-generation prompt；
3. 选中的 recipe；
4. 一段中文创作想法：命题、张力、隐喻和留白如何工作；
5. 简短艺术指导：场景角色、人物角色、保留锚点、舍弃内容和质量检查。

不要默认输出视频 prompt。只有用户明确进入视频阶段时，才基于已经确认的 zine 海报编写轻微的纸张、植物、光影或局部人物动效。
