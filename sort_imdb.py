import csv


def store_movies(file_path):
    """
    (一) 存储数据
    1. 读取movies.csv逗号分隔的数据文件的每一行。第一部分是电影片名，第二部分是对应的电影评分;
    2. 以您喜欢的格式存储数据。最终输出中不应有引号，因此请确保电影标题中没有引号;
    3. 打印数据，用 ' - ' 分隔标题和评级，如示例所示。另起一行打印每个影片。
    提示： 使用 encoding=UTF-8 从文件中读取数据。

    示例 1：
    The Shawshank Redemption - 9.3
    The Avengers - 8.0
    """
    movies = []
    
    # 读取CSV文件
    with open(file_path, mode='r', encoding='UTF-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) >= 2:
                title = row[0].strip().replace('"', '')  # 去除引号
                rating = row[1].strip()
                movies.append((title, rating))
    
    return movies


def search_movies(movies, target_rating=6.0):
    """
    (二) 线性搜索
    下一步是对上一阶段的结果集执行线性搜索。实施线性搜索算法，以查找评分为 6 的电影。

    在此阶段，您的程序应执行以下步骤：
    1. 迭代数据;
    2. 检查每个元素的评分是否等于 6;
    3. 如果是，请打印电影标题和评级，如上一阶段所示。确保将 ratings 转换为 float。

    示例 1： 
    Hercules - 6.0
    The Fast and the Furious: Tokyo Drift - 6.0
    Finding You - 6.0
    """
    for title, rating in movies:
        if float(rating) == target_rating:
            print(f"{title} - {float(rating)}")


def main():
    file_path = 'movies.csv'
    movies = store_movies(file_path)

    search_movies(movies, target_rating=6.0)


if __name__ == "__main__":
    main()
