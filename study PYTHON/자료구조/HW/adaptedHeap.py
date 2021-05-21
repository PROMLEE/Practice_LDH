class AdaptedHeap:  # min_heap으로 정의함!
    def __init__(self):
        self.A = []
        self.D = {}  # dictionary D[key] = index

    def __str__(self):
        return str(self.A)

    def __len__(self):
        return len(self.A)

    def insert(self, key):
        # key값이 최종 저장된 index를 리턴한다!
        self.A.append(key)
        self.D[key] = len(self.A)-1
        self.heapify_up(len(self.A)-1)
        return self.D[key]

    def heapify_up(self, k):
        # code here : key 값의 index가 변경되면 그에 따라 D 변경 필요
        while k > 0 and self.A[(k-1)//2] > self.A[k]:
            self.A[k], self.A[(k-1)//2] = self.A[(k-1)//2], self.A[k]
            self.D[self.A[k]], self.D[self.A[(k-1)//2]] = self.D[self.A[(k-1)//2]], self.D[self.A[k]]
            k = (k-1)//2

    def heapify_down(self, k):
        # code here : key 값의 index가 변경되면 그에 따라 D 변경 필요
        n = len(self.A)
        while 2*k + 1 < n:
            L, R = 2*k + 1, 2*k + 2
            if L < n and self.A[L] < self.A[k]:
                m = L
            else:
                m = k
            if R < n and self.A[R] < self.A[m]:
                m = R
            if m != k:
                self.A[k], self.A[m] = self.A[m], self.A[k]
                self.D[self.A[k]], self.D[self.A[m]] = self.D[self.A[m]], self.D[self.A[k]]
                k = m
            else:
                break

    def find_min(self):
        # 빈 heap이면 None 리턴, 아니면 min 값 리턴
        if len(self.A) == 0:
            return None
        else:
            return self.A[0]

    def delete_min(self):
        # 빈 heap이면 None리턴, 아니면 min 값 지운 후 리턴
        if len(self.A) == 0:
            return None
        else:
            v = self.A[0]
            self.A[0], self.A[len(self.A)-1] = self.A[len(self.A)-1], self.A[0]
            self.D[self.A[0]], self.D[self.A[len(self.A)-1]] = self.D[self.A[len(self.A)-1]], self.D[self.A[0]]
            self.A.pop()
            del self.D[v]
            self.heapify_down(0)
            return v

    def update_key(self, old_key, new_key):
        # old_key가 힙에 없으면 None 리턴
        # 아니면, new_key 값이 최종 저장된 index 리턴
        try:
            index = self.D[old_key]
            self.A[index] = new_key
            self.D[new_key] = index
            del self.D[old_key]
            if self.A[index] < self.A[(index-1)//2]:
                self.heapify_up(index)
            else:
                self.heapify_down(index)
            index = self.D[new_key]
            return index
        except KeyError:
            return None

