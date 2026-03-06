def Optff(k, requests):
    capacity = k
    cache = []
    misses = 0
    m = len(requests)

    # use enumerate to reduce loops, like dict in PA1
    for idx, req in enumerate(requests):
        # check cache hit
        if req in cache:
            continue
        else:
            misses += 1

            # cache has space
            if len(cache) < capacity:
                cache.append(req)
                continue

            # cache full
            farthest = -1
            evicted = None

            # loop and keep track of the cache item that is current farthest
            # index gives next occurence of cache item in requests
            for item in cache:
                used = requests.index(item, idx+1)
                
                if used > farthest
                    farthest = used
                    evicted = item

            # update
            cache.remove(evicted)
            cache.append(req)

    return misses