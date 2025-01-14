from icrawler.builtin import BingImageCrawler

# キーワードリスト
keywords = ["富士山", "富士", "Fuji", "Mount Fuji"]

# 保存先フォルダ（共通フォルダ）
output_folder = "Fuji_Images"

# BingImageCrawlerのインスタンスを生成
crawler = BingImageCrawler(storage={"root_dir": output_folder})

# 各キーワードで画像を収集し、同じフォルダに保存
for keyword in keywords:
    print(f"'{keyword}'の画像を収集中...")
    crawler.crawl(keyword=keyword, max_num=100)
print("すべての画像収集が完了しました！")
