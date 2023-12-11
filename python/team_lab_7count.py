def count_sevens(n):
    """ 数字nに含まれる7の数をカウントする """
    return str(n).count('7')

def count_sevens_in_multiples_of_seven(max_value):
    """ 7以上max_value以下の7の倍数に含まれる7の総数をカウントする """
    count = 0
    for i in range(7, max_value + 1, 7):
        count += count_sevens(i)
    return count

# 7以上7777777以下の7の倍数に含まれる7の総数を計算
total_sevens = count_sevens_in_multiples_of_seven(7777777)
print(total_sevens)
