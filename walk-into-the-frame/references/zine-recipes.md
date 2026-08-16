# Zine 风格配方

这份参考只在用户选择具体视觉方向，或某次生成失败需要定向修复时读取。不要把所有配方混在一条 prompt 里。

## Contents

- [共同约束](#共同约束)
- [手绘旅行明信片](#手绘旅行明信片)
- [彩铅观察稿](#彩铅观察稿)
- [纸张拼贴](#纸张拼贴)
- [线稿与限色块](#线稿与限色块)
- [Risograph / 版画](#risograph--版画)
- [Photo-relic editorial](#photo-relic-editorial)
- [失败修复](#失败修复)

## 共同约束

所有配方都应先写 scene facts，再写媒介。默认保留原场景的主要动线、空间层次和地点识别线索；人物使用同一套色板、纸张和线条，不以写实脸作为主要身份来源。

## 手绘旅行明信片

```text
medium: hand-drawn travel postcard
palette: scene-derived greens, warm paper, one muted accent
surface: visible pencil and ink marks on lightly toothy paper
edges: restrained postcard border or paper edge
composition: preserve the original travel viewpoint and main path
```

适合楼梯、街角、建筑入口和有明确方向感的场景。人物可以像旅行手记里的小插图一样出现在路径上；不要自动生成邮票、品牌或可读文字。

## 彩铅观察稿

```text
medium: colored-pencil field study
palette: limited natural palette sampled from the photo
surface: layered pencil strokes, dry texture, uneven hand pressure
edges: mostly open paper, no glossy digital gradients
composition: preserve plant rhythm, light direction and depth
```

适合植物、花草、楼梯和生活化观察。要求笔触可见，但不要把每一片叶子都画成同样清晰的图标。

## 纸张拼贴

```text
medium: tactile paper collage
palette: 3–6 paper colors plus the scene's dominant tone
surface: torn fibers, cut-paper planes, subtle cast shadows
edges: varied torn and clean-cut edges
composition: simplify into layered depth without changing the scene's spatial logic
```

适合色块和几何结构明显的场景。人物可以是一个小型剪纸形象，利用一两层纸片和自然投影与场景连接。

## 线稿与限色块

```text
medium: observational ink linework with restrained color blocks
palette: black or deep umber line, 2–4 flat scene-derived colors
surface: slightly imperfect print or notebook paper
edges: open margins and intentional blank space
composition: keep the strongest silhouette and directional line
```

适合建筑、街景、楼梯和留白丰富的照片。人物以轮廓和姿态表达，不需要面部细节。

## Risograph / 版画

```text
medium: small-edition risograph or relief-print zine
palette: two or three ink colors with warm uncoated paper
surface: visible grain, restrained ink spread, slight registration offset
edges: printed frame or imperfect ink boundary
composition: preserve the scene anchor while reducing photographic noise
```

适合怀旧、安静和出版物感。套印偏差必须轻微，不能遮蔽人物和场景关系。

## Photo-relic editorial

```text
medium: quiet editorial page built from a photo relic and hand-made marks
palette: original photo tones with one paper and one ink accent
surface: retained photographic fragment, paper grain, pencil annotation or crop mark
edges: visible crop, border, fold, or archival fragment
composition: let the original photo remain evidence while the cameo becomes an editorial decision
```

适合希望保留摄影证据感的作品。可以有少量编辑痕迹，但不要把页面变成模板化杂志封面。

## 失败修复

| 问题 | 收紧方式 |
| --- | --- |
| 变成泛化插画 | 增加 3–5 个具体场景事实，要求保留原动线和空间关系 |
| 风格混杂 | 只保留一个主媒介，删除其他风格名 |
| 人物像贴纸 | 要求人物采用相同纸张、线条、色板、阴影和遮挡；降低人物比例 |
| 人物身份太弱 | 增加发型、服装色块、相机/背包和姿态，不增加写实脸要求 |
| 人物抢主体 | 改为背影、侧影、远景或局部遮挡，恢复原始留白 |
| 画面太干净 | 增加具体的纸张颗粒、铅笔压力、撕纸纤维或轻微套印偏差 |
| 画面太脏 | 减少旧化、噪点和装饰，只保留一种材质痕迹 |
| 文字变形 | 删除自动文字，保留空白标题区；如需文字，后期排版 |
