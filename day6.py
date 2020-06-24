def reconstructQueue(people):
        queue = []        

        sorted_h = sorted(people, key=lambda p: (p[0], -p[1]), reverse=True)

        for i in range(len(sorted_h)):
            h, k = sorted_h[i]
            queue.insert(k, [h, k])
        
        return queue
