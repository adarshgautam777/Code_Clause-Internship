from playsound import playsound

print("No. of available songs\n1.Csk\n2.Jaadui\n3.O Bedardeya\n4.Apna Bana le")
order = input("Enter the music which you want to play : ")
if "Csk" in order:
    playsound('C:\\Users\\HP\\Downloads\\Csk.mp3')
elif "Jaadui" in order:
    playsound('C:\\Users\\HP\\Downloads\\Jaadui.mp3')
elif "O Bedardeya" in order:
    playsound('C:\\Users\\HP\\Downloads\\O Bedardeya.mp3')
elif "Apna Bana le" in order:
    playsound('C:\\Users\\HP\\Downloads\\Apna Bana le.mp3')
    
