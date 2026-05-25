import sys
import os

# 模拟一个本地的许可证知识库
LICENSE_DB = {
    # 宽松许可证 - MIT
    "urllib3": ("MIT", "✅  宽松许可，几乎无限制"),
    "certifi": ("MIT", "✅  宽松许可，几乎无限制"),
    "six": ("MIT", "✅  宽松许可，几乎无限制"),
    "python-dateutil": ("Apache 2.0", "✅  包含专利授权条款，商业友好"),
    "pyyaml": ("MIT", "✅  宽松许可，几乎无限制"),
    "tqdm": ("MIT / MPL-2.0", "✅  双协议，宽松许可"),
    "click": ("BSD-3-Clause", "✅  宽松许可，禁止用作者名义背书"),
    "pillow": ("HPND", "✅  类 MIT 宽松许可，历史悠久许可证"),
    "pytest": ("MIT", "✅  宽松许可，几乎无限制"),
    "beautifulsoup4": ("MIT", "✅  宽松许可，几乎无限制"),

    # 宽松许可证 - Apache 2.0
    "requests": ("Apache 2.0", "✅  包含专利授权条款，商业友好"),
    "boto3": ("Apache 2.0", "✅  包含专利授权条款，商业友好"),
    "botocore": ("Apache 2.0", "✅  包含专利授权条款，商业友好"),
    "sqlalchemy": ("MIT", "✅  宽松许可，几乎无限制"),
    "celery": ("BSD-3-Clause", "✅  宽松许可，商业友好"),

    # 宽松许可证 - BSD
    "flask": ("BSD-3-Clause", "✅  宽松许可，禁止用作者名义背书"),
    "django": ("BSD-3-Clause", "✅  宽松许可，商业友好"),
    "numpy": ("BSD-3-Clause", "✅  宽松许可，商业友好"),
    "pandas": ("BSD-3-Clause", "✅  宽松许可，商业友好"),
    "scipy": ("BSD-3-Clause", "✅  宽松许可，商业友好"),
    "matplotlib": ("PSF / BSD-style", "✅  宽松许可，商业友好"),

    # 弱传染性 - LGPL（重要：体现对弱传染性的理解）
    "chardet": ("LGPL-2.1", "⚠️  弱传染性，动态链接可闭源，但修改库本身须开源，商业项目需评估"),
    "pygments": ("BSD-2-Clause", "✅  宽松许可，几乎无限制"),

    # 强传染性 - GPL
    "gpl-lib": ("GPL-3.0", "⚠️  传染性许可证，衍生作品须以相同协议开源，商业项目需谨慎"),
    "mysqlclient": ("GPL-2.0", "⚠️  强传染性，商业项目若引入须整体开源或购买商业授权"),
}

def check_requirements(file_path):
    if not os.path.exists(file_path):
        print(f"❌ 错误: 找不到文件 '{file_path}'")
        return

    print(f"🔍 正在扫描依赖文件: {file_path}\n" + "-" * 60)

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for line in lines:
        package = line.strip().split('==')[0].lower()  # 简单提取包名
        if not package or package.startswith('#'):
            continue

        if package in LICENSE_DB:
            lic_type, risk_info = LICENSE_DB[package]
            status = "[✅ OK]" if "✅" in risk_info else "[⚠️ 注意]"
            # 格式化输出对齐
            print(f"{status:<9} {package:<15} -> {lic_type:<12} {risk_info.replace('✅', '').replace('⚠️', '').strip()}")
        else:
            print(f"[❔ 未知] {package:<15} -> ❓ 未在本地合规数据库中找到对应信息")

    print("-" * 60 + "\n🎯 扫描完成！请注意：本工具仅供合规参考，不构成法律意见。")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("💡 用法: python license_checker.py <requirements.txt路径>")
    else:
        check_requirements(sys.argv[1])