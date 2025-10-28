import numpy as np
# do not change the code in the block below
# __________start of block__________
class DummyMatch:
    def __init__(self, queryIdx, trainIdx, distance):
        self.queryIdx = queryIdx  # index in des1
        self.trainIdx = trainIdx  # index in des2
        self.distance = distance
# __________end of block__________


def match_key_points_numpy(des1: np.ndarray, des2: np.ndarray) -> list:
    """
    Match descriptors using brute-force matching with cross-check.

    Args:
        des1 (np.ndarray): Descriptors from image 1, shape (N1, D)
        des2 (np.ndarray): Descriptors from image 2, shape (N2, D)

    Returns:
        List[DummyMatch]: Sorted list of mutual best matches.
    """
    # YOUR CODE HERE
    # получается в каждом пикселе есть дескриптор - вектор.
    # попарно сравниваем все дескрипторы, лучшую пару запоминаем.
    # дистанцию между векторами считаем типа sum(abs(vec1 - vec2))
    matches = []

    # matches_1 = []
    # matches_2 = [DummyMatch(0, 0, 10**20) for _ in range(des2.shape[0])]

    # for des1_idx in range(des1.shape[0]):
    #     min_distance = 10**20
    #     best_match = None

    #     for des2_idx in range(des2.shape[0]):
    #         distance = np.sum(np.abs(des1[des1_idx] - des2[des2_idx]))
            
    #         if distance < min_distance:
    #             min_distance = distance
    #             best_match = DummyMatch(des1_idx, des2_idx, distance)
            
    #         # LLM подсказала, что не хватает cross-check
    #         if distance < matches_2[des2_idx].distance:
    #             matches_2[des2_idx] = DummyMatch(des1_idx, des2_idx, distance)

    #         # if distance == 0:
    #         #     print("идеальный мэтч!")
    #         #     break
    #     matches_1.append(best_match)
    
    # # cross-check
    # for match_1 in matches_1:
    #     match_2 = matches_2[match_1.trainIdx]
    #     if match_1.trainIdx == match_2.queryIdx:
    #         matches.append(match_1)

    # matches.sort(key=lambda m: m.distance)


    # Тест не проходит, слишком мало мэтчей.
    # ниже фулл ллм решение


    # Step 1: For each descriptor in des1, find best match in des2 (L2)
    best_1to2 = []
    for i in range(des1.shape[0]):
        diff = des2 - des1[i]           # (N2, D)
        dists = np.sum(diff**2, axis=1)  # L2 squared distances
        j = np.argmin(dists)
        best_1to2.append((i, j, np.sqrt(dists[j])))  # store real distance

    # Step 2: For each descriptor in des2, find best match in des1 (L2)
    best_2to1 = {}
    for j in range(des2.shape[0]):
        diff = des1 - des2[j]           # (N1, D)
        dists = np.sum(diff**2, axis=1)
        i = np.argmin(dists)
        best_2to1[j] = i

    # Step 3: Cross-check
    for i, j, dist in best_1to2:
        if best_2to1[j] == i:
            matches.append(DummyMatch(queryIdx=i, trainIdx=j, distance=dist))

    # Sort matches by distance (smallest first)
    matches.sort(key=lambda m: m.distance)
    return matches
