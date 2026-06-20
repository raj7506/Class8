nums = [2, -1, 3, -4, 5, 7]
print("Full array:",nums)
print()
print("Some arrays: ")
print("[0:2]",nums[0:2], "sum=", sum(nums[0:2]))
print("[2:6]",nums[2:6], "sum=", sum(nums[2:6]))
print("[3:7]",nums[3:7], "sum=", sum(nums[3:7]))
print()

print("Running sum trace:")
running = 0
for num in nums:
    running += num
    if running < 0:
        print(f" {num} -> sum ={running} <-- egative! RUN set to 0")
        running = 0
    else:
        print(f" {num} -> sum ={running}")
print()

running = 0
best = 0
for num in nums:
    running += num
    if running < 0:
        running = 0
    if running > best:
        best = running
print("Array:", nums)
print("Max subarray sum:", best)
print()

hard = [1,2,3,-4,5,6,32,-24,51,-4]
running = 0
best = 0
for num in hard:
    running += num
    if running < 0:
        running = 0
    if running > best:
        best = running

print("Array: ",hard)
print("Max subarray sum:", best)