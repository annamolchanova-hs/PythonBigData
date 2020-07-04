"""3. Отсортировать список."""
import random
import string
from time import perf_counter


def sorting(nums: list):
    return sorted(nums)


def sorting_by_bubble(nums: list):
    n = 1
    while n < len(nums):
        for i in range(len(nums) - n):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
        n += 1
    return nums


def quicksort(nums: list):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
        s_nums = []
        m_nums = []
        e_nums = []
        for n in nums:
            if n < q:
                s_nums.append(n)
            elif n > q:
                m_nums.append(n)
            else:
                e_nums.append(n)
        return quicksort(s_nums) + e_nums + quicksort(m_nums)


if __name__ == "__main__":
    x = random.sample(range(0, 1_000_000), 1_000_000)

    t_start = perf_counter()
    sorting(x)
    t_stop = perf_counter()
    print(f" sorting list by sorted ={t_stop - t_start}")

    t_start = perf_counter()
    sorting_by_bubble(x)
    t_stop = perf_counter()
    print(f" sorting list by bubble ={t_stop - t_start}")

    t_start = perf_counter()
    quicksort(x)
    t_stop = perf_counter()
    print(f" sorting list by quicksort ={t_stop - t_start}")
