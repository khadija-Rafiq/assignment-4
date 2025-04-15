import math  #square root use karny k liye 

def main():
    ab = float(input("\033[1m\033[3m Enter the length of AB:\033[0m "))  
    ac = float(input("\033[1m\033[3m Enter the length of AC:\033[0m "))  

    bc = math.sqrt(ab**2 + ac**2)  

    print(f"The length of BC (the hypotenuse) is: {bc}")  

if __name__ == '__main__':
    main()