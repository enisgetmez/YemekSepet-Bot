#!/usr/bin/env python
# coding: utf-8
from bs4 import BeautifulSoup
import urllib
from urllib.request import urlopen
import json as JSON
from  openpyxl import *



linktxt = open("linkler.txt" , "r")
linkler = linktxt.readlines() ## türk takımları
print(linkler)



kitap = Workbook() # excell olustur
kitap.create_sheet("veriler") # excellde bu takım adında bi sheet olustur
yaz = kitap.get_sheet_by_name("veriler") #  takım adında olusturulan sheete gir


for i in range(len(linkler)):
	adres = linkler[i]
	url = ("https://www.yemeksepeti.com/istanbul/"+adres)
	sayfa = urllib.request.urlopen(url)
	soup = BeautifulSoup(sayfa, "html.parser")

	soupp = soup.encode("utf-8")
	veri = soup.find_all('span', {'data-tooltip': True})
	for item in veri:
		c = item['data-tooltip']
		json = JSON.loads(c) 
		Areaname = json['AreaName']
		CatalogName = json['CatalogName']
		CategoryName = json['CategoryName']
		ClosedByParent = json['ClosedByParent']
		CuisineNameList = json['CuisineNameList']
		DeliveryFee = json['DeliveryFee']
		DeliveryTime = json['DeliveryTime']
		DisplayName = json['DisplayName']
		Flavour = json['Flavour']
		HasDVDPromotion = json['HasDVDPromotion']
		ImagePath = json['ImagePath']
		ImageFullPath = json['ImageFullPath']
		ImageLabelListFullPath = json['ImageLabelListFullPath']
		IsOpen = json['IsOpen']
		IsRestaurantOpen = json['IsRestaurantOpen']
		MainCuisineId = json['MainCuisineId']
		MainCuisineLabelName = json['MainCuisineLabelName']
		MainCuisineName = json['MainCuisineName']
		MinimumDeliveryPrice = json['MinimumDeliveryPrice']
		OpenRestaurantCount = json['OpenRestaurantCount']
		PaymentMethodsText = json['PaymentMethodsText']
		PaymentMethodsList = json['PaymentMethodsList']
		#PromotionText = json['PromotionText']
		Serving = json['Serving']
		Slug = json['Slug']
		Speed = json['Speed']
		WorkHoursText = json['WorkHoursText']
		AvgPoint = json['AvgPoint']
		ServingText = json['ServingText']
		SpeedText = json['SpeedText']
		FlavourText = json['FlavourText']
		AvgRestaurantScore = json['AvgRestaurantScore']
		MinimumDeliveryPriceText = json['MinimumDeliveryPriceText']
		HasCampusDiscount = json['HasCampusDiscount']
		IsFreezoneRestaurant = json['IsFreezoneRestaurant']
		HasPromotion = json['HasPromotion']
		SuperDelivery = json['SuperDelivery']
		print(Areaname)
		print(CatalogName)
		print(CategoryName)
		print(ClosedByParent)
		print(CuisineNameList)
		print(DeliveryFee)
		print(DeliveryTime)
		print(DisplayName)
		print(Flavour)
		print(HasDVDPromotion)
		print(ImagePath)
		print(ImageFullPath)
		print(ImageLabelListFullPath)
		print(IsOpen)
		print(IsRestaurantOpen)
		print(MainCuisineId)
		print(MainCuisineLabelName)
		print(MainCuisineName)
		print(MinimumDeliveryPrice)
		print(OpenRestaurantCount)
		print(PaymentMethodsText)
		print(PaymentMethodsList)
		print(Serving)
		print(Slug)
		print(Speed)
		print(WorkHoursText)
		print(AvgPoint)
		print(ServingText)
		print(SpeedText)
		print(FlavourText)
		print(AvgRestaurantScore)
		print(MinimumDeliveryPriceText)
		print(HasCampusDiscount)
		print(IsFreezoneRestaurant)
		print(HasPromotion)
		print(SuperDelivery)
