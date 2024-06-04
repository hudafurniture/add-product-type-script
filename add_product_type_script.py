import os
from pathlib import Path




def procut_type(fname):
    degem = 0
    if (fname[:2] == "10"):
        degem = 100 #חדר_שינה
    elif (fname[:2] == "20"):
        degem = 200 #חדר_ילדים
    elif (fname[:2] == "30"):
        degem = 1  #ארון_הזזה
    elif (fname[:2] == "40"):
        degem = 2 #ארון_פתיחה
    elif (fname[:2] == "50" or fname[:4] == "6095" or fname[:4] == "6096" or "242508" in fname  ):
        degem = 3 #ארון_קודש
    elif (((fname[:2] == "10" or fname[:2] == "20") and fname[4] == "1" ) or "6097" in fname):
        degem = 8 #מיטה
    elif (fname[:2] == "10" and fname[4] == "2"):  #shedot 7adre yeldem not covered yet
        degem = 7 #שידה   
    elif ("6065" in fname or "6066" in fname or "6067" in fname or "6068" in fname):
        degem = 10 #מזנון    
        
    print(fname + " ===> " + str(degem))
    return degem





def main():
    #script_directory = os.path.dirname(os.path.abspath(__file__))
    #stk_dir = os.path.join(script_directory + "/stk_test")
    stk_directory = "C:/Ardis/younis/2024/Scripts/Add_Product_Type_Script/stk_test"
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
                    for i in range(len(filedata_arr)):
                        if ("DEFAULT=" in filedata_arr[i] and "UITLEG=Don't Delete This" in filedata_arr[i-1]):
                            txtToFix_6 = "DEFAULT=" + str(procut_type(file_name))
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
                            txtToAdd_5 = "UITLEG=Don't Delete This"
                            txtToAdd_6 = "DEFAULT=" + str(procut_type(file_name))
                            txtToAdd_7 = txtToAdd_1
                            new_data.append(txtToAdd_1)
                            new_data.append(txtToAdd_2)
                            new_data.append(txtToAdd_3)
                            new_data.append(txtToAdd_4)
                            new_data.append(txtToAdd_5)
                            new_data.append(txtToAdd_6)
                            new_data.append(txtToAdd_7)
                            new_data.append("")
                            countVRAGENS += 1
                            stop = True
                            new_data.append(filedata_arr[i])
                        else:
                            new_data.append(filedata_arr[i])
                            
                            
  
                #print(file_name + " === " + str(countVRAGENS))            
                with open(file_path, 'w') as file:
                    file.write('\n'.join(new_data))
                    




















if __name__ == "__main__":
    main()