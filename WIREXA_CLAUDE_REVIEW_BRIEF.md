# WIREXA 网站设计评审简报

本文件用于转交 Claude 或其他模型做二次评审。请重点评估是否有助于获得第一个海外 WhatsApp 咨询，而不是追求功能完整。

## 1. 项目定位

项目名称：WireHarness_Global_V1

当前品牌展示：

- 主品牌：WIREXA
- 小字：Wire Processing Solutions
- 公司名：WIREXA TECH
- WhatsApp：+86 180 6628 2233
- Email：WhatsApp support available
- 域名：暂未确定，代码里仍保留 `wirexatech.com`

唯一核心目标：

获得第一个海外 WhatsApp 咨询。

当前阶段：

MVP 验证阶段，不是完整品牌站阶段，也不是复杂内容平台阶段。

## 2. 技术边界

当前网站是纯静态站：

- HTML / CSS / 少量本地 JS
- 无后端
- 无数据库
- 无登录
- 无框架
- 不依赖 CDN
- 适合部署到 Cloudflare Pages、Netlify、宝塔静态站、普通虚拟主机

请不要建议：

- AI 客服
- 数据库
- 后台管理系统
- React / Next.js / Docusaurus / Nextra
- 图片识别
- 复杂统计系统
- 大规模重构

## 3. 当前页面结构

核心页面：

- `index.html`：首页
- `products.html`：产品中心
- `contact.html`：联系页
- `help-center.html`：统一导航式帮助中心
- `selector.html`：60 秒选型问卷
- `404.html`：简单 404 页面

产品页：

- `product-wire-stripping-machine.html`：通用自动电脑剥线机页面
- `product-808-series.html`：FY-808 系列
- `product-806cn-wire-stripping-twisting-machine.html`：806CN 剥线扭线机
- `product-880-series.html`：FY-880 系列重型剥线机
- `product-terminal-crimping-machine.html`：FY-4T 伺服端子压接机

故障文章：

- `fault-feeding-error.html`
- `fault-blade-replacement.html`
- `fault-stripping-length.html`
- `fault-wire-damage.html`
- `fault-length-inconsistent.html`

采购指南：

- `guide-how-to-choose.html`
- `guide-automatic-vs-manual.html`
- `guide-ev-harness.html`
- `guide-blade-selection.html`

轻量多语言入口：

- `index-ru.html`
- `index-pt.html`
- `contact-ru.html`
- `contact-pt.html`

注意：RU/PT 当前只是轻量入口，不是完整多语言站。

## 4. 当前视觉和信任设计

视觉风格：

- 工业风
- 深色背景
- 橙色主色调
- 产品图为真实机器图
- 卡片圆角控制在 8px 左右
- 页面底部保留 WhatsApp 悬浮按钮

信任增强：

- 顶部品牌统一为 WIREXA，避免顶部直接放很长公司名
- 小字保留公司主体，提高可信度
- 首页保留 `20+ Years Experience`
- 未确认真实性的数字已改为更稳妥表达，例如 `Machines Delivered Worldwide`
- Contact 页面直接显示 WhatsApp 和 Email
- Cases 页面已改为 `Typical Wire Harness Equipment Applications`，避免暗示真实客户案例

## 5. 当前产品入口逻辑

当前产品入口：

```text
任意页面导航 Products
    ↓
products.html
    ↓
FY-808 / 806CN / FY-880 Series / FY-4T
    ↓
产品详情页
    ↓
WhatsApp
```

Products 页面当前第一屏重点展示：

1. FY-808 Series Automatic Wire Stripping Machine
2. 806CN Wire Stripping & Twisting Machine
3. FY-880 Series Heavy Wire Stripping Machine
4. Servo Terminal Crimping Machine (FY-4T)

通用剥线机概览页仍保留入口，未删除。

## 6. 当前视频状态

视频目录：

- `video-ready/808-single-wire-branded-v2.mp4`
- `video-ready/808-single-wire-branded.mp4`
- `video-ready/806cn-branded.mp4`
- `video-ready/880a-branded.mp4`
- `video-ready/880c2-branded.mp4`
- `video-ready/880d-branded.mp4`

首个公开视频候选：

- `808-single-wire-branded-v2.mp4`
- 720x1280
- 约 26 秒
- 片尾已替换真实 WhatsApp：+86 180 6628 2233

当前待执行链路：

```text
YouTube Public 808 Video
    ↓
product-wire-stripping-machine.html Video 1 iframe
    ↓
WhatsApp
```

当前还未嵌入 YouTube，因为等待 YouTube embed URL。

## 7. 当前运营策略变化

最初有 90 天大内容路线图，但现在已重新收敛为 MVP 验证：

