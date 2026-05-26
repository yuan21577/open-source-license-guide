# SBOM 快速入门



## 1. 什么是 SBOM？

**SBOM（Software Bill of Materials，软件物料清单）** 是描述软件组成成分的结构化文档，相当于软件的"配料表"。

在现代软件开发中，绝大多数代码由开源组件构成。SBOM 完整记录了应用程序中包含的所有第三方组件及其关键信息：

- **直接依赖**：开发者显式引入的库
- **传递依赖**：直接依赖所依赖的其他组件（即"依赖的依赖"）
- **组件元数据**：版本号、作者信息、许可证类型、构建时间等

SBOM 为软件的**透明度、可追溯性和安全性**提供了基础支持。

---

## 2. 为什么 SBOM 对安全与合规至关重要？

SBOM 的价值体现在三类角色上：

- **对于开发者**：提供清晰的项目依赖关系，帮助快速定位和修复漏洞
- **对于用户/企业**：提供软件组件的详细信息，帮助评估潜在的安全风险
- **对于监管机构**：是确保软件合规性和安全性的重要工具

**典型场景一：安全漏洞快速响应**

2021年 Log4Shell 漏洞（CVE-2021-44228，CVSS评分10.0）爆发时，拥有完整 SBOM 的团队可以在数分钟内定位自己哪些项目受影响；而没有 SBOM 的团队往往需要数天甚至数周的人工排查。讽刺的是，当时许多开发团队甚至不知道自己的应用是否使用了 Log4j。

**典型场景二：许可证合规审查**

通过 SBOM 自动排查项目中是否混入了具有"传染性"的 GPL 许可证，避免商业代码被迫开源的法律风险。这正是本项目 `license_checker.py` 所模拟的核心功能。

**政策背景**

美国国家电信和信息管理局（NTIA）已明确将 SBOM 列为软件组件透明度计划的核心要素，要求关键软件供应商提供标准格式的 SBOM 文件。

---

## 3. 主流 SBOM 标准对比

目前业界主要有三种标准格式：

### 3.1 SPDX（Software Package Data Exchange）

- **主导方**：Linux 基金会
- **核心侧重**：知识产权（许可证）合规
- **主要功能**：
  - 组件信息管理：记录组件名称、版本、作者等基本信息
  - 许可证合规性检查：支持生成详细的许可证报告
  - 源文件信息记录：能够记录组件的源文件信息（如 `hasFile`），便于追踪组件来源
- **适用场景**：需要详细记录组件来源和许可证信息的项目；常用于企业级软件的合规性审计和供应链管理

### 3.2 CycloneDX

- **主导方**：OWASP
- **核心侧重**：安全漏洞和供应链组件分析
- **主要功能**：
  - 组件依赖管理：记录软件的直接依赖和传递依赖，生成层次化的依赖关系图
  - 许可证管理：自动识别组件的许可证信息，帮助用户规避开源许可证风险
  - 安全漏洞检测：与 Dependency-Track 等工具集成，支持安全漏洞的快速溯源和修复
- **支持格式**：XML、JSON 等
- **适用场景**：适用于 Java、Python、JavaScript 等语言的项目；常用于开源软件的安全合规性检查和供应链管理

### 3.3 SWID（Software Identification Tags）

- **主导方**：ISO / NIST
- **核心侧重**：软件资产管理与生命周期追踪
- **主要功能**：
  - 在软件安装、补丁、卸载等生命周期中动态管理标签
  - 定义了四种标签类型（Primary、Patch、Corpus、Supplemental）
  - 被 TCG、IETF 等多个标准组织采纳
- **适用场景**：需要对软件安装情况进行精准识别和生命周期管理的项目

### 三种标准横向对比

| 维度 | SPDX | CycloneDX | SWID |
|------|------|-----------|------|
| 主导方 | Linux 基金会 | OWASP | ISO/NIST |
| 核心侧重 | 许可证合规 | 安全漏洞分析 | 资产生命周期管理 |
| 输出格式 | JSON、XML、TV | JSON、XML | XML |
| 漏洞信息 | 有限支持 | 强支持 | 不支持 |
| 许可证信息 | 强支持 | 支持 | 不支持 |
| 适用阶段 | 开发/审计 | 开发/运行 | 部署/运维 |

---

## 4. SBOM 核心字段（以 CycloneDX 格式为例）

根据课程内容，一份完整的 SBOM 应包含以下核心字段：

