import pandas as pd
from datetime import datetime

if __name__=="__main__":

    choiceList=["Sedol","Cusip","ISIN"]
    choice=input("Choose from Sedol/Cusip/ISIN")
    if choice in choiceList:
        rootID=input("Enter the Root ID: ")
        dateCheck=input("Date to Check wit:  ")
        dateCheck=datetime(int(dateCheck[:4]), int(dateCheck[4:6]),int(dateCheck[-2:]))
        idMapFile=pd.read_csv("IDMapping.txt",sep='|', index_col=False)
        assetMapFile=pd.read_csv("AssetIdentity.txt",sep='|', index_col=False)
        idMapFile["StartDate"]=idMapFile['StartDate'].apply(lambda x: datetime(int(str(x)[:4]), int(str(x)[4:6]),int(str(x)[-2:])))
        idMapFile["EndDate"]=idMapFile['EndDate'].apply(lambda x: datetime(int(str(x)[:4]), int(str(x)[4:6]),int(str(x)[-2:])))

        assetMapFile["StartDate"]=assetMapFile['StartDate'].apply(lambda x: datetime(int(str(x)[:4]), int(str(x)[4:6]),int(str(x)[-2:])))
        assetMapFile["EndDate"]=assetMapFile['EndDate'].apply(lambda x: datetime(int(str(x)[:4]), int(str(x)[4:6]),int(str(x)[-2:])))

        # test=idMapFile[idMapFile["AssetIDType"].str.lower()=="sedol" & ]
        checkedS2ID=assetMapFile[(assetMapFile["RootID"]==rootID) & (assetMapFile["StartDate"]<=dateCheck) & (assetMapFile["EndDate"]>=dateCheck)]["S2ID"].unique()

        print(idMapFile[(idMapFile["S2ID"].isin(checkedS2ID)) & (idMapFile["AssetIDType"].str.lower() == choice.lower())]["S2ID"].unique())
        
    else:
        print("Invalid input")