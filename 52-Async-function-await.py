import time
import asyncio
import requests


async def greet():
    url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRQsG2nW7NUOrbFDf2BpxBsW91ZWFYSn8P277jzr1Ogvw&s=10"
    
    respoce = requests.get(url)
    open("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRQsG2nW7NUOrbFDf2BpxBsW91ZWFYSn8P277jzr1Ogvw&s=10").write(respoce.content)
    await asyncio.sleep(2)
    print("Hello Hisaan how are you!")

async def greet2():
    url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRPvy85joQgHZCMdoYumqzr7mO_VOu0CVeFKpvYPZT66g&s=10"

    respoce = requests.get(url)
    open("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRPvy85joQgHZCMdoYumqzr7mO_VOu0CVeFKpvYPZT66g&s=10").write(respoce.content)
    await asyncio.sleep(2)
    print("Hello Hisaan how are you!")

async def greet3():
    url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQifiA2DtKfMYlwoLZOQjPOBnH0EKkSPHKVAW2WJhppog&s=10"
    
    respoce = requests.get(url)
    open("vhttps://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQifiA2DtKfMYlwoLZOQjPOBnH0EKkSPHKVAW2WJhppog&s=10").write(respoce.content)
    await asyncio.sleep(2)
    print("Hello Hisaan how are you!")

# async def main2():
#     await asyncio.gather(greet(), greet2(), greet3())

async def main():
    await greet()
    await greet2()
    await greet3()

# asyncio.run(main())
# asyncio.run(main2())



async def sqrt(n):
    await asyncio.sleep(3)
    return n * n

async def result():

    output = await asyncio.gather(sqrt(5), sqrt(4))  
    
    print("The square of 5 is", output[0])
    print("The square of 4 is", output[1])


asyncio.run(result())