| 类别 | 字段 | 描述 | 示例 |
|------|------|------|------|
| 组件信息 | 组件名称 | 组件的唯一标识符 | `requests` |
| 组件信息 | 版本号 | 遵循语义版本控制规则 | `2.26.0` |
| 组件信息 | 作者/维护者 | 组件的开发者或维护团队 | `Kenneth Reitz` |
| 组件信息 | 许可证信息 | 组件的开源许可证类型 | `Apache-2.0` |
| 组件信息 | 唯一标识符 | 如 PURL（Package URL） | `pkg:pypi/requests@2.26.0` |
| 依赖关系 | 直接依赖 | 项目显式引入的组件 | `pkg:pypi/urllib3@1.26.7` |
| 依赖关系 | 传递依赖 | 直接依赖所依赖的其他组件 | `pkg:pypi/charsetsnormalizer@2.0.7` |
| 构建信息 | 构建工具 | 使用的构建工具 | `pip` |
| 构建信息 | 构建时间 | 构建发生的时间戳 | `2023-10-01T12:00:00Z` |
| 安全信息 | 已知漏洞 | 组件中已知的安全漏洞（CVE编号） | `CVE-2021-33503` |
| 安全信息 | 漏洞修复状态 | 漏洞是否已修复 | `patched` |
| 安全信息 | 风险评分 | 基于漏洞严重性（CVSS评分） | `CVSS: 7.5 (High)` |

---

## 5. SPDX 格式示例

如果将本仓库的依赖生成 SBOM，其 SPDX JSON 格式核心片段如下：

```json
{
  "spdxVersion": "SPDX-2.3",
  "dataLicense": "CC0-1.0",
  "name": "open-source-license-guide-SBOM",
  "documentNamespace": "https://github.com/yuan21577/open-source-license-guide",
  "packages": [
    {
      "name": "requests",
      "versionInfo": "2.28.1",
      "licenseDeclared": "Apache-2.0",
      "copyrightText": "Copyright 2022 Kenneth Reitz",
      "downloadLocation": "https://pypi.org/project/requests/"
    },
    {
      "name": "flask",
      "versionInfo": "2.2.2",
      "licenseDeclared": "BSD-3-Clause",
      "downloadLocation": "https://pypi.org/project/flask/"
    },
    {
      "name": "chardet",
      "versionInfo": "4.0.0",
      "licenseDeclared": "LGPL-2.1",
      "copyrightText": "Copyright 2015 Mark Pilgrim",
      "downloadLocation": "https://pypi.org/project/chardet/"
    }
  ]
}
```

## 6. CycloneDX 格式示例

CycloneDX 相比 SPDX 更侧重安全漏洞信息，其 JSON 格式核心片段如下：

```json
{
  "bomFormat": "CycloneDX",
  "specVersion": "1.4",
  "metadata": {
    "timestamp": "2024-01-01T00:00:00Z",
    "tools": [{ "name": "pip", "version": "23.0" }],
    "component": {
      "name": "open-source-license-guide",
      "version": "1.0.0",
      "licenses": [{ "license": { "id": "MIT" } }]
    }
  },
  "components": [
    {
      "name": "requests",
      "version": "2.28.1",
      "purl": "pkg:pypi/requests@2.28.1",
      "licenses": [{ "license": { "id": "Apache-2.0" } }]
    },
    {
      "name": "chardet",
      "version": "4.0.0",
      "purl": "pkg:pypi/chardet@4.0.0",
      "licenses": [{ "license": { "id": "LGPL-2.1" } }],
      "vulnerabilities": [
        {
          "id": "CVE-XXXX-XXXX",
          "ratings": [{ "score": 5.3, "severity": "medium" }]
        }
      ]
    }
  ]
}
```

---

## 7. 主流 SBOM 生成工具

| 工具 | 开发方 | 特点 | 适用场景 |
|------|--------|------|----------|
| **Black Duck** | Synopsys | 支持475,000+开源项目、2000+许可证知识库，片段级和文件级扫描 | 企业级合规审计 |
| **Dependency-Track** | OWASP | 开源，支持SBOM上传与分析，自动识别组件已知漏洞，与 CycloneDX 深度集成 | 开源项目漏洞持续监控 |
| **网安云 SBOM 管理平台** | 网安云 | 遵循SPDX、CycloneDX等国际标准，支持全面SBOM梳理与安全风险溯源 | 国内合规环境 |
| **syft** | Anchore | 开源，支持多种语言和容器镜像，可生成 SPDX 和 CycloneDX 格式 | 容器安全 |
| **pip-licenses** | — | 轻量级Python工具，快速生成Python项目的许可证清单 | Python项目快速检查 |

---

## 8. 参考资料

- [NTIA Software Bill of Materials](https://www.ntia.gov/page/software-bill-materials)
- [SPDX 官方规范](https://spdx.dev/)
- [CycloneDX 官方规范](https://cyclonedx.org/)
- [OWASP Dependency-Track](https://dependencytrack.org/)
- [Black Duck SCA](https://www.blackduck.com/)