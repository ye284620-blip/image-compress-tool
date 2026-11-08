from PIL import Image
import os

# ===================== 配置区，自己改这里 =====================
INPUT_FOLDER = "images"    # 原图文件夹
OUTPUT_FOLDER = "output"   # 输出文件夹
MAX_WIDTH = 1920           # 最大宽度
MAX_HEIGHT = 1080          # 最大高度
JPG_QUALITY = 80           # jpg压缩质量 0~100，数字越小体积越小
# ============================================================

# 自动创建输出文件夹
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

# 支持的图片后缀
support_suffix = (".jpg", ".jpeg", ".png", ".webp")

def process_image(img_path, out_path):
    with Image.open(img_path) as img:
        # 等比例缩放，thumbnail自动保持比例
        img.thumbnail((MAX_WIDTH, MAX_HEIGHT), Image.Resampling.LANCZOS)

        # 保存判断
        suffix = os.path.splitext(img_path)[1].lower()
        if suffix in (".jpg", ".jpeg"):
            img.save(out_path, "JPEG", quality=JPG_QUALITY, optimize=True)
        elif suffix == ".png":
            img.save(out_path, "PNG", optimize=True)
        elif suffix == ".webp":
            img.save(out_path, "WEBP", quality=JPG_QUALITY)
    print(f"✅ 处理完成：{os.path.basename(img_path)}")


if __name__ == "__main__":
    count = 0
    for filename in os.listdir(INPUT_FOLDER):
        if filename.lower().endswith(support_suffix):
            in_path = os.path.join(INPUT_FOLDER, filename)
            out_path = os.path.join(OUTPUT_FOLDER, filename)
            process_image(in_path, out_path)
            count += 1
    print(f"\n🎉 全部处理完毕！一共 {count} 张图片")