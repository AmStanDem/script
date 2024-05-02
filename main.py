import math

if __name__ == '__main__':

    def calculate_total_area(arr: [], height):
        result = 0
        for ab, p, fig in arr:
            if fig == 'prisma':
                result += 2 * ab + p * height
            if fig == 'semisfera':
                r = p / (2 * math.pi)
                result += (4 * math.pi * r * r)/2
        return result

    def calculate_volume(arr: [], height):
        result = 0
        for ab, p, fig in arr:
            if fig == 'prisma':
                result += ab * height
            if fig == 'semisfera':
                r = p / (2 * math.pi)
                result += (4 * (math.pi * math.pow(r, 3)) / 3)/2
        return result

    h = 20
    arrLeft = \
        [
            [282.4, 71.71, 'prisma'],
            [3410.18, 323.93, 'prisma'],
            [620.26, 103.7, 'prisma'],
            [417.87, 87.42, 'prisma'],
            [1703.17, 169.62, 'prisma'],
            [295.27, 72.6, 'prisma'],
            [820.09, 115.59, 'prisma'],
        ]

    arrCenter = \
        [
            [402.36, 80.44, 'prisma'],
            [524.62, 105.94, 'prisma'],
            [247.6, 64.74, 'prisma'],
            [167.58, 54.99, 'prisma'],
            [772.81, 111.55, 'prisma'],
            [486.71, 96.8, 'prisma'],
            [114.24, 42.88, 'prisma'],
            [304.03, 76.58, 'prisma'],
            [1393.24, 201.23, 'prisma'],
            [275.64, 108.87, 'prisma'],
            [62.48, 31.7, 'prisma'],
            [152.4, 54.18, 'prisma'],
            [110.39, 42.28, 'prisma'],
            [81.9, 37.53, 'prisma'],
            [67.64, 43.29, 'prisma'],
            [431.2, 89.94, 'prisma'],
            [626.17, 111.72, 'prisma'],
            [2048.7, 208.72, 'prisma']
        ]

    arrRight = \
        [
            [146.06, 53.25, 'prisma'],
            [271.62, 69.4, 'prisma'],
            [549.71, 94.13, 'prisma'],
            [40.57, 25.97, 'prisma'],
            [222.2, 60.53, 'semisfera'],
            [901.51, 149.23, 'prisma'],
            [537.03, 93.27, 'prisma'],
            [495.61, 95.76, 'prisma'],
            [156.81, 62.59, 'prisma'],
            [1765.92, 185, 'prisma'],
            [182.96, 84.33, 'prisma'],
            [584.24, 100.51, 'prisma'],
            [1814.41, 195.14, 'prisma']
        ]

    stLeft = calculate_total_area(arrLeft, h) - ((2 * 282.4 + 71.71 * h) - (2 * 247.6 + 64.74 * 20))
    vLeft = calculate_volume(arrLeft, h)
    stCenter = calculate_total_area(arrCenter, h)
    vCenter = calculate_volume(arrCenter, h)
    stRight = calculate_total_area(arrRight, h) - ((2 * 2048.7 + 20 * 208.72) - (2 * 146.06 + 53.25 * 20))
    vRight = calculate_volume(arrRight, h)

    print(stLeft)
    print(vLeft)
    print(stCenter)
    print(vCenter)
    print(stRight)
    print(vRight)


