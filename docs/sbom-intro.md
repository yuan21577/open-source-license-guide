# SBOM 快速入门

## 1. 什么是 SBOM？
**SBOM (Software Bill of Materials)** 相当于软件的“配料表”。在现代软件开发中，绝大多数代码由开源组件构成。SBOM 记录了应用程序中包含的所有第三方组件、版本号、依赖关系以及**对应的许可证信息**。

## 2. 为什么 SBOM 对安全与合规至关重要？
- **安全漏洞响应：** 当类似 Log4j 的高危漏洞爆发时，企业可以通过 SBOM 瞬间定位自己哪些项目受影响。
- **许可证合规：** 自动排查项目中是否混入了具有“传染性”的 GPL 许可证，避免商业代码被迫开源的法律风险。
*(对应课程知识点：软件供应链安全与开源合规审查)*

## 3. 主流 SBOM 标准
目前业界主要有两种标准格式：
- **SPDX (Software Package Data Exchange):** 由 Linux 基金会主导，侧重于**知识产权（许可证）合规**。
- **CycloneDX:** 由 OWASP 主导，侧重于**安全漏洞和供应链组件分析**。

## 4. SPDX 极简示例
如果我们将本仓库的 `license_checker.py` 的依赖生成 SBOM，其 SPDX JSON 格式的核心片段如下：

```json
{
  "spdxVersion": "SPDX-2.3",
  "dataLicense": "CC0-1.0",
  "name": "My-Python-Project-SBOM",
  "packages": [
    {
      "name": "requests",
      "versionInfo": "2.28.1",
      "licenseDeclared": "Apache-2.0",
      "copyrightText": "Copyright 2022 Kenneth Reitz"
    },
    {
      "name": "flask",
      "versionInfo": "2.2.2",
      "licenseDeclared": "BSD-3-Clause"
    }
  ]
}
```