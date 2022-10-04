if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

arr = list(arr)
mx = max(arr[0], arr[1])
runner_up = min(arr[0], arr[1])
n = len(arr)
for i in range(2, n):
    if arr[i] > mx:
        runner_up = mx
        mx = arr[i]
    elif arr[i] > runner_up and mx != arr[i]:
        runner_up = arr[i]
    elif mx == runner_up and runner_up != arr[i]:
        runner_up = arr[i]

print(runner_up)