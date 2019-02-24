#!/usr/bin/env python
# coding: utf-8
from bs4 import BeautifulSoup
import urllib
from urllib.request import urlopen
import json as JSON
from  openpyxl import *



linktxt = open("linklerr.txt" , "r")
linkler = linktxt.readlines() 


kitap = Workbook() 
kitap.create_sheet("veriler") 
yaz = kitap.get_sheet_by_name("veriler") 
yaz.append(['Bölge','Areaname','CatalogName' , 'CategoryName' , 'ClosedByParent' , 'CuisineNameList', 'DeliveryFee', 'DeliveryTime', 'DisplayName', 'Flavour', 'HasDVDPromotion', 'IsOpen', 'IsRestaurantOpen', 'MainCuisineId', 'MainCuisineLabelName', 'MainCuisineName', 'MinimumDeliveryPrice', 'OpenRestaurantCount', 'PaymentMethodsText', 'PaymentMethodsList', 'Serving', 'Slug', 'Speed', 'WorkHoursText', 'AvgPoint', 'ServingText', 'SpeedText', 'FlavourText', 'AvgRestaurantScore', 'MinimumDeliveryPriceText', 'HasCampusDiscount', 'IsFreezoneRestaurant', 'HasPromotion', 'SuperDelivery']) 

for i in range(len(linkler)):

	adres = linkler[i]
	try:
		url = ("https://www.yemeksepeti.com/"+adres)
		sayfa = urllib.request.urlopen(url)
	except:
		pass
	soup = BeautifulSoup(sayfa, "html.parser")

	soupp = soup.encode("utf-8")
	veri = soup.find_all('span', {'data-tooltip': True})
	for item in veri:
		c = item['data-tooltip']
		json = JSON.loads(c) 
		Areaname = json["AreaName"].encode("utf-8")
		CatalogName = json["CatalogName"]
		CategoryName = json["CategoryName"]
		ClosedByParent = json["ClosedByParent"]
		CuisineNameList = json["CuisineNameList"]
		DeliveryFee = json["DeliveryFee"]
		DeliveryTime = json['DeliveryTime']
		DisplayName = json['DisplayName'].encode("utf-8")
		Flavour = json["Flavour"]
		HasDVDPromotion = json["HasDVDPromotion"]
		ImagePath = json["ImagePath"]
		ImageFullPath = json["ImageFullPath"]
		ImageLabelListFullPath = json["ImageLabelListFullPath"]
		IsOpen = json["IsOpen"]
		IsRestaurantOpen = json["IsRestaurantOpen"]
		MainCuisineId = json["MainCuisineId"]
		MainCuisineLabelName = json["MainCuisineLabelName"]
		MainCuisineName = json["MainCuisineName"]
		MinimumDeliveryPrice = json["MinimumDeliveryPrice"]
		OpenRestaurantCount = json["OpenRestaurantCount"]
		PaymentMethodsText = json["PaymentMethodsText"]
		PaymentMethodsList = json["PaymentMethodsList"]
		#PromotionText = json["PromotionText"]
		Serving = json["Serving"]
		Slug = json["Slug"]
		Speed = json["Speed"]
		WorkHoursText = json["WorkHoursText"]
		AvgPoint = json["AvgPoint"]
		ServingText = json["ServingText"]
		SpeedText = json["SpeedText"]
		FlavourText = json["FlavourText"]
		AvgRestaurantScore = json["AvgRestaurantScore"]
		MinimumDeliveryPriceText = json["MinimumDeliveryPriceText"]
		HasCampusDiscount = json["HasCampusDiscount"]
		IsFreezoneRestaurant = json["IsFreezoneRestaurant"]
		HasPromotion = json["HasPromotion"]
		SuperDelivery = json["SuperDelivery"]
		yaz.append([adres,Areaname.decode("utf-8") ,str(CatalogName).replace("['" , "") , CategoryName, ClosedByParent ,str(CuisineNameList).strip('[]'), DeliveryFee, DeliveryTime, DisplayName, Flavour, HasDVDPromotion, IsOpen, IsRestaurantOpen, MainCuisineId, MainCuisineLabelName, MainCuisineName, MinimumDeliveryPrice,OpenRestaurantCount, str(PaymentMethodsText).strip('[]'), str(PaymentMethodsList).strip('[]'), Serving, Slug, Speed, WorkHoursText, AvgPoint, ServingText, SpeedText, FlavourText, AvgRestaurantScore, MinimumDeliveryPriceText, HasCampusDiscount, IsFreezoneRestaurant, HasPromotion, SuperDelivery]) 
		print(adres)
kitap.save("yemeksepetiheril.xlsx") # exceli kaydet
kitap.close() #excelli kapat
