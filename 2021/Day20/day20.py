import copy

with open('C:\\input.txt') as file:
    enhanceStr = file.readline().rstrip()
    image = [[c for c in line.rstrip()] for line in file.readlines() if len(line.rstrip()) > 0]

lightPixel = '#'
darkPixel = '.'

def DefaultPixel(enhanceStr, step):
    if enhanceStr[0] == darkPixel:
        return darkPixel
    else:
        return lightPixel if step % 2 != 0 else darkPixel

def ExpandImage(image, step):
    pixel = DefaultPixel(enhanceStr, step)
    newRow = [pixel for _ in range(len(image[0]))]
    image.insert(0, newRow)
    image.append(newRow[:])
    for rowIdx in range(len(image)):
        image[rowIdx].insert(0, pixel)
        image[rowIdx].append(pixel)

def EnhancePixel(pixelPos, image, enhanceStr: str, step):
    checkPos = [(pixelPos[0] + r, pixelPos[1] + c ) for r, c in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]]
    pixelStr = ''
    for pos in checkPos:
        if pos[0] < 0 or pos[0] >= len(image) or pos[1] < 0 or pos[1] >= len(image[pos[0]]):
            pixelStr += DefaultPixel(enhanceStr, step)
        else:
            pixelStr += image[pos[0]][pos[1]]
    binStr = pixelStr.replace(darkPixel, '0').replace(lightPixel, '1')
    return enhanceStr[int(binStr, 2)]

def Enhance(image, enhanceStr: str, step):
    enhanceImage = copy.deepcopy(image)
    for rowIdx in range(len(image)):
        for colIdx in range(len(image[rowIdx])):
            enhanceImage[rowIdx][colIdx] = EnhancePixel((rowIdx, colIdx), image, enhanceStr, step)
    return enhanceImage

def CountLightPixel(image):
    counter = 0
    for row in image:
        counter += row.count(lightPixel)
    return counter


for step in range(50):
    ExpandImage(image, step)
    image = Enhance(image, enhanceStr, step)
    if step == 1:
        totalLightPixelPt1 = CountLightPixel(image)
totalLightPixel = CountLightPixel(image)
print(f'Part 1 sol: {totalLightPixelPt1}')
print(f'Part 2 sol: {totalLightPixel}')
