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
    
    return movies
    # for title, rating in movies:
    #     print(f"{title} - {float(rating)}")


def binary_search(movies, target_rating=6.0):
    """
    (四) 二分搜索
    在此阶段，您需要实施二分搜索算法并打印评分为 6 的电影。

    要完成此阶段，您的程序应执行以下操作：
    1. 以排序后的数据收集为例，添加以下变量：low = 0 和 high = n - 1，
    其中 n 是集合中的元素数，用于存储第一个和最后一个元素的索引;
    2. 检查集合中 middle 元素的评级。如果等于 6，则打印电影标题和其他标题;
    3. 如果评分小于 6，则设置低 = 中 + 1。它应该在每次迭代中完成;
    4. 如果评级大于 6，则设置高 = 中 - 1。从步骤 2 开始重复该过程。

    示例 1：
    Hercules - 6.0
    The Fast and the Furious: Tokyo Drift - 6.0
    Finding You - 6.0
    """
    low = 0
    high = len(movies) - 1
    found = False  # 标记是否找到至少一个目标评分
    
    while low <= high:
        mid = (low + high) // 2
        mid_rating = float(movies[mid][1])
        
        if mid_rating == target_rating:
            found = True
            # 向左找到评分相同的第一个位置（左边界）
            left_index = mid
            while left_index >= 0 and float(movies[left_index][1]) == target_rating:
                left_index -= 1
            left_index += 1  # 回到第一个等于目标评分的索引
            
            # 向右找到评分相同的最后一个位置（右边界）
            right_index = mid
            while right_index < len(movies) and float(movies[right_index][1]) == target_rating:
                right_index += 1
            
            # 打印评分相同的所有电影
            for i in range(left_index, right_index):
                print(f"{movies[i][0]} - {float(movies[i][1])}")
                
            break  # 已找到所有目标评分电影，退出循环
            
        elif mid_rating < target_rating:
            low = mid + 1
        else:
            high = mid - 1
    
    if not found:
        print(f"没有找到评分为 {target_rating} 的电影")


def merge(left, right):
    """
    合并两个已排序的子列表。
    """
    merged = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if float(left[i][1]) <= float(right[j][1]):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    # 添加剩余元素
    while i < len(left):
        merged.append(left[i])
        i += 1
    while j < len(right):
        merged.append(right[j])
        j += 1
    
    return merged


def merge_sort(movies):
    """
    (五) 归并排序
    通过组合冒泡排序和二叉搜索算法，您可以在很大程度上加快搜索速度，但使用冒泡排序对输入数据进行排序仍然需要很多时间。
    在此阶段，您将通过实施归并排序来进一步降低总时间复杂度。排序后，像上一阶段一样实现二分搜索。

    您的程序应执行以下操作：
    1. 取未排序的数据，将集合分为两部分;
    2. 使用合并排序算法对左侧部分进行排序。将子部分进一步划分为相等的部分，直到只剩下一个元素并合并它们;
    3. 使用 merge sort 算法对正确的部分进行排序。将子部分进一步划分为相等的部分，直到只剩下一个元素并合并它们;
    4. 通过比较元素 （ratings） 来合并生成的 left 和 right 集合，并形成一个排序的集合;
    5. 对集合进行排序后，应用二进制搜索并打印评级为 6 的电影标题。

    示例 1：
    Hercules - 6.0
    The Fast and the Furious: Tokyo Drift - 6.0
    Finding You - 6.0
    """
    if len(movies) <= 1:
        return movies
    
    mid = len(movies) // 2
    left_half = merge_sort(movies[:mid])
    right_half = merge_sort(movies[mid:])
    
    return merge(left_half, right_half)

def main():
    file_path = 'movies.csv'
    movies = store_movies(file_path)

    # search_movies(movies, target_rating=6.0)
    movies = merge_sort(movies)
    binary_search(movies, target_rating=6.0)


if __name__ == "__main__":
    main()
