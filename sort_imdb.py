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
import csv

def sort_movies(file_path):
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
    
def main():
    file_path = 'movies.csv'
    movies = sort_movies(file_path)

    # 打印结果
    for title, rating in movies:
        print(f"{title} - {rating}")


if __name__ == "__main__":
    main()
