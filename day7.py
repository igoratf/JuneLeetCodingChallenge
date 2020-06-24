def sortColors(nums):
    color_map = {
            
        }
    c_min = float("inf")
    ans = []
    
    for i in nums:
        if i not in color_map:
            color_map[i] = 1
        else:
            color_map[i] += 1
    
    while bool(color_map):
        c_min = min(color_map.keys())
        ans += [c_min] * color_map[c_min]
        del color_map[c_min]
    
    print(ans)

sortColors([2,0,2,1,1,0])
        