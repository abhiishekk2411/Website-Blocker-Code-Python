import datetime
import time

host_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"

print("Welcome to Website Blocker Code")
user_sites=input("Enter the site url that has to be blocked (separated by commas)").strip()
site_block = [site.strip() for site in user_sites.split(",")]

hours=int(input("Enter the nunmber of hours that site must be blocked").strip())

start_time=datetime.datetime.now()
end_time=start_time +datetime.timedelta(hours=hours)

print(f"\n Websites {user_sites} will be blocked till {end_time.strftime('%H:%M:%S')}...")

while True:
    current_time=datetime.datetime.now()

    if current_time<end_time:
        print("Blocked period active")
        with open(host_path,"r+") as file:                                    #we can manually also open file with open then we have to close it with close also
            content=file.read()
            for i in site_block:
                if i in content:
                    pass
                else:
                    file.write(redirect+" "+i+"\n")

    else:
        print("\n Time is up ...unblocking site..")
        with open(host_path,"r+") as file:
            lines=file.readlines()
            file.seek(0)
            for line in lines:
                isClean=True
                for website in site_block:
                    if website in line:
                        isClean=False
                        break
                if isClean == True:
                    file.write(line)
            file.truncate()
        print("Websites unblocked successfully!")
        break

    time.sleep(5)