import os
import sys
from faker import Faker
import aiohttp
import asyncio

# Add project root to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)

from src.configurations.conf import Config



async def user_service(url,id,session):
        user_service_url = url+"/users"+"/"+str(id)
        print(user_service_url)
        async with session.get(user_service_url) as response:
            if response.status == 200:
                user_data=await response.json()
                user_data= {
                    "id": user_data["id"],
                    "name": user_data["name"],
                    "email": user_data["email"]

                }
                return user_data
            else:
                print(f"failde to fetch the user data. status code :{response.status}")
                return None

async def posts_service(url,id, session):
        posts_service_url = url+"/posts"+"/"+str(id)
        print(posts_service_url)
        async with session.get(posts_service_url) as response:
            if response.status == 200:
                posts_data=await response.json()
                posts_data= {
                    "userId": posts_data["userId"],
                    "id": posts_data["id"],
                    "title": posts_data["title"],
                    "body": posts_data["body"]

                }
                return posts_data
            else:
                print(f"failed to fetch the post data. status code :{response.status}")
                return None


async def album_service(url,id,session):
        album_service_url = url+"/albums"+"/"+str(id)
        print(album_service_url)
        async with session.get(album_service_url) as response:
            if response.status == 200:
                album_data=await response.json()
                album_data= {
                    "userId": album_data["userId"],
                    "id": album_data["id"],
                    "title": album_data["title"]

                }
                return album_data
            else:
                print(f"failed to fetch the album  data. status code :{response.status}")
                return None

async def photos_service(url,id,session):
        photos_service_url = url+"/photos"+"/"+str(id)
        print(photos_service_url)
        async with session.get(photos_service_url) as response:
            if response.status == 200:
                photos_data=await response.json()
                photos_data= {
                    "albumId": photos_data["albumId"],
                    "id": photos_data["id"],
                    "title": photos_data["title"],
                    "url": photos_data["url"],
                    "thumbnailUrl": photos_data["thumbnailUrl"]


                }
                return photos_data
            else:
                print(f"failed to fetch the photos data. status code :{response.status}")
                return None


async def dashboard(url):
    async with aiohttp.ClientSession() as session:
        user_data,posts_data,album_data,photos_data=await asyncio.gather(
            user_service(url,1,session),
            posts_service(url,1,session),
            album_service(url,1,session),
            photos_service(url,1,session),
        )
if __name__=="__main__":
    conf=Config()
    print(conf.url)
    try:
        result=asyncio.run(dashboard(conf.url))
        print(result)
    except aiohttp.ClientError as e:
        print(f"HTTP error has occured: {e}")
    except Exception as e:
        print(f"An error occured: {e}")

