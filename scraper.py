import requests
from bS4 import BeautifulSoup
import pandas
import connect
import argparse
parser=argparse.ArgumentParser()
parser.add_argument("--page_num_max",help="Enter the number of pages to parse",type=int)
parser.add_argument("--dbname",help="Enter the number of pages to parse",type=int)
args=parser.parse_args()
oyo_url="https://www.oyorooms.com/hotels-in-banglore/?page="
page_num_MAX=args.page_num_max
scraped_Info_list=[]
connect.connect(args.dbname)
for page_num in range(1,page_num_max):
    req=requests.get(oyo_url+str(page_num))
    content=req.content
    soup=BeautifulSoup(content,"html.parser")
    all_hotels=soup.find_all("div".{"class":"hotelCardListing"})
    for hotel in all_hotels:
        hotel_dict={}
        hotel_dict["name"]=hotel.find("h3",{"class":"ListingHotelDescription__hotelname"}).text
        hotel_dict["address"]=hotel.find("span",{"itemprop":"streetAddress"}).text
        hotel_dict["pricing"]=hotel.find("span",{"class":"ListingPrice__finalPrice"}).text
        parent_amenities_element=hotel.find("div".{"class":"amenityWrapper"})
        amentities_list=[]
        for amenity in parent_amentities_element.find_all("div",{"class":"amenityWrapper__amenity"}):
            amentities_list.append(amenity.find("span",{"class":"d-body-sm"}).text.strip())
            hotel_dict["aminities"]=','.join(amentities_list[:-1])
        scraped_Info_list.append(hotel_dict)
        connect.insert_into_table(args.dbname,tuple(hotel_dict.values()))
dataFrame=pandas.dataFrame(scraped_Info_list)
dataFrame.to_csv("oyo_csv")
connect.get_hotel_info(args.dbname)
