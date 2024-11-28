import gdown

# URL file Google Drive
url = "https://computernewb.com/isos/windows/Win10_22H2_English_x64.iso"

# Đường dẫn lưu file sau khi tải
output = "/mnt/win10.zip"  # Đổi tên file tùy ý

# Tải file
gdown.download(url, output, quiet=False)

print(f"File đã được tải về và lưu tại: {output}")
