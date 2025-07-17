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


def bubble_sort(movies):
    """
    (三) 从低到高排序
    在此阶段，您需要通过实施冒泡排序对数据进行排序。
    复杂度是O(n^2)，其中n是数据集的大小。同样，请注意您的算法执行需要多长时间。

    您的程序应执行以下操作：
    1. 比较第一个和第二个元素的评级。如果第一部电影的评分高于第二部，请交换它们;
    2. 接下来，比较第二个和第三个元素。如果第二个大于第三个，请交换它们。继续比较和交换元素，直到到达列表的最末尾;
    3. 重复上述步骤 n-1时间，其中n是元素的数量;
    4. 以示例中所示的格式打印排序的数据。

    示例 1：
    Hercules - 6.0
    The Avengers - 8.0
    The Shawshank Redemption - 9.3
    """
    n = len(movies)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if float(movies[j][1]) > float(movies[j+1][1]):
                movies[j], movies[j+1] = movies[j+1], movies[j]
    
    for title, rating in movies:
        print(f"{title} - {float(rating)}")

def main():
    file_path = 'movies.csv'
    movies = store_movies(file_path)

    # search_movies(movies, target_rating=6.0)
    bubble_sort(movies)


if __name__ == "__main__":
    main()
