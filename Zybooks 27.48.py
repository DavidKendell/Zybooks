def FirstRectangleSmaller(r1xul :int, r1yul :int, r1xbr :int, r1ybr :int, r2xul :int, r2yul :int, r2xbr :int, r2ybr :int) -> bool:
    area1 = abs(r1xbr - r1xul) * abs(r1ybr - r1yul)
    area2 = abs(r2xbr - r2xul) * abs(r2ybr - r2yul)
    return area1 < area2

r1xul, r1yul, r1xbr, r1ybr, r2xul, r2yul, r2xbr, r2ybr = [int(input()) for i in range(8)]
print(FirstRectangleSmaller(r1xul, r1yul, r1xbr, r1ybr, r2xul, r2yul, r2xbr, r2ybr))