未来 7 天只做：

1. 808 第一个 YouTube Public 视频
2. 将 808 YouTube embed URL 嵌入产品页 Video 1
3. 做 Wire Damage 第一篇强转化内容

暂缓：

- 806CN 视频
- 880 系列视频
- FY-4T 视频
- Pull Force
- Crimp Quality
- 大规模 Technical Knowledge
- 多语言扩展

核心判断：

```text
故障痛点
    ↓
可信视频
    ↓
解决方案文章
    ↓
产品推荐
    ↓
WhatsApp
```

这条链路可能比单纯“产品页 -> 询盘”更容易获得第一个真实咨询。

## 8. 内容栏目规划

已有栏目：

- Products
- Fault Solutions
- Buying Guides
- Machine Selector
- Cases / Applications
- Videos
- Contact

未来建议栏目：

### Technical Knowledge

长期栏目，偏技术解释：

- Crimp Quality
- Wire Damage
- Blade Selection
- Pull Force
- Harness Defects

### Real Factory Tips

更有信任感的栏目，偏真实工厂经验：

- How We Adjust Blade Depth to Avoid Wire Damage
- How We Process Silicone Wire Without Cutting the Core
- How We Choose Guide Tubes for Different Wire Sizes
- How We Check Roller Pressure Before Production
- How We Confirm Blade Type from Wire Samples

当前建议优先做 `Real Factory Tips` 风格内容，因为竞争小、信任感强、贴近真实客户问题。

## 9. 已知风险和不足

1. 域名仍未确定
   - `wirexatech.com` 仍保留在 canonical、OG URL、sitemap、robots 中。

2. YouTube embed 尚未接入
   - `product-wire-stripping-machine.html` 有两个 iframe 占位。
   - Video 1 计划嵌入 808 视频。
   - Video 2 暂时保留占位。

3. RU/PT 不是完整多语言站
   - 目前只作为入口页和联系页。
   - 产品页、故障页、指南页仍是英文。

4. FY-4T 素材较弱
   - 有主图。
   - 缺运行视频。
   - 缺压接样品图。

5. 880D 静态图不足
   - 有视频。
   - 缺独立产品静态图。

6. 内容不要铺太开
   - 当前最危险的是把 90 天计划当成 7 天计划。
   - 现在应优先跑通第一条询盘链路。

## 10. 希望 Claude 重点审查的问题

请 Claude 不要做大而全建议，而是围绕以下问题给优化意见：

1. 首页当前是否足够直接地引导客户进入 WhatsApp 咨询？
2. Products 第一屏的四个产品排序是否合理？
3. WIREXA 作为主品牌、公司名作为小字，是否比直接展示公司全称更适合外贸询盘？
4. `Typical Wire Harness Equipment Applications` 的措辞是否足够稳妥，是否还会让客户误解为真实案例？
5. 当前语言入口 `EN / RU / PT` 指向轻量首页，是否清楚，是否会造成客户期待完整多语言？
6. 808 第一个公开视频接入产品页后，页面是否还需要一个更强的 WhatsApp CTA？
7. Wire Damage 作为第一篇强转化内容是否正确？
8. `Real Factory Tips` 是否比传统 Technical Knowledge 更适合当前阶段？
9. 哪些内容应该继续暂缓，避免分散精力？
10. 如果目标只有“第一个海外 WhatsApp 咨询”，下一步最小动作是否应该继续锁定 808 + Wire Damage？

## 11. 请 Claude 遵守的评审边界

请不要建议新增：

- 后端
- 数据库
- 登录
- AI 客服
- 复杂 CRM
- 完整多语言站
- 大型内容管理系统
- 前端框架重构

请优先建议：

- 更强的询盘路径
- 更可信的页面文案
- 更清晰的产品优先级
- 更适合 YouTube 描述和封面的话术
- 更适合 Wire Damage 内容转化的页面结构
- 能在 7 天内完成的最小动作

## 12. 当前最小下一步

当前最小执行顺序：

1. 上传 `808-single-wire-branded-v2.mp4` 到 YouTube，先 Unlisted 检查，再 Public。
2. 拿到 YouTube embed URL。
3. 只修改 `product-wire-stripping-machine.html` 的 Video 1 iframe。
4. 检查产品页视频播放和 WhatsApp 按钮。
5. 写第一篇 Wire Damage / Real Factory Tips 风格文章。
6. 进入数据观察：YouTube 播放、网站访问、WhatsApp 点击。

核心 KPI：

1. 第一个海外 WhatsApp 咨询
2. 10 个 YouTube 订阅
3. 100 个 Google 访问

内容数量不是当前第一 KPI。
