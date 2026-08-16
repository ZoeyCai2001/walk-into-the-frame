# Zine 视觉配方

这些配方用于选择一张稀疏编辑海报的构图和物质语言。不要把所有配方混在一次生成里。

## 共同系统

- 作品必须独立成立，不是照片滤镜或满版风景插画；
- 默认使用平衡场景拼贴：主体 mass 约占 45–65%，安静纸面约占 30–45%；
- 只有明确要求极简时，才使用稀疏蒸馏：主体 cluster 约占 12–32%，安静纸面约占 68–85%；
- 一个主要视觉隐喻，一个主视觉语法，最多一个辅助语法；
- 默认必须有可见的纸片组装：一张主纸窗 + 2–4 个辅助层 + 边界/重叠/接缝；
- 所有模式默认使用米白/暖象牙色纸底；原照片的天空、海水或墙面不直接铺满画布；
- 场景先被拆成 2–4 个来源明确的层，再进行拼贴；
- 默认一个高饱和色彩重点；
- 人物以抽象 cameo 参与，穿搭/帽子/相机是线索，不恢复写实脸；
- 不使用照片像素、完整原构图、随机装饰、商业广告排版或长文字。

## Balanced Scene Collage｜平衡场景拼贴

这是本项目的默认配方。使用统一米白纸底，保留风景主体的主要关系，但先把场景拆成山脊/椰林/海水/沙滩或门/柱/地面等独立层，再用纸片、干墨和印刷颗粒重新组合。人物放在有明确关系锚点的位置，尺度由凳子、窗户、台阶、门、栏杆、船或路径决定，不使用固定画面比例。

```text
base: warm ivory paper, never source-colored sky or water as the full background
layers: 2–4 source-derived scene layers with independent edges
layout: related scene layers arranged inside an irregular collage field
scene_mass: 45–65% of canvas
quiet_paper: 30–45% of canvas
focal_carrier: complete architectural/landscape mass plus one abstract cameo, assembled from visible paper layers
figure_scale: relational; derive from furniture, openings, steps, rails, boats, paths, or other scale cues
edge: visible torn or cut-paper contour; at least one seam or overlap must remain readable
accent: one source-derived high-chroma hue
location_mark: optional short handwritten @Place only when user supplies a location
```

不要把主体缩成一个小窗口，也不要让人物变成角落里无法辨认的点；更不要为了遵守固定比例而破坏人物与场景的真实关系。主体可以相对完整，但必须由独立纸片层组成，不能变成无边界的连续插画。原照片的天空可以决定上方留白的形状，但最终底色仍是米白纸。

## Asymmetric Island｜不对称岛

一个偏离中心的紧凑图形岛，周围留出较多纸面。适合“人很小、场景很大”的关系，属于显式选择的稀疏蒸馏模式，不是默认模式。

```text
layout: off-center compact cluster surrounded by quiet paper
focal carrier: cut-paper mass or dry-print silhouette
edge: natural isolated contour or one irregular paper edge
accent: one high-chroma focal pin
```

人物可以只是 cluster 中的一块小剪纸，与一条路径、门缝或建筑轮廓产生关系。

## Torn Window｜撕纸窗口

用一个不规则纸边界承载主要图形，让一两个源自场景的元素穿出边界。适合门、窗、山谷、桥或被观看的空间。

```text
layout: irregular paper window with one or two forms escaping
focal carrier: broken contour plus cut-paper mass
edge: torn-fiber edge, shallow and tactile
accent: color field derived from a meaningful source detail
```

避免做成一个标准矩形照片框，也不要加入胶带和漂浮的 3D 纸张。

## Directional Drift｜方向漂移

让台阶、河流、山脊、光线或人物行进方向成为一条视觉路径，图形沿路径逐渐稀释或转向留白。

```text
layout: forms extend along a source-derived direction
focal carrier: broken contour or fragment stack
edge: stippled dissolution or natural isolated contour
accent: directional cue, not a decorative dot pattern
```

适合人物“走向某处”的记忆，但人物不能变成完整叙事插画的主角。

## Staggered Fragments｜错落碎片

由两三组不完全相连的纸片建立时间、距离或观看顺序。适合把人物、场景结构和一个物件分开再重新绑定。

```text
layout: two or three separated fragments with deliberate interval
focal carrier: fragment stack
edge: clean organic contours with light print bite
accent: bridge between fragments
```

碎片必须来自同一个命题，不要变成密集 scrapbook。

## Auxiliary Constellation｜辅助星群

当场景中有明确的可重复元素（窗格、花、树叶、石头、灯光）时，将其作为不均匀的节奏点分布在核心人物或主结构周围。

```text
layout: one core subject plus unequal source-derived supporting beats
focal carrier: dry-print silhouette or paper mass
edge: natural contour or one restrained dissolution
accent: one exact hue shared by the supporting motif
```

不要凭空制造点阵、星星、花瓣或图标；间隔和缺席本身要有意义。

## Solid Color-Block｜单色块模式

只有在用户明确写出 `单色块模式` 时使用：自然纸色 + 中性墨线/图形 + 一个连续的高饱和色块。人物和场景都必须进入统一的中性印刷系统，不能出现第二种彩色区域。

## Failure repair

| 问题 | 修复 |
| --- | --- |
| 仍像完整照片 | 删除完整背景和原构图，改为 2–4 个 source anchors |
| 仍像照片滤镜 | 明确 no photographic pixels，要求 original paper-based artwork |
| 画面太满 | 先删掉装饰和重复细节；只有用户要求极简时，才将留白提高到 68–85% |
| 留白太多、主体受损 | 切换到平衡场景拼贴，恢复 45–65% 主体 mass 和 3–5 个场景锚点 |
| 没有拼贴感 | 加入不规则主纸窗、2–4 个辅助纸片、可见接缝/重叠/断裂和外围留白；禁止连续背景 |
| 像整张插画 | 把场景限制在纸边内，减少无边界的背景延伸，保留纸张之间的空隙 |
| 底色被天空/海水染蓝 | 恢复米白纸底，将天空/海水改成单独的蓝色纸片层 |
| 元素没有分层 | 把场景拆成 2–4 个具体层，每层写清边缘、材质、前后关系和留白 |
| 拼贴很装饰化 | 删除胶带、邮票、坐标、随机圆点和第二个隐喻 |
| 地点信息缺失或错误 | 只使用用户提供的地点，写成短小手写 `@Place`；没有输入就不加 |
| 人物太写实 | 改为 dry-print silhouette 或 cut-paper mass，脸部只保留轮廓 |
| 人物太小 | 指定一个关系锚点和动作，例如坐在凳子上、从窗户探出头、站在门边或走上台阶；再按环境尺度调整人物 |
| 人景关系弱 | 增加接触、遮挡、地面支撑和一个具体动作，不要只调整人物大小 |
| 人物消失 | 增加当天服装色块、草帽、肩带、姿态和一个小 accent |
| 色彩太多 | 只保留一个 exact high-chroma hue；必要时使用单色块模式 |
| 生成无关符号 | 添加 no generic icon, no maritime symbol, no unsupported ornament |
| 文字乱码 | 默认不加文字；后期排版短标题 |
