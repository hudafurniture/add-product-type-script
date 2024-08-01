import os
from pathlib import Path

productTypeDict = {
    0: 'דגם לא זוהה',
    1: 'ארון_הזזה',
    2: 'ארון_פתיחה',
    3: 'ארון_קודש',
    4: 'כוננית',
    5: 'ספריה',
    6: 'כוורת',
    7: 'שולחן_כתיבה',
    8: 'שידה',
    9: 'קומודה/טואלט',
    10: 'מיטה',
    11: 'מזנון',
    12: ' יח מגירות/שידת_טלווזיה',
    100: 'חדר_שינה_שלם'
}


def get_procut_type(fname):
    degem = 0
    if (fname[:2] == "30" or (fname[:2] == "20" and fname[4] == "4" and (fname[2:4] == "44" or fname[2:4] == "46" or fname[2:4] == "50" or fname[2:4] == "60" or fname[2:4] == "64"))):
        degem = 1  #ארון_הזזה
    elif (fname[:2] == "40" or (fname[:2] == "20" and fname[4] == "4")):
        degem = 2 #ארון_פתיחה
    elif (fname[:2] == "50" or fname[:4] == "6095" or fname[:4] == "6096" or "242508" in fname  ):
        degem = 3 #ארון_קודש
    elif (fname[:2] == "20" and fname[4] == "9" ):
        degem = 4 #כוננית
    elif (fname[:2] == "20" and fname[4] == "2"):  
        degem = 5 #ספריה  
    elif (fname[:2] == "20" and fname[4] == "5"):  
        degem = 6 #כוורת  
    elif (fname[:2] == "20" and fname[4] == "8"):  
        degem = 7 #שולחן_כתיבה  
    elif ((fname[:2] == "10" and fname[4] == "2") or (fname[:2] == "20" and fname[4] == "6")):  
        degem = 8 #שידה  
    elif ((fname[:2] == "10" and fname[4] == "3") or (fname[:2] == "20" and fname[4] == "7") or "6098" in fname):  
        degem = 9 #קומודה/טואלט  
    elif (((fname[:2] == "10" or fname[:2] == "20") and fname[4] == "1" ) or "6097" in fname):
        degem = 10 #מיטה
    elif ("6065" in fname or "6066" in fname or "6067" in fname or "6068" in fname):
        degem = 11 #מזנון   
    elif (fname[:2] == "20" and fname[4] == "3"):  
        degem = 12 #יח מגירות/שידת_טלווזיה  
    elif (fname[:2] == "10"):
        degem = 100 #חדר_שינה_שלם
        
    print(fname + " ===> " + str(degem))
    return degem





def main():
    #script_directory = os.path.dirname(os.path.abspath(__file__))
    #stk_dir = os.path.join(script_directory + "/stk_test")
    #------------------------------------------------
    #stk_directory = "C:/Ardis/younis/2024/Scripts/Add_Product_Type_Script/stk_test/"
    stk_directory = "C:/Ardis/Data/Templates/"
    for root, dirs, files in os.walk(stk_directory):
        for file_name in files:
            if(file_name.lower().endswith(".stk")):
                #print(file_name)
                new_data = []
                stop = False
                file_path = os.path.join(root, file_name)
                with open(file_path, 'r') as file:
                    filedata = file.read()
                    filedata_arr= filedata.split('\n')
                    countVRAGENS = 0
                    countVRAGENStreak = 0
                    productType = get_procut_type(file_name)
                    for i in range(len(filedata_arr)):
                        if ("DEFAULT=" in filedata_arr[i] and "UITLEG=Don't Delete" in filedata_arr[i-1]):
                            txtToFix_5 = "UITLEG=Don't Delete" + " - " + productTypeDict[productType]
                            txtToFix_6 = "DEFAULT=" + str(productType)
                            new_data.append(txtToFix_5)
                            new_data.append(txtToFix_6)
                            stop = True
                        elif "VRAGEN-" in filedata_arr[i]:
                            new_data.append(filedata_arr[i])
                            countVRAGENStreak += 1
                            if countVRAGENStreak == 2:
                                countVRAGENS += 1
                                countVRAGENStreak = 0
                        elif("VRAGEN$FORM" in filedata_arr[i] and not stop):
                            #new_data.append("")
                            txtToAdd_1 = "[VRAGEN-" + str(countVRAGENS + 1)+"]"
                            txtToAdd_2 = "NAAM=degem"
                            txtToAdd_3 = "VRAAG=Product Type"
                            txtToAdd_4 = "TYPE=3"
                            txtToAdd_5 = "UITLEG=Don't Delete" + " - " + productTypeDict[productType]
                            txtToAdd_6 = "DEFAULT=" + str(productType)
                            txtToAdd_7 = "Editable=0"
                            txtToAdd_8 = txtToAdd_1
                            new_data.append(txtToAdd_1)
                            new_data.append(txtToAdd_2)
                            new_data.append(txtToAdd_3)
                            new_data.append(txtToAdd_4)
                            new_data.append(txtToAdd_5)
                            new_data.append(txtToAdd_6)
                            new_data.append(txtToAdd_7)
                            new_data.append(txtToAdd_8)
                            new_data.append("")
                            countVRAGENS += 1
                            stop = True
                            new_data.append(filedata_arr[i])
                        else:
                            new_data.append(filedata_arr[i])
                    if(countVRAGENS == 0):  
                        txtToAdd_1 = "[VRAGEN-" + str(countVRAGENS + 1)+"]"
                        txtToAdd_2 = "NAAM=degem"
                        txtToAdd_3 = "VRAAG=Product Type"
                        txtToAdd_4 = "TYPE=3"
                        txtToAdd_5 = "UITLEG=Don't Delete" + " - " + productTypeDict[productType]
                        txtToAdd_6 = "DEFAULT=" + str(productType)
                        txtToAdd_7 = "Editable=0"
                        txtToAdd_8 = txtToAdd_1
                        new_data.append(txtToAdd_1)
                        new_data.append(txtToAdd_2)
                        new_data.append(txtToAdd_3)
                        new_data.append(txtToAdd_4)
                        new_data.append(txtToAdd_5)
                        new_data.append(txtToAdd_6)
                        new_data.append(txtToAdd_7)
                        new_data.append(txtToAdd_8)
                        new_data.append("")
                        countVRAGENS += 1      
                            
  
                print(file_name + " === " + str(countVRAGENS))            
                with open(file_path, 'w') as file:
                    file.write('\n'.join(new_data))
                    




















if __name__ == "__main__":
    main()
