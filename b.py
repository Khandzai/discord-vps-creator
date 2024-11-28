import gdown

# URL file Google Drive (thay đổi từ dạng "view" sang "uc" để gdown hoạt động)
url = "https://computernewb.com/isos/windows/Win11_23H2_English_x64v2.iso"

# Đường dẫn lưu file sau khi tải
output = "/mnt/win11.zip"  # Đường dẫn đầy đủ nơi lưu file

# Tải file
gdown.download(url, output, quiet=False)

print(f"File đã được tải về và lưu tại: {output}")

